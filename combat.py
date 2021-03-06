from random import *
from time import sleep
from intro import *
from Music_sounds import *
from maps import *
from roi_demon_inv import Roi_demon_stats
import pygame
import os

pygame.init()


# statistiques du mob seront intégrées à chaque évènement donc dépendra de la map et de l'ennemi
# Mob_stats = ["Fermier", 6, 9, 2, 1.0, 400, 85, 5]
# MobStats = ["Deva", 25, 38, 15, 1.2, 250, 85, 5]
# signif1ications : nom, attaque mini, attaque max, défense, multiplicateur de dégat (arme), vie, précision, esquive
# King_Stats = ["Dieu-Roi", 45, 67, 25, 1.0, 400, 90, 5, 4, 0, 50, 5, 3, 400, 50]
Prince_stats = ["Izzoth", 8, 12, 2, 1.3, 60, 90, 5, 4, 0, 40, 5, 4, 60, 40]
# Prince_stats = ["Prince", 8, 12, 2, 1.3, 600, 90, 5, 4, 0, 100, 5, 4, 60, 40]
# significations : (0)nom, (1)attaque mini, (2)attaque max, (3)défense, (4)multiplicateur de dégat (arme), (5)vie, (6)précision, (7)chance de coup bas, (8)niveau de coup bas, (9)xp coup bas, (10)mana, (11)esquive, (12)attques magiques, (13) PV max, (14) MP max, (15) defense mini


def attaque_mob(name, atkmini, atkmax, df, mult, hp):
    total_atk = randint(atkmini, atkmax) * mult
    final_atk = round(total_atk) - df
    if final_atk < 0:
        final_atk = 0
        Prince_hp_remaining = hp - final_atk
        round(Prince_hp_remaining)
        print(name, "vous inflige", final_atk, "dégats.")
        return Prince_hp_remaining
    else:
        Prince_hp_remaining = hp - final_atk
        round(Prince_hp_remaining)
        print(name, "vous inflige", final_atk, "dégats.")
        return Prince_hp_remaining


def attaque(name, atkmini, atkmax, df, mult, hp):
    total_atk = randint(atkmini, atkmax) * mult
    final_atk = total_atk - df
    mob_hp_remaining = hp - round(final_atk)
    round(mob_hp_remaining)
    print("vous infligez", round(final_atk), "dégats", "à", name)
    return mob_hp_remaining


def Magic_action(nivatkmag):
    if nivatkmag == 1:
        print("1. Rayon démoniaque mineur | coût : 7 mana")
        print("2. retour au menu des actions")
        rep = str(input("=> "))
        if rep == "1":
            if Prince_stats[10] >= 7:
                evil_beam_spell.play()
                Prince_stats[10] = Prince_stats[10] - 7
                magic_attack = 12
                print("vous infligez", magic_attack, "dégats magiques !")
                mob_hp_remaining = Mob_stats[5] - magic_attack
                return mob_hp_remaining
            else:
                Sentence("pas assez de mana")
                mob_hp_remaining = Magic_action(Prince_stats[12])
                return mob_hp_remaining
        elif rep == "2":
            clsglobal()
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = action()
            return mob_hp_remaining
        else:
            print("veuillez entrer un chiffre valide")
            sleep(1.5)
            clsglobal()
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = Magic_action(Prince_stats[12])
            return mob_hp_remaining
    elif nivatkmag == 2:
        print("1. Rayon démoniaque | coût : 9 mana")
        print("2. Soif d'âme | coût : 15 mana")
        print("3. retour au menu des actions")
        rep = str(input("=> "))
        if rep == "1":
            if Prince_stats[10] >= 9:
                evil_beam_spell.play()
                Prince_stats[10] = Prince_stats[10] - 9
                magic_attack = 15
                print("vous infligez", magic_attack, "dégats magiques !")
                mob_hp_remaining = Mob_stats[5] - magic_attack
                return mob_hp_remaining
            else:
                Sentence("pas assez de mana")
                mob_hp_remaining = Magic_action(Prince_stats[12])
                return mob_hp_remaining
        elif rep == "2":
            if Prince_stats[10] >= 15:
                absorbtion_soundeffect.play()
                Prince_stats[10] = Prince_stats[10] - 15
                magic_attack = randint(9, 11)
                print("vous absorbez", magic_attack, "dégats magiques !")
                sleep(1.0)
                recup = randint(9, 11)
                Prince_stats[5] = Prince_stats[5] + recup
                absorbtion_gain_hp.play(3)
                print("vous récupérez" , recup , "points de vie !")
                sleep(1.0)
                mob_hp_remaining = Mob_stats[5] - magic_attack
                if Prince_stats[5] > Prince_stats[13]:
                    Prince_stats[5] = Prince_stats[13]
                    return mob_hp_remaining
                else:
                    return mob_hp_remaining
            else:
                Sentence("pas assez de mana")
                mob_hp_remaining = Magic_action(Prince_stats[12])
                return mob_hp_remaining
        elif rep == "3":
            clsglobal()
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = action()
            return mob_hp_remaining
        else:
            print("veuillez entrer un chiffre valide")
            sleep(1.5)
            clsglobal()
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = Magic_action(Prince_stats[12])
            return mob_hp_remaining
    elif nivatkmag == 3:
        print("1. Rayon démoniaque majeur | coût : 12 mana")
        print("2. Moisson d'âme | coût : 20 mana")
        print("3. Seconde peau | coût : 15 mana")
        print("4. retour au menu des actions")
        rep = str(input("=> "))
        if rep == "1":
            if Prince_stats[10] >= 12:
                evil_beam_spell.play()
                Prince_stats[10] = Prince_stats[10] - 12
                magic_attack = 20
                print("vous infligez" , magic_attack , "dégats magiques !")
                mob_hp_remaining = Mob_stats[5] - magic_attack
                return mob_hp_remaining
            else:
                Sentence("pas assez de mana")
                mob_hp_remaining = Magic_action(Prince_stats[12])
                return mob_hp_remaining
        elif rep == "2":
            if Prince_stats[10] >= 20:
                absorbtion_soundeffect.play()
                Prince_stats[10] = Prince_stats[10] - 20
                magic_attack = randint(12, 15)
                print("vous absorbez", magic_attack, "dégats magiques !")
                sleep(1.0)
                recup = randint(12, 15)
                Prince_stats[5] = Prince_stats[5] + recup
                absorbtion_gain_hp.play(3)
                print("vous récupérez", recup, "points de vie !")
                sleep(1.0)
                mob_hp_remaining = Mob_stats[5] - magic_attack
                if Prince_stats[5] > Prince_stats[13]:
                    Prince_stats[5] = Prince_stats[13]
                    return mob_hp_remaining
                else:
                    return mob_hp_remaining
            else:
                Sentence("pas assez de mana")
                mob_hp_remaining = Magic_action(Prince_stats[12])
                return mob_hp_remaining
        elif rep == "3":
            if Prince_stats[10] >= 15:
                absorbtion_soundeffect.play()
                Sentence("Votre corps se recouvre d'une étrange matière, elle est dure comme la pierre.")
                Sentence("Vous êtes plus résistant !")
                sleep(1.0)
                Prince_stats[10] = Prince_stats[10] - 15
                Prince_stats[3] += 5
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
            else:
                Sentence("pas assez de mana")
                mob_hp_remaining = Magic_action(Prince_stats[12])
                return mob_hp_remaining
        elif rep == "4":
            clsglobal()
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = action()
            return mob_hp_remaining
        else:
            print("veuillez entrer un chiffre valide")
            sleep(1.5)
            clsglobal()
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = Magic_action(Prince_stats[12])
            return mob_hp_remaining
    elif nivatkmag == 4:
        print("1. Rayon Infernal | coût : 16 mana")
        print("2. Grande moisson | coût : 10 mana")
        print("3. Peau du Seigneur démon | coût : 20 mana")
        print("4. Résurgence Royale | coût : Crâne du roi démon")
        print("5. retour au menu des actions")
        rep = str(input("=> "))
        if rep == "1":
            if Prince_stats[10] >= 16:
                evil_beam_spell.play()
                Prince_stats[10] = Prince_stats[10] - 16
                magic_attack = 25
                print("vous infligez", magic_attack, "dégats magiques !")
                mob_hp_remaining = Mob_stats[5] - magic_attack
                return mob_hp_remaining
            else:
                Sentence("pas assez de mana")
                mob_hp_remaining = Magic_action(Prince_stats[12])
                return mob_hp_remaining
        elif rep == "2":
            if Prince_stats[10] >= 10:
                absorbtion_soundeffect.play()
                Prince_stats[10] = Prince_stats[10] - 10
                magic_attack = randint(15, 20)
                print("vous absorbez", magic_attack, "dégats magiques !")
                sleep(1.0)
                recup = randint(15, 20)
                Prince_stats[5] = Prince_stats[5] + recup
                absorbtion_gain_hp.play(3)
                print("vous récupérez", recup, "points de vie !")
                sleep(1.0)
                mob_hp_remaining = Mob_stats[5] - magic_attack
                if Prince_stats[5] > Prince_stats[13]:
                    Prince_stats[5] = Prince_stats[13]
                    return mob_hp_remaining
                else:
                    return mob_hp_remaining
            else:
                Sentence("pas assez de mana")
                mob_hp_remaining = Magic_action(Prince_stats[12])
                return mob_hp_remaining
        elif rep == "3":
            if Prince_stats[10] >= 20:
                absorbtion_soundeffect.play()
                Sentence("Votre corps se recouvre d'une étrange matière, elle est dure comme de l'acier.")
                Sentence("Vous êtes plus beaucoup résistant !")
                sleep(1.0)
                Prince_stats[10] = Prince_stats[10] - 20
                Prince_stats[3] += 10
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
            else:
                Sentence("pas assez de mana")
                mob_hp_remaining = Magic_action(Prince_stats[12])
                return mob_hp_remaining
        elif rep == "4":
            print("a compléter")
            mob_hp_remaining = Mob_stats[5]
            return mob_hp_remaining
        elif rep == "5":
            clsglobal()
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = action()
            return mob_hp_remaining
        else:
            print("veuillez entrer un chiffre valide")
            sleep(1.5)
            clsglobal()
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = Magic_action(Prince_stats[12])
            return mob_hp_remaining


