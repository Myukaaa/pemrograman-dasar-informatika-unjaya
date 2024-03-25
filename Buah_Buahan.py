def beli_buah():
    jumlah_buah = int(input("Masukkan banyaknya buah yang dibeli: "))
    daftar_buah = []

    for i in range(jumlah_buah):
        buah = input(f"Buah {i+1}: ")
        daftar_buah.append(buah)

    return daftar_buah

# Contoh penggunaan
daftar_buah_dibeli = beli_buah()
print("Daftar buah yang dibeli:")
for buah in daftar_buah_dibeli:
    print("-", buah)
