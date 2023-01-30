import os
import pyaes


file_nome = "arquivo.txt"
file = open(file_nome, "rb")
file_data = file.read()
file.close()


os.remove(file_nome)


key = b"criptografar1234"
pes = pyaes.AESModeOfOperationCTR(key)
crypto_data = pes.encrypt(file_data)



new_file = file_nome + ".byte"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