def Fuite():
    #définir la fonction de fuite, mais pour l'instant :
    mob_hp_remaining = Mob_stats[5]
    return mob_hp_remaining


def Low_Blow(x):
    # x représente le niveau de coups bas, le niveau va déterminer le menu de coups bas et la pussance des capacités
    # il manque le coup bas du grand Sagzinoth
    if x == 1:
        print("1. Sable dans les yeux | 1 sur 2")
        print("2. Retour au menu des actions")
        rep = str(input("=> "))
        if rep == "1":
            rate = randint(1, 10)
            if rate > 5:
                print("Vous vous placez efficacement devant " + Mob_stats[0] + " et vous jetez une poignée de sable dans les yeux !")
                sand_low_blow.play()
                print("Cela l'aveugle partiellement. " + Mob_stats[0] + " est moins précis !")
                sleep(1.0)
                Mob_stats[6] = Mob_stats[6] - 10
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
            else:
                Sentence("Raté")
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
        elif rep == "2":
            clsglobal()
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = action()
            return mob_hp_remaining
        else:
            print("veuillez entrer un chiffre valide")
            sleep(1.5)
            clsglobal()
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = Low_Blow(Prince_stats[8])
        return mob_hp_remaining
    elif x == 2:
        print("1. Sable dans les yeux | 6 sur 10")
        print("2. Coup dans le genou | 1 sur 2")
        print("3. Retour au menu des actions")
        rep = str(input("=> "))
        if rep == "1":
            rate = randint(1, 10)
            if rate > 4:
                print("Vous vous placez efficacement devant " + Mob_stats[0] + " et vous jetez une poignée de sable dans les yeux !")
                sand_low_blow.play()
                print("Cela l'aveugle partiellement. " + Mob_stats[0] + " est moins précis !")
                sleep(1.0)
                Mob_stats[6] = Mob_stats[6] - 10
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
            else:
                print("Raté")
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
        elif rep == "2":
            rate = randint(1,10)
            if rate > 5:
                print("Vous visez le genou de votre adversaire et mettez un puissant coup de pied dedans !")
                crack.play()
                print(Mob_stats[0], "boite, son esquive diminue !")
                sleep(1.0)
                Mob_stats[7] = Mob_stats[7] - 5
                if Mob_stats[7] < 0:
                    print(Mob_stats[0], "ne peut plus esquiver !")
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
                else:
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
            else:
                print("Raté")
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
        elif rep == "3":
            clsglobal()
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = action()
            return mob_hp_remaining
        else:
            print("veuillez entrer un chiffre valide")
            sleep(1.5)
            clsglobal()
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = Low_Blow(Prince_stats[8])
        return mob_hp_remaining
    elif x == 3:
        print("1. Sable dans les yeux | 7 sur 10")
        print("2. Coup dans le genou | 6 sur 10")
        print("3. Brise armure | 4 sur 10")
        print("4. Retour au menu des actions")
        rep = str(input("=> "))
        if rep == "1":
            rate = randint(1, 10)
            if rate > 3:
                print("Vous vous placez efficacement devant " + Mob_stats[0] + " et vous jetez une poignée de sable dans les yeux !")
                sand_low_blow.play()
                print("Cela l'aveugle partiellement. " + Mob_stats[0] + " est moins précis !")
                sleep(1.0)
                Mob_stats[6] = Mob_stats[6] - 10
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
            else:
                print("Raté")
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
        elif rep == "2":
            rate = randint(1, 10)
            if rate > 4:
                print("Vous visez le genou de votre adversaire et mettez un puissant coup de pied dedans !")
                crack.play()
                print(Mob_stats[0], "boite, son esquive diminue !")
                sleep(1.0)
                Mob_stats[7] = Mob_stats[7] - 5
                if Mob_stats[7] <= 0:
                    Mob_stats[7] = 0
                    print(Mob_stats[0], "ne peut plus esquiver !")
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
                else:
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
            else:
                print("Raté")
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
        elif rep == "3":
            rate = randint(1,10)
            if rate > 6:
                print("Vous trouvez une faille dans la défense de votre adversaire !")
                broken_armor.play()
                print("La protection de votre adversaire se fragilise !")
                sleep(1.0)
                Mob_stats[3] = Mob_stats[3] - 2
                if Mob_stats[3] <= 0:
                    Mob_stats[3] = 0
                    print(Mob_stats[0], "voit sa seule protection partir en morceaux !")
                    sleep(1.0)
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
                else:
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
            else:
                print("Raté")
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
        elif rep == "4":
            clsglobal()
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = action()
            return mob_hp_remaining
        else:
            print("veuillez entrer un chiffre valide")
            sleep(1.5)
            clsglobal()
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = Low_Blow(Prince_stats[8])
        return mob_hp_remaining
    elif x == 4:
        print("1. Sable dans les yeux | 7 sur 10")
        print("2. Coup dans le genou | 7 sur 10")
        print("3. Brise armure | 1 sur 2")
        print("4. Liquide corrosif | 1 sur 2")
        print("5. retour au menu des actions")
        rep = str(input("=> "))
        if rep == "1":
            rate = randint(1, 10)
            if rate > 3:
                print("Vous vous placez efficacement devant " + Mob_stats[0] + " et vous jetez une poignée de sable dans les yeux !")
                sand_low_blow.play()
                print("Cela l'aveugle partiellement. " + Mob_stats[0] + " est moins précis !")
                sleep(1.0)
                Mob_stats[6] = Mob_stats[6] - 15
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
            else:
                print("Raté")
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
        elif rep == "2":
            rate = randint(1, 10)
            if rate > 3:
                print("Vous visez le genou de votre adversaire et mettez un puissant coup de pied dedans !")
                crack.play()
                print(Mob_stats[0], "boite, son esquive diminue !")
                sleep(1.0)
                Mob_stats[7] = Mob_stats[7] - 7
                if Mob_stats[7] <= 0:
                    Mob_stats[7] = 0
                    print(Mob_stats[0], "ne peut plus esquiver !")
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
                else:
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
            else:
                print("Raté")
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
        elif rep == "3":
            rate = randint(1, 10)
            if rate > 5:
                print("Vous trouvez une faille dans la défense de votre adversaire !")
                broken_armor.play()
                print("La protection de votre adversaire se fragilise !")
                sleep(1.0)
                Mob_stats[3] = Mob_stats[3] - 4
                if Mob_stats[3] <= 0:
                    Mob_stats[3] = 0
                    print(Mob_stats[0], "voit sa seule protection partir en morceaux !")
                    sleep(1.0)
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
                else:
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
            else:
                print("Raté")
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
        elif rep == "4":
            rate = randint(1,10)
            if rate > 5:
                print("vous profitez du moment parfait pour verser un liquide corrosif sur l'arme de l'adversaire !")
                sleep(1.0)
                acid_sound.play()
                print("les dégats de l'adversaire sont réduits !")
                Mob_stats[2] = Mob_stats[2] - 2
                if Mob_stats[2] <= 0:
                    Mob_stats[2] = 0
                    print(Mob_stats[0], "voit son arme fondre devant ses yeux !")
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
                else:
                    mob_hp_remaining = Mob_stats[5]
                    return mob_hp_remaining
            else:
                print("Raté")
                mob_hp_remaining = Mob_stats[5]
                return mob_hp_remaining
        elif rep == "5":
            clsglobal()
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = action()
            return mob_hp_remaining
        else:
            print("veuillez entrer un chiffre valide")
            sleep(1.5)
            clsglobal()
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_hp_remaining = Low_Blow(Prince_stats[8])
        return mob_hp_remaining


