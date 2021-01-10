
from random import *
from collections import *
from index import *
from mob import *
from sauvgarde import *
from combat import *
from time import sleep

#permet de fusioner les inventaires ou l'xp gagner au combat
#exemple : updating(char['inv'], gobelin['inv'])
#exemple : updating(char['xp'], gobelin['xp'])
def updating(objetupdate1, objetupdate2):
    for k, v in objetupdate2.items():
        if k in objetupdate1:
            objetupdate1[k] += objetupdate2[k]
        else:
            objetupdate1[k] = objetupdate2[k]

# permet la monter de niveau du hero
# exemple : update_niv(char['xp'])
def update_niv(xp1) :
    while xp1['xp'] >= xp1['lvlnext'] :
        xp1['lvl'] += 1
        xp1['xp'] -= xp1['lvlnext']
        xp1['lvlnext'] = round(xp1['lvlnext'] * 1.5)
        print("Félicitation vous avez gagner 1 niveau")
        print("vous êtes au niveau", xp1['lvl'])
        update_stats()


# permet la monter des stats du hero quand il gagne un niveau
# exemple : update_stats(char['stats'])


def update_stats():
    Prince_stats[1] += 1
    Prince_stats[2] += 1
    Sentence("Votre puissance augmente de 0.5 point !")
    Prince_stats[3] += 0.5
    Prince_stats[15] += 0.5
    Sentence("Votre défense augmente de 1 point !")
    Prince_stats[5] += 10
    Prince_stats[13] += 10
    Sentence("Votre vie augmente de 10 points !")
    Prince_stats[10] += 5
    Prince_stats[14] += 5
    Sentence("Votre mana augmente de 5 points !")


#a utiliser quand le hero gagne un combat
def win(enemie):
    print("Victoire !")
    print("Vous gagnez", enemie["xp"],".")
    print("Le ", enemie["nom"], " avait sur lui ", enemie["inv"], "et", enemie["gold"],"or.")
    updating(char['inv'], enemie['inv']) #gaint des drops de l'enemie
    updating(char['xp'], enemie['xp']) # gaint de l'xp de l'enemie
    updating(char['gold'], enemie['or'])
    update_niv(char['xp']) #monté de niveau du hero si possible


#a utiliser quand le hero trouve un coffre
def chest(coffreN): #mettre le numéro du coffre
    print("Vous ouvrez le coffre.")
    print("Il contenait ")
    print_coffre(coffreN)
    updating(char['inv'], coffreN["inv"])

def print_coffre(coffre):
    Kgold = coffre['gold'].keys()  # transformation de l'inv en liste
    Igold = coffre['gold'].values()
    Kgold_list = list(Kgold)
    Igold_list = list(Igold)
    for n in range(len(Kgold_list)):
        print(Kgold_list[n], ":", Igold_list[n])
    Kinv = coffre['inv'].keys() #transformation de l'inv en liste
    Iinv = coffre['inv'].values()
    Kinv_list = list(Kinv)
    Iinv_list = list(Iinv)
    for n in range(len(Kinv_list)) :
        print(n+1,Kinv_list[n],"n°:",Iinv_list[n])


def print_objet():
    Kinv = char['inv'].keys() #transformation de l'inv en liste
    Iinv = char['inv'].values()
    Kinv_list = list(Kinv)
    Iinv_list = list(Iinv)
    for n in range(len(Kinv_list)) :
        print(n+1,Kinv_list[n],"n°:",Iinv_list[n])


