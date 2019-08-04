# This app makes a call between number A and number B.

from totalvoice.cliente import Cliente
import requests

api_totalvoice = Cliente("089f722451983a4ef92db0e5eba812b0", 'api.totalvoice.com.br')

src_number = input('Insert A number: ')
dst_number = input('Insert B number: ')

response = api_totalvoice.chamada.enviar(src_number, dst_number, gravar_audio=True)
print(response)






