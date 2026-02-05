valik = "jukebox.txt"
fail = open(valik, encoding="UTF-8")
nr = 1
for  rida in fail:
    print(nr, rida, end="")
    nr += 1

fail.close()

nr = 1

otsus = int(input("Millist laulu tahad?: "))
fail = open(valik, encoding="UTF-8")
for  rida in fail:
    if otsus == nr:
        print(nr, rida, end="")
    nr += 1


fail.close()