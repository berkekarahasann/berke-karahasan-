# Müşterinin başlangıç bakiyesi
kontostand = float(input("Başlangıç bakiyenizi girin: "))

# Yapılacak işlemi al
transaktion = input("İşlemi girin (Einzahlung/ Auszahlung): ").strip()

if transaktion == "Einzahlung":
    betrag = float(input("Yatırılacak miktarı girin: "))
    kontostand += betrag  # Yatırma işlemi
elif transaktion == "Auszahlung":
    betrag = float(input("Çekilecek miktarı girin: "))
    kontostand -= betrag  # Çekme işlemi
else:
    print("Geçersiz işlem")
    betrag = 0  # Geçersiz işlem durumunda bakiye değişmez

# Negatif bakiye kontrolü
if kontostand < 0:
    print("Negatif bakiye olamaz!")
else:
    print("Son bakiyeniz: {kontostand}")