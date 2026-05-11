import requests

vastus = requests.get("https://dummyjson.com/carts")
andmed = vastus.json()
ostukorvid = andmed["carts"]
print("Ostukorv nr 1 tooted:")
for toode in ostukorvid[0]["products"]:
    print(toode["title"], "-", toode["quantity"], "tk")

kokku = 0
for korv in ostukorvid:
    kokku = kokku + korv["total"]

keskmine = kokku / len(ostukorvid)
print("Keskmine summa:", keskmine)

kogusumma = 0
for korv in ostukorvid:
    kogusumma = kogusumma + korv["total"]
print("Kogusumma:", kogusumma)

suurim = ostukorvid[0]
for korv in ostukorvid:
    if korv["totalProducts"] > suurim["totalProducts"]:
        suurim = korv

print("Kõige rohkem tooteid on korvis nr", suurim["id"])
print("Tooteid:", suurim["totalProducts"])