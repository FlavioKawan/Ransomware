import pyaes
import os


file_nome = "arquivo.txt.byte"
file = open(file_nome , "rb")
file_data = file.read()
file.close()




key = b"criptografar1234"
pes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = pes.encrypt(file_data)


os.remove(file_nome)



new_file = "arquivo.txt"
new_file = open(f'{new_file}' , 'wb')
new_file.write(decrypt_data)
new_file.close()