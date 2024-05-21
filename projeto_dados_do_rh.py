# -*- coding: utf-8 -*-
"""PROJETO: Dados do RH

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QU99OT6Bnne8At6u2438KXSo2_z6TAhQ
"""

import pandas as pd

rh = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vREf90i4HH2dyOAmu7mI51KhsaLB8Gl80ucUubPBIAIF9AlkTwekpJzIEXwYi-1mrQiAl93TELN_sfJ/pub?gid=0&single=true&output=csv')

# Exibir todas as colunas de um dataframe e os tipos
rh.dtypes

#Quantos foram demitidos e quantos não
D = rh.groupby('Demissão')['Demissão'].count()
df = pd.DataFrame(D)
display(df)

#Criando um novo dataframe só para os demitidos
filtro01 = rh.loc[rh['Demissão']=='Sim', :]
display(filtro01)

# Correlacioando os funcionário demitidos com departamento
agrupamento01 = filtro01['Departamento'].value_counts()
agrupamento01 = pd.DataFrame(agrupamento01)
display(agrupamento01)

# Correlacioando os funcionário demitidos com cargos
agrupamento02 = filtro01['Cargo'].value_counts()
agrupamento02 = pd.DataFrame(agrupamento02)
display(agrupamento02)

# Correlacioando os funcionários demitidos com o Nível de Satisfação com o ambiente de trabalho
agrupamento03 = filtro01['Nível de Satisfação com o ambiente de trabalho'].value_counts()
percentual = filtro01['Nível de Satisfação com o ambiente de trabalho'].value_counts(normalize=True)*100
tabela = pd.DataFrame({'Frequência Absoluta':agrupamento03,'Frequência Percentual':percentual})
display(tabela)

# Correlacioando os funcionários demitidos com o Nível de envolvimento com o trabalho

agrupamento04 = filtro01['Nível de envolvimento com o trabalho'].value_counts()
agrupamento04 = pd.DataFrame(agrupamento04)
display(agrupamento04)

agrupamento05 = rh['Nível de envolvimento com o trabalho'].value_counts()
agrupamento05 = pd.DataFrame(agrupamento05)
display(agrupamento05)

# Correlacioando os funcionários demitidos com o Nível hieráquico
agrupamento06 = filtro01['Nível hierárquico'].value_counts()
agrupamento06 = pd.DataFrame(agrupamento06)
display(agrupamento06)

#Qual o nível de satisfação dos funcionário demitidos no departamento de pesquisa e desenvolvimento?
pesdev = filtro01.loc[filtro01['Departamento'] == 'Pesquisa e Desenvolvimento']
correlacao = pesdev.groupby('Nível de Satisfação com o ambiente de trabalho')['Departamento']
tabelacor = pd.DataFrame(correlacao.count())
display(tabelacor)

#Qual o cargo dos funcionário demitidos no departamento de pesquisa e desenvolvimento?
pesdev = filtro01.loc[filtro01['Departamento'] == 'Pesquisa e Desenvolvimento']
correlacao = pesdev.groupby('Cargo')['Departamento']
tabelacor = pd.DataFrame(correlacao.count())
display(tabelacor)

#Qual o percentual de aumento de salário dos funcionário demitidos no departamento de pesquisa e desenvolvimento?
pesdev = filtro01.loc[filtro01['Departamento'] == 'Pesquisa e Desenvolvimento']
correlacao = pesdev.groupby('percentual de aumento de salário')['Departamento']
tabelacor = pd.DataFrame(correlacao.count())
display(tabelacor)

# Qual o percentual de aumento de salário para cada departameto?
correlacao02 = filtro01.groupby('Departamento')['percentual de aumento de salário']
tabelacor02 = pd.DataFrame(correlacao02.mean())
display(tabelacor02)

# Correlação demissões e renda mensal
agrupamento7 = rh.groupby('Demissão')['Renda mensal']
agrupamento7.describe()

# Frequência do percentual de aumento de salário dos demitidos

Cont = filtro01['percentual de aumento de salário'].value_counts() # aqui estamos criando um objeto com a contagem de todos os valores únicos da variável de interesse
percentual = filtro01['percentual de aumento de salário'].value_counts(normalize=True)*100 # aqui estamos criando um objeto com a contagem percentual de todos os valores únicos da variável de interesse
tabela = pd.DataFrame({'Frequência Absoluta':Cont,'Frequência Percentual':percentual})

tabela = tabela.sort_values(by='percentual de aumento de salário')
tabela.reset_index(inplace=True)

faixas = ['10% a 15%','15% a 20%','20% a 25%']
tabela['faixa_de_percentual'] = pd.cut(x=tabela['percentual de aumento de salário'],bins=[10,15,20,25],labels=faixas)

freq = filtro01['faixa_de_percentual'].value_counts()  # Criando uma contagem dos valores em cada faixa
freq1 = filtro01['faixa_de_percentual'].value_counts(normalize=True)*100  # Criando o percentual dos valores dentro das faixas
freq1 = pd.DataFrame({'Frêquencia':freq,'Frequência Percentual':freq1}) # Criando um dataframe com a frequencia e o percentual
display(freq1)

# Total de anos trabalhados na empresa para demitidos

Cont1 = filtro01['Total de anos trabalhados na empresa'].value_counts() # aqui estamos criando um objeto com a contagem de todos os valores únicos da variável de interesse
percentual = filtro01['Total de anos trabalhados na empresa'].value_counts(normalize=True)*100 # aqui estamos criando um objeto com a contagem percentual de todos os valores únicos da variável de interesse
tabela1 = pd.DataFrame({'Frequência Absoluta':Cont1,'Frequência Percentual':percentual})

tabela1 = tabela1.sort_values(by='Total de anos trabalhados na empresa')
tabela1.reset_index(inplace=True)

anos = ['0 a 2', '2 a 5', '5 a 10','10 a 20','20 a 30','30 a 40']
filtro01['faixa_de_anos'] = pd.cut(x=filtro01['Total de anos trabalhados na empresa'],bins=[0,2,5,10,20,30,40],labels=anos)

freq = filtro01['faixa_de_anos'].value_counts()  # Criando uma contagem dos valores em cada faixa
freq1 = filtro01['faixa_de_anos'].value_counts(normalize=True)*100  # Criando o percentual dos valores dentro das faixas
freq1 = pd.DataFrame({'Frêquencia':freq,'Frequência Percentual':freq1}) # Criando um dataframe com a frequencia e o percentual
display(freq1)

# @title Frêquencia

from matplotlib import pyplot as plt
freq1['Frêquencia'].plot(kind='line', figsize=(8, 4), title='Frêquencia')
plt.gca().spines[['top', 'right']].set_visible(False)

"""# Conclusões

"""

'''
O departamento de Pesquisa e Desenvolvimento possui o maior número de demissões, sendo que o cargo onde há mais demitidos é o de técnico de laboratório.
'''
'''
O nível de envolvimento com o trabalho parece não ter muita correlação com as demissões, pois a maioria dos funcionários demitidos relataram nível 3, ou seja, bom.
'''
'''
Percentual de aumento de salário não parece estar relacionado, pois o departamento com mais demissões teve o maior percentual de aumento.
A média de renda mensal dos demitidos é menor do que dos não demitidos, mas isso parece ser pelo fato da maioria dos demitidos serem de cargos mais baixos.
'''
'''
A maioria dos funcionários se demitem nos primeiros dois anos de empresa.
'''