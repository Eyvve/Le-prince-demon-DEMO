from inventaire import *
from intro import *
from combat import *
from index import *
from time import sleep
import Music_sounds
from demo import *
import pickle

roi_demon = {
    'xp' : {
        "lvl": 666,
        "xp" : 0,
        "lvlnext": 666,
    },
    'hands' :{
        'hand1' : None,
        'armor' : 'Armure des Abysses'
    },
    'gold' : {
        'Argent' : 666,
    },
    'inv' : {
        'Sceptre de pouvoir' : 2,
        'Potion de soin n3' : 20,
        'Potion de mana n3' : 10,
        },
    'equipement' : {
        "Épée légendaire Sxyrsbaane" : 1,
    },
    'armor' :{
        'Armure des Abysse' : 0,
    }
}

Roi_demon_stats = ["Dieu-Roi", 55, 75, 25, 1.1, 600, 90, 5, 4, 0, 50, 5, 4, 600, 50,10]
Deva_stats = ["Deva", 25, 38, 15, 1.2, 250, 85, 5]







# significations : (0)nom, (1)attaque mini, (2)attaque max, (3)défense, (4)multiplicateur de dégat (arme), (5)vie, (6)précision, (7)chance de coup bas, (8)niveau de coup bas, (9)xp coup bas, (10)mana, (11)esquive, (12)attques magiques, (13) PV max, (14) MP max, (15) defense mini



def win_roi(enemie): #use in demo (en cas de victoire)
    from intro import Sentence
    sleep(0.5)
    os.system("cls")
    Sentence("Victoire !")
    Sentence("Vous gagnez contre " + str(enemie["nom"]) + ".")
    #bruitage de victoir (optinelle)


# # permet la monter de niveau du hero
# # exemple : update_niv_roi(char['xp'])
# def update_niv_roi(xp1) :
#     while xp1['xp'] >= xp1['lvlnext'] :
#         xp1['lvl'] += 1
#         xp1['xp'] -= xp1['lvlnext']
#         xp1['lvlnext'] = round(xp1['lvlnext'] * 1.5)
#         Sentence("Félicitation vous avez gagner 1 niveau")
#         Sentence("vous êtes au niveau " + str(xp1['lvl']))
#         update_stats_roi()
#
#
# def update_stats_roi():
#     from intro import Sentence
#     Roi_demon_stats[1] += 1
#     Roi_demon_stats[2] += 1
#     Sentence("Votre puissance augmente de 0.5 point !")
#     Roi_demon_stats[3] += 0.5
#     Roi_demon_stats[15] += 0.5
#     Sentence("Votre défense augmente de 1 point !")
#     Roi_demon_stats[5] += 10
#     Roi_demon_stats[13] += 10
#     Sentence("Votre vie augmente de 10 points !")
#     Roi_demon_stats[10] += 5
#     Roi_demon_stats[14] += 5
#     Sentence("Votre mana augmente de 5 points !")
#
#
# #a utiliser quand le hero gagne un combat
# def win_roi(enemie): #update de niveau
#     from intro import Sentence
#     Sentence("Victoire !")
#     Sentence("Vous gagnez " + str(enemie["xp"]) + ".")
#     Sentence("Le " + str(enemie["nom"]) + " avait sur lui " + str(enemie["inv"]) + " et " + str(enemie["gold"]) + " or.")
#     updating(roi_demon['inv'], enemie['inv']) #gaint des drops de l'enemie
#     updating(roi_demon['xp'], enemie['xp']) # gaint de l'xp de l'enemie
#     updating(roi_demon['gold'], enemie['or'])
#     update_niv_roi(roi_demon['xp']) #monté de niveau du hero si possible

# def pierre_sword_roi():
#     from intro import Sentence
#     Sentence("Voulez vous retirer l'épée ?.")
#     print("1. Oui")
#     print("2. Non")
#     while True:
#         choix = input("Choix :")
#         if str(choix) == "":
#             Sentence("veuillez entrer un chiffre valide")
#         else:
#             if int(choix) >= 1 and int(choix) <= 2:
#                 if int(choix) == 1:
#                     use_equipement_wapon_roi()
#                     return
#                 elif int(choix) == 2:
#                     return
#                 else:
#                    Sentence("veuillez entrer un chiffre valide")


