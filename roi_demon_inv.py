from inventaire import *
from intro import *
from combat import *
from index import *
from time import sleep
import Music_sounds

roi_demon = {
    'xp' : {
        "lvl": 666,
        "xp" : 0,
        "lvlnext": 666,
    },
    'hands' :{
        'hand1' : None,
        'armor' : 'Armure des Abysse'
    },
    'gold' : {
        'Argent' : 666,
    },
    'inv' : {
        'sceptre de pouvoir' : 2,
        'Potion de soin n3' : 20,
        'Potion de mana n3' : 10,
        },
    'equipement' : {

    },
    'armor' :{
        'Armure des Abysse' : 0,
    }
}
Roi_demon_stats = ["Dieu-Roi", 55, 75, 25, 1.1, 500, 90, 5, 4, 0, 50, 5, 4, 500, 50]
Deva_stats = ["Deva", 25, 38, 15, 1.2, 250, 85, 5]
# significations : (0)nom, (1)attaque mini, (2)attaque max, (3)défense, (4)multiplicateur de dégat (arme), (5)vie, (6)précision, (7)chance de coup bas, (8)niveau de coup bas, (9)xp coup bas, (10)mana, (11)esquive, (12)attques magiques, (13) PV max, (14) MP max, (15) defense mini



def win_roi(enemie): #use in demo (en cas de victoire)
    os.system("cls")
    print("Victoire !")
    print("Vous gagnez contre", enemie["nom"],".")
    #bruitage de victoir (optinelle)


# # permet la monter de niveau du hero
# # exemple : update_niv_roi(char['xp'])
# def update_niv_roi(xp1) :
#     while xp1['xp'] >= xp1['lvlnext'] :
#         xp1['lvl'] += 1
#         xp1['xp'] -= xp1['lvlnext']
#         xp1['lvlnext'] = round(xp1['lvlnext'] * 1.5)
#         print("Félicitation vous avez gagner 1 niveau")
#         print("vous êtes au niveau", xp1['lvl'])
#         update_stats_roi()
#
#
# def update_stats_roi():
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
#     print("Victoire !")
#     print("Vous gagnez", enemie["xp"],".")
#     print("Le ", enemie["nom"], " avait sur lui ", enemie["inv"], "et", enemie["gold"],"or.")
#     updating(roi_demon['inv'], enemie['inv']) #gaint des drops de l'enemie
#     updating(roi_demon['xp'], enemie['xp']) # gaint de l'xp de l'enemie
#     updating(roi_demon['gold'], enemie['or'])
#     update_niv_roi(roi_demon['xp']) #monté de niveau du hero si possible

# def pierre_sword_roi():
#     print("Voulez vous retirer l'épée ?.")
#     print("1. Oui")
#     print("2. Non")
#     while True:
#         choix = input("Choix :")
#         if str(choix) == "":
#             print("Choix indisponible.")
#         else:
#             if int(choix) >= 1 and int(choix) <= 2:
#                 if int(choix) == 1:
#                     use_equipement_wapon_roi()
#                     return
#                 elif int(choix) == 2:
#                     return
#                 else:
#                    print("Choix indisponible.")


def print_objet_roi():
    Kinv = roi_demon['inv'].keys() #transformation de l'inv en liste
    Iinv = roi_demon['inv'].values()
    Kinv_list = list(Kinv)
    Iinv_list = list(Iinv)
    for n in range(len(Kinv_list)) :
        print(n+1,Kinv_list[n],"n°:",Iinv_list[n])


