from utils import mod2div
import socket

HOST = "127.0.0.1"
PORT = 60001

# Gerador de 16 bits, CRC-16-Chakravarty.
CRC_16_DIVISOR = 0x2F15

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    received_message_with_checksum = conn.recv(4)
    recv_message = received_message_with_checksum[0:2]
    checksum = received_message_with_checksum[2:4]
    print(f"Mensagem recebida: {recv_message.decode('ascii')}")
    print(f"Sufixo/dividendo recebido: {format(int.from_bytes(checksum, byteorder='big'), '016b')}")
    mod2div_remainder = mod2div(int.from_bytes(received_message_with_checksum, byteorder='big'), CRC_16_DIVISOR)
    print(f"Resto da divisão módulo 2: {mod2div(int.from_bytes(received_message_with_checksum, byteorder='big'), CRC_16_DIVISOR)}")
    if mod2div_remainder == 0:
        print("Logo a mensagem recebida é correta.")
    else:
        print("Logo a mensagem recebida possui erro.")