def print_objet_roi():
    Kinv = roi_demon['inv'].keys() #transformation de l'inv en liste
    Iinv = roi_demon['inv'].values()
    Kinv_list = list(Kinv)
    Iinv_list = list(Iinv)
    for n in range(len(Kinv_list)) :
        print(n+1,Kinv_list[n],"n°:",Iinv_list[n])


def use_objet_roi(anchor) :
    from intro import Sentence
    sleep(0.2)
    os.system("cls")
    Sentence("objet")
    print("Vie :", str(Roi_demon_stats[5]) , "/",  str(Roi_demon_stats[13]), " Mana :", str(Roi_demon_stats[10]) , "/" , str(Roi_demon_stats[14]))
    print_objet_roi()
    Kinv = roi_demon['inv'].keys()
    Kinv_list = list(Kinv)
    plop = len(Kinv_list) + 1
    print(plop, "Retour")

    while True :
        from intro import Sentence
        Ninv = input("Utiliser quel objet ? :")
        if str(Ninv) == "":
            Sentence("veuillez entrer un chiffre valide")
        elif int(Ninv) == plop:
            menu_roi(anchor)
            return
        else:
            if int(Ninv) < 1 or int(Ninv) > len(Kinv_list)+1:
                Sentence("veuillez entrer un chiffre valide")
            else:
                objet = Kinv_list[int(Ninv)-1]
                if roi_demon['inv'][objet] == 0:
                    Sentence("Vous n'avez plus de cet objet en stock")
                    sleep(1)
                    use_objet_roi(anchor)
                    return
                if len(index_objet[str(objet)]) >= 2 and len(index_objet[str(objet)]) <= 4 :
                    sleep(0.5)
                    os.system("cls")
                    print("Vous utilisez " + str(objet) + ".")
                    sleep(0.5)
                    if index_objet[str(objet)][2] == 1:
                        absorbtion_soundeffect.play()
                        print("Vous gagnez ", str(index_objet[str(objet)][1]), "Pv.")
                        Roi_demon_stats[5] += index_objet[str(objet)][1]
                        if Roi_demon_stats[5] > Roi_demon_stats[13] :
                            Roi_demon_stats[5] = Roi_demon_stats[13]
                        print("")
                        roi_demon['inv'][str(objet)] -= 1
                        print("Vie :", str(Roi_demon_stats[5]) , "/",  str(Roi_demon_stats[13]), " Mana :", str(Roi_demon_stats[10]) , "/" , str(Roi_demon_stats[14]))

                    elif index_objet[str(objet)][2] == 2:
                        #bruitage de heal popo
                        print("Vous gagnez ", str(index_objet[str(objet)][1]), "Pm.")
                        Roi_demon_stats[10] += index_objet[str(objet)][1]
                        if Roi_demon_stats[10] > Roi_demon_stats[14] :
                            Roi_demon_stats[10] = Roi_demon_stats[14]
                        Sentence("")
                        roi_demon['inv'][str(objet)] -= 1
                        print("Vie :", str(Roi_demon_stats[5]) , "/",  str(Roi_demon_stats[13]), " Mana :", str(Roi_demon_stats[10]) , "/" , str(Roi_demon_stats[14]))
                    elif index_objet[str(objet)][2] == None:
                        print("Vous ne pouvez pas utiliser cet objet tout de suite.")
                        sleep(2)
                        use_objet_roi(anchor)
                        return

                    sleep(2)
                    os.system("cls")
                    Sentence("Utiliser un autre objet ? :")
                    print("1. oui")
                    print("2. non")
                    while True:
                        choix = input("Choix :")
                        menu_sound.play()
                        if str(choix) == "":
                            Sentence("veuillez entrer un chiffre valide")
                        else:
                            if int(choix) >= 1 and int(choix) <= 2:
                                if int(choix) == 1:
                                    sleep(0.5)
                                    os.system("cls")
                                    use_objet_roi(anchor)
                                    return
                                elif int(choix) == 2:
                                    menu_roi(anchor)
                                    return
                            else:
                                Sentence("veuillez entrer un chiffre valide")
                else:
                    Sentence("Ceci n'est pas un objet utilisable")
                    use_objet_roi(anchor)

def print_equipement_roi():
    Kequipement = roi_demon['equipement'].keys()
    Iequipement = roi_demon['equipement'].values()
    Kequipement_list = list(Kequipement)
    Iequipement_list = list(Iequipement)
    for n in range(len(Kequipement_list)):
        print(n+1,Kequipement_list[n],":",Iequipement_list[n])


