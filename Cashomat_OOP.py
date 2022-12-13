# Bankamatik


class Hesaplar:
    def __init__(self,name,password,IBAN,bakiye,nakitavans,nakitavanslimiti):
        self.name = name
        self.password = password
        self.IBAN = IBAN
        self.bakiye = bakiye
        self.nakitavans = nakitavans
        self.nakitavanslimiti = nakitavanslimiti

class İslemler:
    def __init__(self,hesaplar):
        self.hesaplar = hesaplar
        self.accountIndex = 0
        self.Index = 0

    def ShowMenu(self):
        while True:
            print("1-) Para Cek. \n2-) Para Yatır. \n3-) Para Transferi Yap. \n4-) Cıkıs Yap.")
            Options = int(input("Islem yapmak istediginiz numarayı seciniz."))
            if Options == 1:
                bankahesapları.ParaCek()
                Options = int(input("Islem yapmak istediginiz numarayı seciniz."))
            elif Options == 2:
                bankahesapları.ParaYatır()
            elif Options == 3:
                bankahesapları.ParaTransferi()
            elif Options == 4:
                print(f"Sevgili {bankahesapları.hesaplar[self.accountIndex].name}, iyi günler dileriz.")
                break

    def SifreGir(self):
        sifre = int(input("Sifrenizi giriniz: "))
        for self.accountIndex in range(self.accountIndex,len(list)):
            if (sifre == (bankahesapları.hesaplar[self.accountIndex].password)):
                print(f"{bankahesapları.hesaplar[self.accountIndex].name} hos geldiniz.")
                print("1-) Para Cek. \n2-) Para Yatır. \n3-) Para Transferi Yap. \n4-) Cıkıs Yap.")
                Options = int(input("Islem yapmak istediginiz numarayı seciniz."))
                if Options == 1:
                    bankahesapları.ParaCek()
                    bankahesapları.ShowMenu()
                elif Options == 2:
                    bankahesapları.ParaYatır()
                    bankahesapları.ShowMenu()
                elif Options == 3:
                    bankahesapları.ParaTransferi()
                    bankahesapları.ShowMenu()
                elif Options == 4:
                    print(f"Sevgili {bankahesapları.hesaplar[self.accountIndex].name}, iyi günler dileriz.")
                    bankahesapları.ShowMenu()
                    break

    def ParaCek(self):
        cekilenPara = int(input("Lutfen cekmek istediginiz miktarı yazınız."))
        bakiye = bankahesapları.hesaplar[self.accountIndex].bakiye 
        nakitavans = bankahesapları.hesaplar[self.accountIndex].nakitavans
        if (cekilenPara <= (bakiye+nakitavans)):
            if (cekilenPara < bakiye):
                bakiye -= cekilenPara
                nakitavans -= 0
                print(f"Sayın {bankahesapları.hesaplar[self.accountIndex].name}, cekmek istediginiz tutar olan {cekilenPara} TL'yi cektiniz. Bakiyenizde {bakiye} TL ve nakit avans hesabınızda ise {nakitavans} TL bulunmaktadır.")
            if ((cekilenPara > bakiye) and (nakitavans + bakiye >= cekilenPara)):
                Secenek = int(input(f"Bakiyenizde {bakiye} TL ve nakit avans hesabınızda ise {nakitavans} TL bulunmaktadır. Nakit avans hesabınızdan para cekmek icin 1'i islemi iptal etmek icin 2'yi tuslayiniz."))
                if Secenek == 1:
                    Borc = cekilenPara - bakiye
                    bakiye -= bakiye
                    nakitavans -= Borc
                    print(f"Sayın {bankahesapları.hesaplar[self.accountIndex].name}, cekmek istediginiz tutar olan {cekilenPara} TL'yi cektiniz. Bakiyenizde {bakiye} TL ve nakit avans hesabınızda ise {nakitavans} TL bulunmaktadır.")
                if Secenek == 2:
                    ("Sayın {bankahesapları.hesaplar[self.accountIndex].name}, iyi gunler dileriz.")
        else:
            print(f"Sayın {bankahesapları.hesaplar[self.accountIndex].name}, cekmek istediginiz miktar olan {cekilenPara} TL hesabınızda bulunmamaktadır. Bakiyenizde {bakiye} TL ve nakit avans hesabınızda ise {nakitavans} TL bulunmaktadır.")

    def ParaYatır(self):
        YatırılanPara = int(input("Yatırmak istediginiz miktarı giriniz?  "))
        name = bankahesapları.hesaplar[self.accountIndex].name
        bakiye = bankahesapları.hesaplar[self.accountIndex].bakiye 
        nakitavans = bankahesapları.hesaplar[self.accountIndex].nakitavans
        nakitavanslimiti = bankahesapları.hesaplar[self.accountIndex].nakitavanslimiti
        if ({bankahesapları.hesaplar[self.accountIndex].nakitavans} == {bankahesapları.hesaplar[self.accountIndex].nakitavanslimiti}):
            bakiye += YatırılanPara
            print(f"Sevgili {name}, {YatırılanPara} TL bakiyenize aktarılmıstır. Guncel bakiyeniz {bakiye} TL ve {nakitavans} TL'dir.")
        else:
            Borc = (nakitavanslimiti-nakitavans)
            if (Borc>YatırılanPara):
                nakitavans += YatırılanPara
                print(f"{name}, {YatırılanPara} TL nakit avans hesabınıza aktarılmıstır. Guncel bakiyeniz {bakiye} TL ve nakit avans bakiyeniz ise {nakitavans} TL'dir.")
            elif (YatırılanPara>Borc):
                KalanPara = YatırılanPara - Borc
                bakiye += KalanPara
                nakitavans += Borc
                print(f"{name}, {KalanPara} TL bakiyenize aktarılmıstır. {Borc} TL ise nakit avans hesabınıza aktarılmıstır. Guncel bakiyeniz {nakitavans} TL ve {nakitavanslimiti} TL'dir.")                

    def ParaTransferi(self):
        YatırılanPara = int(input("Yatırmak istediginiz miktarı giriniz?  "))
        name = bankahesapları.hesaplar[self.accountIndex].name
        bakiye = bankahesapları.hesaplar[self.accountIndex].bakiye 
        nakitavans = bankahesapları.hesaplar[self.accountIndex].nakitavans
        nakitavanslimiti = bankahesapları.hesaplar[self.accountIndex].nakitavanslimiti
        ParayıAlacakIBAN = int(input("Para yatırmak istediginiz IBAN'ı giriniz:  "))
        for self.Index in range(self.Index,len(list)):
            if (ParayıAlacakIBAN == bankahesapları.hesaplar[self.Index].IBAN):
                isim = bankahesapları.hesaplar[self.Index].name
                if (YatırılanPara>0):
                    if((bakiye + nakitavans > YatırılanPara ) or (bakiye + nakitavans == YatırılanPara)):
                        if bakiye > YatırılanPara:
                            bakiye -= YatırılanPara
                            print(f"Sevgili {name}, {YatırılanPara} TL'yi {ParayıAlacakIBAN} IBAN No'lu musterimiz olan  {isim}'a yolladınız. Bakiyenizde ve nakit avans hesabınızda kalan para ise {bakiye} ve {nakitavans}'dir. İyi günler dileriz. " )
                        elif (YatırılanPara>=bakiye) and (bakiye+ nakitavans >= YatırılanPara):
                            Borc = YatırılanPara - bakiye
                            bakiye -= bakiye
                            nakitavans -= Borc
                            print(f"Sevgili {name}, {YatırılanPara} TL'yi {ParayıAlacakIBAN} IBAN No'lu musterimiz olan  {isim}'a yolladınız. Bakiyenizde ve nakit avans hesabınızda kalan para ise {bakiye} ve {nakitavans}'dir. İyi günler dileriz. " )
                    else:
                        print(f"Sevgili {name}, {YatırılanPara} TL'yi {isim} adlı musterimize yollayamadınız. Cunku toplam varlıgınız {bakiye + nakitavans} TL'dir.")
                else:
                    print(f"Sevgili {name}, mal mısınız?")

        def ShowMenu(self):
            while True:
                print("1-) Para Cek. \n2-) Para Yatır. \n3-) Para Transferi Yap. \n4-) Cıkıs Yap.")
                Options = int(input("Islem yapmak istediginiz numarayı seciniz."))
                if Options == 1:
                    bankahesapları.ParaCek()
                    Options = int(input("Islem yapmak istediginiz numarayı seciniz."))
                elif Options == 2:
                    bankahesapları.ParaYatır()
                elif Options == 3:
                    bankahesapları.ParaTransferi()
                elif Options == 4:
                    print(f"Sevgili {bankahesapları.hesaplar[self.accountIndex].name}, iyi günler dileriz.")
                    break


Umit = Hesaplar("Umit Ekmekci",1234,5678,1000,2000,2000)
Hasan = Hesaplar("Hasan Nesanır",5678,1234,100,200,200)
Mehmet = Hesaplar("Mehmet",7894,4987,100000,1000000,1000000)
list = [Hasan,Umit,Mehmet]

bankahesapları = İslemler(list)

bankahesapları.SifreGir()
