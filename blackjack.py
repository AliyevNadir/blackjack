import random
import os


# Kart dəstəsi 123 
kart_destesi = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4

oyuncu_qazanma_sayi = 0
komputer_qazanma_sayi = 0

# Kart dağitma
def kart_dagit():
    return kart_destesi.pop()

# Bir əlin toplam dəyərini hesabla
def toplam(el):
    toplam_deyer = 0
    tuz_sayi = 0
    
    for kart in el:
        if kart in ['J', 'Q', 'K']:
            toplam_deyer += 10
        elif kart == 'A':
            tuz_sayi += 1
        else:
            toplam_deyer += kart
    
    toplam_deyer += tuz_sayi * 11
    
    while toplam_deyer > 21 and tuz_sayi:
        toplam_deyer -= 10
        tuz_sayi -= 1
    
    return toplam_deyer




# Oyun döngüsü
def blackjack():
    global oyuncu_qazanma_sayi,komputer_qazanma_sayi
    
    oyuncu_el = []
    komputer_el = []
    
    for _ in range(2):
        oyuncu_el.append(kart_dagit())
        komputer_el.append(kart_dagit())
    
    print("Oyunçunun əli:", oyuncu_el)
    print("Komputerin əli:", [komputer_el[0], 'X']) # oyunçunun bir daşını göstərir
    
    # Oyunçunun sırası
    while toplam(oyuncu_el) < 21:
        secim = input("1: Pas\n2: Kart Çək\nSeçim edin: ")
        
        if secim == '2':
            oyuncu_el.append(kart_dagit())
            print("Oyunçunun əli:", oyuncu_el)
        elif secim == '1':
            break
        else:
            print("1: Pas\n2: Kart Çək\nSeçim edin: ")


    
    oyuncu_xali = toplam(oyuncu_el)
    
    # Komputerin sırası
    while toplam(komputer_el) < 17:
        komputer_el.append(kart_dagit())
    
    komputer_xali = toplam(komputer_el)
    
    # Qazananı təyin et
    print("Oyunçunun əli:", oyuncu_el, "Toplam:", oyuncu_xali)
    print("Komputerin əli:", komputer_el, "Toplam:", komputer_xali)
    
    
    if oyuncu_xali > 21:
        print("Oyunçu uduzdu! Komputer qazandı!")
        komputer_qazanma_sayi += 1 
    elif komputer_xali > 21:
        print("Komputer uduzdu! Oyunçu qazandı!")
        oyuncu_qazanma_sayi += 1
    elif oyuncu_xali == komputer_xali:
        print("Bərabər!")
    elif oyuncu_xali > komputer_xali:
        print("Oyunçu qazandı!")
        oyuncu_qazanma_sayi += 1
    else:
        print("Komputer qazandı!")
        komputer_qazanma_sayi += 1

while True:
    if len(kart_destesi) < 10:
        print("---Kart dəstəsi bitdi!, Oyun Bitdi---")
        print(f'Oyunçu: {oyuncu_qazanma_sayi} dəfə,\nKomputer: {komputer_qazanma_sayi} dəfə qazandi')
        break

    tekrar_oyna = input("Blackjack oynamaq istəyirsiniz? (y/n): ").lower()
    
    if tekrar_oyna != 'y':
        print("Sağ olun!")
        break
    
    random.shuffle(kart_destesi)
    blackjack()
