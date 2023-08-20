import requests
import sqlite3

# URL de autenticação
auth_url = 'https://pontowebintegracaoexterna.secullum.com.br/api/autenticar'

# Dados de autenticação (substitua com suas credenciais)
EMPRESA = 'sua_empresa'
USUARIO = 'seu_usuario'
SENHA = 'sua_senha'

# Dicionário com os dados de autenticação
auth_data = {
    'empresa': EMPRESA,
    'usuario': USUARIO,
    'senha': SENHA
}

# Faz a solicitação de autenticação
response = requests.post(auth_url, data=auth_data)

# Verifica se a autenticação foi bem-sucedida
if response.status_code == 200:
    # Obtém o token de acesso a partir da resposta
    token = response.json().get('access_token')

    # URL para obter todos os dados disponíveis
    dados_url = 'https://pontowebintegracaoexterna.secullum.com.br/api/todos'

    # Define o cabeçalho da solicitação com o token de acesso
    headers = {
        'Authorization': f'Bearer {token}'
    }

    # Faz a solicitação para obter todos os dados disponíveis
    response = requests.get(dados_url, headers=headers)

    # Verifica se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Obtém os dados a partir da resposta
        dados = response.json()

        # Cria o banco de dados SQLite
        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()

        # Cria as tabelas no banco de dados
        for tabela in dados:
            nome_tabela = tabela['nome']

            # Obtém os campos da tabela
            campos = tabela['campos']

            # Cria a tabela no banco de dados
            campos_definicao = ', '.join([f"{campo['nome']} {campo['tipo']}" for campo in campos])
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {nome_tabela} ({campos_definicao})")

            # Obtém os registros da tabela
            registros = tabela['registros']

            # Insere os registros na tabela
            for registro in registros:
                campos_registro = registro['campos']
                valores = [campo_registro['valor'] for campo_registro in campos_registro]
                valores_formatados = ', '.join(['?' for _ in campos_registro])
                cursor.execute(f"INSERT INTO {nome_tabela} VALUES ({valores_formatados})", valores)

        # Commit e fecha a conexão com o banco de dados
        conn.commit()
        conn.close()

        print("Dados inseridos no banco de dados.")
    else:
        print("Falha ao obter os dados disponíveis.")
else:
    print("Falha na autenticação.")
