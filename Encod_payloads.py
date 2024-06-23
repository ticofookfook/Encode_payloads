import argparse
from urllib.parse import quote
import base64
import binascii
import quopri
from html import escape
import os

substitutions = {
    '<': '\\u{0:04x}'.format(ord('<')),
    '>': '\\u{0:04x}'.format(ord('>')),
    '/': '\\u{0:04x}'.format(ord('/')),
    '[': '\\u{0:04x}'.format(ord('[')),
    ']': '\\u{0:04x}'.format(ord(']')),
    '^': '\\u{0:04x}'.format(ord('^')),
    '?': '\\u{0:04x}'.format(ord('?')),
    ':': '\\u{0:04x}'.format(ord(':')),
    ';': '\\u{0:04x}'.format(ord(';')),
    '.': '\\u{0:04x}'.format(ord('.')),
    ',': '\\u{0:04x}'.format(ord(',')),
    '`': '\\u{0:04x}'.format(ord('`')),
    '´': '\\u{0:04x}'.format(ord('´')),
    '~': '\\u{0:04x}'.format(ord('~')),
    '-': '\\u{0:04x}'.format(ord('-')),
    '+': '\\u{0:04x}'.format(ord('+')),
    '=': '\\u{0:04x}'.format(ord('=')),
    '_': '\\u{0:04x}'.format(ord('_')),
    ')': '\\u{0:04x}'.format(ord(')')),
    '(': '\\u{0:04x}'.format(ord('(')),
    '*': '\\u{0:04x}'.format(ord('*')),
    '&': '\\u{0:04x}'.format(ord('&')),
    '¨': '\\u{0:04x}'.format(ord('¨')),
    '%': '\\u{0:04x}'.format(ord('%')),
    '$': '\\u{0:04x}'.format(ord('$')),
    '#': '\\u{0:04x}'.format(ord('#')),
    '@': '\\u{0:04x}'.format(ord('@')),
    '!': '\\u{0:04x}'.format(ord('!')),
    '\"': '\\u{0:04x}'.format(ord('\"')),
    '\'': '\\u{0:04x}'.format(ord('\'')),
    '|': '\\u{0:04x}'.format(ord('|')),
    '\\': '\\u{0:04x}'.format(ord('\\'))
    
    
}


parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-s', '--string', help='String para codificar em Unicode ou URL encode')
group.add_argument('-f', '--file', help='Nome do arquivo para codificar')
parser.add_argument('-uni', '--unicode', action='store_true', help='Codificar em Unicode')
parser.add_argument('-url', '--urlencode', action='store_true', help='Codificar em URL encode')
parser.add_argument('-b64', '--base64', action='store_true', help='Codificar em Base64')
parser.add_argument('-hex', '--hex', action='store_true', help='Codificar em Hexadecimal')
parser.add_argument('-html', '--htmlentity', action='store_true', help='Codificar em HTML Entity')
parser.add_argument('-mime', '--mime', action='store_true', help='Codificar em MIME')
parser.add_argument('-all', '--all', action='store_true', help='Codificar usando todos os métodos')
parser.add_argument('-n', '--num', type=int, default=1, help='Número de vezes para codificar payloads para URL (padrão: 1)')
args = parser.parse_args()

if args.string:
    input_string = args.string
elif args.file:
    try:
        with open(args.file, 'r') as file:
            input_string = file.read()
    except FileNotFoundError:
        print("Arquivo não encontrado!")
        exit()

def write_to_file(filename, content):
    directory = "encodes"
    if not os.path.exists(directory):
        os.makedirs(directory)
    filepath = os.path.join(directory, filename)
    with open(filepath, "a") as file:
        file.write(content + '\n')

def encode_url(input_string):
    lines = input_string.splitlines()
    for line in lines:
        url_encoded = line
        for _ in range(args.num):
            url_encoded = quote(url_encoded)
        write_to_file("Urlencode_.txt", url_encoded)

def encode_base64(input_string):
    lines = input_string.splitlines()
    for line in lines:
        base64_encoded = base64.b64encode(line.encode()).decode()
        write_to_file("Base64_.txt", base64_encoded)

def encode_hex(input_string):
    lines = input_string.splitlines()
    for line in lines:
        hex_encoded = binascii.hexlify(line.encode()).decode()
        write_to_file("Hex_.txt", hex_encoded)

def encode_html_entity(input_string):
    lines = input_string.splitlines()
    for line in lines:
        html_encoded = escape(line)
        write_to_file("HtmlEntity_.txt", html_encoded)


def encode_mime(input_string):
    lines = input_string.splitlines()
    for line in lines:
        mime_encoded = quopri.encodestring(line.encode()).decode()
        write_to_file("MIME_.txt", mime_encoded)

def encode_unicode(input_string):
    unicode_string = ''
    for char in input_string:
        unicode_string += substitutions.get(char, char)
    write_to_file("Unicode_.txt", unicode_string)

# Codificação URL
if args.urlencode:
    encode_url(input_string)

# Codificação Base64
if args.base64:
    encode_base64(input_string)

# Codificação Hexadecimal
if args.hex:
    encode_hex(input_string)

# Codificação HTML Entity
if args.htmlentity:
    encode_html_entity(input_string)



# Codificação MIME
if args.mime:
    encode_mime(input_string)

# Codificação Unicode
if args.unicode:
    encode_unicode(input_string)

# Codificação All
if args.all:
    encode_url(input_string)
    encode_base64(input_string)
    encode_hex(input_string)
    encode_html_entity(input_string)
    encode_mime(input_string)
    encode_unicode(input_string)