def use_equipement_wapon_roi():
    from intro import Sentence
    from index import index_wapone
    if roi_demon['hands']['hand1'] == None:
        sleep(0.5)
        os.system("cls")
        Sentence("Arme")
        Kequipement = roi_demon['equipement'].keys()
        Kequipement_list = list(Kequipement)
        print_equipement_roi()
        print(len(Kequipement_list) + 1, "Retour")
        while True:
            wapone = str(input("Quel equipement :"))
            menu_sound.play()
            if str(wapone) == "":
                Sentence("veuillez entrer un chiffre valide")

            elif int(wapone) == len(Kequipement_list) + 1:
                menu_roi(Anchor)
                return
            else:
                if int(wapone) >= 1 and int(wapone) <= len(Kequipement_list):
                    Kequipement = roi_demon['equipement'].keys()
                    Kequipement_list = list(Kequipement)
                    wapone_equipement = Kequipement_list[int(wapone) - 1]
                    roi_demon['hands']['hand1'] = str(wapone_equipement)
                    bonus = index_wapone[str(wapone_equipement)][0]
                    Roi_demon_stats[4] += bonus
                    # bruitage equipement épée
                    Sentence("Vous équipez " + str(wapone_equipement))
                    roi_demon['equipement'][str(wapone_equipement)] -= 1
                    return
                else:
                    Sentence("veuillez entrer un chiffre valide")

    elif roi_demon['hands']['hand1'] != None:
        sleep(0.5)
        os.system("cls")
        Sentence("Voulez-vous le retirer ?")
        print("1. Oui")
        print("2. Non")
        while True:
            choix = input("Choix :")
            menu_sound.play()
            if str(choix) == "":
                Sentence("veuillez entrer un chiffre valide")
            else:
                if int(choix) >= 1 and int(choix) <= 2:
                    if int(choix) == 1:
                        remove_equipement_roi(roi_demon['hands']['hand1'])
                        return
                    elif int(choix) == 2:
                        return
                else:
                    Sentence("veuillez entrer un chiffre valide")


def remove_equipement_roi(wapone) :
    from intro import Sentence
    sleep(0.5)
    os.system("cls")
    roi_demon['hands']['hand1'] = None
    Roi_demon_stats[4] = 1
    roi_demon['equipement'][str(wapone)] = 1
    # bruitage retire equipement épée
    Sentence("Équiper un autre objet à la place ?")
    print("1. Oui")
    print("2. Non")
    while True:
        choix = input("Choix :")
        menu_sound.play()
        if str(choix) == "":
            Sentence("veuillez entrer un chiffre valide")
        else:
            if int(choix) >= 1 and int(choix) <= 2:
                if int(choix) == 1:
                    use_equipement_wapon_roi()
                    return
                elif int(choix) == 2:
                    return
            else:
                Sentence("veuillez entrer un chiffre valide")


def print_armor_roi():
    Karmor = roi_demon['armor'].keys()
    Iarmor = roi_demon['armor'].values()
    Karmor_list = list(Karmor)
    Iarmor_list = list(Iarmor)
    for n in range(len(Karmor_list)):
        print(n + 1, Karmor_list[n], "n°:", Iarmor_list[n])


def use_equipement_armor_roi():
    from intro import Sentence
    if roi_demon['hands']['armor'] == None:
        sleep(0.5)
        os.system("cls")
        Sentence("Armure")
        Karmor = roi_demon['armor'].keys()
        Karmor_list = list(Karmor)
        print_armor_roi()
        print(len(Karmor_list) + 1, "Retour")
        while True:
            armor = str(input("Quel equipement :"))
            menu_sound.play()
            if str(armor) == "":
                Sentence("veuillez entrer un chiffre valide")

            elif int(armor) == len(Karmor_list) + 1:
                menu_roi(Anchor)
                return
            else:
                if int(armor) >= 1 and int(armor) <= len(Karmor_list):
                    Karmor = roi_demon['armor'].keys()
                    Karmor_list = list(Karmor)
                    armor_equipement = Karmor_list[int(armor) - 1]
                    roi_demon['hands']['armor'] = str(armor_equipement)
                    bonus = index_armor[str(armor_equipement)][0]
                    Roi_demon_stats[3] += bonus
                    # bruitage equipement armure
                    Sentence("Vous équipez " + str(armor_equipement))
                    roi_demon['armor'][str(armor_equipement)] += 1
                    return
                else:
                    Sentence("veuillez entrer un chiffre valide")

    elif roi_demon['hands']['armor'] != None:
        sleep(0.5)
        os.system("cls")
        Sentence("Voulez-vous le retirer ?")
        print("1. Oui")
        print("2. Non")
        while True:
            choix = input("Choix :")
            menu_sound.play()
            if str(choix) == "":
                Sentence("veuillez entrer un chiffre valide")
            else:
                if int(choix) >= 1 and int(choix) <= 2:
                    if int(choix) == 1:
                        remove_armor_roi(roi_demon['hands']['armor'])
                        return
                    elif int(choix) == 2:
                        return
                else:
                    Sentence("veuillez entrer un chiffre valide")


