dosyam = 'dosya.txt'

print("try")
dosyaoku = open(dosyam, 'r')
oku = dosyaoku.readlines()

print(oku, type(oku), type(dosyaoku), type(dosyam))
for cem, satir in enumerate(oku):
    if 'd\n' in satir:
        print(cem, satir)
