# dosya = open('dosyax.txt', 'x')
# dosya.write('\nxxxxxxxx')
# dosya.close()

# dosya = open('dosya.txt', 'w')
# dosya.write('\nwrite')
# dosya.close()
#
# dosya = open('dosya_append.txt', 'a')
# dosya.write('\nappendddddd')
# dosya.close()
#
dosyaoku = open('dosya.txt', 'r')
oku = dosyaoku.read()
print(oku)
dosyaoku.close()
