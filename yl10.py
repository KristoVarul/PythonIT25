# Kirjutage Pythoni skript, mis simuleerib arvu äraarvamise mängu.
# Programm peab esmalt genereerima juhusliku arvu vahemikus 1 -10.
# Seejärel küsib programm kasutajalt arve, püüdes ära arvata genereeritud arvu. Kasutaja jätkab arvude sisestamist, kuni ta arvab õige arvu ära. Iga kord, kui kasutaja sisestab arvu, peab programm andma tagasisidet, kas pakutud arv on õige või mitte.
# Pärast õige arvu äraarvamist teavitab programm kasutajat, mitmenda katsega õige arv ära arvati, ja küsib, kas kasutaja soovib mängida uuesti.
# Kui kasutaja vastab jaatavalt, genereerib programm uue juhusliku arvu ja mäng algab otsast peale.
# Kui kasutaja otsustab mitte jätkata, tänab programm kasutajat mängus osalemise eest ja kuvab kõik senised tulemused: mitmenda katsega igal korral õige arv ära arvati.
# Programm peab kasutama while-tsüklit nii arvude sisestamise protsessi juhtimiseks kui ka mängu kordamise otsustamiseks.

#IT25 GR2
import random
tulemused=[]
suv=(random.randint(1,10))
katsed = 0
skoor = 0
for i in range(10):
    vastus=int(input("Arva arv ära 1-10"))
    katsed += 1
    if vastus == suv:
        print(f"Õige!", katsed, "katsega")
        valik=int(input("Arva arv ära 1-10"))
        skoor+= 1
    else:
        print(f"Vale, proovi uuesti")


print(f"{katsed} katset ja skoor {skoor}")