def mob_action():
    print(Mob_stats[0], "attaque !")
    sleep(1.0)
    rateaccuracy = randint(1, 100)
    if rateaccuracy < Mob_stats[6]:
        rateesq = randint(1, 100)
        if rateesq <= Prince_stats[11]:
            print("Vous esquivez l'attaque !")
            degats = Prince_stats[5]
            return degats
        else:
            degats = attaque_mob(Mob_stats[0], Mob_stats[1], Mob_stats[2], Prince_stats[3], Mob_stats[4], Prince_stats[5])
            sword_sound.play()
            fork_sound.play()
            return degats
    else:
        print(Mob_stats[0], "rate son attaque !")
        degats = Prince_stats[5]
        return degats


def action():
    Sentence("A votre tour :")
    print("1. Attaquer")
    print("2. Magie")
    print("3. Coup bas")
    print("4. Fuite")
    rep = str(input("=> "))
    if rep == "1":
        Sentence("Vous attaquez !")
        rateaccuracy = randint(1,100)
        if rateaccuracy < Prince_stats[6]:
            rateesq = randint(1,100)
            if rateesq <= Mob_stats[7]:
                print(Mob_stats[0], "esquive votre attaque !")
                degats = Mob_stats[5]
                return degats
            else:
                degats = attaque(Mob_stats[0], Prince_stats[1], Prince_stats[2], Mob_stats[3], Prince_stats[4], Mob_stats[5])
                sword_sound.play()
                return degats
        else:
            print("vous ratez votre attaque !")
            degats = Mob_stats[5]
            return degats

    elif rep == "2":
        Sentence("Vous concentrez votre mana")
        degats = Magic_action(Prince_stats[12])
        return degats
    elif rep == "3":
        Sentence("Vous prenez un air sournois...")
        degats = Low_Blow(Prince_stats[8])
        return degats
    elif rep == "4":
        Sentence("Vous tentez de fuir")
        #fly_chance = randint(1, 10)
        #if fly_chance > 5:
        degats = Fuite()
        return degats
        #else:
            #Sentence("Votre fuite échoue")
            #degats = Mob_stats[5]
            #return degats
    else:
        while rep != "1" or rep != "2" or rep != "3" or rep != "4":
            Sentence("veuillez entrer un chiffre valide")
            sleep(1.5)
            clsglobal()
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            degats = action()
            return degats


def fight(princes_stats, MobStats):
    print(princes_stats)
    print(MobStats)
    first = randint(1, 10)
    prince_life = Prince_stats[5]
    mob_life = Mob_stats[5]
    mp = Prince_stats[10]
    hp = Prince_stats[5]
    clsglobal()
    if first < 5:
        Sentence("Vous frappez en premier !")
        print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
        print("                                                                 Mana :", Prince_stats[10])
        mob_life = action()
        sleep(1.5)
        Mob_stats[5] = mob_life
        clsglobal()
        while prince_life > 0 or mob_life > 0:
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            prince_life = mob_action()
            Prince_stats[5] = prince_life
            sleep(1.5)
            clsglobal()
            if prince_life < 0:
                print("Défaite")
                Prince_stats[5] = hp
                Prince_stats[10] = mp
                #la musique s'arrête
                #fonction défaite avec tp au sancturaire des démons
                victoire = False,
                return victoire

            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_life = action()
            Mob_stats[5] = mob_life
            sleep(1.5)
            clsglobal()
            if mob_life < 0:
                print(Mob_stats[0], "est vaincu")
                Prince_stats[10] = mp
                enemy_death.play()
                sleep(4.0)
                # la musique s'arrête
                # fonction victoire avec musique de victoire + affichage du loot + xp
                # faire en sorte de return la vie restante et de la réattribuer à la liste Prince_Stats
                victoire = True
                return victoire
    else:
        Sentence(str(Mob_stats[0]) + " frappe en premier !")
        print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
        print("                                                                 Mana :", Prince_stats[10])
        prince_life = mob_action()
        Prince_stats[5] = prince_life
        sleep(1.5)
        clsglobal()
        while prince_life > 0 or mob_life > 0:
            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            mob_life = action()
            Mob_stats[5] = mob_life
            sleep(1.5)
            clsglobal()
            if mob_life < 0:
                print(Mob_stats[0], "est vaincu")
                Prince_stats[10] = mp
                enemy_death.play()
                sleep(4.0)
                #la musique s'arrête
                #fonction victoire avec musique de victoire + affichage du loot + xp
                # faire en sorte de return la vie restante et de la réattribuer à la liste Prince_Stats
                victoire = True
                return victoire

            print(Mob_stats[0], ":", int(Mob_stats[5]), "pv", "                         ", Prince_stats[0], ":", Prince_stats[5], "pv")
            print("                                                                 Mana :", Prince_stats[10])
            prince_life = mob_action()
            Prince_stats[5] = prince_life
            sleep(1.5)
            clsglobal()
            if prince_life < 0:
                print("Défaite")
                Prince_stats[10] = mp
                Prince_stats[5] = hp
                # la musique s'arrête
                # fonction défaite avec tp au sancturaire des démons
                victoire = False
                return victoire



# //////////////////////////////////////////////////////////// CONTENU DE LA DEMO CI DESSOUS //////////////////////////////////////////////////////////////////////////////////////////////////


# //////////////////////////////////////////////////////////// FONCTIONS DE COMBAT CLASSIQUE //////////////////////////////////////////////////////////////////////////////////////////////////


