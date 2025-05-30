
from pathlib import Path
import streamlit as st
from PIL import Image

# path Settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file    = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Profile.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
csc_print   = current_dir / "assets" / "cscprint.png"
constatlogo = current_dir / "assets" / "constatlogo.png"
log1        = current_dir / "assets" / "logistica.png"
sales       = current_dir / "assets" / "Sales BRasil.png"
comercial   = current_dir / "assets" / "vendas01.png"
dash01      = current_dir / "assets" / "csc.pbix"
dash02      = current_dir / "assets" / "Dashboard.pbix"
dash03      = current_dir / "assets" / "South cargo vzero.pbix"
dash04      = current_dir / "assets" / "Sales BRasil - IPTV.pbix"
 
sqldw       = current_dir / "assets" / "Views_qualitor_SA.rar"
python01    = current_dir / "assets" / "enviar_mensagem.py"
python02    = current_dir / "assets" / "Extract_Pypdf2.txt"
python03    = current_dir / "assets" / "Request API.txt"
skill       = current_dir / "assets" / "skils.txt"

#dash05     = current_dir / "assets" / "Painel Suprimentos.pbix"
suprimento_img = current_dir / "assets" / "painel_suprimentos.png"

#dash06     = current_dir / "assets" / "Painel Receita.pbix"
receita_img = current_dir / "assets"/ "painel_receitas.png"


# General Settings
PAGE_TITLE = 'Eduardo Mendes'
PAGE_ICON = ':notebook:'
NAME = 'Eduardo Mendes da Silveira'


EMAIL = 'eduardoms1988@gmail.com'
LINKDIN = 'https://www.linkedin.com/in/eduardo-mendes-da-silveira-5476a1237/'
INSTAGRAM = 'https://www.instagram.com/eduardoms88/'
GITHUB = 'https://github.com/edms88'


PROJECTS = {
    ':snake: - Extração de dados em massa',
    ':notebook: - DASHBOARD em Power BI MS',
    'Views e relatórios em SQL - Qualitor',
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

# --- LOAD CSS, PDF, E PROFILE PIC ---
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)
    csc_print = Image.open(csc_print)
    logistica = Image.open(log1)
    salesbr   =  Image.open(sales)
    comercial01 = Image.open(comercial)
    logcargo = Image.open(log1)
    sales_img = Image.open(sales)
    painel_receita = Image.open(receita_img)
    painel_supri = Image.open(suprimento_img)


with open(dash01, "rb") as dashboard_file01:
    dash01bt  = dashboard_file01.read()

with open(dash02, "rb") as dashboard_file02:
    dash02bt  = dashboard_file02.read()

with open(dash03, "rb") as dashboard_file03:
    dash03bt  = dashboard_file03.read()

with open(dash04, "rb") as dashboard_file04:
    dash04bt  = dashboard_file04.read()






st.title(NAME)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")

with col1:
    st.image(profile_pic, width=230)
    st.write("- Phone: +55 51 9 8940 9895\n- Porto Alegre / RS")
    st.markdown(':e-mail: [eduardoms@outlook.com](mailto:eduardoms@outlook.com)')
    st.write(':camera:[Instagram](https://www.instagram.com/eduardoms88/)')
    st.write(':briefcase:[LinkedIn](https://www.linkedin.com/in/eduardo-mendes-da-silveira-5476a1237)')
    st.write(':blue_book:[Facebook](https://www.facebook.com/du.mendes/)')
    st.write(':computer:[GitHub](https://github.com/edms88)')

