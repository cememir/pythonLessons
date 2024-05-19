dosyam = 'dosya.txt'

try:

    print("try")
    dosyaoku = open(dosyam, 'r')
    oku = dosyaoku.read()
    print(oku)
    dosyaoku.close()

except Exception as err:
    ## try içindeki herhangi bir satırda hata olursa burası devreye girer

    print("except")
    print(err)
    if "Errno 3" in str(err) or "Errno 2" in str(err):
        print("error 2 bulundu")
    print('Dosya (' + dosyam + ') bulunamadı')

finally:
    # hata olsa da olmasa da yani ne olursa olsun çalışır
    print("finally")