def demodefaite():
    Sentence("Vous tombez au sol, mort, laissant votre peuple à l'extinction...")
    sleep(1.5)
    Sentence( "Aucun contact ne fut jamais pris avec les humains, ")
    Sentence("qui se contentèrent de bouter les démons dans les montagnes d'Aurgelmirtann, au nord de Ljosalfer...")
    skip_touch()
    clsglobal()
    demo_deva_combat.fadeout(1000)
    battle_sound_effect.fadeout(1000)
    print("")
    Sentence("Jusqu'à des siècles plus tard, les hommes se rappellent de cet évènement comme la Bataille de la Couronne,")
    Sentence("ou grâce à une alliance avec des créatures célestes, les humains ont repoussé les démons.")
    sleep(1.5)
    Sentence("Ces derniers finirent sous le joug des premiers,")
    Sentence("le peu d'entre eux encore libres se terrant dans les montagnes. ")
    sleep(1.5)
    print("")
    Sentence("À ce jour, nul ne sait comment les humains ont obtenu l'aide des anges,")
    Sentence("mais depuis, un certain 'Prince en Blanc', que personne ne voit jamais,")
    Sentence("semble avoir remplacé le roi précédent, et règne sur Ljosalfer d'une main juste,  ")
    Sentence("ferme,")
    Sentence("et désinteressée...")
    sleep(3.0)
    clsglobal()
    print("")
    print("")
    Sentence("Voulez vous continuer ?")
    print("1. Oui")
    print("2. Non")
    print("")
    rep = str(input("=> "))
    while rep != "1" or rep != "2":
        if rep == "1":
            clsglobal()
            print("")
            Sentence("Chargement de la dernière sauvegarde...")
            sleep(2.0)
            clsglobal()
            load()
            return
        elif rep == "2":
            clsglobal()
            print("")
            Sentence("Retour au menu principal...")
            sleep(2.0)
            clsglobal()
            titlebis()
            return
        if rep != "1" or rep != "2":
            Sentence("veuillez entrer un chiffre valide")
        rep = str(input("=> "))




def demo_attaque_mob(name, atkmini, atkmax, df, mult, hp):
    total_atk = randint(atkmini, atkmax) * mult
    final_atk = round(total_atk) - df
    if final_atk < 0:
        final_atk = 0
        Prince_hp_remaining = hp - final_atk
        round(Prince_hp_remaining)
        print(name, "vous inflige", final_atk, "dégats.")
        sleep(1.0)
        return Prince_hp_remaining
    else:
        Prince_hp_remaining = hp - final_atk
        round(Prince_hp_remaining)
        print(name, "vous inflige", final_atk, "dégats.")
        sleep(1.0)
        return Prince_hp_remaining


def demo_attaque(name, atkmini, atkmax, df, mult, hp):
    total_atk = randint(atkmini, atkmax) * mult
    final_atk = total_atk - df
    mob_hp_remaining = hp - round(final_atk)
    print("vous infligez", round(final_atk), "dégats", "à", name)
    sleep(1.0)
    return round(mob_hp_remaining)


def demo_Magic_action(nivatkmag, MobStats):
    if nivatkmag == 1:
        print("1. Rayon démoniaque mineur | coût : 7 mana")
        print("2. retour au menu des actions")
        rep = str(input("=> "))
        if rep == "1":
            if Prince_stats[10] >= 7:
                evil_beam_spell.play()
                Roi_demon_stats[10] = Roi_demon_stats[10] - 7
                magic_attack = 12
                print("vous infligez", magic_attack, "dégats magiques !")
                mob_hp_remaining = MobStats[5] - magic_attack
                return mob_hp_remaining
            else:
                Sentence("pas assez de mana")
                mob_hp_remaining = demo_Magic_action(Roi_demon_stats[12], MobStats)
                return mob_hp_remaining
        elif rep == "2":
            clsglobal()
            print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
            print("                                                                 Mana :", Roi_demon_stats[10])
            mob_hp_remaining = action()
            return mob_hp_remaining
        else:
            print("Veuillez entrer un chiffre valide")
            sleep(1.5)
            clsglobal()
            print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
            print("                                                                 Mana :", Roi_demon_stats[10])
            mob_hp_remaining = demo_Magic_action(Roi_demon_stats[12], MobStats)
            return mob_hp_remaining
    elif nivatkmag == 2:
        print("1. Rayon démoniaque | coût : 9 mana")
        print("2. Soif d'âme | coût : 15 mana")
        print("3. retour au menu des actions")
        rep = str(input("=> "))
        if rep == "1":
            if Roi_demon_stats[10] >= 9:
                evil_beam_spell.play()
                Roi_demon_stats[10] = Roi_demon_stats[10] - 9
                magic_attack = 15
                print("vous infligez", magic_attack, "dégats magiques !")
                mob_hp_remaining = MobStats[5] - magic_attack
                return mob_hp_remaining
            else:
                Sentence("pas assez de mana")
                mob_hp_remaining = demo_Magic_action(Roi_demon_stats[12], MobStats)
                return mob_hp_remaining
        elif rep == "2":
            if Roi_demon_stats[10] >= 15:
                absorbtion_soundeffect.play()
                Roi_demon_stats[10] = Roi_demon_stats[10] - 15
                magic_attack = randint(9, 11)
                print("vous absorbez", magic_attack, "dégats magiques !")
                sleep(1.0)
                recup = randint(9, 11)
                Roi_demon_stats[5] = Roi_demon_stats[5] + recup
                absorbtion_gain_hp.play(3)
                print("vous récupérez" , recup , "points de vie !")
                sleep(1.0)
                mob_hp_remaining = MobStats[5] - magic_attack
                if Roi_demon_stats[5] > Roi_demon_stats[13]:
                    Roi_demon_stats[5] = Roi_demon_stats[13]
                    return mob_hp_remaining
                else:
                    return mob_hp_remaining
            else:
                Sentence("pas assez de mana")
                mob_hp_remaining = demo_Magic_action(Roi_demon_stats[12], MobStats)
                return mob_hp_remaining
        elif rep == "3":
            clsglobal()
            print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
            print("                                                                 Mana :", Roi_demon_stats[10])
            mob_hp_remaining = action()
            return mob_hp_remaining
        else:
            print("veuillez entrer un chiffre valide")
            sleep(1.5)
            clsglobal()
            print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
            print("                                                                 Mana :", Roi_demon_stats[10])
            mob_hp_remaining = demo_Magic_action(Roi_demon_stats[12], MobStats)
            return mob_hp_remaining
    elif nivatkmag == 3:
        print("1. Rayon démoniaque majeur | coût : 12 mana")
        print("2. Moisson d'âme | coût : 20 mana")
        print("3. Seconde peau | coût : 15 mana")
        print("4. retour au menu des actions")
        rep = str(input("=> "))
        if rep == "1":
            if Roi_demon_stats[10] >= 12:
                evil_beam_spell.play()
                Roi_demon_stats[10] = Roi_demon_stats[10] - 12
                magic_attack = 20
                print("Vous infligez" , magic_attack , "dégats magiques !")
                mob_hp_remaining = MobStats[5] - magic_attack
                return mob_hp_remaining
            else:
                Sentence("Pas assez de mana")
                mob_hp_remaining = demo_Magic_action(Roi_demon_stats[12], MobStats)
                return mob_hp_remaining
        elif rep == "2":
            if Roi_demon_stats[10] >= 20:
                absorbtion_soundeffect.play()
                Roi_demon_stats[10] = Roi_demon_stats[10] - 20
                magic_attack = randint(12, 15)
                print("vous absorbez", magic_attack, "dégats magiques !")
                sleep(1.0)
                recup = randint(12, 15)
                Roi_demon_stats[5] = Roi_demon_stats[5] + recup
                absorbtion_gain_hp.play(3)
                print("Vous récupérez", recup, "points de vie !")
                sleep(1.0)
                mob_hp_remaining = MobStats[5] - magic_attack
                if Roi_demon_stats[5] > Roi_demon_stats[13]:
                    Roi_demon_stats[5] = Roi_demon_stats[13]
                    return mob_hp_remaining
                else:
                    return mob_hp_remaining
            else:
                Sentence("Pas assez de mana")
                mob_hp_remaining = demo_Magic_action(Roi_demon_stats[12], MobStats)
                return mob_hp_remaining
        elif rep == "3":
            if Roi_demon_stats[10] >= 15:
                absorbtion_soundeffect.play()
                Sentence("Votre corps se recouvre d'une étrange matière, elle est dure comme la pierre.")
                Sentence("Vous êtes plus résistant !")
                sleep(1.0)
                Roi_demon_stats[10] = Roi_demon_stats[10] - 15
                Roi_demon_stats[3] += 5
                mob_hp_remaining = MobStats[5]
                return mob_hp_remaining
            else:
                Sentence("pas assez de mana")
                mob_hp_remaining = demo_Magic_action(Roi_demon_stats[12], MobStats)
                return mob_hp_remaining
        elif rep == "4":
            clsglobal()
            print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
            print("                                                                 Mana :", Roi_demon_stats[10])
            mob_hp_remaining = action()
            return mob_hp_remaining
        else:
            print("veuillez entrer un chiffre valide")
            sleep(1.5)
            clsglobal()
            print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
            print("                                                                 Mana :", Roi_demon_stats[10])
            mob_hp_remaining = demo_Magic_action(Roi_demon_stats[12], MobStats)
            return mob_hp_remaining
    elif nivatkmag == 4:
        print("1. Rayon Infernal | coût : 16 mana")
        print("2. Grande moisson | coût : 10 mana")
        print("3. Peau du Seigneur démon | coût : 20 mana")
        print("4. Retour au menu des actions")
        rep = str(input("=> "))
        if rep == "1":
            if Roi_demon_stats[10] >= 16:
                evil_beam_spell.play()
                Roi_demon_stats[10] = Roi_demon_stats[10] - 16
                magic_attack = 70
                print("vous infligez", magic_attack, "dégats magiques !")
                mob_hp_remaining = MobStats[5] - magic_attack
                return mob_hp_remaining
            else:
                Sentence("Pas assez de mana")
                mob_hp_remaining = demo_Magic_action(Roi_demon_stats[12], MobStats)
                return mob_hp_remaining
        elif rep == "2":
            if Roi_demon_stats[10] >= 10:
                absorbtion_soundeffect.play()
                Roi_demon_stats[10] = Roi_demon_stats[10] - 10
                magic_attack = randint(25, 35)
                print("vous absorbez", magic_attack, "dégats magiques !")
                sleep(1.0)
                recup = randint(25, 35)
                Roi_demon_stats[5] = Roi_demon_stats[5] + recup
                absorbtion_gain_hp.play(3)
                print("vous récupérez", recup, "points de vie !")
                sleep(1.0)
                mob_hp_remaining = MobStats[5] - magic_attack
                if Roi_demon_stats[5] > Roi_demon_stats[13]:
                    Roi_demon_stats[5] = Roi_demon_stats[13]
                    return mob_hp_remaining
                else:
                    return mob_hp_remaining
            else:
                Sentence("Pas assez de mana")
                mob_hp_remaining = demo_Magic_action(Roi_demon_stats[12], MobStats)
                return mob_hp_remaining
        elif rep == "3":
            if Roi_demon_stats[10] >= 20:
                absorbtion_soundeffect.play()
                Sentence("Votre corps se recouvre d'une étrange matière, elle est dure comme de l'acier.")
                Sentence("Vous êtes beaucoup plus résistant !")
                sleep(1.0)
                Roi_demon_stats[10] = Roi_demon_stats[10] - 20
                Roi_demon_stats[3] = Roi_demon_stats[3] + 10
                mob_hp_remaining = MobStats[5]
                return mob_hp_remaining
            else:
                Sentence("Pas assez de mana")
                mob_hp_remaining = demo_Magic_action(Roi_demon_stats[12], MobStats)
                return mob_hp_remaining
        elif rep == "4":
            clsglobal()
            print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
            print("                                                                 Mana :", Roi_demon_stats[10])
            mob_hp_remaining = demo_action(MobStats)
            return mob_hp_remaining
        else:
            Sentence("Veuillez entrer un chiffre valide")
            sleep(1.5)
            clsglobal()
            print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
            print("                                                                 Mana :", Roi_demon_stats[10])
            mob_hp_remaining = demo_Magic_action(Roi_demon_stats[12], MobStats)
            return mob_hp_remaining


