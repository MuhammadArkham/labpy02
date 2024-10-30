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
