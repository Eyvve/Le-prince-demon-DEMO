import pygame
import os
from time import sleep
from maps import *
from Music_sounds import *
from about import *
from combat import *
from demo import *
import sys
from roi_demon_inv import *

pygame.init()

questdone = False
qeastdone = False
qwestdone = False
Anchor = 0

def Sentence(x):
    lines = [x]

    from time import sleep
    import sys

    for line in lines:
        sleep(1.0)
        for c in line:
            print(c, end='')
            sys.stdout.flush()
            text_sound.play()
            sleep(0.03)
        print('')

def SentenceSlow(x):
    lines = [x]

    from time import sleep
    import sys

    for line in lines:
        sleep(1.0)
        for c in line:
            print(c, end='')
            sys.stdout.flush()
            text_sound.play()
            sleep(0.6)
        print('')

def title():
    import time
    print("NotPirates studios présente...")
    time.sleep(2.3)
    print("""
                                                        ,-.                               
                                   ___,---.__          /'|`\          __,---,___          
                                ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.       
                              ,'        |           ~'\     /`~           |        `.      
                             /      ___//              `. ,'          ,  , \___      \    
                            |    ,-'   `-.__   _         |        ,    __,-'   `-.    |    
                            |   /          /\_  `   .    |    ,      _/\          \   |   
                            \  |           \ \`-.___ \   |   / ___,-'/ /           |  /  
                             \  \           | `._   `\\  |  //'   _,' |           /  /      
                              `-.\         /'  _ `---'' , . ``---' _  `\         /,-'     
                                 ``       /     \    ,='/ \`=.    /     \       ''          
                                         |__   /|\_,--.,-.--,--._/|\   __|                  
                                         /  `./  \\`\ |  |  | /,//' \,'  \                  
    ██╗     ███████╗    ██████╗ ██████╗ ██╗███╗   ██╗ ██████╗███████╗\   ██████╗ ███████╗███╗   ███╗ ██████╗ ███╗   ██╗
    ██║     ██╔════╝    ██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██╔════╝ \  ██╔══██╗██╔════╝████╗ ████║██╔═══██╗████╗  ██║
    ██║     █████╗      ██████╔╝██████╔╝██║██╔██╗ ██║██║     █████╗    \ ██║  ██║█████╗  ██╔████╔██║██║   ██║██╔██╗ ██║
    ██║     ██╔══╝      ██╔═══╝ ██╔══██╗██║██║╚██╗██║██║     ██╔══╝    | ██║  ██║██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║
    ███████╗███████╗    ██║     ██║  ██║██║██║ ╚████║╚██████╗███████╗  | ██████╔╝███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║
    ╚══════╝╚══════╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝  | ╚═════╝ ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                       |Canonne, Delaire & Goldbronn - 2020|                 ver. demo
                                       |   |     /'\_\_\ | /_/_/`\     |   |                
                                        \   \__, \_     `~'     _/ .__/   /            
                                         `-._,-'   `-._______,-'   `-._,-'
                                         
                                         
                                         
                      """)
    time.sleep(0.8)
    main_menu()


def titlebis():
    import time
    os.system("cls")
    print("NotPirates studios présente...")
    intro_music_bis.play(-1)
    time.sleep(1.1)
    print("""
                                                        ,-.                               
                                   ___,---.__          /'|`\          __,---,___          
                                ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.       
                              ,'        |           ~'\     /`~           |        `.      
                             /      ___//              `. ,'          ,  , \___      \    
                            |    ,-'   `-.__   _         |        ,    __,-'   `-.    |    
                            |   /          /\_  `   .    |    ,      _/\          \   |   
                            \  |           \ \`-.___ \   |   / ___,-'/ /           |  /  
                             \  \           | `._   `\\  |  //'   _,' |           /  /      
                              `-.\         /'  _ `---'' , . ``---' _  `\         /,-'     
                                 ``       /     \    ,='/ \`=.    /     \       ''          
                                         |__   /|\_,--.,-.--,--._/|\   __|                  
                                         /  `./  \\`\ |  |  | /,//' \,'  \                  
    ██╗     ███████╗    ██████╗ ██████╗ ██╗███╗   ██╗ ██████╗███████╗\   ██████╗ ███████╗███╗   ███╗ ██████╗ ███╗   ██╗
    ██║     ██╔════╝    ██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██╔════╝ \  ██╔══██╗██╔════╝████╗ ████║██╔═══██╗████╗  ██║
    ██║     █████╗      ██████╔╝██████╔╝██║██╔██╗ ██║██║     █████╗    \ ██║  ██║█████╗  ██╔████╔██║██║   ██║██╔██╗ ██║
    ██║     ██╔══╝      ██╔═══╝ ██╔══██╗██║██║╚██╗██║██║     ██╔══╝    | ██║  ██║██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║
    ███████╗███████╗    ██║     ██║  ██║██║██║ ╚████║╚██████╗███████╗  | ██████╔╝███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║
    ╚══════╝╚══════╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝  | ╚═════╝ ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                       |Canonne, Delaire & Goldbronn - 2020|                 ver. demo
                                       |   |     /'\_\_\ | /_/_/`\     |   |                
                                        \   \__, \_     `~'     _/ .__/   /            
                                         `-._,-'   `-._______,-'   `-._,-'



                      """)
    main_menu()