def use_objet_roi() :
    os.system("cls")
    print("objet")
    print("Vie :", Roi_demon_stats[5],"/",Roi_demon_stats[13], "Mana :", Roi_demon_stats[10], "/", Roi_demon_stats[14])
    print_objet_roi()
    Kinv = roi_demon['inv'].keys()
    Kinv_list = list(Kinv)
    plop = len(Kinv_list) + 1
    print(plop, "Retour")

    while True :
        Ninv = input("Utiliser quel objet ? :")
        if str(Ninv) == "":
            print("Choix indisponible.")
        elif int(Ninv) == plop:
            menu_roi()
            return
        else:
            if int(Ninv) < 1 or int(Ninv) > len(Kinv_list)+1:
                print("Choix indisponible.")
            else:
                objet = Kinv_list[int(Ninv)-1]
                if len(index_objet[str(objet)]) >= 2 and len(index_objet[str(objet)]) <= 4 :
                    os.system("cls")
                    print("Vous utilisez ",objet,".")
                    if index_objet[str(objet)][2] == 1:
                        # bruitage de heal popo
                        print("Vous gagnez ",index_objet[str(objet)][1],"Pv.")
                        Roi_demon_stats[5] += index_objet[str(objet)][1]
                        if Roi_demon_stats[5] > Roi_demon_stats[13] :
                            Roi_demon_stats[5] = Roi_demon_stats[13]
                        print("")
                        print("Vie :", Roi_demon_stats[5],"/",Roi_demon_stats[13], "Mana :", Roi_demon_stats[10], "/", Roi_demon_stats[14])

                    elif index_objet[str(objet)][2] == 2:
                        #bruitage de heal popo
                        print("Vous gagnez ",index_objet[str(objet)][1], "Pm.")
                        Roi_demon_stats[10] += index_objet[str(objet)][1]
                        if Roi_demon_stats[10] > Roi_demon_stats[14] :
                            Roi_demon_stats[10] = Roi_demon_stats[14]
                        print("")
                        print("Vie :", Roi_demon_stats[5],"/",Roi_demon_stats[13], "Mana :", Roi_demon_stats[10], "/", Roi_demon_stats[14])
                    elif index_objet[str(objet)][2] == None:
                        print("Vous ne pouvez pas utiliser cet objet tout de suite.")
                        use_objet_roi()
                        return

                    os.system("cls")
                    print("Utiliser un autre objet ? :")
                    print("1. oui")
                    print("2. non")
                    while True:
                        choix = input("Choix :")
                        menu_sound.play()
                        if str(choix) == "":
                            print("Choix indisponible.")
                        else:
                            if int(choix) >= 1 and int(choix) <= 2:
                                if int(choix) == 1:
                                    os.system("cls")
                                    use_objet_roi()
                                    return
                                elif int(choix) == 2:
                                    return
                            else:
                                print("Choix indisponible.")
                else:
                    print("Ceci n'est pas un objet utilisable")
                    use_objet_roi()

def print_equipement_roi():
    Kequipement = roi_demon['equipement'].keys()
    Iequipement = roi_demon['equipement'].values()
    Kequipement_list = list(Kequipement)
    Iequipement_list = list(Iequipement)
    for n in range(len(Kequipement_list)):
        print(n+1,Kequipement_list[n],"n°:",Iequipement_list[n])


def use_equipement_wapon_roi():
    from index import index_wapone
    if roi_demon['hands']['hand1'] == None:
        os.system("cls")
        print_equipement_roi()
        wapone = str(input("Quel equipement :"))
        Kequipement = roi_demon['equipement'].keys()
        Kequipement_list = list(Kequipement)
        wapone_equipement = Kequipement_list[int(wapone)-1]
        roi_demon['hands']['hand1'] = str(wapone_equipement)
        bonus = index_wapone[str(wapone_equipement)][0]
        Roi_demon_stats[4] += bonus
        # bruitage equipement épée
        print("Vous équipez", wapone_equipement)
        roi_demon['equipement'][str(wapone_equipement)] -= 1
        return

    elif roi_demon['hands']['hand1'] != None:
        os.system("cls")
        print("Voulez-vous le retirer ?")
        print("1. Oui")
        print("2. Non")
        while True:
            choix = input("Choix :")
            menu_sound.play()
            if str(choix) == "":
                print("Choix indisponible.")
            else:
                if int(choix) >= 1 and int(choix) <= 2:
                    if int(choix) == 1:
                        remove_equipement_roi(roi_demon['hands']['hand1'])
                        return
                    elif int(choix) == 2:
                        return
                else:
                    print("Choix indisponible.")


