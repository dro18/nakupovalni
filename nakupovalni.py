spar = []

x = raw_input("Ali zelis dodati izdelek na nakupovalni seznam? ")

if  x == "da":
    y = raw_input("Kateri izdelek zelis dodati na listo? ")
    spar.append(y)


    while raw_input("Ali zelis dodati se kaj?") == "da":
        y = raw_input("Kateri izdelek zelis dodati na listo? ")
        spar.append(y)




else:
    print "Onda nista"

print spar