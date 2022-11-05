from utils import mod2div
import socket

# Utilize essa opção para forçar um erro na mensagem enviada
FORCE_ERROR = False

HOST = "127.0.0.1"
PORT = 60001

# Gerador de 16 bits, o padrão geralmente possui 17, mas foi removido um bit para permitir
# que caiba em uma mensagem de 32 bits. 16 bits de mensagem + 16 bits de checksum
CRC_16_DIVISOR = 0b1100000000000101

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Mensagem: 'oi' em binário
    bits_sent = format(0x6f69, '016b')
    # Calculando checksum
    dividend = mod2div(0x6f690000, CRC_16_DIVISOR)
    if FORCE_ERROR:
        # Forçando um erro, alterando um bit da mensagem enviada
        treated_message = format(0x6f68, '016b') + format(dividend, '016b')
    else:
        # Mensagem correta
        treated_message = bits_sent + format(dividend, '016b')
    message = s.send(int.to_bytes(int(treated_message, base=2), length=4, byteorder='big'))