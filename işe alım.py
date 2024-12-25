def aday_evaluasyonu(yas, mezuniyet_notu):
    if 20 <= yas <= 50 and mezuniyet_notu > 80:
        return "einstellen"
    else:
        return "ablehnen"

# Kullanıcıdan veri alma
yas = int(input("Adayın yaşını girin: "))
mezuniyet_notu = float(input("Adayın mezuniyet notunu girin: "))

# Sonucu ekrana yazdırma
print(aday_evaluasyonu(yas, mezuniyet_notu))