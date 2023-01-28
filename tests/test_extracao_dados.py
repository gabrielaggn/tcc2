import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb
import streamlit as st
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

def test_extrair_df():
    
    #relação nova
    relacao_enderecos = pd.read_csv(r'ldif2csv.csv')
    #pegar apenas as colunas necessárias
    relacao_enderecos = relacao_enderecos[['channel','createTimestamp','modifyTimestamp','mHSCommonName','redirect']]

    #transformar o formato da data de criação para yyyy-mm-dd
    relacao_enderecos['createTimestamp']  = relacao_enderecos['createTimestamp'].apply(lambda x : x.split('.')[0])
    relacao_enderecos['createTimestamp'] = relacao_enderecos['createTimestamp'].apply(lambda x : f'{x[0:4]}-{x[4:6]}-{x[6:8]}')


    #colocar o alias no espaço vazio
    relacao_enderecos['channel'].fillna('Alias', inplace=True)
    #substituir os espaços vazios na coluna modifytimestamp
    relacao_enderecos['modifyTimestamp'].fillna('00000000000000.000000000Z', inplace=True)
    #substituir os espaços vazios em redirect por 'nao esta desviado'
    relacao_enderecos['redirect'].fillna('Não está desviado', inplace=True)
    #retirar as linhas com espaços vazios
    relacao_enderecos = relacao_enderecos.dropna()
    #colocar em ordem alfabética
    relacao_enderecos = relacao_enderecos.sort_values(by='mHSCommonName')

    #modificar o formato de data na coluna modifytimestamp para formato de data
    relacao_enderecos['modifyTimestamp']  = relacao_enderecos['modifyTimestamp'].apply(lambda x : x.split('.')[0])
    relacao_enderecos['modifyTimestamp'] = relacao_enderecos['modifyTimestamp'].apply(lambda x : f'{x[0:4]}-{x[4:6]}-{x[6:8]}')


    #transformando para o tipo data

    relacao_enderecos['createTimestamp'] = pd.to_datetime(relacao_enderecos['createTimestamp'], format='%Y-%m-%d')
    
    #remover valores duplicados
    relacao_enderecos = relacao_enderecos.drop_duplicates(subset='mHSCommonName', keep='first')

    #pegar planilha anterior
    relacao_antiga = pd.read_excel('Planilha_antiga.xlsx')

    #deletar colunas que tem na planilha nova
    del relacao_antiga['Unnamed: 0']
    del relacao_antiga['channel']
    del relacao_antiga['createTimestamp']
    del relacao_antiga['modifyTimestamp']
    del relacao_antiga['redirect']

    #juntar o dataframes com os comum names da tabela nova
    relacao_enderecos = pd.merge(relacao_enderecos, relacao_antiga, how = 'left', on = 'mHSCommonName')
    relacao_enderecos = relacao_enderecos.drop_duplicates(subset='mHSCommonName', keep='first')

    #tirar os espaços vazios
    relacao_enderecos['Localidade'].fillna('Não foi registrado', inplace=True)
    relacao_enderecos['Órgão'].fillna('Não foi registrado', inplace=True)
    relacao_enderecos['Número SIGAD'].fillna('Não foi registrado', inplace=True)
    relacao_enderecos['Doc de \nReferência'].fillna('Não foi registrado', inplace=True)
    relacao_enderecos['Contato'].fillna('Não foi registrado', inplace=True)
    
    assert "relacao_enderecos" == "relacao_enderecos"

def test_extrair_df_orgaos():
    orgaos = pd.read_excel('orgãoDECEA (1).xlsx')
    assert "orgaos" == "orgaos"

def transformar_excel(dataframe):
    # determinando o nome do arquivo
    nome_arquivo = 'Planilha_antiga.xlsx'
  
    # saving the excel
    pd.read_csv(dataframe).to_excel(nome_arquivo)
    #print('DataFrame is written to Excel File successfully.')
    return dataframe

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    writer.save()
    processed_data = output.getvalue()
    return processed_data

#funçao para filtro geral
def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adiciona a UI no dataframe para o usuário filtrar colunas
    Args:
        df (pd.DataFrame): dataframe original
    Returns:
        pd.DataFrame: dataframe filtrado
    """
    modify = st.sidebar.checkbox("Adicione Mais Filtros")

    if not modify:
        return df

    df = df.copy()

    # Try to convert datetimes into a standard format (datetime, no timezone)
    for col in df.columns:
        if is_object_dtype(df[col]):
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass

        if is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)

    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.sidebar.multiselect("Filtre a tabela por:", df.columns)
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            # Treat columns with < 10 unique values as categorical
            if is_categorical_dtype(df[column]) or df[column].nunique() < 10:
                
                user_cat_input = st.sidebar.multiselect(
                    f"Valores para {column}",
                    df[column].unique(),
                   	default=list(df[column].unique()),
                )
                df = df[df[column].isin(user_cat_input)]
            elif is_numeric_dtype(df[column]):
                _min = float(df[column].min())
                _max = float(df[column].max())
                step = (_max - _min) / 100
                user_num_input = st.sidebar.slider(
                    f"Valores para {column}",
                    min_value=_min,
                    max_value=_max,
                    value=(_min, _max),
                    step=step,
                )
                df = df[df[column].between(*user_num_input)]
            elif is_datetime64_any_dtype(df[column]):
                user_date_input = st.sidebar.date_input(
                    f"Valores para {column}",
                    value=(
                        df[column].min(),
                        df[column].max(),
                    ),
                )
                if len(user_date_input) == 2:
                    user_date_input = tuple(map(pd.to_datetime, user_date_input))
                    start_date, end_date = user_date_input
                    df = df.loc[df[column].between(start_date, end_date)]
            else:
                user_text_input = st.sidebar.text_input(
                    f"Substring or regex in {column}",
                )
                if user_text_input:
                    df = df[df[column].astype(str).str.contains(user_text_input)]

    return df 


