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
    clsglobal()
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
    clsglobal()
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
                Sentence("Veuillez entrer un chiffre valide")
            else:
                objet = Kinv_list[int(Ninv)-1]
                if roi_demon['inv'][objet] == 0:
                    Sentence("Vous n'avez plus de cet objet en stock")
                    sleep(1)
                    use_objet_roi(anchor)
                    return
                if len(index_objet[str(objet)]) >= 2 and len(index_objet[str(objet)]) <= 4 :
                    sleep(0.5)
                    clsglobal()
                    print("Vous utilisez " + str(objet) + ".")
                    sleep(0.5)
                    if index_objet[str(objet)][2] == 1:
                        if Roi_demon_stats[5] == Roi_demon_stats[13] :
                            Sentence("Pourquoi vous avez bu la potion, vos pv sont déjà au max.")
                            roi_demon['inv'][str(objet)] -= 1
                            sleep(0.5)
                        else:
                            absorbtion_soundeffect.play()
                            print("Vous gagnez ", str(index_objet[str(objet)][1]), "Pv.")
                            Roi_demon_stats[5] += index_objet[str(objet)][1]
                            if Roi_demon_stats[5] > Roi_demon_stats[13] :
                                Roi_demon_stats[5] = Roi_demon_stats[13]
                            print("")
                            roi_demon['inv'][str(objet)] -= 1
                            print("Vie :", str(Roi_demon_stats[5]) , "/",  str(Roi_demon_stats[13]), " Mana :", str(Roi_demon_stats[10]) , "/" , str(Roi_demon_stats[14]))

                    elif index_objet[str(objet)][2] == 2:
                        if Roi_demon_stats[10] == Roi_demon_stats[14] :
                            Sentence("Pourquoi vous avez bu la potion, vos pm sont déjà au max.")
                            roi_demon['inv'][str(objet)] -= 1
                            sleep(0.5)
                        else:
                            absorbtion_soundeffect.play()
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
                    clsglobal()
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
                                    clsglobal()
                                    use_objet_roi(anchor)
                                    return
                                elif int(choix) == 2:
                                    menu_roi(anchor)
                                    return
                            else:
                                Sentence("Veuillez entrer un chiffre valide")
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
        clsglobal()
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
                    Sentence("Veuillez entrer un chiffre valide")

    elif roi_demon['hands']['hand1'] != None:
        sleep(0.5)
        clsglobal()
        Sentence("Voulez-vous le retirer ?")
        print("1. Oui")
        print("2. Non")
        while True:
            choix = input("Choix :")
            menu_sound.play()
            if str(choix) == "":
                Sentence("Veuillez entrer un chiffre valide")
            else:
                if int(choix) >= 1 and int(choix) <= 2:
                    if int(choix) == 1:
                        remove_equipement_roi(roi_demon['hands']['hand1'])
                        return
                    elif int(choix) == 2:
                        return
                else:
                    Sentence("Veuillez entrer un chiffre valide")


def remove_equipement_roi(wapone) :
    from intro import Sentence
    sleep(0.5)
    clsglobal()
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
            Sentence("Veuillez entrer un chiffre valide")
        else:
            if int(choix) >= 1 and int(choix) <= 2:
                if int(choix) == 1:
                    use_equipement_wapon_roi()
                    return
                elif int(choix) == 2:
                    return
            else:
                Sentence("Veuillez entrer un chiffre valide")


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
        clsglobal()
        Sentence("Armure")
        Karmor = roi_demon['armor'].keys()
        Karmor_list = list(Karmor)
        print_armor_roi()
        print(len(Karmor_list) + 1, "Retour")
        while True:
            armor = str(input("Quel equipement :"))
            menu_sound.play()
            if str(armor) == "":
                Sentence("Veuillez entrer un chiffre valide")

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
                    Sentence("Veuillez entrer un chiffre valide")

    elif roi_demon['hands']['armor'] != None:
        sleep(0.5)
        clsglobal()
        Sentence("Voulez-vous le retirer ?")
        print("1. Oui")
        print("2. Non")
        while True:
            choix = input("Choix :")
            menu_sound.play()
            if str(choix) == "":
                Sentence("Veuillez entrer un chiffre valide")
            else:
                if int(choix) >= 1 and int(choix) <= 2:
                    if int(choix) == 1:
                        remove_armor_roi(roi_demon['hands']['armor'])
                        return
                    elif int(choix) == 2:
                        return
                else:
                    Sentence("Veuillez entrer un chiffre valide")