def titleintro():
    import os
    os.system("cls")
    intro_music.play(-1)
    lines = ["Il y a 200 ans, une guerre entre humains et démons faisait rage...",
             "Les démons perdirent cette guerre et furent forcés à se cacher pour survivre...",
             "Les humains, paisibles, eurent l'occasion de jouir de 200 ans ans de paix...",
             "MAIS CE TEMPS",
             "EST",
             "REVOLU."]

    from time import sleep
    import sys

    for line in lines:
        sleep(1.3)
        for c in line:
            print(c, end='')
            sys.stdout.flush()
            text_sound.play()
            sleep(0.07)
        print('')
    import time
    time.sleep(2.7)
    import os
    os.system("cls")
    title()


def main_menu():
    print("                  1: Nouvelle partie")
    print("                  2: Charger partie")
    print("                  3: À propos")
    print("                  4: Quitter le jeu")
    choice = str(input("=> "))
    validation_sound.play()
    while choice != "" or choice != "" or choice != "" or choice != "":
        if choice == "1":
            intro_music.stop()
            intro_music_bis.stop()
            sleep(2.0)
            choice_mode()
            return
        elif choice == "2":
            intro_music.stop()
            intro_music_bis.stop()
            sleep(2.0)
            load()
            return
        elif choice == "3":
            intro_music.stop()
            intro_music_bis.stop()
            sleep(2.0)
            About()
            return
        elif choice == "4":
            intro_music.stop()
            intro_music_bis.stop()
            Sentence("À bientôt ! :)")
            sleep(2.0)
            sys.exit()
            return
        if choice != "" or choice != "" or choice != "" or choice != "":
            Sentence("Veuillez entrer un choix valide")
        choice = str(input("=> "))


def PlayGame():
    import os
    os.system("cls")
    Sentence("Disclamer : pour éviter des choix involontaires, n'appuyez sur votre clavier que quand on vous le demande.")
    Sentence("Il est recommandé de jouer avec un casque.")
    Sentence("Appuyez sur 'Entrée' lorsque vous êtes prêt.")
    skip_touch()
    validation_sound.play()
    import time
    Sentence("Bon jeu !")
    time.sleep(2.0)
    import os
    os.system("cls")
    titleintro()
    return



def choice_mode():
    os.system("cls")
    print("""
    
    """)
    print("")
    print("                    1 - MODE TUTO                                                  2 - DEMO")
    print("")
    print("           Le mode tuto est à choisir si vous                          Vivez les dernières heures de la Grande ")
    print("           Souhaitez connaître l'histoire du prince                    Guerre en incarnant le Roi Démon.")
    print("           et vivre les premières minutes de ce qu'était               Ce mode fait office de préquelle et de ")
    print("           sensé être le jeu à la base.                                démo incluant tout ce que offre le gameplay")
    print("           Ce mode est à privilégier si vous souhaitez                 du jeu final. Ce mode est à privilegier si ")
    print("           prendre le temps de découvrir le système                    en savoir plus sur l'histoire de Prince Démon.")
    print("           de combat.")
    print("""
    
    
    
    """)
    choix = str(input("Choisissez un mode de jeu : "))
    while choix != "1" or choix != "2":
        if choix == "1":
            validation_sound.play()
            os.system("cls")
            print("")
            Sentence("MODE TUTO")
            sleep(2.0)
            beginning()
            return
        elif choix == "2":
            validation_sound.play()
            os.system("cls")
            print("")
            Sentence("DEMO")
            sleep(2.0)
            demo(questdone, qeastdone, qwestdone, Anchor)
            return
        elif choix != "1" and choix != "2":
            print("veuillez choisir un mode qui existe")
            choix = str(input("Choisissez un mode de jeu :"))

            
def load():
    from roi_demon_inv import roi_demon
    from roi_demon_inv import Roi_demon_stats
    Sentence("Veuillez entrer un mot de passe")
    print("1. Retour")
    mdp = str(input("=> "))
    while mdp != "Zazranoth" or mdp != "Ginn" or mdp != "Ulric" or mdp != "1":
        if mdp == "1":
            sleep(0.2)
            titlebis()
            return
        if mdp == "Zazranoth":
            pickle_load()
            questdone = False
            qeastdone = False
            qwestdone = False
            SaveAnchor1(questdone, qeastdone, qwestdone, Anchor)
            return
        elif mdp == "Ginn":
            pickle_load()
            questdone = False
            qeastdone = False
            qwestdone = False
            SaveAnchor2(questdone, qeastdone, qwestdone, Anchor)
            return
        elif mdp == "Ulric":
            pickle_load()
            questdone = False
            qeastdone = False
            qwestdone = False
            SaveAnchor3(questdone, qeastdone, qwestdone, Anchor)
            return
        if mdp != "Zazranoth" or mdp != "Ginn" or mdp != "Ulric" or mdp != "1":
            Sentence("Ce mot de passe n'existe pas.")
        mdp = str(input("=> "))

