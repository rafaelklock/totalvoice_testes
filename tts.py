# This app makes a call between number A and number B.

from totalvoice.cliente import Cliente
import requests

access_token_totalvoice = ''  # you need insert your Totalvoice access-token api.totalvoice.com.br/painel

api_totalvoice = Cliente(access_token_totalvoice, 'api.totalvoice.com.br')

src_number = input('Insert A number: ')
dst_number = input('Insert B number: ')

response = api_totalvoice.chamada.enviar(src_number, dst_number, gravar_audio=True)
print(response)