def Fuite():
    #définir la fonction de fuite, mais pour l'instant :
    mob_hp_remaining = MobStats[5]
    return mob_hp_remaining


def demo_mob_action(MobStats):
    print(MobStats[0], "attaque !")
    sleep(1.0)
    rateaccuracy = randint(1, 100)
    if rateaccuracy < MobStats[6]:
        rateesq = randint(1, 100)
        if rateesq <= Roi_demon_stats[11]:
            print("Vous esquivez l'attaque !")
            sleep(1.0)
            degats = Roi_demon_stats[5]
            return degats
        else:
            degats = round(demo_attaque_mob(MobStats[0], MobStats[1], MobStats[2], Roi_demon_stats[3], MobStats[4], Roi_demon_stats[5]))
            sword_sound.play()
            fork_sound.play()
            return degats
    else:
        print(MobStats[0], "rate son attaque !")
        sleep(1.0)
        degats = Roi_demon_stats[5]
        return degats


def demo_action(MobStats):
    Sentence("A votre tour :")
    print("1. Attaquer")
    print("2. Magie")
    print("3. Attaque spéciale")
    print("4. Éviter le combat")
    rep = str(input("=> "))
    if rep == "1":
        Sentence("Vous attaquez !")
        rateaccuracy = randint(1,100)
        if rateaccuracy < Roi_demon_stats[6]:
            rateesq = randint(1,100)
            if rateesq <= MobStats[7]:
                print(MobStats[0], "esquive votre attaque !")
                degats = MobStats[5]
                return degats
            else:
                degats = attaque(MobStats[0], Roi_demon_stats[1], Roi_demon_stats[2], MobStats[3], Roi_demon_stats[4], MobStats[5])
                sword_sound.play()
                return degats
        else:
            print("vous ratez votre attaque !")
            degats = MobStats[5]
            return degats
    elif rep == "2":
        Sentence("Vous concentrez votre mana")
        degats = demo_Magic_action(Roi_demon_stats[12], MobStats)
        return degats
    elif rep == "3":
        degats = demo_Low_Blow(MobStats)
        return degats
    elif rep == "4":
        Sentence("Pensez-vous que la fuite est digne du roi des démons ?")
        sleep(1.5)
        clsglobal()
        print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":",
              Roi_demon_stats[5], "pv")
        print("                                                                 Mana :", Roi_demon_stats[10])
        degats = demo_action(MobStats)
        return degats
    else:
        while rep != "1" or rep != "2" or rep != "3" or rep != "4":
            Sentence("Veuillez entrer un chiffre valide")
            sleep(1.5)
            clsglobal()
            print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
            print("                                                                 Mana :", Roi_demon_stats[10])
            degats = demo_action(MobStats)
            return degats


