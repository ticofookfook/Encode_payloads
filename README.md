# Encode string and Files

Este programa em Python permite codificar strings em diferentes formatos como URL encode, Base64, Hexadecimal, HTML Entity, Quoted-Printable, Punycode, MIME, e Unicode.

## Requisitos

- Python 3.x

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git

2. Navegue para o diretório do projeto:
    cd seu-repositorio

3. Instale os requeriments
    pip3 install -r requirements.txt


Uso
Você pode usar o programa de várias maneiras, conforme descrito abaixo:

- Codificação de uma string diretamente:

python seu_script.py -s "sua string aqui" --urlencode --base64 --htmlentity

- Codificação de um arquivo:

python seu_script.py -w seu_arquivo.txt --all


Opções disponíveis:
-s, --string: Especifica a string a ser codificada.
-w, --file: Especifica o arquivo contendo a string a ser codificada.
-uni, --unicode: Codifica a string em Unicode.
-url, --urlencode: Codifica a string em URL encode.
-b64, --base64: Codifica a string em Base64.
-hex, --hex: Codifica a string em Hexadecimal.
-html, --htmlentity: Codifica a string em HTML Entity.
-mime, --mime: Codifica a string em MIME.
-all, --all: Codifica a string usando todos os métodos disponíveis.
-n, --num, default=1, help='Número de vezes para codificar payloads para URL (padrão: 1)
