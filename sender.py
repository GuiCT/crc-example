from utils import mod2div
import socket

HOST = "127.0.0.1"
PORT = 60001

# Gerador de 16 bits, CRC-16-Chakravarty.
CRC_16_DIVISOR = 0x2F15

# Pergunta a quem está rodando ao script se irá forçar um bit-flip
while True:
    option = input('Deseja forçar um erro na mensagem enviada? (S/N): ')
    option = option.capitalize()[0]
    if option == 'S':
        force_error = True
        break
    elif option == 'N':
        force_error = False
        break
    else:
        print('Deve ser S ou N')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Mensagem: 'oi' em binário
    # ASCII: 6f -> o, 69 -> i
    # 016b: Escreve como binário com 16 bits, com zeros à esquerda se necessário
    bits_sent = format(0x6f69, '016b')
    # Adicionando 16 bits zerados ao fim da mensagem e aplicando divisão módulo 2
    # O resto da divisão é recebido
    dividend = mod2div(0x6f690000, CRC_16_DIVISOR)
    if force_error:
        # Forçando um erro, alterando um bit da mensagem enviada
        # Concatenando o resto da divisão módulo 2
        treated_message = format(0x6f68, '016b') + format(dividend, '016b')
    else:
        # Mensagem correta, concatenando o resto da divisão módulo 2
        treated_message = bits_sent + format(dividend, '016b')
    message = s.send(int.to_bytes(int(treated_message, base=2), length=4, byteorder='big'))