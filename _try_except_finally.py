dosyam = 'dosya.txt'

try:

    print("try")
    dosyaoku = open(dosyam, 'r')
    oku = dosyaoku.readlines()
    print(oku)
    for i, satir in enumerate(oku):
        if 'd\n' in satir:
            print(i, satir)
    dosyaoku.close()

except Exception as err:
    ## try içindeki herhangi bir satırda hata olursa burası devreye girer

    print("except")
    print(err)

finally:
    # hata olsa da olmasa da yani ne olursa olsun çalışır
    print("finally")
