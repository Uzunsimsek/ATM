kullanici_adi="Rabia" #kullanıcının adını tanımladık
kullanici_sifre="123" #kullanıcının şifresini tanımladık
bakiye=1000 #kullanıcının başlangıç bakiyesini tanımladık
print("   Bolparalı ATM'ye Hoş Geldiniz") #kod çalıştırıldığında açılışta gelecek hoş geldin metnini yazdırdık

print("Adınızı Giriniz") #kullanıcının adını girmesini istedik
adiniz=(input()) #adını gireceği alana input ekledik ismini alabilmek için
print("Şifrenizi Giriniz") #aynı işlemleri şifre için de yaptık
sifre=(input())
if((adiniz==kullanici_adi) & (sifre==kullanici_sifre)): #kullanıcının gireceği isim ve şifre ile bizim tanımladığımız şifre ve isim aynı ise
    print("Başarıyla Giriş Yaptınız") #başarıyla giriş yaptınız de ve while true ile devam et dedik. Eğer yanlışsa en aşağıda yer alan şifre yanlış çıktısını verecek
    while True:
        islem=int(input(""" 
                 
          1-Bakiye Sorgulama
          2-Para Yatırma
          3-Para Çekme
          4-Şifre Değiştirme
          5-Çıkış                     
    Yapmak istediğiniz işlemi seçiniz:
            """))  #yapılacak işlemlere sayılar verdik


        if (islem == 1): #eğer kullanıcı biri seçerse bakiye tutarını format fonksiyonu ile kullanıcıya gösterdik. Sonrasında çıkış yaparsa #break ile işlemi bitir, devam etmek isterse başa sar
            print("***Bakiye tutarınız: {}***".format(bakiye))
            islem2=(int(input("***Çıkmak için 1'e devam etmek için 2'ye basınız: ***")))
            if (islem2 == 2):
                islem2==islem
            if (islem2 == 1):
                print("Bakiye sorguladığınız için teşekkürler, tekrar görüşmek üzere") 
                break
        if (islem == 2): #kullanıcı ikiyi seçerse yatırmak istediği miktarı sor ve bakiyeden çıkar. güncel bakiyeyi göster. yine çıkmak isteyip istemediğini sor. Bu işlemler 5. işleme kadar aynı devam etmekte.
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
else: #kullanıcı en başta şifre ve ismini yanlış yazarsa aşağıdaki metni yazdıracak
    print("Girmiş olduğunuz şifre veya isim yanlış, tekrar deneyiniz!")