def demofight(MobStats):
    clsglobal()
    sleep(0.3)
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("""
                                 ██████╗ ██████╗ ███╗   ███╗██████╗  █████╗ ████████╗    ██╗
                                ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝    ██║
                                ██║     ██║   ██║██╔████╔██║██████╔╝███████║   ██║       ██║
                                ██║     ██║   ██║██║╚██╔╝██║██╔══██╗██╔══██║   ██║       ╚═╝
                                ╚██████╗╚██████╔╝██║ ╚═╝ ██║██████╔╝██║  ██║   ██║       ██╗
                                 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═╝
                """)
    sleep(2.0)
    clsglobal()
    first = randint(1, 10)
    prince_life = Roi_demon_stats[5]
    mob_life = MobStats[5]
    mp = Roi_demon_stats[10]
    hp = Roi_demon_stats[5]
    if first < 5:
        Sentence("Vous frappez en premier !")
        print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
        print("                                                                 Mana :", Roi_demon_stats[10])
        mob_life = demo_action(MobStats)
        sleep(1.5)
        MobStats[5] = mob_life
        clsglobal()
        while prince_life > 0 or mob_life > 0:
            print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
            print("                                                                 Mana :", Roi_demon_stats[10])
            prince_life = demo_mob_action(MobStats)
            Roi_demon_stats[5] = prince_life
            sleep(1.5)
            clsglobal()
            if prince_life <= 0:
                print("Défaite")
                Roi_demon_stats[5] = hp
                Roi_demon_stats[10] = mp
                demodefaite()
                #la musique s'arrête
                #fonction défaite avec tp au sancturaire des démons
                victoire = False,
                return victoire

            print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
            print("                                                                 Mana :", Roi_demon_stats[10])
            mob_life = demo_action(MobStats)
            MobStats[5] = mob_life
            sleep(1.5)
            clsglobal()
            if mob_life <= 0:
                print(MobStats[0], "est vaincu")
                Roi_demon_stats[10] = mp
                enemy_death.play()
                sleep(4.0)
                # la musique s'arrête
                # fonction victoire avec musique de victoire + affichage du loot + xp
                # faire en sorte de return la vie restante et de la réattribuer à la liste Prince_Stats
                victoire = True
                return victoire
    else:
        Sentence(str(MobStats[0]) + " frappe en premier !")
        print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
        print("                                                                 Mana :", Roi_demon_stats[10])
        prince_life = demo_mob_action(MobStats)
        Roi_demon_stats[5] = prince_life
        sleep(1.5)
        clsglobal()
        while prince_life > 0 or mob_life > 0:
            print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
            print("                                                                 Mana :", Roi_demon_stats[10])
            mob_life = demo_action(MobStats)
            MobStats[5] = mob_life
            sleep(1.5)
            clsglobal()
            if mob_life <= 0:
                print(MobStats[0], "est vaincu")
                Roi_demon_stats[10] = mp
                enemy_death.play()
                sleep(4.0)
                victoire = True
                return victoire

            print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
            print("                                                                 Mana :", Roi_demon_stats[10])
            prince_life = demo_mob_action(MobStats)
            Roi_demon_stats[5] = prince_life
            sleep(1.5)
            clsglobal()
            if prince_life <= 0:
                print("Défaite")
                Roi_demon_stats[10] = mp
                Roi_demon_stats[5] = hp
                demodefaite()
                # la musique s'arrête
                # fonction défaite avec tp au sancturaire des démons
                victoire = False
                return victoire


def demo_Low_Blow(MobStats):
    print("1. Déchainement d'aura (précision - ) | 7 chances sur 10")
    print("2. Seisme (esquive - ) | 7 chances sur 10")
    print("3. Brise armure (armure - )| 1 chance sur 2")
    print("4. Oxydation (dégats - )| 1 chance sur 2")
    print("5. Retour au menu des actions")
    rep = str(input("=> "))
    if rep == "1":
        rate = randint(1, 10)
        if rate > 3:
            print("Vous déchainez votre pouvoir, faisant s'envoler les débris au sol !")
            seism_sound.play()
            sleep(0.5)
            king_scream.play()
            sleep(0.5)
            print("Cela aveugle partiellement votre adversaire. " + MobStats[0] + " est moins précis !")
            sleep(1.0)
            MobStats[6] = MobStats[6] + 5
            mob_hp_remaining = MobStats[5]
            return mob_hp_remaining
        else:
            print("Raté")
            mob_hp_remaining = MobStats[5]
            return mob_hp_remaining
    elif rep == "2":
        rate = randint(1, 10)
        if rate > 3:
            print("Vous mettez un grand coup de pied par terre de manière à fendre le sol")
            seism_sound.play()
            sleep(0.3)
            crack.play()
            sleep(0.3)
            print(MobStats[0], "est déséquilibré, son esquive diminue !")
            sleep(1.0)
            MobStats[7] = MobStats[7] - 2
            if MobStats[7] <= 0:
                MobStats[7] = 0
                print(MobStats[0], "ne peut plus esquiver !")
                mob_hp_remaining = MobStats[5]
                return mob_hp_remaining
            else:
                mob_hp_remaining = MobStats[5]
                return mob_hp_remaining
        else:
            print("Raté")
            mob_hp_remaining = MobStats[5]
            return mob_hp_remaining
    elif rep == "3":
        rate = randint(1, 10)
        if rate >= 5:
            print("Vous trouvez une faille dans l'armure de votre adversaire !")
            broken_armor.play()
            print("La protection de votre adversaire se fragilise !")
            sleep(1.0)
            MobStats[3] = MobStats[3] - 4
            if MobStats[3] <= 0:
                MobStats[3] = 0
                print(MobStats[0], "voit son armure partir en morceaux !")
                sleep(1.0)
                mob_hp_remaining = MobStats[5]
                return mob_hp_remaining
            else:
                mob_hp_remaining = MobStats[5]
                return mob_hp_remaining
        else:
            print("Raté")
            mob_hp_remaining = MobStats[5]
            return mob_hp_remaining
    elif rep == "4":
        rate = randint(1, 10)
        if rate > 5:
            print("Vous saisissez l'arme de votre adversaire et la faîtes rouiller en un instant !")
            sleep(1.0)
            acid_sound.play()
            print("les dégats de l'adversaire sont réduits !")
            MobStats[4] = MobStats[4] - 0.1
            if MobStats[4] <= 1.0:
                MobStats[4] = 1.0
                print(MobStats[0], "voit son arme tomber en morceaux devant ses yeux !")
                broken_weapon.play()
                mob_hp_remaining = MobStats[5]
                return mob_hp_remaining
            else:
                mob_hp_remaining = MobStats[5]
                return mob_hp_remaining
        else:
            print("Raté")
            mob_hp_remaining = MobStats[5]
            return mob_hp_remaining
    elif rep == "5":
        clsglobal()
        print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
        print("                                                                 Mana :", Roi_demon_stats[10])
        mob_hp_remaining = demo_action(MobStats)
        return mob_hp_remaining
    else:
        print("Veuillez entrer un chiffre valide")
        sleep(1.5)
        clsglobal()
        print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
        print("                                                                 Mana :", Roi_demon_stats[10])
        mob_hp_remaining = demo_Low_Blow(MobStats)
    return mob_hp_remaining



def demo_Low_Blow(MobStats):
    print("1. Déchainement d'aura (précision - ) | 7 chances sur 10")
    print("2. Seisme (esquive - ) | 7 chances sur 10")
    print("3. Brise armure (armure - )| 1 chance sur 2")
    print("4. Oxydation (dégats - )| 1 chance sur 2")
    print("5. Retour au menu des actions")
    rep = str(input("=> "))
    if rep == "1":
        rate = randint(1, 10)
        if rate > 3:
            print("Vous déchainez votre pouvoir, faisant s'envoler les débris au sol !")
            seism_sound.play()
            sleep(0.5)
            king_scream.play()
            sleep(0.5)
            print("Cela aveugle partiellement votre adversaire. " + MobStats[0] + " est moins précis !")
            sleep(1.0)
            MobStats[6] = MobStats[6] + 5
            mob_hp_remaining = MobStats[5]
            return mob_hp_remaining
        else:
            print("Raté")
            mob_hp_remaining = MobStats[5]
            return mob_hp_remaining
    elif rep == "2":
        rate = randint(1, 10)
        if rate > 3:
            print("Vous mettez un grand coup de pied par terre de manière à fendre le sol")
            seism_sound.play()
            sleep(0.3)
            crack.play()
            sleep(0.3)
            print(MobStats[0], "est déséquilibré, son esquive diminue !")
            sleep(1.0)
            MobStats[7] = MobStats[7] - 2
            if MobStats[7] <= 0:
                MobStats[7] = 0
                print(MobStats[0], "ne peut plus esquiver !")
                mob_hp_remaining = MobStats[5]
                return mob_hp_remaining
            else:
                mob_hp_remaining = MobStats[5]
                return mob_hp_remaining
        else:
            print("Raté")
            mob_hp_remaining = MobStats[5]
            return mob_hp_remaining
    elif rep == "3":
        rate = randint(1, 10)
        if rate >= 5:
            print("Vous trouvez une faille dans l'armure de votre adversaire !")
            broken_armor.play()
            print("La protection de votre adversaire se fragilise !")
            sleep(1.0)
            MobStats[3] = MobStats[3] - 4
            if MobStats[3] <= 0:
                MobStats[3] = 0
                print(MobStats[0], "voit son armure partir en morceaux !")
                sleep(1.0)
                mob_hp_remaining = MobStats[5]
                return mob_hp_remaining
            else:
                mob_hp_remaining = MobStats[5]
                return mob_hp_remaining
        else:
            print("Raté")
            mob_hp_remaining = MobStats[5]
            return mob_hp_remaining
    elif rep == "4":
        rate = randint(1, 10)
        if rate > 5:
            print("vous saisissez l'arme de votre adversaire et la faites rouiller en un instant !")
            sleep(1.0)
            acid_sound.play()
            print("les dégats de l'adversaire sont réduits !")
            MobStats[4] = MobStats[4] - 0.1
            if MobStats[4] <= 1.0:
                MobStats[4] = 1.0
                print(MobStats[0], "voit son arme tomber en morceaux devant ses yeux !")
                broken_weapon.play()
                mob_hp_remaining = MobStats[5]
                return mob_hp_remaining
            else:
                mob_hp_remaining = MobStats[5]
                return mob_hp_remaining
        else:
            print("Raté")
            mob_hp_remaining = MobStats[5]
            return mob_hp_remaining
    elif rep == "5":
        clsglobal()
        print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
        print("                                                                 Mana :", Roi_demon_stats[10])
        mob_hp_remaining = demo_action(MobStats)
        return mob_hp_remaining
    else:
        print("veuillez entrer un chiffre valide")
        sleep(1.5)
        clsglobal()
        print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
        print("                                                                 Mana :", Roi_demon_stats[10])
        mob_hp_remaining = demo_Low_Blow(MobStats)
    return mob_hp_remaining


