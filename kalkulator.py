
while True:
    print("Masukkan Pilihan Anda")
    x = int(input())

    if x == 1:
        print("Ini adalah pertambahan")
        print("Masukkan Bilangan Pertama")
        bilangan1 = int(input())
        print("Masukkan Bilangan Kedua")
        bilangan2 = int(input())
        hasil = bilangan1 + bilangan2
        print("Hasilnya adalah", hasil)

    elif x == 2:
        print("Ini adalah Pengurangan")
        print("Masukkan Bilangan Pertama")
        bilangan1 = int(input())
        print("Masukkan Bilangan Kedua")
        bilangan2 = int(input())
        hasil = bilangan1 - bilangan2
        print("Hasilnya adalah", hasil)

    elif x == 3:
        print("Ini adalah penentu bilangan ganjil atau genap")
        print("Masukkan Angka Anda")
        angka = int(input())
        if angka % 2 == 0:
            print(angka,"adalah Genap")
        else:
            print(angka, "adalah Ganjil")

    else:
        print("Fitur selanjutnya segera datang")

    ulang = input("Ingin Mengulang? (y/n) :")
    if ulang.lower() != 'y':
        break
