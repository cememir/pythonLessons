dosyam = 'dosya.txt'

print("try")
dosyaoku = open(dosyam, 'r')
oku = dosyaoku.readlines()

print(oku, type(oku), type(dosyaoku), type(dosyam))
