# Nama : Hendriana Mayrino Mahdiyyah
# NIM : 1203220040
# Kelas : IF 02-01

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
   ```

2. **Menerima Koneksi dari Klien**
   - Server akan menunggu koneksi dari klien dengan memanggil `server_socket.recvfrom()`.
   - Ketika koneksi diterima, alamat klien akan disimpan untuk digunakan dalam pengiriman pesan balik.
   ```python
   data, client_address = server_socket.recvfrom(1024)
   ```

3. **Membuat Thread untuk Setiap Koneksi**
   - Setiap koneksi dari klien akan ditangani oleh sebuah thread terpisah untuk memungkinkan server menerima koneksi dari beberapa klien secara bersamaan.
   ```python
   import threading

   def handle_client(client_address):
       # Kode penanganan klien
       pass

   threading.Thread(target=handle_client, args=(client_address,)).start()
   ```

4. **Kirim dan Terima Data**
   - Server akan mengirimkan kata warna dalam bahasa Inggris ke klien dengan menggunakan `server_socket.sendto()`.
   - Kemudian, server akan menerima jawaban dari klien dan memberikan feedback sesuai dengan jawaban tersebut.
   ```python
   server_socket.sendto(color_en.encode(), client_address)
   response, addr = server_socket.recvfrom(1024)
   ```

### Client

1. **Inisialisasi Socket Client**
   - Pada client, juga dibuat sebuah socket menggunakan modul `socket`.
   ```python
   import socket

   server_ip = '127.0.0.1'
   server_port = 12345
   client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   ```

2. **Kirim Permintaan Koneksi ke Server**
   - Client akan mengirim permintaan koneksi ke server untuk memulai permainan.
   ```python
   client_socket.sendto("Connect".encode(), (server_ip, server_port))
   ```

3. **Terima dan Tanggapi Kata Warna**
   - Client akan menerima kata warna dalam bahasa Inggris dari server dan menampilkannya kepada pengguna.
   - Pengguna diminta untuk memasukkan kata warna dalam bahasa Indonesia.
   - Jawaban pengguna dikirimkan kembali ke server untuk diverifikasi.
   ```python
   data, addr = client_socket.recvfrom(1024)
   response = input("Masukkan kata warna dalam bahasa Indonesia: ")
   client_socket.sendto(response.encode(), (server_ip, server_port))
   ```

## Konfigurasi
- IP dan port server: `127.0.0.1:12345`
- Daftar kata warna dalam bahasa Inggris: `['red', 'green', 'blue', 'yellow', 'purple', 'orange']`
- Daftar kata warna dalam bahasa Indonesia: `['merah', 'hijau', 'biru', 'kuning', 'ungu', 'oranye']`

## Cara Menjalankan
1. Jalankan server dengan menjalankan file `server.py`.
2. Jalankan klien dengan menjalankan file `client.py`.

## Dependencies
- Python 3.x
- Module `socket`
- Module `random`
- Module `time`
- Module `threading`

## Catatan
- Pastikan untuk menjalankan server terlebih dahulu sebelum menjalankan klien.
- Server harus dijalankan pada komputer yang sama dengan klien, atau IP server harus diubah sesuai dengan alamat IP server yang digunakan.

## Cara Penggunaan
![image](https://github.com/hendrianaa/Hendriana-Mayrino-Mahdiyyah_1203220040_UTS-PROJAR/assets/162070830/5c0d3ed5-9c27-4089-a915-7d32d2aa6f0f)

