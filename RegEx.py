print("1. menggunakan ekspresi reguler")
import re 
txt = "the rain in spain"
x = re.search("^the.*spain$", txt)

if x:
  print("ya")
else:
  print("tidak")
  
print("\n 2. fungsi findall")
import re
txr = "the rain in spain"
y = re.findall("ai", txr)
print(y)
   # kembalikan daftar kosong
m = re.findall("portugal", txr)
print(m)   

print("\n 3. fungsi pencarian")
#mencari karakter spasi pertama dalam string
import re
txt = "the rain in spain"
x = re.search("portugal", txt)
print(x)

print("\n 4. fungsi split")
import re
txt = "the rain in spain"
x = re.split("\s", txt)
print(x)
   # mengontrol jumlah kejadian
import re
t = "the rain in spain"
p = re.search("\s", txt, 1)
print(p)   

print("\n 5. fungsi sub")
import re
txt = "the rain in spain"
x = re.sub("\s", "9", txt)
print(x)
     # mengontrol jumlah penggantian
import re
txt = "the rain in spain"
x = re.sub ("\s", "9", txt, 1)
print(x)     

print("\n 6. cocokkan objek")
import re
txt = "the rain in spain"
x = re.search("ai", txt)
print(x)
    # ekspresi reguler mencari kata dimulai dengan huruf kapital
import re
txt = "the rain in spain"
x = re.search(r"\bs\w+", txt)
print(x.span())    
      #cetak string yqng dilewatkan
import re
txt = "the rain in spain"
x = re.search(r"\bs\w+", txt)
print(x.string)      
     # cetak bagian tali yang terdapqt kecocokan
import re
txt = "the rain in spain"
x = re.search(r"\bs\w+", txt)
print(x.group())     