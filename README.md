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
# Eksekusi program
![Foto]