with col2:
    st.subheader('Skills')
   
    st.write(   
        """
        Python :star: :star: :star::star:

    SQL :star: :star: :star::star:

    English :star: :star: :star:

    Data Engineering :star: :star: :star:

    Coding :star: :star: :star:

    Spanish :star: :star:

    Data Science :star: :star:

    HTML :star: :star:

    CSS :star: :star:
    """)

    st.download_button(
        label='Download Resume',
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

### Social links ####


### Experience

st.subheader("Graduações")

st.write(""" 
    1) Graduação Bacharel em Administração (7º semestre)
    2) Tecnólogo em Análise e desenvolvimento de sistemas (Concluído)
    """)


### Histórico profissional ###
st.write("-"*30)
col7, col8 = st.columns(2, gap='small')
with col7:

    st.subheader('[20barra9](https://www.20barra9.com/)')
    st.header('Analista de dados')
    st.subheader('07/2024 até o momento')

    st.write("""
            :triangular_flag_on_post: Coleta e Integração de Dados: Extraio e integro dados de múltiplas fontes (bancos de dados, APIs, Excel), consolidando-os em estruturas coerentes no Power BI.

            :triangular_flag_on_post: Modelagem de Dados Avançada: Desenvolvo modelos de dados robustos, criando relacionamentos e medidas complexas em DAX para análises detalhadas e precisas.

            :triangular_flag_on_post: Desenvolvimento de Dashboards Interativos: Crio dashboards e relatórios interativos que comunicam dados de forma clara e eficaz, ajudando stakeholders a identificar tendências e tomar decisões baseadas em dados.

            :triangular_flag_on_post: Otimização de Desempenho: Garanto a eficiência dos relatórios otimizando queries e modelos de dados, proporcionando uma experiência de análise rápida e fluida.

            :triangular_flag_on_post: Colaboração e Compartilhamento: Publico e gerencio dashboards no Power BI Service, facilitando o acesso seguro e colaborativo às informações essenciais para o negócio.

            :triangular_flag_on_post: Monitoramento e Manutenção: Monitoro e mantenho dashboards em produção, realizando atualizações conforme as necessidades do negócio evoluem.

            :triangular_flag_on_post: Capacitação e Documentação: Treino equipes na utilização dos dashboards e documento processos para assegurar a continuidade e a transferência de conhecimento."""
             )
with col8:
     
    st.subheader("Competências")
    st.write("""
        :label: Visualização de dados

        :label: Manipulação e tratamento de grandes volumes de dados

        :label: SQL

        :label: ElasticSearch

        :label: Análise Exploratória de dados

        :label: Inteligência de negócios (BI)

        :label: Microsoft Azure Machine Learning

        :label: Microsoft Power BI

        :label: Microsoft Office

        :label: Python

        :label: HTML & CSS
    """)




st.write("-" * 30)
col9, col10 = st.columns(2, gap='small')
with col9:

    st.subheader('[Constat Serviços de Tecnologia](https://constat.com.br/)')
    st.header('Analista de dados')
    st.subheader('05/2020 - 07/2024')

    st.write("""
        
             :triangular_flag_on_post: Elaboração e análise de Indicadores Gerenciais e Financeiros para suportar decisões corporativas estratégicas.
        
             :triangular_flag_on_post: Desenvolvimento de relatórios automatizados e modelos de projeção para facilitar a análise de dados e o processo de tomada de decisão.
        
             :triangular_flag_on_post: Modelagem e mineração de dados em bancos de dados como Postgres, Oracle, e web scraping usando Python (Scrapy e BeautifulSoup) para coletar e processar informações relevantes.
    """)

with col10:

    st.subheader("Competências")
    st.write("""
        :label: Visualização de dados

        :label: Manipulação e tratamento de grandes volumes de dados

        :label: SQL

        :label: ElasticSearch

        :label: Análise Exploratória de dados

        :label: Inteligência de negócios (BI)

        :label: Microsoft Azure Machine Learning

        :label: Microsoft Power BI

        :label: Microsoft Office

        :label: Python

        :label: HTML & CSS
    """)

st.write("-" * 30)
col11, col12 = st.columns(2, gap='small')
with col11:

    st.subheader('[Atlas Schindler Elevadores](https://www.schindler.com.br/pt.html)')
    st.header('Analista de Fullfilment')
    st.subheader('02/2018 - 03/2020')

    st.write("""

             :triangular_flag_on_post: Elaboração de relatórios abrangendo indicadores de produtividade como OLE (Overall Labor Effectiveness), man/hour, MTTR (Mean Time to Repair), eficiência mecânica, além de métricas financeiras como EBITDA, ROI, Margem Bruta e SecurePass.
        
             :triangular_flag_on_post: Participação ativa em reuniões gerenciais utilizando a metodologia Agile, contribuindo com insights e soluções para crises e desafios enfrentados por clientes de padrão exclusivo.
        
             :triangular_flag_on_post: Responsável pelo planejamento e análise dos dados financeiros e operacionais da região Sul, visando impulsionar a eficiência e o desempenho da organização.
    """)

with col12:
    st.subheader("Competências")
    st.write("""
             
        :label: Compreender as necessidades dos clientes para a criação do produto ou serviço

        :label: Visualização de dados

        :label: Manipulação e tratamento de grandes volumes de dados

        :label: Análise Exploratória de dados

        :label: Inteligência de negócios (BI)

        :label: Microsoft Office
    """)

st.write("-" * 30)
col13, col14 = st.columns(2, gap='small')
with col13:

    st.subheader('[TKE Elevadores](https://www.tkelevator.com/br-pt/)')
    st.header('Assistente Comercial')
    st.subheader('12/2016 - 03/2018')

    st.write("""
        
             :triangular_flag_on_post: Responsável pelo apoio logístico de obras nas regiões norte e sul das Américas, colaborando com os setores de especificação de projetos novos, modernizações e acessibilidade.
        
             :triangular_flag_on_post: Desenvolvimento e implementação de processos de melhoria para resolver demandas de reprogramação, aditivos contratuais e apresentação de indicadores-chave de desempenho como MTTR, MTBF e LEAN TIME, visando otimizar prazos e eficiência operacional.
        
             :triangular_flag_on_post: Análise e apresentação dos indicadores de entrega para a América Latina, monitorando o cumprimento de prazos e identificando áreas de melhoria para garantir o sucesso das operações.
        
             :triangular_flag_on_post: Colaboração com equipes multidisciplinares para garantir o alinhamento entre as áreas de logística, especificação de projetos e demandas dos clientes, assegurando uma coordenação eficiente e o cumprimento dos objetivos.
    """)

with col14:
    st.subheader("Competências")
    st.write("""
        :label: Compreender as necessidades dos clientes para a criação do produto ou serviço

        :label: Visualização de dados

        :label: Manipulação e tratamento de grandes volumes de dados

        :label: Lean Six Sigma

        :label: Inteligência de negócios (BI)

        :label: Microsoft Office

    """)

st.write("-" * 30)
col15, col16 = st.columns(2, gap='small')
with col15:

    st.subheader('[Yara Brasil](https://www.yarabrasil.com.br/)')
    st.header('Back Office')
    st.subheader('10/2013 - 03/2016')

    st.write("""
              
        :triangular_flag_on_post: Responsável pelo envio de relatórios gerenciais com indicadores como RFP, OLE, man/hour, MTTR e eficiência mecânica, para auxiliar na tomada de decisões estratégicas.
        
        :triangular_flag_on_post: Gerenciamento do envio de demonstrativos de comissões, arquivos e controle de notas de prestação de serviço, assegurando precisão e conformidade com requisitos legais.
        
        :triangular_flag_on_post: Emissão de certificados de análise de exportação e notas fiscais de remessa, incluindo operações de triangulação, para garantir o cumprimento de obrigações fiscais e conformidade regulatória.
    """)

with col16:
    st.subheader("Competências")
    st.write("""
        :label: SAP ERP

        :label: Gestão logística

        :label: Manipulação e tratamento de grandes volumes de dados

        :label: Gestão de relacionamento com o cliente (CRM)

        :label: Inteligência de negócios (BI)

        :label: Microsoft Office
        
        :label: Inglês
    """)

st.write("-" * 30)



st.title("Dashboards em Microsoft Power BI")
suprimentos, receita = st.columns(2, gap="small")

with suprimentos:

    st.subheader("Suprimentos")
    
    st.image(painel_supri, width=300, caption= "Suprimentos")

    st.write("""
        O dashboard foi desenvolvido para mostrar
        os principais indicadores indicadores de Suprimentos  """)
    
    
    st.write(':computer:[Download](https://drive.google.com/file/d/1vsB8EW2iKkkzvlqLYKWoWDeXK7KjvwLu/view?usp=sharing)')
    
with receita:

    st.subheader("Receitas")
    
    st.image(painel_receita, width=300, caption= "Receitas")

    st.write("""
        O dashboard foi desenvolvido para mostrar um Overview, rank de atendentes com grafico EXCLUSIVO
             E por final um CURVA ABC dinamica.  """)
    
    

    st.write(':computer:[Download](https://drive.google.com/file/d/1vsB8EW2iKkkzvlqLYKWoWDeXK7KjvwLu/view?usp=sharing)')

st.write('-' * 30)

csc, comercial = st.columns(2, gap="small")

with csc:

    st.subheader("Dashboard CSC")
   

    st.write("""
        O dashboard foi desenvolvido para mostrar
        os principais indicadores chave da central de serviços
    """)
    
    st.image(csc_print, width=300, caption = 'Dashboard CSC')
    st.download_button(
        label="Download",
        data=dash01bt,
        file_name=dash01.name,
        mime="application/octet-stream",
    
    )

with comercial:
    st.subheader("Dashboard Comercial-produtos")

    st.write("""
        O dashboard foi criado com a visualização por produto não regionalizado""")
        
    st.image(comercial01, caption='Dashboard de Comercial', width=300)
        
    st.download_button(
        label="Download",
            data=dash02bt,
            file_name=dash02.name,
            mime="application/octet-stream")


st.write('-' * 30)

carg, slbr = st.columns(2, gap="small")

with carg:
    st.subheader("Dashboard Logística")

    st.write("""
        O dashboard foi desenvolvido para mostrar
        os principais portuarios da america latina
    """)
    st.image(logcargo, caption='Dashboard de logistica', width=300)

    st.download_button(
        label="Download",
            data=dash03bt,
            file_name=dash03.name,
            mime="application/octet-stream")


with slbr:
    st.subheader("Dashboard Rastreio de vendas")

    st.write("""
        O dashboard foi desenvolvido para mostrar
        os principais indicadores chave da central de serviços
    """)
    st.image(sales_img, caption='Dashboard de Rastreio de Vendas', width=300)

    st.download_button(
        label="Download",
            data=dash04bt,
            file_name=dash04.name,
            mime="application/octet-stream")


st.write('-' * 30)

st.title('MySql')
st.write("16 querys em sql criados para diversas demandas e situações.")

with open(sqldw, "rb") as sql_file:
    sql_01 = sql_file.read()
    st.download_button(
        label="Baixar Views do SQL",
        data=sql_01,
        file_name=sqldw.name,
        mime="application/octet-stream")

st.write('-' * 30)

st.title('Python')
st.write("Alguns pequenos exemplos de scripts em python que possuimos")

st.write("Seleciona usuarios para envio de mensagens automaticas a qualquer operador de mensagem MS")

with open(python01, "rb") as send01:
    py01 = send01.read()
    st.download_button(
        label="Download",
        data=py01,
        file_name=python01.name,
        mime="application/octet-stream")

st.write("Extrai qualquer informaçãodesejada de arquivos .pdf e cria dataframes com eles")

with open(python02, "rb") as pdfextr:
    py02 = pdfextr.read()
    st.download_button(
        label="Download",
        data=py02,
        file_name=python02.name,
        mime="application/octet-stream")

st.write("REQUEST API")

with open(python03, "rb") as req:
    py03 = req.read()
    st.download_button(
        label="Download",
        data=py03,
        file_name=python03.name,
        mime="application/octet-stream")

st.write("""
Estamos sempre criando algum novo, recomendo utilizar a rede github para
se manter informado
""")


st.write('-' * 30)