def remove_armor_roi(armor) :
    from intro import Sentence
    Roi_demon_stats[3] = Roi_demon_stats[15]
    roi_demon['armor'][str(armor)] += 1
    roi_demon['hands']['armor'] = None
    sleep(0.5)
    clsglobal()
    # bruitage retire equipement armure
    Sentence("Équiper un autre objet à la place ?")
    print("1. Oui")
    print("2. Non")
    while True:
        choix = input("Choix :")
        menu_sound.play()
        if str(choix) == "":
            Sentence("Veuillez entrer un chiffre valide")
        else:
            if int(choix) >= 1 and int(choix) <= 2:
                if int(choix) == 1:
                    use_equipement_armor_roi()
                    return
                elif int(choix) == 2:
                    return
            else:
                Sentence("Veuillez entrer un chiffre valide")


def pickle_save(save):
    from demo import save_number
    f = open("save", "wb")
    roi_demon_save_hands = roi_demon["hands"]
    roi_demon_save_inv = roi_demon["inv"]
    roi_demon_save_equipement = roi_demon["equipement"]
    roi_demon_save_armor = roi_demon["armor"]
    Roi_demon_stats_save_0 = Roi_demon_stats[0]
    Roi_demon_stats_save_3 = Roi_demon_stats[3]
    Roi_demon_stats_save_4 = Roi_demon_stats[4]
    Roi_demon_stats_save_5 = Roi_demon_stats[5]
    save_number_save = save

    d = {
        "roi_demon_hands" : roi_demon_save_hands,
        "roi_demon_inv" : roi_demon_save_inv,
        "roi_demon_equipement" : roi_demon_save_equipement,
        "roi_demon_armor" : roi_demon_save_armor,
        "Roi_demon_stats_0" : Roi_demon_stats_save_0,
        "Roi_demon_stats_3" : Roi_demon_stats_save_3,
        "Roi_demon_stats_4" : Roi_demon_stats_save_4,
        "Roi_demon_stats_5" : Roi_demon_stats_save_5,
        "save_number" : save_number_save
    }

    pickle.dump(d,f)
    f.close()

def pickle_print_save():
    pickle_file = open("save", "rb")
    objects = []
    while True:
        try:
            objects.append(pickle.load(pickle_file))
        except EOFError:
            break
    pickle_file.close()
    print(objects)
def pickle_print_new_game() :
    pickle_file = open("new_game", "rb")
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

    roi_demon["hands"] = d["roi_demon_hands"]
    roi_demon["inv"] = d["roi_demon_inv"]
    roi_demon["equipement"] = d["roi_demon_equipement"]
    roi_demon["armor"] = d["roi_demon_armor"]
    Roi_demon_stats[0] = d["Roi_demon_stats_0"]
    Roi_demon_stats[3] = d["Roi_demon_stats_3"]
    Roi_demon_stats[4] = d["Roi_demon_stats_4"]
    Roi_demon_stats[5] = d["Roi_demon_stats_5"]

    f.close()

def save_number_load():
    f = open("save", "rb")
    d = pickle.load(f)

    save_number = d["save_number"]


    return save_number


def save(anchor):
    from intro import Sentence
    from maps import skip_touch
    from demo import save_number
    if anchor == 1:
        save_number = 1
        pickle_save(save_number)
    elif anchor == 2:
        save_number = 2
        pickle_save(save_number)
    elif anchor == 3:
        save_number = 3
        pickle_save(save_number)

def new_game() :
    f = open("new_game", "rb")
    d = pickle.load(f)
    roi_demon["hands"] = d["roi_demon_hands"]
    roi_demon["inv"] = d["roi_demon_inv"]
    roi_demon["equipement"] = d["roi_demon_equipement"]
    roi_demon["armor"] = d["roi_demon_armor"]
    Roi_demon_stats[0] = d["Roi_demon_stats_0"]
    Roi_demon_stats[3] = d["Roi_demon_stats_3"]
    Roi_demon_stats[4] = d["Roi_demon_stats_4"]
    Roi_demon_stats[5] = d["Roi_demon_stats_5"]
    f.close()



