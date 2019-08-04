from totalvoice.cliente import Cliente
import requests

api_totalvoice = Cliente("089f722451983a4ef92db0e5eba812b0", 'api.totalvoice.com.br')

src_number = '48996516004'
dst_number = '48996516005'

response = api_totalvoice.chamada.enviar(src_number, dst_number, gravar_audio=True)
print(response)






