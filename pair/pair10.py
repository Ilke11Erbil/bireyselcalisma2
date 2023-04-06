print("Not: vize notunun %40 final notunun %70")

vize = float(input("Lütfen vize notunu giriniz :"))
final = float(input("Lütfen final notunu giriniz :"))
ortalama = (float(vize) * 0.4)+(float(final) * 0.7)

if (ortalama>= 0 and ortalama<=49):
    print("Harf Notunuz FF")
elif (ortalama >= 50 and ortalama<=59):
    print("Harf Notunuz DD")
elif (ortalama >= 60 and ortalama<=69):
    print("Harf Notunuz CC")
elif(ortalama >= 70 and ortalama <= 79):
    print("Harf Notunuz BB")
elif(ortalama >=70 and ortalama<=100):
    print("Harf Notunuz AA")