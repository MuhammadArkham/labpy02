# Praktikum2

Muhammad Arkhamullah Rifai Asshidiq

Bahasa pemrograman

312410545

# code program
```python
# Program Pemesanan Tiket Bioskop

# Harga tiket
harga_reguler = 50000
harga_vip = 100000

# Diskon untuk member
diskon_member = 0.2

# Input tipe tiket dan status member
tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").lower()
status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()

# Menghitung harga tiket berdasarkan tipe dan status member
if tipe_tiket == "reguler":
    harga = harga_reguler
elif tipe_tiket == "vip":
    harga = harga_vip
else:
    harga = 0
    print("Tipe tiket tidak valid!")

# Cek status member
if harga != 0:
    harga_akhir = harga * (1 - diskon_member) if status_member == "ya" else harga
    print("Total harga yang harus dibayar: Rp", int(harga_akhir))

```
# Hasil Code Program
![Foto](https://github.com/MuhammadArkham/Foto/blob/main/Screenshot%202024-10-29%20193632.png?raw=true)

# Penjelasan dan langkah-langkah kode program

# Menentukan Harga Dasar
   
```Python

harga_reguler = 50000  # Harga tiket reguler
harga_vip = 100000     # Harga tiket VIP
```
 Program menetapkan harga dasar untuk dua jenis tiket:

 Tiket Reguler: Rp 50.000

 Tiket VIP: Rp 100.000

# Menentukan Besaran Diskon

```Python

diskon_member = 0.2  # Diskon 20% untuk member
```
 Program menetapkan besaran diskon untuk pemegang kartu member sebesar 20% (0.2)

# Input Data Pelanggan

   ```Python
   
   tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").lower()
   status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()
   ```
A. Program meminta input dari pengguna:

   Tipe tiket yang diinginkan (reguler/vip)

   Status kepemilikan kartu member (ya/tidak)

B. Fungsi .lower() digunakan untuk mengubah input menjadi huruf kecil agar memudahkan pengecekan.

# Menentukan Harga Berdasarkan Tipe Tiket

 ```Python

if tipe_tiket == "reguler":
    harga = harga_reguler
elif tipe_tiket == "vip":
    harga = harga_vip
else:
    harga = 0
    print("Tipe tiket tidak valid!")
```
 Program melakukan pengecekan tipe tiket:

Jika "reguler": harga = Rp 50.000
Jika "vip": harga = Rp 100.000
Jika input tidak valid: harga = 0 dan menampilkan pesan error.
 
# Menghitung Harga Akhir

 ```Python

if harga != 0:
    harga_akhir = harga * (1 - diskon_member) if status_member == "ya" else harga
    print("Total harga yang harus dibayar: Rp", int(harga_akhir))
```
Program menghitung harga akhir dengan ketentuan:

Jika harga tidak 0 (tipe tiket valid), lanjut ke pengecekan status member
Jika memiliki kartu member: harga dikurangi 20%
Jika tidak memiliki kartu member: harga tetap
Hasil akhir ditampilkan dalam format Rupiah



Contoh Perhitungan:

1. Tiket Reguler dengan Member:

Harga dasar: Rp 50.000
Diskon: 20% × Rp 50.000 = Rp 10.000
Harga akhir: Rp 40.000


2. Tiket VIP tanpa Member:

Harga dasar: Rp 100.000
Tidak ada diskon
Harga akhir: Rp 100.000

# Gambar Flowchart

