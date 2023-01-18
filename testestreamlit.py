import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import extracao_dados as ed
from streamlit_option_menu import option_menu
from PIL import Image
import datetime
import numpy as np

st.set_page_config(page_title="Relação de Endereços", page_icon=":bar_chart", layout="wide", initial_sidebar_state="expanded")

with open('style.css') as f:
    st.markdown(f"<style>f.read()</style>", unsafe_allow_html = True)

#pegar o df 
relacao_enderecos = ed.extrair_df()
orgaos = ed.extrair_df_orgaos()




# função para selecionar a quantidade de linhas do dataframe
def mostra_qntd_linhas(dataframe):

    #qntd_linhas = st.sidebar.slider('Selecione a quantidade de linhas que deseja mostrar na tabela', min_value = 1, max_value = len(dataframe), step = 1)

    st.write(dataframe.style.format(subset = ['createTimestamp'], formatter="{:%Y/%m/%d}"))
    
    st.write('Foram encontrados %d registros!'%(len(dataframe.index)))

    df_xlsx = ed.to_excel(dataframe)

    st.download_button(
        label="📥 Download data as EXCEL",
        data=df_xlsx,
        file_name='Planilha_filtrada.xlsx'
    )

#menu horizontal (navbar)

selected = option_menu(
    menu_title=None, 
    options=["Consultar Endereços", "Dados Estatísticos", "Inserir Dados"], 
    icons=["person-fill","graph-up","journal-text"], 
    menu_icon="cast", 
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#D9D9D9"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-size": "20px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "blue"},

    }
)    



#-----------------botão Consultar Endereços-----------------------
if selected == 'Consultar Endereços':
    st.title("✈️ Endereços CTMA")
    st.markdown('##')

    # filtros para a tabela
    image = Image.open('logo.png')
    st.sidebar.image(image, width=100, use_column_width=39)

    checkbox_mostrar_tabela = st.sidebar.checkbox('Mostrar tabela')
    checkbox_mostrar_orgaos = st.sidebar.checkbox('Mostrar Orgãos Decea')

    #se clicar em mostrar tabela:
    if checkbox_mostrar_tabela:
        
        #criar um subtitulo no app
        st.markdown('## Tabela com a relação de endereços do CTMA, para anáslise dos dados:')
        st.markdown('### Filtro por endereço:')
        st.sidebar.markdown('## Filtro para a tabela')
        #filtro para o nome comum
        nome_comum = list(relacao_enderecos['mHSCommonName'].unique())
        nome_comum.append('Todas')

        nome_comum2 = st.sidebar.selectbox('Selecione o nome comum do endereço para apresentar na tabela', options = nome_comum)

        if nome_comum2 != 'Todas':
            df_nome_comum = relacao_enderecos.query('mHSCommonName == @nome_comum2')
            mostra_qntd_linhas(df_nome_comum)      
        else:
            mostra_qntd_linhas(relacao_enderecos)
        

        st.markdown('### Filtro Geral')
         
        relacao_enderecos_filtro = ed.filter_dataframe(relacao_enderecos)
        st.write(relacao_enderecos_filtro.style.format(subset = ['createTimestamp'], formatter="{:%Y/%m/%d}"))

        #botão de download
        df_xlsx = ed.to_excel(relacao_enderecos_filtro)

        st.write('Foram encontrados %d registros!'%(len(relacao_enderecos_filtro.index)))

        st.download_button(
            label="📥 Download data as EXCEL",
            data=df_xlsx,
            file_name='Planilha_filtrada.xlsx'
        )
        
    
    #se clicar em mostrar orgãos:
    if checkbox_mostrar_orgaos:
        #criar um subtitulo no app
        st.write('Tabela com a relação de órgãos do anexo D da MCA 102-7:')
        st.dataframe(orgaos)

#-----------------botão Dados Estatísticos-----------------------
if selected == 'Dados Estatísticos':
    st.title(":bar_chart: Dados estatísticos e gráficos")
    st.markdown('##')
    
    #ocorrencias de cada canal
    st.write('Quantidade de endereços para cada canal:')
    occur_canal = relacao_enderecos['channel'].value_counts()
    occur_canal = pd.DataFrame(occur_canal)
    st.dataframe(occur_canal)
    occur_canal = relacao_enderecos['channel'].value_counts()
    occur_canal.plot(figsize=(8,5), kind='bar')
    plt.legend()
    plt.title('Quantidade de endereços por canal')

    plt.show()
    st.pyplot(plt)
    
    #ocorrencias de cada localidade
    st.write('Quantidade de endereços para cada Localidade:')
    occur_local = relacao_enderecos['Localidade'].value_counts()
    occur_local = pd.DataFrame(occur_local)
    st.dataframe(occur_local)
    occur_local[1:6].plot(figsize=(8,5), kind='bar')
    plt.legend()
    plt.title('TOP 5 localidades com mais endereços')
    plt.show()
    st.pyplot(plt)
    
#-----------------botão Inserir Dados-------------------------
if selected == 'Inserir Dados':
    st.title(f"📓 Inserir dado de um endereço")
    #formulário para inserir dados
    with st.form(key="include_dados"):
        nome_comum = list(relacao_enderecos['mHSCommonName'].unique())
        nome_comum2 = st.selectbox('Selecione o nome comum do endereço que deseja inserir dados:', options = nome_comum)
        input_contato = st.text_input(label="Insira o contato do endereço")
        input_orgao = st.text_input(label="Insira o orgão do endereço")
        input_localidade = st.text_input(label="Insira a localidade do endereço")
        input_sigad = st.text_input(label="Insira o sigad que solicitou o endereço")
        input_doc = st.text_input(label="Insira o documento que solicitou o endereço")
        input_button_submit = st.form_submit_button("Enviar")
    
    #inserir os dados novos no arquivo excel para atualizar dados caso o botão enviar seja clicado
    if input_button_submit:
        if (input_contato=="") or (input_orgao=="") or (input_localidade=="") or (input_sigad=="") or (input_doc==""):
            st.error("Não deixe espaço em branco, caso o dado não esteja disponível, escreva: Não encontrado. ❌") 
        else:
            st.success("Os dados foram inseridos com sucesso! ✔️")
            st.write(f'Endereço: {nome_comum2}')
            st.write(f'Contato: {input_contato}')
            st.write(f'Órgao: {input_orgao}')
            st.write(f'Localidade: {input_localidade}')
            st.write(f'Sigad: {input_sigad}')
            st.write(f'doc: {input_doc}')
            relacao_enderecos.loc[relacao_enderecos['mHSCommonName'] == nome_comum2, 'Contato'] = input_contato
            relacao_enderecos.loc[relacao_enderecos['mHSCommonName'] == nome_comum2, 'Órgão'] = input_orgao
            relacao_enderecos.loc[relacao_enderecos['mHSCommonName'] == nome_comum2, 'Localidade'] = input_localidade
            relacao_enderecos.loc[relacao_enderecos['mHSCommonName'] == nome_comum2, 'Número SIGAD'] = input_sigad
            relacao_enderecos.loc[relacao_enderecos['mHSCommonName'] == nome_comum2, 'Doc de \nReferência'] = input_doc
            #st.dataframe(relacao_enderecos)     

            ed.transformar_excel(relacao_enderecos)       




    
        