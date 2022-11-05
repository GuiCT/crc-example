from utils import mod2div
import socket

HOST = "127.0.0.1"
PORT = 60001

# Gerador de 16 bits, o padrão geralmente possui 17, mas foi removido um bit para permitir
# que caiba em uma mensagem de 32 bits. 16 bits de mensagem + 16 bits de checksum
CRC_16_DIVISOR = 0b1100000000000101

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    received_message_with_checksum = conn.recv(4)
    recv_message = received_message_with_checksum[0:2]
    checksum = received_message_with_checksum[2:4]
    print(f"Mensagem recebida: {recv_message.decode('ascii')}")
    print(f"Checksum recebido: {format(int.from_bytes(checksum, byteorder='big'), '016b')}")
    mod2div_remainder = mod2div(int.from_bytes(received_message_with_checksum, byteorder='big'), CRC_16_DIVISOR)
    print(f"Resultado da divisão módulo 2: {mod2div(int.from_bytes(received_message_with_checksum, byteorder='big'), CRC_16_DIVISOR)}")
    if mod2div_remainder == 0:
        print("Logo a mensagem recebida é correta.")
    else:
        print("Logo a mensagem recebida possui erro.")