def remove_equipement_roi(wapone) :
    os.system("cls")
    roi_demon['hands']['hand1'] = None
    Roi_demon_stats[4] = 1
    roi_demon['equipement'][str(wapone)] = 1
    # bruitage retire equipement épée
    print("Équiper un autre objet à la place ?")
    print("1. Oui")
    print("2. Non")
    while True:
        choix = input("Choix :")
        menu_sound.play()
        if str(choix) == "":
            print("Choix indisponible.")
        else:
            if int(choix) >= 1 and int(choix) <= 2:
                if int(choix) == 1:
                    use_equipement_wapon_roi()
                    return
                elif int(choix) == 2:
                    return
            else:
                print("Choix indisponible.")


def print_armor_roi():
    Karmor = roi_demon['armor'].keys()
    Iarmor = roi_demon['armor'].values()
    Karmor_list = list(Karmor)
    Iarmor_list = list(Iarmor)
    for n in range(len(Karmor_list)):
        print(n + 1, Karmor_list[n], "n°:", Iarmor_list[n])


def use_equipement_armor_roi():
    from index import index_wapone
    if roi_demon['hands']['armor'] == None:
        os.system("cls")
        print_armor_roi()
        armor = str(input("Quelle armure :"))
        Karmor = roi_demon['armor'].keys()
        Karmor_list = list(Karmor)
        armor_equipement = Karmor_list[int(armor)-1]
        roi_demon['hands']['armor'] = str(armor_equipement)
        bonus = index_armor[str(armor_equipement)][0]
        Roi_demon_stats[3] += bonus
        # bruitage equipement armure
        print("Vous équipez", armor_equipement)
        roi_demon['armor'][str(armor_equipement)] += 1
        return

    elif roi_demon['hands']['armor'] != None:
        os.system("cls")
        print("Voulez-vous le retirer ?")
        print("1. Oui")
        print("2. Non")
        while True:
            choix = input("Choix :")
            menu_sound.play()
            if str(choix) == "":
                print("Choix indisponible.")
            else:
                if int(choix) >= 1 and int(choix) <= 2:
                    if int(choix) == 1:
                        remove_armor_roi(roi_demon['hands']['armor'])
                        return
                    elif int(choix) == 2:
                        return
                else:
                    print("Choix indisponible.")


def remove_armor_roi(armor) :
    Roi_demon_stats[3] = Roi_demon_stats[15]
    roi_demon['armor'][str(armor)] += 1
    roi_demon['hands']['armor'] = None
    os.system("cls")
    # bruitage retire equipement armure
    print("Équiper un autre objet à la place ?")
    print("1. Oui")
    print("2. Non")
    while True:
        choix = input("Choix :")
        menu_sound.play()
        if str(choix) == "":
            print("Choix indisponible.")
        else:
            if int(choix) >= 1 and int(choix) <= 2:
                if int(choix) == 1:
                    use_equipement_armor_roi()
                    return
                elif int(choix) == 2:
                    return
            else:
                print("Choix indisponible.")



