import pandas as pd

pd.set_option('display.max_columns', 500)

df_raw = pd.read_csv('data/raw/State of Data 2021 - Dataset.csv', low_memory=False)

cols = ["('P1_a ', 'Idade')",
        "('P1_b ', 'Genero')",
        "('P1_e ', 'Estado onde mora')",
        "('P1_e_a ', 'uf onde mora')",
        "('P1_e_b ', 'Regiao onde mora')",
        "('P1_h ', 'Nivel de Ensino')",
        "('P1_i ', 'Área de Formação')",
        "('P2_f ', 'Cargo Atual')",
        "('P2_g ', 'Nivel')",
        "('P2_h ', 'Faixa salarial')",
        "('P2_i ', 'Quanto tempo de experiência na área de dados você tem?')",
        "('P2_q ', 'Atualmente qual a sua forma de trabalho?')"]
        
name = ['Idade', 'Genero', 'Estado', 'UF', 'Regiao', 'Nivel de Ensino', 'Area de Formacao',
        'Cargo', 'Nivel', 'Faixa Salarial', 'Tempo de Experiencia', 'Forma de Trabalho']

df = df_raw[cols].copy()
df.columns = name

# Estados
df.replace('Alagoas (AL)', 'Alagoas', inplace=True)
df.replace('Bahia (BA)', 'Bahia', inplace=True)
df.replace('Ceará (CE)', 'Ceará', inplace=True)
df.replace('Distrito Federal (DF)', 'Distrito Federal', inplace=True)
df.replace('Espírito Santo (ES)', 'Espírito Santo', inplace=True)
df.replace('Goiás (GO)', 'Goiás', inplace=True)
df.replace('Maranhão (MA)', 'Maranhão', inplace=True)
df.replace('Mato Grosso (MT)', 'Mato Grosso', inplace=True)
df.replace('Mato Grosso do Sul (MS)', 'Mato Grosso do Sul', inplace=True)
df.replace('Minas Gerais (MG)', 'Minas Gerais', inplace=True)
df.replace('Paraná (PR)', 'Paraná', inplace=True)
df.replace('Paraíba (PB)', 'Paraíba', inplace=True)
df.replace('Pernambuco (PE)', 'Pernambuco', inplace=True)
df.replace('Piauí (PI)', 'Piauí', inplace=True)
df.replace('Rio Grande do Norte (RN)', 'Rio Grande do Norte', inplace=True)
df.replace('Rio Grande do Sul (RS)', 'Rio Grande do Sul', inplace=True)
df.replace('Rio de Janeiro (RJ)', 'Rio de Janeiro', inplace=True)
df.replace('Santa Catarina (SC)', 'Santa Catarina', inplace=True)
df.replace('Sergipe (SE)', 'Sergipe', inplace=True)
df.replace('São Paulo (SP)', 'São Paulo', inplace=True)

# Cargos
df.replace('Engenheiro de Dados/Data Engineer', 'Engenheiro de Dados', inplace=True)
df.replace('Cientista de Dados/Data Scientist', 'Cientista de Dados', inplace=True)
df.replace('Analista de BI/BI Analyst/Analytics Engineer', 'Analista de BI', inplace=True)
df.replace('Analista de Negócios/Business Analyst', 'Analista de Negócios', inplace=True)
df.replace('Analista de Dados/Data Analyst', 'Analista de Dados', inplace=True)
df.replace('Desenvolvedor ou Engenheiro de Software', 'Desenvolvedor', inplace=True)
df.replace('Engenheiro de Machine Learning/ML Engineer', 'Engenheiro de Machine Learning', inplace=True)
df.replace('Outras Engenharias (não inclui dev)', 'Outras Engenharias', inplace=True)
df.replace('DBA/Administrador de Banco de Dados', 'Administrador de Banco de Dados', inplace=True)
df.replace('Analista de Sistemas/Analista de TI', 'Analista de Sistemas', inplace=True)
df.replace('Analista de Inteligência de Mercado/Market Intelligence', 'Analista de Inteligência de Mercado', inplace=True)
df.replace('Analista de Inteligência de Mercado/Market Intelligence', 'Analista de Inteligência de Mercado', inplace=True)

# Regiões
df.replace('Centro-oeste', 'Centro-Oeste', inplace=True)

# Cargos
df.replace('Arquiteto de dados', 'Arquiteto de Dados', inplace=True)


df.to_csv('data/processed/state-of-data-2021.csv', index=False)