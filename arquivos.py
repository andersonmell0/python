import requests
import os

# URL do arquivo que você deseja baixar
url = 'https://idb.prodeb.ba.gov.br/Relatorios/xlspaHomologado'

# Diretório onde você deseja salvar o arquivo
diretorio_destino = 'c:/diretorio'

# Nome do arquivo após o download (pode manter o mesmo nome ou escolher outro)
nome_arquivo = 'arquivo.xlsx'

# Combinação do diretório de destino e o nome do arquivo
caminho_completo = os.path.join(diretorio_destino, nome_arquivo)

# Download do arquivo
response = requests.get(url)

# Verifica se foi bem-sucedido (código de status 200)
if response.status_code == 200:
    # Abre o arquivo no modo binário e escreva os dados baixados nele
    with open(caminho_completo, 'wb') as arquivo:
        arquivo.write(response.content)
    print(f'O arquivo foi baixado e salvo em: {caminho_completo}')
else:
    print('Falha ao baixar o arquivo.')