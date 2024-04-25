# Permainan Kata Warna - README

## Deskripsi
Aplikasi ini adalah permainan sederhana dimana server akan mengirimkan kata warna dalam bahasa Inggris kepada klien, dan klien harus menjawab dengan kata warna yang sama dalam bahasa Indonesia. Server akan memberikan feedback apakah jawaban yang diberikan oleh klien benar atau salah.

## Cara Kerja

### Server
1. **Inisialisasi Socket Server**
   - Pada server, sebuah socket dibuat dengan menggunakan modul `socket`.
   - Socket ini diatur untuk menggunakan protokol UDP dengan menggunakan `socket.SOCK_DGRAM`.
   ```python
   import socket

   server_ip = '127.0.0.1'
   server_port = 12345
   server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   server_socket.bind((server_ip, server_port))