# //////////////////////////////////////////////////////////// FONCTIONS DE COMBAT DE BOSS //////////////////////////////////////////////////////////////////////////////////////////////////

# //////////////////////////////////////////////////////////// FONCTIONS ULRIC //////////////////////////////////////////////////////////////////////////////////////////////////

def demo_ulric_action(MobStats):
    print(MobStats[0], "attaque !")
    sleep(1.0)
    randattack = randint(1, 10)
    if randattack < 8:
        rateaccuracy = randint(1, 100)
        if rateaccuracy < MobStats[6]:
            rateesq = randint(1, 100)
            if rateesq <= Roi_demon_stats[11]:
                print("Vous esquivez l'attaque !")
                degats = Roi_demon_stats[5]
                return degats
            else:
                degats = round(demo_attaque_mob(MobStats[0], MobStats[1], MobStats[2], Roi_demon_stats[3], MobStats[4], Roi_demon_stats[5]))
                sword_sound.play()
                fork_sound.play()
                return degats
        else:
            print(MobStats[0], "rate son attaque !")
            degats = Roi_demon_stats[5]
            return degats
    else:
        Sentence("Ulric vous lance un sort de lumière")
        degats = demo_sort_boss(MobStats[0], MobStats[1], MobStats[2], MobStats[4], Roi_demon_stats[5])
        light_attack_2.play()
        return degats

def bossfightulric(MobStats):
    from intro import Sentence
    mess1done = False
    mess2done = False
    mess3done = False
    clsglobal()
    sleep(0.3)
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("""
                    ███████╗ ██████╗ ██╗   ██╗███████╗      ██████╗  ██████╗ ███████╗███████╗    ██╗
                    ██╔════╝██╔═══██╗██║   ██║██╔════╝      ██╔══██╗██╔═══██╗██╔════╝██╔════╝    ██║
                    ███████╗██║   ██║██║   ██║███████╗█████╗██████╔╝██║   ██║███████╗███████╗    ██║
                    ╚════██║██║   ██║██║   ██║╚════██║╚════╝██╔══██╗██║   ██║╚════██║╚════██║    ╚═╝
                    ███████║╚██████╔╝╚██████╔╝███████║      ██████╔╝╚██████╔╝███████║███████║    ██╗
                    ╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝      ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    ╚═╝
                                                Chef de cotterie Ulric
                """)
    sleep(2.0)
    clsglobal()
    first = randint(1, 10)
    prince_life = Roi_demon_stats[5]
    mob_life = MobStats[5]
    mp = Roi_demon_stats[10]
    hp = Roi_demon_stats[5]
    if first < 5:
        Sentence("Vous frappez en premier !")
        print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
        print("                                                                 Mana :", Roi_demon_stats[10])
        mob_life = demo_action(MobStats)
        sleep(1.5)
        MobStats[5] = mob_life
        while prince_life > 0 or mob_life > 0:
            clsglobal()
            print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
            print("                                                                 Mana :", Roi_demon_stats[10])
            prince_life = demo_ulric_action(MobStats)
            Roi_demon_stats[5] = prince_life
            sleep(1.5)
            clsglobal()
            if prince_life <= 0:
                print("Défaite")
                Roi_demon_stats[5] = hp
                Roi_demon_stats[10] = mp
                demodefaite()
                #la musique s'arrête
                #fonction défaite avec tp au sancturaire des démons
                victoire = False,
                return victoire

            clsglobal()
            print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
            print("                                                                 Mana :", Roi_demon_stats[10])
            mob_life = demo_action(MobStats)
            MobStats[5] = mob_life
            sleep(1.5)
            clsglobal()
            if mob_life <= 0:
                print(MobStats[0], "est vaincu")
                Roi_demon_stats[10] = mp
                enemy_death.play()
                sleep(4.0)
                victoire = True
                return victoire
            elif mob_life < 100 and mess3done == False:
                print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":",
                      Roi_demon_stats[5], "pv")
                print("                                                                 Mana :", Roi_demon_stats[10])
                print("")
                print("Ulric")
                Sentence("Tu... ne... m'a pas... encore...vaincu !")
                sleep(1.5)
                mess3done = True
            elif mob_life < 200 and mess2done == False:
                print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":",
                      Roi_demon_stats[5], "pv")
                print("                                                                 Mana :", Roi_demon_stats[10])
                print("")
                print("Ulric")
                Sentence("Tu es coriace Roi démon, ma lumière aura raison de toi.")
                sleep(1.5)
                mess2done = True
            elif mob_life < 400 and mess1done == False:
                print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":",
                      Roi_demon_stats[5], "pv")
                print("                                                                 Mana :", Roi_demon_stats[10])
                print("")
                print("Ulric")
                Sentence("Je vengerai mon peuple !")
                sleep(1.5)
                mess1done = True
    else:
        Sentence(str(MobStats[0]) + " frappe en premier !")
        print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
        print("                                                                 Mana :", Roi_demon_stats[10])
        prince_life = demo_ulric_action(MobStats)
        Roi_demon_stats[5] = prince_life
        sleep(1.5)
        clsglobal()
        while prince_life > 0 or mob_life > 0:
            clsglobal()
            print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
            print("                                                                 Mana :", Roi_demon_stats[10])
            mob_life = demo_action(MobStats)
            MobStats[5] = mob_life
            sleep(1.5)
            clsglobal()
            if mob_life <= 0:
                print(MobStats[0], "est vaincu")
                Roi_demon_stats[10] = mp
                enemy_death.play()
                sleep(4.0)
                victoire = True
                return victoire
            elif mob_life < 100 and mess3done == False:
                print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":",
                      Roi_demon_stats[5], "pv")
                print("                                                                 Mana :", Roi_demon_stats[10])
                print("")
                print("Ulric")
                Sentence("Tu... ne... m'a pas... encore...vaincu !")
                sleep(1.5)
                mess3done = True
            elif mob_life < 200 and mess2done == False:
                print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":",
                      Roi_demon_stats[5], "pv")
                print("                                                                 Mana :", Roi_demon_stats[10])
                print("")
                print("Ulric")
                Sentence("Tu es coriace Roi démon, mais ma lumière aura raison de toi.")
                sleep(1.5)
                mess2done = True
            elif mob_life < 400 and mess1done == False:
                print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":",
                      Roi_demon_stats[5], "pv")
                print("                                                                 Mana :", Roi_demon_stats[10])
                print("")
                print("Ulric")
                Sentence("Je vengerai mon peuple !")
                sleep(1.5)
                mess1done = True
            clsglobal()
            print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
            print("                                                                 Mana :", Roi_demon_stats[10])
            prince_life = demo_ulric_action(MobStats)
            Roi_demon_stats[5] = prince_life
            sleep(1.5)
            clsglobal()
            if prince_life <= 0:
                print("Défaite")
                Roi_demon_stats[10] = mp
                Roi_demon_stats[5] = hp
                demodefaite()
                # la musique s'arrête
                # fonction défaite avec tp au sancturaire des démons
                victoire = False
                return victoire


