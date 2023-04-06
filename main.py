print("Merhaba Etiya")
print("Hos geldiniz")

# yorum

# degiskenler-start 
# metinsel, numerik, obje

# string
text = "Merhaba"

print(text)
print(text)
print(text)
text = "selam"
print(text)
print(text)

studentCount  = 45 # int, integer => tam sayı
print(studentCount + 5)

avaragePoint = 25.5
print(avaragePoint + 5)

isVeriFied = True # bool, boolean => True veya False
print(isVeriFied)

print(type(text))
print(type(studentCount))
print(type(avaragePoint))
print(type(isVeriFied))
# degiskenler-end

# operatorler -start
number = 10
# matematiksel operatorler - mantıksal operatorler
print(10 + 10)
print(number + number)

print(number - 5)

print(number / 2)

print(number * 5)

# mood operartoru => sol tarafindaki degerin sag taraftaki degere bolumunden kalan sonuc 
print(number % 3)

print(number + ((10 - number) * (5/10)))

# mantiksal operatorler - karsilastirma operatorleri

print(number == 10) #true
print(10 != 10) #false
print(11 !=10) #true
print(number < 10) #false
print(number <= 10) #true 

#operatorler -end

#diziler ve listeler-start
sayilar =[100,200,300,400,500,"Merhaba", 15.5, True]
print(sayilar[0])
print(sayilar[5])

print(sayilar)
sayilar.append(600)
print(sayilar)
sayilar.pop()
print(sayilar)
sayilar.remove("Merhaba")
print(sayilar)
sayilar.extend([700,800,900])
print(sayilar)
sayilar.clear()
print(sayilar)
#diziler ve listeler-end

#string interpolation - start
hello = "Merhaba"
userName = "Halit"

totalText = hello+" "+userName
print(totalText)

totalText = "{massage} Sayın {name}".format(massage=hello, name=userName)
print(totalText)

#f-string
totalText = f"Hosgeldiniz{userName}"
print(totalText)

#string interpolation - end
#karar yapıları
ortalamaNot = input("Lütfen Ortalamanızı Giriniz:")

#if else blokları
if ortalamaNotAsInteger > 50:
   print("Bravo")
   ortalamaNostAsInteger > 80:
    print("Basariyla Gectiniz")
    
else:
    print("maalesef")
    print("kaldınız")
print("if bloğundan bağımsız kısım")
#karar yapıları -end
vize = input("vize notu giriniz")


vize = int(input("Vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))
ortalama = (vize * 0.4) + (final * 0.6) 


# eğer final 40'dan küçükse kullanıcı kaldı
# eğer ortalama 50'den küçükse kullanıcı kaldı
# eğer vize finalin 2 katı ise kullanıcı kaldı
# bunun dışındaki tüm durumlarda kullanıcı geçti yazdırmak istiyoruz.

