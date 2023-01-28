# TCC2
## Projeto para obtenção de menção no tcc2 da UnB - FGA.
Os dados do arquivos .csv e excel são fictícios para teste das funcionalidades da ferramenta.

### Para instalar a ferramenta:
- Baixe os arquivos no botão verde <> Code e clique em Download ZIP;
- Descompacte o arquivo .ZIP;
![This is an image](https://github.com/gabrielaggn/tcc2/blob/main/imagens/Sem%20t%C3%ADtulo.png)

- certifique-se que todos os arquivos encontram-se na mesma pasta;
- instale as seguintes bibliotecas dos arquivos .py, caso ainda não estejam instaladas:  Pandas, Streamlit, PIL,  numpy, io, pyxlsb, Matplotlib e Datetime no terminal anaconda (ex: pip install SomePackage);
- abra o terminal anaconda prompt, ou em outro interpretador python3, dentro da pasta tcc2-main e digite o seguinte comando: streamlit run appStreamlit.py;
- Após isso, o app irá abrir no seu navegador principal.

### Para navegar na ferramenta:
- A ferramenta possui 3 telas: Consultar Endereços, Dados Estatísticos e Inserir Dados;
- Na tela "Consultar Endereços", na barra lateral é possível clicar em "Mostrar Tabela" ou "Órgãos DECEA";
- Ao clicar em "Órgãos DECEA" é possível visualizar a tabela que consta na MCA 102-7, com os órgãos existentes;
- Ao clicar em "Mostrar Tabela", é possível fazer filtros por endereço "COMMON NAME", ao selecionar "Todas", é possível visualizar todos os endereços existentes. No botão "Download data as EXCEL" é possível fazer o download da tabela filtrada ou completa se for selecionado "Todas";
- Ao clicar em "Adicionar Mais Filtro", é possível selecionar por qual ou quais colunas deseja filtrar. A Tabela filtrada irá aparecer em "Filtro Geral";
- Na tela "Dados Estatísticos" é possivel visualizar gráficos e tabelas sobre os endereços;
- Na tela "Inserir Dados" possui um formulário para inserir novos dados de algum endereço; e
- Na primeira caixa é possível selecionar o endereço o qual deseja atualizar os dados.