# //////////////////////////////////////////////////////////// FONCTIONS BOSS //////////////////////////////////////////////////////////////////////////////////////////////////

def demo_sort_boss(name, atkmini, atkmax, mult, hp):
    total_atk = randint(atkmini, atkmax)
    Prince_hp_remaining = hp - round(total_atk)
    round(Prince_hp_remaining)
    print(name, "vous inflige", total_atk, "dégats.")
    sleep(1.5)
    return Prince_hp_remaining

def demo_boss_action(MobStats):
    print(MobStats[0], "attaque !")
    sleep(1.0)
    randattack = randint(1, 10)
    if randattack < 5:
        rateaccuracy = randint(1, 100)
        if rateaccuracy < MobStats[6]:
            rateesq = randint(1, 100)
            if rateesq <= Roi_demon_stats[11]:
                print("Vous esquivez l'attaque !")
                degats = Roi_demon_stats[5]
                return degats
            else:
                Sentence("Le prince en blanc vous porte un coup d'épée")
                degats = demo_attaque_mob(MobStats[0], MobStats[1], MobStats[2], Roi_demon_stats[3], MobStats[4], Roi_demon_stats[5])
                sword_sound.play()
                fork_sound.play()
                return degats
        else:
            print(MobStats[0], "rate son attaque !")
            degats = Roi_demon_stats[5]
            return degats
    elif randattack < 5 and randattack > 7:
        Sentence("Le Prince en Blanc vous lance un sort de lumière ")
        degats = demo_sort_boss(MobStats[0], MobStats[1], MobStats[2], MobStats[4], Roi_demon_stats[5])
        light_attack.play()
        return degats
    else:
        Sentence("Le Prince en Blanc vous attaque à l'aide de sa lance de lumière ")
        degats = demo_sort_boss(MobStats[0], MobStats[1], MobStats[2], MobStats[4], Roi_demon_stats[5]) + 20
        light_beam.play()
        return degats

def bossfightking(MobStats):
    from intro import Sentence
    messb1done = False
    messb2done = False
    messb3done = False
    clsglobal()
    sleep(0.3)
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("""
                                        ██████╗  ██████╗ ███████╗███████╗    ██╗
                                        ██╔══██╗██╔═══██╗██╔════╝██╔════╝    ██║
                                        ██████╔╝██║   ██║███████╗███████╗    ██║
                                        ██╔══██╗██║   ██║╚════██║╚════██║    ╚═╝
                                        ██████╔╝╚██████╔╝███████║███████║    ██╗
                                        ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    ╚═╝
                                                  Le Prince en Blanc
                """)
    sleep(2.0)
    clsglobal()
    first = randint(1, 10)
    prince_life = Roi_demon_stats[5]
    mob_life = MobStats[5]
    mp = Roi_demon_stats[10]
    hp = Roi_demon_stats[5]
    if first < 5:
        Sentence("Vous frappez en premier !")
        print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
        print("                                                                 Mana :", Roi_demon_stats[10])
        mob_life = demo_action(MobStats)
        sleep(1.5)
        MobStats[5] = mob_life
        while prince_life > 0 or mob_life > 0:
            clsglobal()
            print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
            print("                                                                 Mana :", Roi_demon_stats[10])
            prince_life = demo_boss_action(MobStats)
            Roi_demon_stats[5] = prince_life
            sleep(1.5)
            clsglobal()
            if prince_life <= 0:
                Roi_demon_stats[5] = hp
                Roi_demon_stats[10] = mp
                victoire = False,
                return victoire
            elif prince_life < 100 and messb3done == False:
                print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":",
                      Roi_demon_stats[5], "pv")
                print("                                                                 Mana :", Roi_demon_stats[10])
                print("")
                print("Le Prince en Blanc")
                Sentence("Soit purifié démon.")
                sleep(1.5)
                messb3done = True
            elif prince_life < 200 and messb2done == False:
                print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":",
                      Roi_demon_stats[5], "pv")
                print("                                                                 Mana :", Roi_demon_stats[10])
                print("")
                print("Le Prince en Blanc")
                Sentence("Vous n'êtes rien face à la lumière.")
                sleep(1.5)
                messb2done = True
            elif prince_life < 400 and messb1done == False:
                print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":",
                      Roi_demon_stats[5], "pv")
                print("                                                                 Mana :", Roi_demon_stats[10])
                print("")
                print("Le Prince en Blanc")
                Sentence("Toute action contre moi est futile.")
                sleep(1.5)
                messb1done = True

            clsglobal()
            print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
            print("                                                                 Mana :", Roi_demon_stats[10])
            mob_life = demo_action(MobStats)
            MobStats[5] = mob_life
            sleep(1.5)
            clsglobal()
            if mob_life <= 0:
                print(MobStats[0], "est vaincu")
                Roi_demon_stats[10] = mp
                enemy_death.play()
                print("")
                print("Les Devs")
                Sentence("Bravo !")
                SentenceSlow("...")
                Sentence("Malheureusement pour le bien du jeu et le respect du lore... Vous devez perdre... :'(")
                sleep(3.0)
                clsglobal()

                victoire = True
                return victoire

    else:
        Sentence(str(MobStats[0]) + " frappe en premier !")
        print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
        print("                                                                 Mana :", Roi_demon_stats[10])
        prince_life = demo_boss_action(MobStats)
        Roi_demon_stats[5] = prince_life
        sleep(1.5)
        clsglobal()
        while prince_life > 0 or mob_life > 0:
            clsglobal()
            print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
            print("                                                                 Mana :", Roi_demon_stats[10])
            mob_life = demo_action(MobStats)
            MobStats[5] = mob_life
            sleep(1.5)
            clsglobal()
            if mob_life <= 0:
                print(MobStats[0], "est vaincu")
                Roi_demon_stats[10] = mp
                enemy_death.play()
                sleep(4.0)
                victoire = True
                print("")
                print("Les Devs")
                Sentence("Bravo !")
                SentenceSlow("...")
                Sentence("Malheureusement pour le bien du jeu et le respect du lore... Vous devez perdre... :'(")
                sleep(3.0)
                clsglobal()
                return victoire
            clsglobal()
            print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":", Roi_demon_stats[5], "pv")
            print("                                                                 Mana :", Roi_demon_stats[10])
            prince_life = demo_boss_action(MobStats)
            Roi_demon_stats[5] = prince_life
            sleep(1.5)
            clsglobal()
            if prince_life <= 0:
                Roi_demon_stats[10] = mp
                Roi_demon_stats[5] = hp
                victoire = False
                return victoire
            elif prince_life < 100 and messb3done == False:
                print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":",
                      Roi_demon_stats[5], "pv")
                print("                                                                 Mana :", Roi_demon_stats[10])
                print("")
                print("Le Prince en Blanc")
                Sentence("Soit purifié démon.")
                sleep(1.5)
                messb3done = True
            elif prince_life < 200 and messb2done == False:
                print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":",
                      Roi_demon_stats[5], "pv")
                print("                                                                 Mana :", Roi_demon_stats[10])
                print("")
                print("Le Prince en Blanc")
                Sentence("Vous n'êtes rien face à la lumière.")
                sleep(1.5)
                messb2done = True
            elif prince_life < 400 and messb1done == False:
                print(MobStats[0], ":", int(MobStats[5]), "pv", "                         ", Roi_demon_stats[0], ":",
                      Roi_demon_stats[5], "pv")
                print("                                                                 Mana :", Roi_demon_stats[10])
                print("")
                print("Le Prince en Blanc")
                Sentence("Toute action contre moi est futile.")
                sleep(1.5)
                messb1done = True