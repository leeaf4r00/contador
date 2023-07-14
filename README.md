Contador de Moedas
Este é um script em Python que permite contar e armazenar a quantidade de moedas e cédulas, além de gerar relatórios com os valores totais.

Requisitos
Python 3.x
Biblioteca Tkinter
Biblioteca sqlite3
Certifique-se de ter o Python instalado em seu ambiente e as bibliotecas necessárias instaladas antes de executar o script.

Funcionalidades
O script possui as seguintes funcionalidades:

Contagem de moedas: permite inserir a quantidade de moedas para diferentes valores e armazená-las em um banco de dados.
Contagem de cédulas: permite inserir a quantidade de cédulas para diferentes valores e armazená-las em um banco de dados.
Inserção manual de moedas: permite inserir manualmente a descrição, quantidade e valor de uma moeda e armazená-la no banco de dados.
Inserção manual de cédulas: permite inserir manualmente a descrição, quantidade e valor de uma cédula e armazená-la no banco de dados.
Geração de relatório: exibe um relatório com o total de valor das moedas e cédulas armazenadas no banco de dados.
Utilização
Certifique-se de ter o Python 3.x instalado.

Instale as bibliotecas necessárias executando o seguinte comando no terminal:

Copy code
pip install tkinter sqlite3
Copie o código do script contador de moedas para um arquivo com extensão ".py".

Execute o arquivo Python utilizando o comando:

Copy code
python arquivo.py
A interface gráfica será exibida, permitindo que você insira a quantidade de moedas e cédulas, ou insira manualmente os valores.

Para gerar um relatório, clique no botão "Gerar relatório".

Banco de Dados
O script utiliza um banco de dados SQLite chamado "controle_moedas_cedulas.db" para armazenar as informações das moedas e cédulas. As tabelas "MOEDAS" e "CEDULAS" são criadas automaticamente se não existirem.

Limitações
O script está configurado para lidar com um conjunto específico de valores de moedas e cédulas. Se desejar modificar ou adicionar novos valores, será necessário ajustar o código manualmente.
A interface gráfica não possui validação de entrada, portanto, certifique-se de inserir apenas valores numéricos válidos.
O relatório é exibido em uma janela separada e não é salvo em um arquivo.
O script não possui tratamento de erros abrangente.
Certifique-se de ler o código e compreender seu funcionamento antes de utilizá-lo.
