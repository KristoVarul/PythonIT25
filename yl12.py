#pank depo ja väljavõte
def depo(s, r):
    """"
    Docstring for repo
    
    """
    uus = s + r
    return uus

def vv(s, r):
    """"
    Docstring for vv
    
    """
    uus = s - r
    return uus

saldo = 100


print(saldo)
saldo = depo(saldo, 10)
saldo = depo(saldo, 100)
saldo = depo(saldo, 10000)
saldo = depo(saldo, 15)
saldo = depo(saldo, 1)
print(saldo)
saldo = vv(saldo, 100)
saldo = vv(saldo, 100)
saldo = vv(saldo, 100)
saldo = vv(saldo, 100)
saldo = vv(saldo, 100)
saldo = vv(saldo, 100)
print(saldo)






#lambda näide
#5L/100
#100km
# L * KM/100
kytus = lambda x, y: x * y/100
print(kytus(5, 150))





#funktsioon dokumentatsiooniga
#12.1

def tempTeisendamine(t, k):
    """
    Teisendab C > F või F > C

    Parameetrid:
    t (string): Tekst.
    k (int): Teine arv.

    Tagastab:
    Prindib vastuse

    Näide:
    >>> tempTeisendamine("c", 19.43)
    5
    5
    5
    """
    if t == "c":
        #F leidmine
        vastus = k * 9/5 + 32
    elif t == "f":
        #C leidmine
        vastus = (k - 32) / (9/5)
    else:
        vastus = "Ma ei mõista sind!"
    print(vastus)

tempTeisendamine("c", 19.43)
tempTeisendamine("f", 19.43)
tempTeisendamine("fklshfklsahfsalkf", 19.43)
print(tempTeisendamine.__doc__)