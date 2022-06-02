from IPython.display import display
import pandas as pd
ecom = pd.read_csv('Ecommerce Purchases')
# Checar head
check = ecom.head(3)
#display(check)

# Numero de linhas e colunas
n_linhas = len(ecom.index)
#print(n_linhas)
n_colunas = len(ecom.columns)
#print(n_colunas)

# Checar informação
#ecom.info()

# Preço de compra médio
compra_medio = ecom['Purchase Price'].mean()
#display(compra_medio)

# Maior e menor preço
maior_preco = ecom['Purchase Price'].max()
#display(maior_preco)
menor_preco = ecom['Purchase Price'].min()
#display(menor_preco)

# Quantas pessoas escolheram Ingles(en) no site
n_en = ecom[ecom['Language'] == 'en']['Language'].count()
#display(n_en)
#ecom[ecom['Language'] == 'en'].info()


# Quatos advogados
n_adv = ecom[ecom['Job'] == 'Lawyer']['Job'].count()
#display(n_adv)
n_adv2 = len(ecom[ecom['Job'] == 'Lawyer'].index)
#print(n_adv2)

# Compras de dia e de noite
n_dia_noite = ecom['AM or PM'].value_counts()
#display(n_dia_noite)

# 5 trabalhos mais comuns
cinco_trabalhos = ecom['Job'].value_counts().head(5)
#display(cinco_trabalhos)

# Preço da transação 90 WT
p_90wt = ecom[ecom['Lot'] == '90 WT']['Purchase Price']
#display(p_90wt)

# Email do dono do cartao: 4926535242672853
cartao_email = ecom[ecom['Credit Card'] == 4926535242672853]['Email']
#display(cartao_email)

# Utilizam cartao da American Express e fizeram compras acima de $95
n_ae_95 = ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count()['Credit Card']
#display(n_ae_95)

# Cartoes que vencem em 2025
cartao_25 = ecom[ecom['CC Exp Date'].apply(lambda str: str[3:] == '25')].count()[0]
#display(cartao_25)

# 5 emails mais populares
provedores = ecom['Email'].apply(lambda str: str.split('@')[1]).value_counts()
#display(provedores)
email_5 = provedores.head(5)
#display(email_5)


