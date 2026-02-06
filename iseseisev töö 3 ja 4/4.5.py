failinimi = input("Palun sisesta failinimi: ")
fail = open("mündid.txt", encoding="utf-8")

def pronksikarva_summa(a_arv):
    summa = 0
    for arv in a_arv:
        if arv == 1:
            value += 1
        if arv == 2:
            value += 2
        if arv == 5:
            value += 5
    return summa

a_arv = []
for rida in fail:
    arv = int(rida.strip())
    a_arv.append(arv)

fail.close()

tulemus = pronksikarva_summa(a_arv)

print(f"Hoiupõrsasse läheb {tulemus} senti")