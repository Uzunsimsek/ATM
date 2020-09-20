kullanici_adi="Rabia"
kullanici_sifre="123"
bakiye=1000
print("   Bolparalı ATM'ye Hoş Geldiniz")

print("Adınızı Giriniz")
adiniz=(input())
print("Şifrenizi Giriniz")
sifre=(input())
if((adiniz==kullanici_adi) & (sifre==kullanici_sifre)):
    print("Başarıyla Giriş Yaptınız")
    while True:
        islem=int(input(""" 
                 
          1-Bakiye Sorgulama
          2-Para Yatırma
          3-Para Çekme
          4-Şifre Değiştirme
          5-Çıkış                     
    Yapmak istediğiniz işlemi seçiniz:
            """))


        if (islem == 1):
            print("***Bakiye tutarınız: {}***".format(bakiye))
            islem2=(int(input("***Çıkmak için 1'e devam etmek için 2'ye basınız: ***")))
            if (islem2 == 2):
                islem2==islem
            if (islem2 == 1):
                print("Bakiye sorguladığınız için teşekkürler, tekrar görüşmek üzere") 
                break
        if (islem == 2):
            miktar= int(input("Yatırılacak miktar: "))
            bakiye= bakiye+miktar
            print("Güncel Bakiyeniz {0} TL oldu".format(bakiye))
            islem3=(int(input("Çıkmak için 1'e devam etmek için 2'ye basınız: ")))
            if (islem3 == 2):
                islem3==islem
            if (islem3 == 1):
                print("Para yatırdığınız için teşekkür ederiz! Yine Bekleriz! ") 
                break
        if (islem ==3):
            cekim=int(input("Çekeceğiniz miktarı yazınız: "))
            bakiye=bakiye-cekim
            if((bakiye-cekim)<0):
                print("Para Çekilemedi : Çekeceğiniz miktar bakiyenize eşit veya az olmalıdır!")
            elif((bakiye-cekim)>=0):
                print("Tebrikler {} TL çektiniz".format(cekim))
                print("Yeni bakiyeniz {} TL".format(bakiye))
            islem5=(int(input("Çıkmak için 1'e devam etmek için 2'ye basınız: ")))
            if (islem5 == 2):
                islem5==islem
            if (islem5 == 1):
                print("Para çektiğiniz için üzgünüz:( ") 
                break
        if (islem==4):
            eski_sifre=input("Şu an kullandığınız şifreyi giriniz: ")
            yeni_sifre=int(input("Yeni şifrenizi giriniz:"))
            yeni_sifre_onay=(int(input("Yeni şifrenizi tekrar giriniz:")))
            if ((eski_sifre==kullanici_sifre) & (yeni_sifre==yeni_sifre_onay)):
                print("Şifreniz Başarıyla Değiştirildi")
            else:
                print("Şifreleriniz eşleşmemektedir! Tekrar Deneyiniz!")
            islem4=(int(input("Çıkmak için 1'e devam etmek için 2'ye basınız: ")))
            if (islem4 == 2):
                islem4==islem
            if (islem4 == 1):
                print("Şifre değiştirdiğiniz için teşekkür ederiz") 
                break
        if (islem==5):
            print("Zaman ayırdığınız için teşekkür ederiz. Yine Bekleriz!")
            break
else:
    print("Girmiş olduğunuz şifre veya isim yanlış, tekrar deneyiniz!")