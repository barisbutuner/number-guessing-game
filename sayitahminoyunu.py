import random

# 1. OYUN Bilgisayarın tahminini kullanıcı bulmaya çalışır
oyun = input("Oynamak istediğiniz oyunu seçiniz (1,2) :")
if oyun == "1":
    rastgele = random.randint(1,100)
    for i in range(6):
        tahmin = int(input("Bir Sayı Giriniz: "))
        if rastgele > tahmin:
            print("Sayınızı yükseltin")
        elif rastgele < tahmin:
            print("Sayınızı düşürün")
        else:
            print("Tebrikler! Doğru tahmin Ettiniz.")
            break    
    if rastgele != tahmin:
        print("Hakkınız Kalmadı. Kaybettiniz! Tuttuğum sayı: ",rastgele)     
  

else:
    # 2. OYUN Kullanıcının tahminini bilgisayar bulmaya çalışır
    ksayi = int(input("Bir sayı girin: "))

    # Bilgisayarın rastgele tahminleri yapması sağlanır
    for hak in range(8):
        pctahmin = random.randint(1, 100)
        print(pctahmin)        
        if pctahmin > ksayi:
            print("Sayınızı Düşürün.")
        elif pctahmin < ksayi:
            print("Sayınızı Yükseltin.")
        else:
            print("Kazandınız")    
            break

    if pctahmin != ksayi:
        print("Kaybettiniz. Tuttuğum sayı: ",ksayi)        