def menu_roi() :#use in demo (entré de map et sortie de map)
    os.system("cls")
    print("Voulez-vous faire quelque chose ?")
    print("1. Inventaire")
    print("2. Sauvgarder")
    print("3. Continuer")
    while True :
        choix = input("Choix :")
        if str(choix) == "":
            print("Choix indisponible.")
        else:
            if int(choix) >= 1 and int(choix) <= 3:
                if int(choix) == 1 : #inventaire
                    menu_sound.play()
                    os.system("cls")
                    print(roi_demon['gold']['Argent'], "or.")
                    print("1. Objet")
                    print("2. Équipement")
                    print('3. Retour')
                    while True:
                        choix = input("Choix :")
                        menu_sound.play()
                        if str(choix) == "":
                            print("Choix indisponible.")
                        else:
                            if int(choix) >= 1 and int(choix) <= 3:
                                if int(choix) == 1:
                                    os.system("cls")
                                    use_objet_roi()
                                    return
                                elif int(choix) == 2:
                                    os.system("cls")
                                    if roi_demon['hands']['hand1'] != None:
                                        print("Vous avez", roi_demon['hands']['hand1'], "d'équipé.")
                                    if roi_demon['hands']['armor'] != None:
                                        print("Vous avez", roi_demon['hands']['armor'], "d'équipé.")
                                    print("1. Equiper une arme")
                                    print("2. Equiper une armure")
                                    print("3. Retour")
                                    while True:
                                        choix = input("Choix :")
                                        menu_sound.play()
                                        if str(choix) == "":
                                            print("Choix indisponible.")
                                        else:
                                            if int(choix) >= 1 and int(choix) <= 2:
                                                if int(choix) == 1:
                                                    os.system("cls")
                                                    use_equipement_wapon_roi()
                                                    menu_roi()
                                                    return
                                                elif int(choix) == 2:
                                                    os.system("cls")
                                                    use_equipement_armor_roi()
                                                    menu_roi()
                                                    return
                                                elif int(choix) == 3:
                                                    os.system("cls")
                                                    menu_roi()
                                                    return
                                            else:
                                                print("Choix indisponible.")
                                elif int(choix) == 3:
                                    os.system("cls")
                                    menu_roi()
                                    return
                            else:
                                print("Choix indisponible.")
                elif int(choix) == 2 : #sauvgarder :
                    menu_sound.play()
                    os.system("cls")
                    print("Êtes vous sur de vouloir sauvegarder ?")
                    print("1. oui")
                    print("2. non")
                    while True:
                        choix = input("Choix :")
                        menu_sound.play()
                        if str(choix) == "":
                            print("Choix indisponible.")
                        else:
                            if int(choix) >= 1 and int(choix) <= 2:
                                if int(choix) == 1:
                                    os.system("cls")
                                    save(roi_demon, history)
                                    print("Voulez vous quitter ?")
                                    print("1. oui")
                                    print("2. non")
                                    while True:
                                        choix = input("Choix :")
                                        menu_sound.play()
                                        if str(choix) == "":
                                            print("Choix indisponible.")
                                        if int(choix) >= 1 and int(choix) <= 2:
                                            if int(choix) == 1:
                                                os.system("cls")
                                                titlebis()
                                                return
                                            elif int(choix) == 2:
                                                os.system("cls")
                                                menu_roi()
                                                return
                                        else:
                                            print("Choix indisponible.")
                                elif int(choix) == 2:
                                    os.system("cls")
                                    menu_roi()
                                    return
                            else:
                                print("Choix indisponible.")
                elif int(choix) == 3:
                    validation_sound.play()
                    os.system("cls")
                    return
            else:
                print("Choix indisponible.")

def use_objet_roi_sceptre() :
    print_objet_roi()
    Kinv = roi_demon['inv'].keys()
    Kinv_list = list(Kinv)
    while True:
        Ninv = input("Utiliser quel objet ? :")
        if str(Ninv) == "":
            print("Choix indisponible.")
        else:
            if int(Ninv) >= 1 and int(Ninv) <= len(Kinv_list):
                objet = Kinv_list[int(Ninv)-1]
                if len(index_objet[str(objet)]) == 4:
                    print("Vous utilisez ", objet, ".")
                    roi_demon['inv']['sceptre de pouvoir'] -= 1
                    return

                else:
                    print("Vous tentez d'utiliser ", objet, ".")
                    print("Ceci n'est pas un sceptre de pouvoir")
                    use_objet_roi_sceptre()
            else:
                print("Choix indisponible.")
                use_objet_roi_sceptre()


def menu_roi_sceptre() :#use in demo (utilisation quand tu dois planter un sceptre de pouvoir)
    print(roi_demon['gold']['Argent'], "or.")
    print("Utiliser un sceptre de pouvoir.")
    use_objet_roi_sceptre()
