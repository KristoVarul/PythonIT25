# Kristo Varul
# 05.02.2026

fail = open("rebased.txt", encoding="UTF-8")

vastuvõetud = []

for rida in fail:
    vastuvõetud.append(int(rida))

fail.close()
aasta = int(input("sisesta aasta 2011-2019"))
print(vastuvõetud[aasta])
#2011 2012 2013