def remove_armor_roi(armor) :
    from intro import Sentence
    Roi_demon_stats[3] = Roi_demon_stats[15]
    roi_demon['armor'][str(armor)] += 1
    roi_demon['hands']['armor'] = None
    sleep(0.5)
    os.system("cls")
    # bruitage retire equipement armure
    Sentence("Équiper un autre objet à la place ?")
    print("1. Oui")
    print("2. Non")
    while True:
        choix = input("Choix :")
        menu_sound.play()
        if str(choix) == "":
            Sentence("veuillez entrer un chiffre valide")
        else:
            if int(choix) >= 1 and int(choix) <= 2:
                if int(choix) == 1:
                    use_equipement_armor_roi()
                    return
                elif int(choix) == 2:
                    return
            else:
                Sentence("veuillez entrer un chiffre valide")


def pickle_save(roi_demon,Roi_demon_stats):
    f = open("save", "wb")
    roi_demon_save = roi_demon
    Roi_demon_stats_save = Roi_demon_stats
    d = {
        "roi_demon" : roi_demon_save,
        "Roi_demon_stats" : Roi_demon_stats_save
    }
    pickle.dump(d,f)
    f.close()

def pikle_print_save():
    pickle_file = open("save", "rb")
    objects = []
    while True:
        try:
            objects.append(pickle.load(pickle_file))
        except EOFError:
            break
    pickle_file.close()
    print(objects)

def pickle_load():
    f = open("save","rb")
    d = pickle.load(f)
    roi_demon = d["roi_demon"]
    f.close()
    return(roi_demon)

def pickle_load_stats():
    f = open("save","rb")
    d = pickle.load(f)
    Roi_demon_stats = d["Roi_demon_stats"]
    f.close()
    return(Roi_demon_stats)

def save(anchor):
    from intro import Sentence
    from intro import skip_touch
    Sentence("Le mot de passe associé à votre progression est :")
    print("")
    if anchor == 1:
        print("Zazranoth")
        skip_touch()
    elif anchor == 2:
        print("Ginn")
        skip_touch()
    elif anchor == 3:
        print("Ulric")
        skip_touch()

if Anchor != 0 :
    roi_demon = pickle_load()
    Roi_demon_stats = pickle_load_stats()


