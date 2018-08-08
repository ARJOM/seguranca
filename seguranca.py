import os
import base64
import random
import struct
import hashlib

from Crypto.Cipher import AES
from Crypto import Random

arquivo = "imagem.jpg"
arquivo_decriptado = "imagem_decriptografada.jpg"
md5_arquivo = hashlib.md5(open(arquivo, 'rb').read()).hexdigest()
md5_arquivo_d = hashlib.md5(open(arquivo_decriptado, 'rb').read()).hexdigest()
if md5_arquivo == md5_arquivo_d:
    print("mesmo")
else:
    print("nao mesmo")

'''
arquivo_encriptado = "imagem_criptografada.jpg"
arquivo_decriptado = "imagem_decriptografada.jpg"

AES_length = 32
chave_secreta = str(input())
chave_secreta_string = base64.b64encode(chave_secreta)

parametro_iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
AES_cipher = AES.new(chave_secreta, AES.MODE_CBC, parametro_iv)
tamanho_arquivo = str(os.path.getsize(arquivo)).zfill(16)

tamanho_blocos = 64 * 1024

with open(arquivo, 'rb') as infile:

    with open(arquivo_encriptado, 'wb') as outfile:

        outfile.write(tamanho_arquivo)
        outfile.write(parametro_iv)

        while True:
            chunk = infile.read(tamanho_blocos)
            if len(chunk) == 0:
                break
            elif len(chunk) % 16 != 0:
                chunk += ' ' * (16 - len(chunk) % 16)

            outfile.write(AES_cipher.encrypt(chunk))

tamanho_blocos = 64 * 1024

with open(arquivo_encriptado, 'rb') as infile:

    tamanho_original = long(infile.read(16))

    parametro_iv = infile.read(16)

    AES_cipher = AES.new(chave_secreta, AES.MODE_CBC, parametro_iv)

    with open(arquivo_decriptado, 'wb') as outfile:
        while True:
            chunk = infile.read(tamanho_blocos)
            if len(chunk) == 0:
                break
            outfile.write(AES_cipher.decrypt(chunk))

        outfile.truncate(tamanho_original)
'''
