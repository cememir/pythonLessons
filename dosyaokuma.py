
dosya =open('dosya.txt', 'w')
dosya.write('\nwrite')
dosya.close()


dosya =open('dosya.txt', 'a')
dosya.write('\nappend')
dosya.close()



dosyaoku =open('dosya.txt', 'r')
print(dosyaoku.read())
dosyaoku.close()

