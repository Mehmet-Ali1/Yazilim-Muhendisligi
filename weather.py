import random

def get_info():
    sehirler = ["İzmir", "İstanbul", "Ankara", "Antalya"]
    durumlar = ["Güneşli ", "Parçalı Bulutlu ", "Sağanak Yağışlı ", "Rüzgarlı "]
    
    sehir = random.choice(sehirler)
    sicaklik = random.randint(10, 35)
    durum = random.choice(durumlar)
    
    rapor = (
        f" HAVA DURUMU MODÜLÜ\n"
        f"------------------------\n"
        f" Şehir: {sehir}\n"
        f" Sıcaklık: {sicaklik}°C\n"
        f" Durum: {durum}\n"
        f"------------------------"
    )
    
    return rapor