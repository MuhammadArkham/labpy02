# Praktikum2

Muhammad Arkhamullah Rifai Asshidiq

Bahasa pemrograman

312410545

#  Kasus 1: Program Pemesanan Tiket Bioskop
Buat program yang menghitung harga tiket bioskop. Tiket reguler berharga Rp50.000,
sedangkan tiket VIP berharga Rp100.000. Jika user memiliki kartu member, mereka
mendapatkan diskon 20% dari harga tiket. Program ini harus meminta tipe tiket dan status
member dari user, lalu menghitung total harga yang harus dibayar.

Petunjuk:
Gunakan if else dan operator ternary.
## Kode Program
```python
# Program Pemesanan Tiket Bioskop

harga_reguler = 50000
harga_vip = 100000

diskon_member = 0.2

tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").lower()
status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()

if tipe_tiket == "reguler":
    harga = harga_reguler
elif tipe_tiket == "vip":
    harga = harga_vip
else:
    harga = 0
    print("Tipe tiket tidak valid!")

if harga != 0:
    harga_akhir = harga * (1 - diskon_member) if status_member == "ya" else harga
    print("Total harga yang harus dibayar: Rp", int(harga_akhir))

```
## Hasil kode Program
![Foto](https://github.com/MuhammadArkham/Foto/blob/main/Screenshot%202024-10-29%20193632.png?raw=true)

## Penjelasan dan langkah-langkah kode Program

### Menentukan Harga Dasar
   
```Python

harga_reguler = 50000  # Harga tiket reguler
harga_vip = 100000     # Harga tiket VIP
```
 Program menetapkan harga dasar untuk dua jenis tiket:

 Tiket Reguler: Rp 50.000

 Tiket VIP: Rp 100.000

### Menentukan Besaran Diskon

```Python

diskon_member = 0.2  # Diskon 20% untuk member
```
 Program menetapkan besaran diskon untuk pemegang kartu member sebesar 20% (0.2)

### Input Data Pelanggan

   ```Python
   
   tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").lower()
   status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()
   ```
A. Program meminta input dari pengguna:

   Tipe tiket yang diinginkan (reguler/vip)

   Status kepemilikan kartu member (ya/tidak)

B. Fungsi .lower() digunakan untuk mengubah input menjadi huruf kecil agar memudahkan pengecekan.

### Menentukan Harga Berdasarkan Tipe Tiket

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
 
### Menghitung Harga Akhir

 ```Python

if harga != 0:
    harga_akhir = harga * (1 - diskon_member) if status_member == "ya" else harga
    print("Total harga yang harus dibayar: Rp", int(harga_akhir))
```
Program menghitung harga akhir dengan ketentuan:

Jika harga tidak 0 (tipe tiket valid), lanjut ke pengecekan status member
Jika memiliki kartu member: harga dikurangi 20%
Jika tidak memiliki kartu member: harga tetap
Hasil akhir ditampilkan dalam format Rupiah.



Contoh Perhitungan:

1.Tiket Reguler dengan Member:

Harga dasar: Rp 50.000
Diskon: 20% × Rp 50.000 = Rp 10.000
Harga akhir: Rp 40.000

2.Tiket VIP tanpa Member:

Harga dasar: Rp 100.000
Tidak ada diskon
Harga akhir: Rp 100.000

## Gambar Flowchart
![Foto](https://github.com/MuhammadArkham/Foto/blob/main/Kasus1.drawio%20(1).png?raw=true)


# Kasus 2: Program Kalkulator Sederhana
Buat program yang menghitung harga tiket bioskop. Tiket reguler berharga Rp50.000,
sedangkan tiket VIP berharga Rp100.000. Jika user memiliki kartu member, mereka
mendapatkan diskon 20% dari harga tiket. Program ini harus meminta tipe tiket dan status
member dari user, lalu menghitung total harga yang harus dibayar.

Petunjuk:
Gunakan if elif else untuk menentukan operasi aritmatika.

## Kode Program
 ```Python

# Program Kalkulator Sederhana
while True:  
    print("\n=== Kalkulator Sederhana ===")
    
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("Input harus berupa angka. Silakan coba lagi.")
        continue

    print("Operator yang tersedia: +, -, *, /")
    operator = input("Masukkan operator: ")

    if operator == "+":
        hasil = angka1 + angka2
        print(f"Hasil: {angka1} + {angka2} = {hasil}")
    elif operator == "-":
        hasil = angka1 - angka2
        print(f"Hasil: {angka1} - {angka2} = {hasil}")
    elif operator == "*":
        hasil = angka1 * angka2
        print(f"Hasil: {angka1} * {angka2} = {hasil}")
    elif operator == "/":
        if angka2 != 0:
            hasil = angka1 / angka2
            print(f"Hasil: {angka1} / {angka2} = {hasil}")
        else:
            print("Error: Tidak bisa membagi dengan nol.")
    else:
        print("Operator tidak valid. Silakan coba lagi.")

    ulang = input("Ingin menghitung lagi? (y/n): ").lower()
    if ulang != 'y':
        print("Terima kasih telah menggunakan kalkulator!")
        break
```
## Hasil kode Program
![Foto](https://github.com/MuhammadArkham/Foto/blob/main/Screenshot%202024-10-30%20000828.png?raw=true)

## Penjelasan dan langkah-langkah kode program

### while True


 ```Python

while True:
```
 ini digunakan untuk membuat looping yang akan menjalankan program secara berulang.

### Input Angka Pertama dan Kedua

  ```Python
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

```
Untuk meminta input dua angka dari pengguna. 

Fungsi float() digunakan agar bisa menerima angka dengan desimal.

### If-Elif-Else

  ```Python

if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        print("Error: Tidak bisa membagi dengan nol.")
else:
    print("Operator tidak valid. Silakan coba lagi.")

```
### If

Jika operator yang dimasukkan user adalah +, maka program akan melakukan penjumlahan antara dua angka.

### elif 

Setiap elif memeriksa kondisi lain jika kondisi sebelumnya tidak terpenuhi. Program akan memeriksa operator dan melakukan operasi sesuai dengan input pengguna.

### else

Jika input operator tidak sesuai dengan salah satu kondisi yang telah ditentukan (+, -, *, atau /), maka program akan menjalankan blok else dan menampilkan pesan bahwa operator tersebut tidak valid.

### Pengulangan Program

  ```Python

ulang = input("Ingin menghitung lagi? (y/n): ").lower()
if ulang != 'y':
    print("Terima kasih telah menggunakan kalkulator!")
    break
```
Setelah perhitungan selesai, program menanyakan apakah pengguna ingin melanjutkan. Jika jawaban bukan 'y', program akan berhenti dengan menggunakan break.

## Gambar Flowchart
![Foto](https://github.com/MuhammadArkham/Foto/blob/main/Kasus2.drawio%20(2).png?raw=true)