def menu_roi(anchor) :#use in demo (entré de map et sortie de map)
    from intro import titlebis
    from intro import Sentence
    sleep(0.5)
    clsglobal()
    Sentence("Voulez-vous faire quelque chose ?")
    print("1. Inventaire")
    print("2. Sauvegarder")
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
                    clsglobal()
                    print(roi_demon['gold']['Argent'], "or.")
                    print("1. Objet")
                    print("2. Équipement")
                    print('3. Retour')
                    while True:
                        choix = input("Choix :")
                        menu_sound.play()
                        if str(choix) == "":
                            Sentence("Veuillez entrer un chiffre valide")
                        else:
                            if int(choix) >= 1 and int(choix) <= 3:
                                if int(choix) == 1:
                                    sleep(0.5)
                                    clsglobal()
                                    use_objet_roi(anchor)
                                    return
                                elif int(choix) == 2:
                                    sleep(0.5)
                                    clsglobal()
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
                                            Sentence("Veuillez entrer un chiffre valide")
                                        else:
                                            if int(choix) >= 1 and int(choix) <= 3:
                                                if int(choix) == 1:
                                                    sleep(0.5)
                                                    clsglobal()
                                                    use_equipement_wapon_roi()
                                                    menu_roi(anchor)
                                                    return
                                                elif int(choix) == 2:
                                                    sleep(0.5)
                                                    clsglobal()
                                                    use_equipement_armor_roi()
                                                    menu_roi(anchor)
                                                    return
                                                elif int(choix) == 3:
                                                    sleep(0.5)
                                                    clsglobal()
                                                    menu_roi(anchor)
                                                    return
                                            else:
                                                Sentence("Veuillez entrer un chiffre valide")
                                elif int(choix) == 3:
                                    sleep(0.5)
                                    clsglobal()
                                    menu_roi(anchor)
                                    return
                            else:
                                Sentence("Veuillez entrer un chiffre valide")
                elif int(choix) == 2 : #sauvgarder :
                    menu_sound.play()
                    sleep(0.5)
                    clsglobal()
                    Sentence("Êtes vous sur de vouloir sauvegarder ?")
                    print("1. oui")
                    print("2. non")
                    while True:
                        choix = input("Choix :")
                        menu_sound.play()
                        if str(choix) == "":
                            Sentence("Veuillez entrer un chiffre valide")
                        else:
                            if int(choix) >= 1 and int(choix) <= 2:
                                if int(choix) == 1:
                                    sleep(0.5)
                                    # action de sauvegarde
                                    clsglobal()
                                    save(anchor)
                                    print("Progression sauvegardée !")
                                    save_sound.play()
                                    sleep(1)
                                    clsglobal()
                                    print("")
                                    Sentence("Voulez vous quitter ?")
                                    print("1. oui")
                                    print("2. non")
                                    while True:
                                        choix = input("Choix :")
                                        menu_sound.play()
                                        if str(choix) == "":
                                            Sentence("Veuillez entrer un chiffre valide")
                                        if int(choix) >= 1 and int(choix) <= 2:
                                            if int(choix) == 1:
                                                sleep(0.5)
                                                clsglobal()
                                                titlebis()
                                                return
                                            elif int(choix) == 2:
                                                sleep(0.5)
                                                clsglobal()
                                                menu_roi(anchor)
                                                return
                                        else:
                                            Sentence("Veuillez entrer un chiffre valide")
                                elif int(choix) == 2:
                                    sleep(0.5)
                                    clsglobal()
                                    menu_roi(anchor)
                                    return
                            else:
                                Sentence("Veuillez entrer un chiffre valide")
                elif int(choix) == 3:
                    validation_sound.play()
                    sleep(0.5)
                    clsglobal()
                    return
            else:
                Sentence("Veuillez entrer un chiffre valide")




def menu_roi_sceptre() :#use in demo (utilisation quand tu dois planter un sceptre de pouvoir)
    from intro import Sentence
    sleep(1.5)
    clsglobal()
    Sentence("Utiliser un sceptre de pouvoir.")
    from intro import Sentence
    print_objet_roi()
    Kinv = roi_demon['inv'].keys()
    Kinv_list = list(Kinv)
    while True:
        Ninv = input("Utiliser quel objet ? :")
        if str(Ninv) == "":
            Sentence("Veuillez entrer un chiffre valide")
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
                Sentence("Veuillez entrer un chiffre valide")
                menu_roi_sceptre()
                return
    return


