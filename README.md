# TCC2
## Projeto para obtenção de menção no tcc2 da UnB - FGA.
Os dados do arquivos .csv e excel são fictícios para teste das funcionalidades da ferramenta.

## Uma ferramenta para o STMA (SISTEMA DE TRATAMENTO DE MENSAGENS AERONÁUTICAS):
O programa trata-se de uma ferramenta web, com a finalidade de fazer um melhor gerenciamento dos endereços telegráficos nacionais.
Possui filtros, dados estatísticos e a possibilidade de inserir novos dados.

### Para instalar a ferramenta:
- Baixe os arquivos no botão verde <> Code e clique em Download ZIP;
- Descompacte o arquivo .ZIP;

![This is an image](https://github.com/gabrielaggn/tcc2/blob/main/imagens/Sem%20t%C3%ADtulo.png)

- certifique-se que todos os arquivos encontram-se na mesma pasta;
- instale as seguintes bibliotecas dos arquivos .py, caso ainda não estejam instaladas:  Pandas, Streamlit, PIL,  numpy, io, pyxlsb, Matplotlib e Datetime no terminal anaconda (ex: pip install SomePackage);

![This is an image](https://github.com/gabrielaggn/tcc2/blob/main/imagens/pip_install.png)

- abra o terminal anaconda prompt, ou em outro interpretador python3, dentro da pasta tcc2-main e digite o seguinte comando: streamlit run appStreamlit.py;

![This is an image](https://github.com/gabrielaggn/tcc2/blob/main/imagens/streamlit.png)

- Após isso, o app irá abrir no seu navegador principal.

### Para navegar na ferramenta:
1. A ferramenta possui 3 telas: Consultar Endereços, Dados Estatísticos e Inserir Dados;

![This is an image](https://github.com/gabrielaggn/tcc2/blob/main/imagens/tela_principal.png)

2. Na tela "Consultar Endereços", na barra lateral é possível clicar em "Mostrar Tabela" ou "Órgãos DECEA";
![This is an image](https://github.com/gabrielaggn/tcc2/blob/main/imagens/filtros.png)

3. Ao clicar em "Órgãos DECEA" é possível visualizar a tabela que consta na MCA 102-7, com os órgãos existentes;

![This is an image](https://github.com/gabrielaggn/tcc2/blob/main/imagens/tela_principal.png)

4. Ao clicar em "Mostrar Tabela", é possível fazer filtros por endereço "COMMON NAME", ao selecionar "Todas", é possível visualizar todos os endereços existentes. No botão "Download data as EXCEL" é possível fazer o download da tabela filtrada ou completa se for selecionado "Todas";

![This is an image](https://github.com/gabrielaggn/tcc2/blob/main/imagens/mostrar_tabela.png)

5. Ao clicar em "Adicionar Mais Filtro", é possível selecionar por qual ou quais colunas deseja filtrar. A Tabela filtrada irá aparecer em "Filtro Geral";

![This is an image](https://github.com/gabrielaggn/tcc2/blob/main/imagens/add_filtros.png)

![This is an image](https://github.com/gabrielaggn/tcc2/blob/main/imagens/add_filtros2.png)

6. Na tela "Dados Estatísticos" é possivel visualizar gráficos e tabelas sobre os endereços;

![This is an image](https://github.com/gabrielaggn/tcc2/blob/main/imagens/dados_est.png)

8. Na tela "Inserir Dados" possui um formulário para inserir novos dados de algum endereço; e

![This is an image](https://github.com/gabrielaggn/tcc2/blob/main/imagens/inserir_dados.png)

9. Na primeira caixa é possível selecionar o endereço o qual deseja atualizar os dados.

![This is an image](https://github.com/gabrielaggn/tcc2/blob/main/imagens/add_filtros2.png)




