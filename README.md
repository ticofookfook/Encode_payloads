# Encode string and Files

Este programa em Python permite codificar strings e arquivos em diferentes formatos como URL encode, Base64, Hexadecimal, HTML Entity, MIME, e Unicode.</br>

## Requisitos

- Python 3.x</br>

## Instalação

1. Clone o repositório:</br>
   ```bash</br>
   git clone https://github.com/ticofookfook/Encode_payloads.git

2. Navegue para o diretório do projeto:</br>
    cd Encode_payloads</br>

3. Instale os requeriments</br>
    pip3 install -r requirements.txt</br>

## OBS

Url encode tem a opção -n que por padrão vem 1 que é o numero de vezes que ele vai encodar, pode passar quantas quiser</br>

Uso
Você pode usar o programa de várias maneiras, conforme descrito abaixo:</br>

- Codificação de uma string diretamente:</br>

python seu_script.py -s "sua string aqui" --urlencode --base64 --htmlentity</br>

- Codificação de um arquivo:</br>

python seu_script.py -w seu_arquivo.txt --all</br>


Opções disponíveis:</br>
-s, --string: Especifica a string a ser codificada.</br>
-w, --file: Especifica o arquivo contendo a string a ser codificada.</br>
-uni, --unicode: Codifica a string em Unicode.</br>
-url, --urlencode: Codifica a string em URL encode.</br>
-b64, --base64: Codifica a string em Base64.</br>
-hex, --hex: Codifica a string em Hexadecimal.</br>
-html, --htmlentity: Codifica a string em HTML Entity.</br>
-mime, --mime: Codifica a string em MIME.</br>
-all, --all: Codifica a string usando todos os métodos disponíveis.</br>
-n, --num, default=1, help='Número de vezes para codificar payloads para URL (padrão: 1)</br>
