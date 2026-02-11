# Ülesanne 11
# Kristo Varul
# argumendid
import turtle
import random
turtle.speed(0)
# def minu_oma(a, b):
#     c = a + b
#     return c
#     
# print(minu_oma(55,66))

# def pikim_sona(list):
#     pikimArv = 0
#     pikimNimi = ""
#     for i in list:
#         if len(i) > pikimArv:
#             pikimArv = len(i)
#             pikimNimi = i
#     return pikimNimi
#   
#   
#   
# nimed = ["Joosep", "Joonas", "Mario", "Kivakesekesekesekene"]
# print(pikim_sona(nimed))

def pikim_sona(list):
    prev_value = 0
    sona = ""
    for i in list:
        if len(i) > prev_value:
            prev_value = len(i)
            sona = i
    return sona

def kolm_pikimat_sona(lis):
    if len(lis) > 2:
        lis.sort(key=len, reverse=True)
        return lis[:3]
    return(lis)

def viisnurk(k):
    for i in range(5):
        turtle.fd(k)
        turtle.lt(144)

def ring(r):
    turtle.circle(r)

def ruut(k):
    for i in range(4):
        turtle.fd(k)
        turtle.lt(90)

def suvaline(k):
    suv = random.randint(1,3)
    if suv==1:
        viisnurk(k)
    elif suv==2:
        ring(k)
    else:
        ruut(k)

sonad = ["Auto", "Jalgratas", "Horsecock", "IsaneVaal", "MarioMetshein"]

print(pikim_sona(sonad))
print(kolm_pikimat_sona(sonad))

suvaline(100)
        
turtle.done()