def use_objet() :
    print("objet")
    from combat import Prince_stats
    print("Vie :", Prince_stats[5],"/",Prince_stats[13], "Mana :", Prince_stats[10], "/", Prince_stats[14])
    print_objet()
    Kinv = char['inv'].keys()
    Kinv_list = list(Kinv)
    while True :
        Ninv = input("Utiliser quel obejt ? :")
        if str(Ninv) == "":
            print("Choix indisponnible.")
        else:
            if int(Ninv) >= 1 and int(Ninv) <= len(Kinv_list):
                objet = Kinv_list[int(Ninv)-1]
                if len(index_objet[str(objet)]) >= 2:
                    print("Vous utilisez ",objet,".")
                    if index_objet[str(objet)][2] == 1:
                        print("Vous gagnez ",index_objet[str(objet)][1],"Pv.")
                        Prince_stats[5] += index_objet[str(objet)][1]
                        if Prince_stats[5] > Prince_stats[13] :
                            Prince_stats[5] = Prince_stats[13]
                        print("")
                        print("Vie :", Prince_stats[5],"/",Prince_stats[13], "Mana :", Prince_stats[10], "/", Prince_stats[14])
                        return
                    elif index_objet[str(objet)][2] == 2:
                        print("Vous gagnez ",index_objet[str(objet)][1], "Pm.")
                        Prince_stats[10] += index_objet[str(objet)][1]
                        if Prince_stats[10] > Prince_stats[14] :
                            Prince_stats[10] = Prince_stats[14]
                        print("")
                        print("Vie :", Prince_stats[5],"/",Prince_stats[13], "Mana :", Prince_stats[10], "/", Prince_stats[14])
                        print("Utiliser un autre obejt ? :")
                        print("1. oui")
                        print("2. non")
                        while True:
                            choix = input("Choix :")
                            if str(choix) == "":
                                print("Choix indisponnible.")
                            else:
                                if int(choix) >= 1 and int(choix) <= 2:
                                    if int(choix) == 1:
                                        use_objet()
                                        return
                                    elif int(choix) == 2:
                                        return
                                else:
                                    print("Choix indisponnible.")

            else:
                print("Choix indisponnible.")



def print_equipement():
    Kequipement = char['equipement'].keys()
    Iequipement = char['equipement'].values()
    Kequipement_list = list(Kequipement)
    Iequipement_list = list(Iequipement)
    for n in range(len(Kequipement_list)):
        print(n+1,Kequipement_list[n],"n°:",Iequipement_list[n])


def use_equipement_wapon():
    from index import index_wapone
    if char['hands']['hand1'] == None:
        print_equipement()
        wapone = str(input("Quelle equipement :"))
        Kequipement = char['equipement'].keys()
        Kequipement_list = list(Kequipement)
        wapone_equipement = Kequipement_list[int(wapone)-1]
        char['hands']['hand1'] = str(wapone_equipement)
        bonus = index_wapone[str(wapone_equipement)][0]
        combat.Prince_stats[4] += bonus
        print("Vous équipez", wapone_equipement)
        char['equipement'][str(wapone_equipement)] -= 1
        return

    elif char['hands']['hand1'] != None:
        print("Voulez vous le retirer ?")
        print("1. Oui")
        print("2. Non")
        while True:
            choix = input("Choix :")
            if str(choix) == "":
                print("Choix indisponnible.")
            else:
                if int(choix) >= 1 and int(choix) <= 2:
                    if int(choix) == 1:
                        remove_equipement(char['hands']['hand1'])
                        return
                    elif int(choix) == 2:
                        return
                else:
                    print("Choix indisponnible.")


def remove_equipement(wapone) :
    char['hands']['hand1'] = None
    combat.Prince_stats[4] = 1
    char['equipement'][str(wapone)] = 1
    print("Équiper un objet à la place ?")
    print("1. Oui")
    print("2. Non")
    while True:
        choix = input("Choix :")
        if str(choix) == "":
            print("Choix indisponnible.")
        else:
            if int(choix) >= 1 and int(choix) <= 2:
                if int(choix) == 1:
                    use_equipement_wapon()
                    return
                elif int(choix) == 2:
                    return
            else:
                print("Choix indisponnible.")


def print_armor():
    Karmor = char['armor'].keys()
    Iarmor = char['armor'].values()
    Karmor_list = list(Karmor)
    Iarmor_list = list(Iarmor)
    for n in range(len(Karmor_list)):
        print(n + 1, Karmor_list[n], "n°:", Iarmor_list[n])


def use_equipement_armor():
    from index import index_wapone
    if char['hands']['armor'] == None:
        print_armor()
        armor = str(input("Quelle armure :"))
        Karmor = char['armor'].keys()
        Karmor_list = list(Karmor)
        armor_equipement = Karmor_list[int(armor)-1]
        char['hands']['armor'] = str(armor_equipement)
        bonus = index_armor[str(armor_equipement)][0]
        combat.Prince_stats[3] += bonus
        print("Vous équipez", armor_equipement)
        char['armor'][str(armor_equipement)] += 1
        return

    elif char['hands']['armor'] != None:
        print("Voulez vous le retirer ?")
        print("1. Oui")
        print("2. Non")
        while True:
            choix = input("Choix :")
            if str(choix) == "":
                print("Choix indisponnible.")
            else:
                if int(choix) >= 1 and int(choix) <= 2:
                    if int(choix) == 1:
                        remove_armor(char['hands']['armor'])
                        return
                    elif int(choix) == 2:
                        return
                else:
                    print("Choix indisponnible.")


