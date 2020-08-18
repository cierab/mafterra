from random import seed
from random import random

roleblock = False
blackmailer = False
strongman = False
graverobber = False
spy = False
lawyer = False
godfather = False
nightkill = False
protective = False
lovers = False
sleepwalker = False
night_owl = False
pariah = False
chatterbox = False
traitor = False
survivor = False
jester = False

n = int(input("Enter number of players, minimum 7: "))
s = int(input("Enter random seed, any whole number: "))
seed(s)
value = random()
print(value)

# input seed too

if n > 9:
    mafia_value = (n-5)**(1/2)
else:
    mafia_value = 2
mafia_chance = mafia_value - int(mafia_value)

if mafia_chance > value:
    mafia_value = mafia_value + 1

value = random()
print(value)

if n < 9:
    town_roles_value = 2
else:
    town_roles_value = (n-9)**(1/2)+2
town_role_chance = town_roles_value - int(town_roles_value)

if town_role_chance > value:
    town_roles_value = town_roles_value + 1

third_party_count = 0

third_party_value = int(((n-7)**(1/2)-0.5)*2)
while third_party_value > 0:
    value = random()
    print(value)
    print(third_party_count)
    print(third_party_value)
    if value > 0.7:
        third_party_count = third_party_count + 1
    third_party_value = third_party_value - 1

mafia_count = int(mafia_value)
role_count = int(town_roles_value)
town_count = int(n - mafia_count - role_count - third_party_count)

print("Number of Mafia: " + str(mafia_count))
print("Number of Town Roles: " + str(role_count))
print("Number of Third Party: " + str(third_party_count))
print("Number of Regular Town: " + str(n - mafia_count - role_count - third_party_count))

print("Mafia Roles:")
while mafia_count > 0:
    value = random()
    if value <= 0.3:
        print("Mafia Goon")
        mafia_count = mafia_count - 1
    if value <= 0.5 and value > 0.3 and roleblock == False:
            print("Hooker")
            roleblock = True
            mafia_count = mafia_count - 1
    if value <= 0.65 and value > 0.5 and blackmailer == False:
        print("Blackmailer")
        blackmailer = True
        mafia_count = mafia_count - 1
    if value <= 0.75 and value > 0.65 and strongman == False:
        print("Strongman")
        strongman = True
        mafia_count = mafia_count - 1
    if value <= 0.9 and value > 0.75 and graverobber == False and n > 9:
        print("Graverobber")
        graverobber = True
        mafia_count = mafia_count - 1
    if value <= 0.95 and value > 0.9 and spy == False:
        print("Spy")
        spy = True
        mafia_count = mafia_count - 1
    if value <= 0.975 and value > 0.95 and n > 12 and lawyer == False:
        print("Lawyer")
        lawyer = True
        mafia_count = mafia_count - 1
    if value <= 1 and value > 0.975 and n > 12 and godfather == False:
        print("Godfather")
        godfather = True
        mafia_count = mafia_count - 1

print("Town Roles:")
value = random()
if roleblock == False and protective == False:
    if value <= 0.8:
        print("Nurse")
        roleblock = True
        protective = True
        role_count = role_count - 1
    if value > 0.8:
        print("Jailer")
        roleblock = True
        nightkill = True
        protective = True
        role_count = role_count - 1
if roleblock == True and protective == False:
    if value <= 0.7:
        print("Doctor")
        protective = True
        role_count = role_count - 1
    if value > 0.7:
        print("Bodyguard")
        protective = True
        role_count = role_count - 1

value = random()
if value <= 0.8:
    print("Detective")
    role_count = role_count - 1
if value > 0.8 and value <= 0.925:
    print("Seer")
    role_count = role_count - 1
if value > 0.925:
    print("Quack Psychic")
    role_count = role_count - 1

if role_count > 0:
    value = random()
    if value <= 0.6:
        print("Coroner")
        role_count = role_count - 1
    if value > 0.6 and value <= 0.9:
        print("Mortician")
        role_count = role_count - 1
    if value > 0.9:
        print("Forensic Analyst")
        role_count = role_count - 1

if role_count > 0:
    value = random()
    if value <= 0.3:
        print("Lovers")
        lovers = True
        role_count = role_count - 1
    if value > 0.3 and value <= 0.5:
        print("Celebrity")
        role_count = role_count - 1
    if value > 0.5 and value <= 0.7:
        print("Saint")
        role_count = role_count - 1
    if value > 0.7:
        print("Innocent Child")
        role_count = role_count - 1
    
if role_count > 0:
    value = random()
    if value <= 0.5:
        print("Governor")
        role_count = role_count - 1
    if value > 0.5:
        print("Mayor")
        role_count = role_count - 1

if role_count > 0 and nightkill == False:
        if value <= 0.4:
            print("Vigilante")
            nightkill = True
            role_count = role_count - 1
        if value <= 0.8 and value > 0.4:
            print("Veteran")
            nightkill = True
            role_count = role_count - 1
        if value > 0.8:
            print("Granny")
            nightkill = True
            role_count = role_count - 1 

while town_count > 0:
    value = random()
    if lovers == True:
        print("Lovers")
        lovers = False
        town_count = town_count - 1
    if value <= 0.75:
        print("Townie")
        town_count = town_count - 1
    if value <= 0.8 and value > 0.75 and pariah == False:
        print("Pariah")
        pariah = True
        town_count = town_count - 1
    if value <= 0.825 and value > 0.8 and sleepwalker == False:
        print("Sleepwalker")
        sleepwalker = True
        town_count = town_count - 1
    if value <= 0.85 and value > 0.825 and night_owl == False:
        print("Night Owl")
        night_owl = True
        town_count = town_count - 1
    if value <= 0.875 and value > 0.85 and traitor == False:
        print("Traitor")
        traitor = True
        town_count = town_count - 1
    if value <= 0.9 and value > 0.875 and chatterbox == False:
        print("Chatterbox")
        chatterbox = True
        town_count = town_count - 1
    if value <= 0.95 and value > 0.9 and nightkill == False:
        print("Vigilante")
        nightkill = True
        town_count = town_count - 1
    if value <= 0.98 and value > 0.95 and nightkill == False:
        print("Veteran")
        nightkill = True
        town_count = town_count - 1
    if value > 0.98 and nightkill == False:
        print("Granny")
        nightkill = True
        town_count = town_count - 1

print("Third Party Roles:")
while third_party_count > 0:
    value = random()
    if value <= 0.25:
        print("Angel")
        third_party_count = third_party_count - 1
    if value <= 0.5 and value > 0.25:
        print("Hater")
        third_party_count = third_party_count - 1
    if value <= 0.7 and value > 0.5 and survivor == False:
        print("Survivor")
        survivor = True
        third_party_count = third_party_count - 1
    if value <= 0.8 and value > 0.7 and survivor == False:
        print("Mastermind")
        survivor = True
        third_party_count = third_party_count - 1
    if value <= 0.9 and value > 0.8 and n > 9:
        print("Serial Killer")
        third_party_count = third_party_count - 1
    if value > 0.9 and jester == False and n > 12:
        print("Jester")
        third_party_count = third_party_count - 1