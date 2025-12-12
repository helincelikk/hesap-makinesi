import math
import time

def Topla(x,y):
    return x+y

def Cikar(x,y):
    return x-y

def Carp(x,y):
    return x*y

def Bol(x,y):
    if y != 0:
        return x/y
    else: 
        return "Bir sayiyi sifira bolemezsiniz. Lutfen tekrar deneyiniz.."
    
def Coklu_Topla(sayilar3):
    toplam = 0
    for sayi in sayilar3:
        toplam += sayi

    return toplam

def Coklu_Carp(numbers3):
    sonuc = 1
    for sayi in numbers3:
        sonuc *= sayi

    return sonuc

def Karekok(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Negatif bir sayinin karekoku alinamaz. Lütfen tekrar deneyiniz.."
    
def Us_Al(x,y):
    return x**y
    
def guvenli_girdi_al(prompt):
    while True:
        try:
            x = float(input(f"{prompt} istediginiz sayıları giriniz: "))
            break
        except ValueError:
            print("Hatali deger girdiniz. Tekrar deneyin..")
    return x

def guvenli_coklu_girdi_al(prompt):
    while True:
        try:
            sayilar1 = input(f"{prompt} istediginiz sayıları giriniz: ")
            sayilar2 = [i.strip() for i in sayilar1.split(" ")]
            sayilar_filtrelenmis = [s for s in sayilar2 if s != ""]
            sayilar3 = [float(t) for t in sayilar_filtrelenmis]
            break
        except ValueError:
            print("Hatali bir deger girdiniz. Tekrar deneyin..")
    return sayilar3

def isleme_devam_mi():
    answer = input("Baska bir islem yapmak ister misiniz? (e/h): ")
    while True:
        if answer == "h":
            print("Cikis yapiliyor..")
            return True
        elif answer == "e":
            print("Karsilama ekranina yonlendiriliyorsunuz..")
            return False 
        else:
            answer = input("Yanlis bir karakter girdiniz. Lütfen (e/h)'den birini girin: ")
    
def Karsilama_Ekrani():
    print("Hosgeldiniz. Hesap Makinesi Baslatiliyor..")

    while True:
        time.sleep(1.5)
        islem = input("""Lutfen yapmak istediginiz islemi secin:
            
        1- Toplama
        2- Cikarma
        3- Carpma
        4- Bolme
        5- Karekok Alma
        6- Us Alma
        7- Cikis Yap
    """)

        if islem == "1":
            sayilar3 = guvenli_coklu_girdi_al("Toplamak")

            print("Hesaplaniyor..")
            time.sleep(1.5)
            print(f"Sonuc: {Coklu_Topla(sayilar3)}")

            sonuc = isleme_devam_mi()
            if sonuc:
                return

        elif islem == "2":
            x = guvenli_girdi_al("Cikarmak")
            y = guvenli_girdi_al("Cikarmak")

            print("Hesaplaniyor..")
            time.sleep(1.5)
            print(f"Sonuc: {Cikar(x,y)}")

            sonuc = isleme_devam_mi()
            if sonuc:
                return
            
        elif islem == "3":
            sayilar3 = guvenli_coklu_girdi_al("Carpmak")

            print("Hesaplaniyor..")
            time.sleep(1.5)
            print(f"Sonuc: {Coklu_Carp(sayilar3)}")

            sonuc = isleme_devam_mi()
            if sonuc:
                return

        elif islem == "4":
            x = guvenli_girdi_al("Bolmek")
            y = guvenli_girdi_al("Bolmek")
            
            print("Hesaplaniyor..")
            time.sleep(1.5)
            print(f"Sonuc: {Bol(x,y)}")

            sonuc = isleme_devam_mi()
            if sonuc:
                return
            
        elif islem == "5":
            x = guvenli_girdi_al("Karekokunu almak")

            print("Hesaplaniyor..")
            time.sleep(1.5)
            print(f"Sonuc: {Karekok(x)}")

            sonuc = isleme_devam_mi()
            if sonuc:
                return
                    
        elif islem == "6":
            x = guvenli_girdi_al("İlki taban, ikincisi us olacak sekilde us almak")
            y = guvenli_girdi_al("İlki taban, ikincisi us olacak sekilde us almak")

            print("Hesaplaniyor..")
            time.sleep(1.5)
            print(f"Sonuc: {Us_Al(x,y)}")

            sonuc = isleme_devam_mi()
            if sonuc:
                return

        elif islem == "7":
            print("Cikis yapiliyor..")
            break
    
        else:
            print("Gecersiz bir deger girdiniz, tekrar deneyiniz.")
            continue
            
    
Karsilama_Ekrani()