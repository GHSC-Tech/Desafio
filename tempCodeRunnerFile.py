import pandas as pd
import numpy as np

# Supondo que você já carregou seu df:
df = pd.read_csv('funcionarios.csv')


# 1. Tenta converter 'bonus_percentual' para numérico, convertendo o que não for número em NaN
bonus_convertido = pd.to_numeric(df['bonus_percentual'], errors='coerce')

# 2. Filtra o DataFrame para manter APENAS as linhas onde a conversão FOI bem-sucedida (não é NaN)
df_filtrado = df[bonus_convertido.notna()].copy()

# 3. Atribui a Série numérica convertida de volta à coluna 'bonus_percentual' do DF limpo
# Usamos o .dropna() na Série convertida para garantir que ela se alinhe ao DF filtrado
df_filtrado['bonus_percentual'] = bonus_convertido.dropna()

# =================================================================
# Limpeza Adicional para a coluna 'salario' (Caso precise)
# =================================================================

# Se 'salario' também puder ter texto, você deve repetir o processo:
salario_convertido = pd.to_numeric(df_filtrado['salario'], errors='coerce')
df_final = df_filtrado[salario_convertido.notna()].copy()
df_final['salario'] = salario_convertido.dropna()

BONUS_BASE = 1000
df_final['bonus_final'] = BONUS_BASE + df_final['salario'] * df_final['bonus_percentual']


print("DF FINAL APÓS LIMPEZA:")
print(df_final)
print("-" * 50)
print("Tipos de Dados Finais:")
print(df_final.dtypes)