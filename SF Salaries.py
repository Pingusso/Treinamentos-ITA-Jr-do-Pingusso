from IPython.display import display
import pandas as pd
sal = pd.read_csv('Salaries.csv')
# Checagem
check_2 = sal.head(2)
# display(check_2)

# Quantas entrdas há
# entradas = sal.info()

# Media salarial
media = sal['BasePay'].mean()
#display(media)

# Maximo de horia extra
maximo_Hora_Extra = sal['OvertimePay'].max()
#display(maximo_Hora_Extra)

# Cargo de Joseph Driscoll
cargo_JD = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']
#display(cargo_JD)

# Quanto Joseph Driscoll ganha
ganhos_JD = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']
#display(ganhos_JD)

# Pessoa com maior salário
maior_sal = sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName']
#display(maior_sal)

# Pessoa com menor salario
menor_sal = sal.iloc[sal['TotalPayBenefits'].argmin()]
#display(menor_sal)
menor_sal2 = sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]['EmployeeName']
#display(menor_sal2)

# Salario medio por ano
sal_medio_por_ano = sal.groupby('Year').mean()['BasePay']
#display(sal_medio_por_ano)

# Quantos cargos existem
cargos = sal['JobTitle'].nunique()
#display(cargos)

# Trabalhos mais comuns
cinco_mais_comuns = sal['JobTitle'].value_counts().head(5)
#display(cinco_mais_comuns)

# Numero de cargos com apenas um empregado em 2013
n_2013 = sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)
#display(n_2013)

# Quantos chefes existem?


def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False


n_chefes = sum(sal['JobTitle'].apply(lambda x: chief_string(x)))
#display(n_chefes)
