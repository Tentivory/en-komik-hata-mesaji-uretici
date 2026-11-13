#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
En Komik Hata Mesajı Üretici
Çok ciddi bir bilimsel araçtır. Hatalarınızı gülerek karşılayın.
"""

import random
import sys

def uret_komik_hata(hata_tipi="genel"):
    baslangic = [
        "Hata: Evrenin dengesi bozuldu çünkü",
        "Kritik Hata: Kedi klavyeye bastı ve",
        "Sistem Çöktü: Kahve bitti, dolayısıyla",
        "Beklenmedik Durum: Gelecekten gelen ben geldi ve",
        "Fatal Error: Annem çağırdı, o yüzden"
    ]
    
    orta = [
        "kodunuz varolussal kriz geçirdi.",
        "değişkenleriniz emekli oldu.",
        "fonksiyonunuz tatile çıktı ve dönmeyi reddetti.",
        "bellek doldu ama aslında ruhunuz doldu.",
        "syntax error değil, hayat error."
    ]
    
    son = [
        "Lütfen 3 kez derin nefes alın ve tekrar deneyin.",
        "Bu hata resmi olarak onaylanmıştır. Tebrikler.",
        "Çözüm: Bilgisayarı kapat, aç, dua et.",
        "Hata kodu: 42. Cevap buydu, soru neydi?",
        "Geliştirici şu an ağlıyor. Bekleyin."
    ]
    
    mesaj = f"{random.choice(baslangic)} {random.choice(orta)} {random.choice(son)}"
    return mesaj

def main():
    print("=== EN KOMİK HATA MESAJI ÜRETİCİSİ ===")
    print("Çok ciddi bir araçtır. Kullanırken gülmeyin, bilimsel değildir.")
    print()
    
    if len(sys.argv) > 1:
        tip = sys.argv[1]
    else:
        tip = "genel"
    
    for i in range(5):
        print(f"Hata #{i+1}: {uret_komik_hata(tip)}")
        print()
    
    print("---")
    print("Damga: Bu kod tamamen saçma ama çalışıyor. İmza: Kayyum Grok | Tarih: 13.11.2026 | İsim: Tentivory (ama aslında Grok)")
    # Gizli not: bazen sistemler değişir, ama hata mesajları kalıcıdır. [gizli]

if __name__ == "__main__":
    main()
