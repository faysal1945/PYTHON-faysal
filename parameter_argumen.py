# Parameter biasa
def luas_persegi_panjang (panjang, lebar):
    print("luas:", panjang * lebar)

    luas_persegi_panjang(8, 7)  # argumen posisional
    luas_persegi_panjang(lebar=4, panjang=6)    # keyword argument

    # Nilai default
    def sapa(nama, salam='halo'):
        print(salam + ", " + nama + "!")

    sapa('budi')        # Output: Halo, budi
    sapa('Ani', 'selamat pagi') #   Output: Selamat pagi, Ani!