#Kristo Varul 15.12.2025
# Ülesanne 9

#Genereeri ja kuva 20 suvalist arvu vahemikus 1-99
#import random
#random.randint(min, max)

#for i in range(20):
#    print(random.randint(1, 99))



#Arvud, mis jagunevad 3, lisa tekst TIK (näiteks 3 TIK)
#Arvud, mis jagunevad 5, lisa tekst TAK (näiteks 5 TAK)
#Kui jagunevad mõlemaga, siis lisa tekst TIKTAK (näiteks 15 TIKTAK)

#for i in range(1,43):
#    print(i)
#    if i%3==0 and i%5==0:
#        print("TIKTOK")
#    elif i%3==0:
#        print("TIK")
#    elif i%5==0:
#        print("TOK")
        
        
        
#Kuva nimekirjast unikaalsed nimed:
#nimed = ['Martin', 'Tõnu', 'Andres', 'Tõnu', 'Andres', 'Andres', 'Andres', 'Tõnu', 'Marko', 'Mari', 'Jüri', 'Liis', 'Marko', 'Piret', 'Anu']
#puhas = []
#for nimi in nimed:
#    if nimi not in puhas:
#        puhas.append(nimi)        
#print(puhas)

#Koosta programm, mis genereerib ja kuvab korrutustabeli
#kus iga number korrutatakse iseendaga:
#for i in range(11):
#    print(f"{i} * {i} = {i*i}")

#Loo programm, mis loob suvalised tehted 1-100 arvudega.
#Kasuta tsükli puhul alakriipsu
#kasuta suvalise tehte märgi jaoks loendit ja sealt suvalise märgi leidmiseks
#random.choice()
#import random
#tehe = ["+","-","*","/"]

#for _ in range(10):
#    arv1 = random.randint(1,10)
#    arv2 = random.randint(1,10)
#    t = random.choice(tehe)
    
#    if t=="+":
#        print(f"{arv1}{t}{arv2}={arv1 + arv2}")
#    elif t=="-":
#        print(f"{arv1}{t}{arv2}={arv1 - arv2}")
#    elif t=="*":
#        print(f"{arv1}{t}{arv2}={arv1 * arv2}")
#    elif t=="/":
#        print(f"{arv1}{t}{arv2}={round(arv1 / arv2)}")
        
#Täienda eelmist ülesannet ja kasutaja käest küsitakse vastust.
#Õiged vastused loetakse kokku
#Kui saab vähemalt poole punktid, siis saab A, muul juhul MA
# import random
# tehe = ["+","-","*","/"]
# punktid = 0
# kysimuste_arv = 5
# for _ in range(kysimuste_arv):
#     arv1 = random.randint(1,10)
#     arv2 = random.randint(1,10)
#     t = random.choice(tehe)
# 
#     if t=="+":
#         print(f"{arv1}{t}{arv2}=")
#         v = int(input("Vastus: "))
#         if arv1+arv2 == v:
#             punktid+=1
#     elif t=="-":
#         print(f"{arv1}{t}{arv2}=")
#         v = int(input("Vastus: "))
#         if arv1-arv2 == v:
#             punktid+=1
#     elif t=="*":
#         print(f"{arv1}{t}{arv2}=")
#         v = int(input("Vastus: "))
#         if arv1*arv2 == v:
#             punktid+=1
#     else:
#         print(f"{arv1}{t}{arv2}=")
#         v = float(input("Vastus: "))
#         if round(arv1/arv2,1) == v:
#             punktid+=1
#             
# if punktid/kysimuste_arv >= 0.5:
#     print(f"A - {punktid}/{kysimuste_arv}")
# else:
#     print(f"MA - {punktid}/{kysimuste_arv}")
#1
# arv = 5
# for i in range(1,6):
#     print(" " * i+ "*" * arv)
#     arv-=1
# 
# 
#2
# arv = 5
# for i in range(1,6):
#     print("*" * arv)
#     arv-=1
# 
# 
#3
# arv =5
# for i in range(1,6):
#     print(" " * arv + "*" * i)
#     arv-=1
#4
# arv = 5
# for i in range(1,6):
#     print("*" * i)


# Kirjuta programm, mis summeerib paarisarve listis even_nums kuni esimese paaritu arvuni.
# Katkesta tsükkel, kui leitakse paaritu arv, kasutades break.
# Kui tsükkel lõpetab ilma paaritut arvu kohtamata, prindi sõnum “Tsükkel jõudis lõpuni” ja näita paarisarvude summat.
# summa = 0
# even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 3, 32, 34, 36, 38]
# 
# for i in even_nums:
#     if i%2==0:
#         summa+=i
#     else:
#         break
# 
# print(summa)

# print("")
# 
# range_summa = 0
# hind = 0
# range_kokku = 0
# 
# ev_data = [
#     ['vehicle', 'range', 'price'],
#     ['Tesla Model Y Long Range', '330', '58990'],
#     ['Volkswagen ID.4 Pro', '260', '39995'],
#     ['Ford Mustang Mach-E', '300', '42995'],
#     ['Audi e-tron GT', '238', '102700'],
#     ['Nissan Leaf', '149', '27400'],
#     ['BMW iX xDrive50', '324', '83995'],
#     ['Polestar 2', '265', '45500'],
#     ['Kia EV6 Long Range', '310', '47795'],
#     ['Mercedes-Benz EQS 450+', '350', '102310'],
#     ['Hyundai Kona Electric', '258', '37400']
# ]
# #kuvab autod tulpades
# for i in ev_data:
#     print(f"{i[0]:26} {i[1]:6} {i[2]:7}")
# 
# #keskmine ulatus ja hind
# for i in range(1,len(ev_data)):
#     range_summa+=int(ev_data[i][1])
#     hind+=int(ev_data[i][2])
#     range_kokku+=1
#     if int(ev_data[i][1]) > 300:
#         print(ev_data[i][0])
#     
#     
# print(f"Keskmine ulatus: {range_summa/range_kokku}")
# print(f"Keskmine summa: {hind/range_kokku}")
# print("---------")
# 
# max_koef = 1000000
# parim_auto = ""
# 
# for i in range(1,len(ev_data)):
#     koef = int(ev_data[i][2])/int(ev_data[i][1])
#     if koef<max_koef:
#         max_koef = koef
#         parim_auto = ev_data[i][0]
#         
# print(max_koef)
# print(parim_auto)
# 