def menu_roi(anchor) :#use in demo (entré de map et sortie de map)
    from intro import titlebis
    from intro import Sentence
    sleep(0.5)
    os.system("cls")
    Sentence("Voulez-vous faire quelque chose ?")
    print("1. Inventaire")
    print("2. Sauvgarder")
    print("3. Continuer")
    while True :
        choix = input("Choix :")
        if str(choix) == "":
            Sentence("veuillez entrer un chiffre valide")
        else:
            if int(choix) >= 1 and int(choix) <= 3:
                if int(choix) == 1 : #inventaire
                    menu_sound.play()
                    sleep(0.5)
                    os.system("cls")
                    print(roi_demon['gold']['Argent'], "or.")
                    print("1. Objet")
                    print("2. Équipement")
                    print('3. Retour')
                    while True:
                        choix = input("Choix :")
                        menu_sound.play()
                        if str(choix) == "":
                            Sentence("veuillez entrer un chiffre valide")
                        else:
                            if int(choix) >= 1 and int(choix) <= 3:
                                if int(choix) == 1:
                                    sleep(0.5)
                                    os.system("cls")
                                    use_objet_roi(anchor)
                                    return
                                elif int(choix) == 2:
                                    sleep(0.5)
                                    os.system("cls")
                                    if roi_demon['hands']['hand1'] != None:
                                        Sentence("Vous avez " + str(roi_demon['hands']['hand1']) + " d'équipé.")
                                    if roi_demon['hands']['armor'] != None:
                                        Sentence("Vous avez " + str(roi_demon['hands']['armor']) + " d'équipé.")
                                    print("1. Equiper une arme")
                                    print("2. Equiper une armure")
                                    print("3. Retour")
                                    while True:
                                        choix = input("Choix :")
                                        menu_sound.play()
                                        if str(choix) == "":
                                            Sentence("veuillez entrer un chiffre valide")
                                        else:
                                            if int(choix) >= 1 and int(choix) <= 3:
                                                if int(choix) == 1:
                                                    sleep(0.5)
                                                    os.system("cls")
                                                    use_equipement_wapon_roi()
                                                    menu_roi(anchor)
                                                    return
                                                elif int(choix) == 2:
                                                    sleep(0.5)
                                                    os.system("cls")
                                                    use_equipement_armor_roi()
                                                    menu_roi(anchor)
                                                    return
                                                elif int(choix) == 3:
                                                    sleep(0.5)
                                                    os.system("cls")
                                                    menu_roi(anchor)
                                                    return
                                            else:
                                                Sentence("veuillez entrer un chiffre valide")
                                elif int(choix) == 3:
                                    sleep(0.5)
                                    os.system("cls")
                                    menu_roi(anchor)
                                    return
                            else:
                                Sentence("veuillez entrer un chiffre valide")
                elif int(choix) == 2 : #sauvgarder :
                    menu_sound.play()
                    sleep(0.5)
                    os.system("cls")
                    Sentence("Êtes vous sur de vouloir sauvegarder ?")
                    print("1. oui")
                    print("2. non")
                    while True:
                        choix = input("Choix :")
                        menu_sound.play()
                        if str(choix) == "":
                            Sentence("veuillez entrer un chiffre valide")
                        else:
                            if int(choix) >= 1 and int(choix) <= 2:
                                if int(choix) == 1:
                                    sleep(0.5)
                                    # action de sauvegarde
                                    os.system("cls")
                                    save(anchor)
                                    pickle_save(roi_demon,Roi_demon_stats)
                                    Sentence("Voulez vous quitter ?")
                                    print("1. oui")
                                    print("2. non")
                                    while True:
                                        choix = input("Choix :")
                                        menu_sound.play()
                                        if str(choix) == "":
                                            Sentence("veuillez entrer un chiffre valide")
                                        if int(choix) >= 1 and int(choix) <= 2:
                                            if int(choix) == 1:
                                                sleep(0.5)
                                                os.system("cls")
                                                titlebis()
                                                return
                                            elif int(choix) == 2:
                                                sleep(0.5)
                                                os.system("cls")
                                                menu_roi(anchor)
                                                return
                                        else:
                                            Sentence("veuillez entrer un chiffre valide")
                                elif int(choix) == 2:
                                    sleep(0.5)
                                    os.system("cls")
                                    menu_roi(anchor)
                                    return
                            else:
                                Sentence("veuillez entrer un chiffre valide")
                elif int(choix) == 3:
                    validation_sound.play()
                    sleep(0.5)
                    os.system("cls")
                    return
            else:
                Sentence("veuillez entrer un chiffre valide")




def menu_roi_sceptre() :#use in demo (utilisation quand tu dois planter un sceptre de pouvoir)
    from intro import Sentence
    sleep(1.5)
    os.system("cls")
    Sentence("Utiliser un sceptre de pouvoir.")
    from intro import Sentence
    print_objet_roi()
    Kinv = roi_demon['inv'].keys()
    Kinv_list = list(Kinv)
    while True:
        Ninv = input("Utiliser quel objet ? :")
        if str(Ninv) == "":
            Sentence("veuillez entrer un chiffre valide")
        else:
            if int(Ninv) >= 1 and int(Ninv) <= len(Kinv_list):
                objet = Kinv_list[int(Ninv) - 1]
                if len(index_objet[str(objet)]) == 4:
                    Sentence("Vous utilisez " + str(objet) + ".")
                    scepter_sound.play()
                    roi_demon['inv'][str(objet)] -= 1
                    return

                else:
                    Sentence("Vous tentez d'utiliser " + str(objet) + ".")
                    Sentence("Ceci n'est pas un sceptre de pouvoir")
                    menu_roi_sceptre()
                    return
            else:
                Sentence("veuillez entrer un chiffre valide")
                menu_roi_sceptre()
                return
    return


