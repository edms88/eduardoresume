#Passo 1: Entendimento do Desafio

#Passo 2: Entendimento da Área/Empresa

#Passo 3: Extração/Obtenção de Dados
import pandas as pd
df = pd.read_csv('/content/Advertising.csv')
#display(df)

#Passo 4: Ajuste de Dados (Tratamento/Limpeza)
#não há necessidade.

#Passo 5: Análise Exploratória
import seaborn as sns
import matplotlib.pyplot as plt  #sempre importar os 2 modulos juntos

sns.heatmap(df.corr(), annot=True)
sns.pairplot(df)
plt.show()

#Passo 6: Modelagem + Algoritmos (Aqui que entra a Inteligência Artificial, se necessário)

from sklearn.model_selection import train_test_split
y = df['Sales'] #dizendo teu objetivo
x = df.drop('Sales', axis=1) 
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1)


#regressão linear #randomForest (arvore de decisão)

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

modelo_regressaolinear = LinearRegression()
modelo_arvorededecisao = RandomForestRegressor()

 
#Treino das IA
modelo_regressaolinear.fit(x_treino,y_treino)
modelo_arvorededecisao.fit(x_treino,y_treino)

RandomForestRegressor()

#Definir o R² do objetivo do modelo

from sklearn import metrics

#criar previsão de vendas
previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvorededecisao.predict(x_teste)

#comparar os modelos
print(f'{metrics.r2_score(y_teste, previsao_regressaolinear):.2f}')
print(metrics.r2_score(y_teste, previsao_arvoredecisao))

#Graficos
tabela_auxiliar = pd.DataFrame()
tabela_auxiliar['y_teste'] = y_teste
tabela_auxiliar['Previsão Arvoredecisao'] = previsao_arvoredecisao
tabela_auxiliar['Previsão RegressãoLinea'] = previsao_regressaolinear

plt.figure(figsize=(15,6))
sns.lineplot(data= tabela_auxiliar)
plt.show()

sns.barplot(x= x_treino.columns,y= modelo_arvorededecisao.feature_importances_)
plt.show()