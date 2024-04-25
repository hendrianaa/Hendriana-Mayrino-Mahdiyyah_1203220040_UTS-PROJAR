import socket
import random
import time
import threading

# variabel konfigurasi server
server_ip = '127.0.0.1'
server_port = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))

# kode warna dalam bahasa Inggris dan Indonesia
colors_en = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
colors_id = ['merah', 'hijau', 'biru', 'kuning', 'ungu', 'oranye']

# fungsi untuk menerima respon dari klien
def receive_response(client_address):
    try:
        server_socket.settimeout(5)
        data, addr = server_socket.recvfrom(1024)
        response = data.decode().strip().lower()
        return response
    except socket.timeout:
        return None

# fungsi untuk menangani koneksi dari klien
def handle_client(client_address):

    while True:
        # kirim kata warna ke klien
        color_en = random.choice(colors_en)
        color_id = colors_id[colors_en.index(color_en)]
        print(f"Warna en: {color_en} warna id {color_id}")
        server_socket.sendto(color_en.encode(), client_address)
        
        # terima jawaban dari klien
        response = receive_response(client_address)
        # berikan feedback kepada klien
        if response is None:
            print(f"Waktu habis. Klien {client_address} tidak merespons.")
            server_socket.sendto("0. Waktu Habis".encode(), client_address)
        elif response is not None and response == color_id:
            print(f"Klien {client_address} menjawab dengan warna: {response}")
            server_socket.sendto("100".encode(), client_address)
        else:
            print(f"Klien {client_address} menjawab dengan: {response}. Jawaban salah.")
            server_socket.sendto("0".encode(), client_address)
        time.sleep(10)

while True:
    print("Menunggu koneksi dari klien...")
    data, client_address = server_socket.recvfrom(1024)
    print(f"Klien terhubung dari {client_address}")
    server_socket.settimeout(5)
    # buat thread baru untuk menangani koneksi dari klien
    threading.Thread(target=handle_client, args=(client_address,)).start()