def remove_armor(armor) :
    combat.Prince_stats[3] = combat.Prince_stats[15]
    char['armor'][str(armor)] += 1
    char['hands']['armor'] = None
    print("Équiper un objet à la place ?")
    print("1. Oui")
    print("2. Non")
    while True:
        choix = input("Choix :")
        if str(choix) == "":
            print("Choix indisponnible.")
        else:
            if int(choix) >= 1 and int(choix) <= 2:
                if int(choix) == 1:
                    use_equipement_armor()
                    return
                elif int(choix) == 2:
                    return
            else:
                print("Choix indisponnible.")



def menu() :
    print("Voulez vous faire quelque chause ?")
    print("1. Inventaire")
    print("2. Sauvgarder")
    print("3. Quitter")
    while True :
        choix = input("Choix :")
        if str(choix) == "":
            print("Choix indisponnible.")
        else:
            if int(choix) >= 1 and int(choix) <= 3:
                if int(choix) == 1 : #inventaire
                    print(char['gold']['Argent'], "or.")
                    print("1. Objet")
                    print("2. Équipement")
                    print('3. Quitter')
                    while True:
                        choix = input("Choix :")
                        if str(choix) == "":
                            print("Choix indisponnible.")
                        else:
                            if int(choix) >= 1 and int(choix) <= 3:
                                if int(choix) == 1:
                                    print("Vie :", Prince_stats[5],"/",Prince_stats[13], "Mana :", Prince_stats[10],"/",Prince_stats[14])
                                    print_objet()
                                    print("1. Utiliser un objet")
                                    print("2. Quitter")
                                    while True:
                                        choix = input("Choix :")
                                        if str(choix) == "":
                                            print("Choix indisponnible.")
                                        else:
                                            if int(choix) >= 1 and int(choix) <= 2:
                                                if int(choix) == 1:
                                                    use_objet()
                                                    return
                                                elif int(choix) == 2:
                                                    return
                                            else:
                                                print("Choix indisponnible.")
                                elif int(choix) == 2:
                                    if char['hands']['hand1'] != None:
                                        print("Vous avez", char['hands']['hand1'], "d'équipé.")
                                    if char['hands']['armor'] != None:
                                        print("Vous avez", char['hands']['armor'], "d'équipé.")
                                    print("1. Equiper une arme")
                                    print("2. Equiper une armure")
                                    print("3. Quitter")
                                    while True:
                                        choix = input("Choix :")
                                        if str(choix) == "":
                                            print("Choix indisponnible.")
                                        else:
                                            if int(choix) >= 1 and int(choix) <= 3:
                                                if int(choix) == 1:
                                                    use_equipement_wapon()
                                                    return
                                                elif int(choix) == 2:
                                                    use_equipement_armor()
                                                    return
                                                elif int(choix) == 3:
                                                    return
                                            else:
                                                print("Choix indisponnible.")
                                elif int(choix) == 3:
                                    return
                            else:
                                print("Choix indisponnible.")
                elif int(choix) == 2 : #sauvgarder :
                    print("Êtes vous sur de vouloir sauvegarder ?")
                    print("1. oui")
                    print("2. non")
                    while True:
                        choix = input("Choix :")
                        if str(choix) == "":
                            print("Choix indisponnible.")
                        else:
                            if int(choix) >= 1 and int(choix) <= 2:
                                if int(choix) == 1:
                                    save(char, history)
                                    print("Voulez vous quiter ?")
                                    print("1. oui")
                                    print("2. non")
                                    while True:
                                        choix = input("Choix :")
                                        if str(choix) == "":
                                            print("Choix indisponnible.")
                                        if int(choix) >= 1 and int(choix) <= 2:
                                            if int(choix) == 1:
                                                titlebis()
                                                return
                                            elif int(choix) == 2:
                                                return
                                        else:
                                            print("Choix indisponnible.")
                            else:
                                print("Choix indisponnible.")
                elif int(choix) == 3:
                    return
            else:
                print("Choix indisponnible.")
