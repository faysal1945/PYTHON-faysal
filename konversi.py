# Kalkulator Konversi Satuan
print ("=== KALKULATOR KONEVRSI ===")
cm =  float(input("Masukkan panjang  (cm): "))

# Konversi Ke berbagai Satuan
meter       = cm / 100
km          = cm / 100.000
inci        = cm / 2.54
ft          = inci / 12

print ()
print (cm, "cm =", meter, "meter")
print (cm, "cm =", km, "kilometer")
print (cm, "cm =", round (inci, 2), "inci")
print (cm, "cm =", round(ft, 2), "ft")