import random

capitals = {"Afganistan" : "Kabul" ,
    "Albania" : "Tirana" ,
    "Algeria" :	"Algiers",
    "Andorra" :	"Andorra",
    "Angola" :	"Luanda",
    "Antigua and Barbuda" : "Saint John's",
    "Argentina" :	"Buenos Aires",
    "Armenia" : "Yerevan",
    "Australia" :	"Canberra",
    "Austria":	"Vienna",
    "Azerbaijan" :	"Baku"
}

print "Si zelis igrati igrico glavna mesta?"

if raw_input() == "da":
    drzava_x = random.choice(capitals.keys())

    score = 0
    print "Kaj je glavno mesto "+drzava_x+"?"
    izbrana_drzava = raw_input()



    while izbrana_drzava == capitals[drzava_x] :
        score += 1
        drzava_x = random.choice(capitals.keys())
        print "Kaj je glavno mesto "+drzava_x+"?"
        izbrana_drzava = raw_input()

    print "Your score is " + str(score)

else:
    print "Res si guzlar"
