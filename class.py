class kurs():
    saglayici = "KyK"

    def __init__(self,ogrenci,kapasite):
        self.ogrenci = ogrenci
        self.kapasite = kapasite
    
    def kapasite_guncelle(self):
        return self.kapasite - self.ogrenci
    
    def kayit(self,kayit):
        if self.ogrenci + kayit <= self.kapasite:
            self.ogrenci += kayit
            self.kapasite_guncelle()
            print("{} kişi kayıt yaptırmıştır. Guncel kalan kontejyan sayisi {}".format(
                kayit,
                self.kapasite_guncelle()))
        else:
            print("Kayit gerceklestirilemedi. Kursta yer kalmadi.")

    def kayit_iptal(self,kayit=1):
        if self.ogrenci >= kayit:
            self.ogrenci -= kayit
            self.kapasite_guncelle()
            print("{} adet kayit iptal edirmistir.Guncel kalan kontejyan sayisi {}.".format(
                kayit,
                self.kapasite_guncelle()))
            
        else:
            print("Isleminiz gerceklestirilemedi.Iptal edilecek kadar ogrenci yok.")

masa_tenisi = kurs(7,50)
voleybol = kurs(11,60)
futbol = kurs(32,80)
masa_tenisi.kapasite_guncelle()
voleybol.kapasite_guncelle()
futbol.kapasite_guncelle()
print("secmek istediginiz kursu yaziniz.")
print("1 Masa Tenisi")
print("2 Voleybol")
print("3 Futbol")
print("4 kayit sildirme")
while True:
    secim= (input("1,2,3,4 :"))
    if secim == ("1"):
        print("kaç kişi kayit yaptirmak istiyorsunuz")
        kisi_sayisi = (input())
        masa_tenisi.kayit(float(kisi_sayisi))
        print("Baska bir kursa daha kayit yaptirmak ister misiniz?(Evet/Hayir)")
        secim2=(input())
        if secim2 == ("Evet"):
            print("secmek istediginiz kursu yaziniz.")
            print("1 Masa Tenisi")
            print("2 Voleybol")
            print("3 Futbol")
        elif secim2 ==("Hayir"):
            break
    elif secim== ("2"):
         print("kaç kişi kayit yaptirmak istiyorsunuz")
         kisi_sayisi = (input())
         voleybol.kayit(float(kisi_sayisi))
         print("Baska bir kursa daha kayit yaptirmak ister misiniz?(Evet/Hayir)")
         secim2=(input())
         if secim2 == ("Evet"):
            print("secmek istediginiz kursu yaziniz.")
            print("1 Masa Tenisi")
            print("2 Voleybol")
            print("3 Futbol")
         elif secim2 ==("Hayir"):
            break
         
    elif secim == ("3"):
         print("kaç kişi kayit yaptirmak istiyorsunuz")
         kisi_sayisi = (input())
         futbol.kayit((float(kisi_sayisi)))
         print("Baska bir kursa daha kayit yaptirmak ister misiniz?(Evet/Hayir)")
         secim2=(input())
         if secim2 == ("Evet"):
            print("secmek istediginiz kursu yaziniz.")
            print("1 Masa Tenisi")
            print("2 Voleybol")
            print("3 Futbol")
         elif secim2 ==("Hayir"):
            break
        
    elif secim == ("4"):
        print("hangi kurstan kayit sildirmek istiyorsunuz?")
        print("1 Masa Tenisi")
        print("2 Voleybol")
        print("3 Futbol")
        sildirme=(input("1,2,3 :"))
        print("kac kisilik kayit sildirmek istiyorsunuz?")
        kisi_sayisi= (input())
        if sildirme ==("1"):
            masa_tenisi.kayit_iptal(float(kisi_sayisi))
            print("Baska bir kursa kayit yaptirmak ister misiniz?(Evet/Hayir)")
            secim2=(input())
            if secim2 == ("Evet"):
                print("secmek istediginiz kursu yaziniz.")
                print("1 Masa Tenisi")
                print("2 Voleybol")
                print("3 Futbol")
            elif secim2 ==("Hayir"):
                break
        elif sildirme == ("2"):
            voleybol.kayit_iptal(float(kisi_sayisi))
            print("Baska bir kursa kayit yaptirmak ister misiniz?(Evet/Hayir)")
            secim2=(input())
            if secim2 == ("Evet"):
                print("secmek istediginiz kursu yaziniz.")
                print("1 Masa Tenisi")
                print("2 Voleybol")
                print("3 Futbol")
            elif secim2 ==("Hayir"):
                break
        elif sildirme == ("3"):
            futbol.kayit_iptal(float(kisi_sayisi))
            print("Baska bir kursa kayit yaptirmak ister misiniz?(Evet/Hayir)")
            secim2=(input())
            if secim2 == ("Evet"):
                print("secmek istediginiz kursu yaziniz.")
                print("1 Masa Tenisi")
                print("2 Voleybol")
                print("3 Futbol")
            elif secim2 ==("Hayir"):
                break
            