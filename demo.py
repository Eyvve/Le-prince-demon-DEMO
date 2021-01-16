from time import sleep
from maps import skip_touch
from Music_sounds import *
from roi_demon_inv import *
from combat import *
from intro import *
from os import *

questdone = False
qeastdone = False
qwestdone = False
Anchor = 0

def demo(qdone, qwest, qeast, anchor):
    from intro import Sentence
    from combat import demofight
    from roi_demon_inv import Roi_demon_stats
    from roi_demon_inv import pickle_save

    deva_stats = ["Deva", 30, 40, 15, 1.2, 200, 85, 5]
    cotterie_stats = ["Chef de Cotterie", 45, 55, 20, 1.2, 300, 85, 5]
    Sentence("Conformement au lore établi, le Roi démon ou Dieu-Roi porte le nom d'Ibliss Nizidramanii'yt.")
    print("")
    Sentence("Quel est votre nom ? Si vous souhaitez le nom lore friendly, appuyez simplement sur Entrée.")
    kingsName = str(input("=> "))
    if kingsName == "":
        Roi_demon_stats[0] = "Ibliss"
    else:
        Roi_demon_stats[0] = kingsName
    validation_sound.play()
    pickle_save()
    sleep(5)
    sleep(2.0)
    os.system("cls")
    demo_intro_sound.play()
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
                              ██████╗ ██████╗  ██████╗ ██╗      ██████╗  ██████╗ ██╗   ██╗███████╗
                              ██╔══██╗██╔══██╗██╔═══██╗██║     ██╔═══██╗██╔════╝ ██║   ██║██╔════╝
                    █████╗    ██████╔╝██████╔╝██║   ██║██║     ██║   ██║██║  ███╗██║   ██║█████╗      █████╗
                    ╚════╝    ██╔═══╝ ██╔══██╗██║   ██║██║     ██║   ██║██║   ██║██║   ██║██╔══╝      ╚════╝
                              ██║     ██║  ██║╚██████╔╝███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗
                              ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝

                                                        Le Dieu Roi
        """)
    sleep(11.0)
    os.system("cls")
    narration_intro_music.play(-1)
    # wind_thunder_sound.play(-1)
    battle_sound_effect.play(-1)
    os.system("cls")
    print("Champ de bataille de la citadelle - coeur de la bataille")
    print("")
    Sentence("La bataille faisait rage.")
    sleep(1.5)
    Sentence(" Les cieux étaient aussi rougeâtre que le sol devant la citadelle dorée des Hommes..")
    sleep(1.5)
    Sentence("Les corps, de différentes formes et couleurs, jonchaient le sol.")
    sleep(1.5)
    Sentence("Dans le flou du combat, impossible pour vous, le Dieu-roi S'rhaal, de faire le point sur la situation.")
    skip_touch()
    os.system("cls")
    print("Champ de bataille de la citadelle - coeur de la bataille")
    print("")
    Sentence("Vous débarrassant de votre opposant d'un lourd coup de lame,")
    Sentence("fendant du même mouvement la lourde armure et le corps du paladin, avant de lancer un long cri de ralliement.")
    sleep(1.5)
    Sentence("La situation des forces en présence est désastreuse.")
    skip_touch()
    os.system("cls")
    print("Champ de bataille de la citadelle - coeur de la bataille")
    print("")
    Sentence("Les brutes ont bien encaissé la mêlée,")
    Sentence("mais tous vos suivants plus fragiles se sont fait découper par l'acier chantant des créatures célestes...")
    sleep(1.5)
    Sentence("Avant de pouvoir lancer une série d'ordres, deux silhouettes d'or et de sang se dressent devant vous. ")
    print("")
    Sentence("A vue d'oeil, un chef de cotterie et un déva.")
    skip_touch()
    narration_intro_music.fadeout(1000)
    sleep(2)
    demo_deva_combat.play(-1)
    Sentence("Ils ne sont rien.")
    sleep(6.0)
    demofight(deva_stats)
    os.system("cls")
    Sentence("Alors que vous veniez à peine de tuer le deva, le chef de cotterie tente de vous porter un coup d'épée.")
    sleep(1.5)
    demofight(cotterie_stats)
    demo_deva_combat.fadeout(1000)
    sleep(1.0)
    os.system("cls")
    print("Champ de bataille de la citadelle - coeur de la bataille")
    print("")
    sleep(1.0)
    # fin des deux combats, si le joueur est pas mort il à pris un peu cher, hop sequence gameplay potion
    Sentence("Vous ressortez de ce combat blessé, vous trouvez judicieux de regagner de la santé avant de retourner au voir vos troupes.")
    sleep(1.5)
    Sentence("Par chance vous avez suffisamment de potions sur vous pour reprendre des forces.")
    skip_touch()
    os.system("cls")
    anchor = 1
    SaveAnchor1(qdone, qwest, qeast, anchor)
    return

def SaveAnchor1(qdone, qwest, qeast, anchor):
    from intro import Sentence
    from roi_demon_inv import menu_roi
    anchor = 1
    menu_roi(anchor)
    battle_sound_effect.fadeout(1000)
    battle_sound_effect.play(-1)
    os.system("cls")
    print("Champ de bataille de la citadelle - coeur de la bataille")
    print("")
    gates_music.play(-1)
    Sentence("Vous vous relevez et regardez à vos pieds.")
    sleep(1.5)
    Sentence("Dominant de toute votre hauteur le cadavre de vos ennemis, vous entendez un cri d'alerte puissant et familier.")
    sleep(1.5)
    Sentence("Zazranoth, votre général, et Ginn, son fils et aide de camp viennent vers vous,")
    Sentence("se mouvant dans le charnier avec difficulté, le visage de l'un grave, celui de l'autre en détresse. ")
    skip_touch()
    os.system("cls")
    print("Champ de bataille de la citadelle - coeur de la bataille")
    print("")
    print("Zazranoth :")
    Sentence("Mon seigneur, nous sommes en train de perdre. Ces maudits pourceaux ont obtenu l'aide de créatures de lumière inconnues.")
    sleep(1.5)
    Sentence("Il nous faut prendre une décision avant la débâcle complète. Deux choix s'offrent à nous,")
    Sentence("tenter d'abattre les portes, trouver leur leader et le tuer, pour arracher la victoire,")
    Sentence("ou sonner la retraite et tenter de sauver un maximum des nôtres.")
    sleep(1.5)
    print("")
    Sentence("*Fuir se résumerait à faire un aveu de faiblesse, ceci ne nous ressemble pas...*")
    Sentence("*Vaut-il vraiment mieux nous battre et risquer plus de troupes ou bien fuir quitte à perdre notre honneur ?..*")
    print("1. Abattre les portes")
    print("2. fuir")
    print("")
    print("Zazranoth :")
    Sentence("Quel est votre choix mon seigneur ?")
    rep = str(input())
    while rep != "1" or rep != "2":
        if rep == "1":
            qassautportes(qdone, qwest, qeast, anchor)
            return
        elif rep == "2":
            Retraite()
            return
        if rep != "1" or rep != "2":
            Sentence("Malheureusement, il n'y a pas d'autres options mon seigneur.")
        rep = str(input())


#    - choix a faire:
#       attaquer les portes
#       fuir


def Retraite():
    from roi_demon_inv import Roi_demon_stats
    from intro import Sentence
    os.system("cls")
    print("Champ de bataille de la citadelle - coeur de la bataille")
    print("")
    gates_music.fadeout(1000)
    sleep(1.0)
    throne_theme.play()
    Sentence("Laissant votre regard planer sur le désastre de ce champ de bataille, votre résolution flanche.")
    print("")
    Sentence("*À quoi bon changer l'ordre des choses, ")
    Sentence("et instaurer un ordre nouveau pour les nouvelles générations si presque tout son peuple doit périr dans la tentative ?*")
    sleep(1.5)
    Sentence("Les mots de l'arcaniste Seraphos lui revinrent en tête...")
    print("")
    Sentence(' "Quand tu lèveras ton épée contre le bastion des mortels, tu feras trembler une civilisation." ')
    skip_touch()
    print("Champ de bataille de la citadelle - coeur de la bataille")
    print("")
    Sentence("Ce maudit corbeau de mauvaise augure pouvait bien là prédire la chute de son peuple! ")
    Sentence("Et il ne sera pas relaté dans les Sombres Grimoires que vous,")
    Sentence("Nizidramanii'yt le Roi-Dieu, aurez causé la ruine des siens !")
    Sentence("Quoi qu'il en coûte et peu importe la honte, survivre est l'essentiel. L'ennemi est beaucoup trop nombreux,")
    Sentence("soutenu par des  créatures inconnues, béni d'une magie imprévue. ")
    Sentence("Les humains, créatures certes éphémères, se relèveraient bien mieux que son peuple d'une guerre de cette ampleur, ")
    Sentence("étant bien plus nombreux et bien plus fertiles... ")
    Sentence("Devant la réalité imposée par l'étude des faits, et la mort dans la l'âme, ne pouvant vous")
    Sentence("donner l'ordre à vous-même, vous annoncez à voix basse, comme brisée :")
    sleep(1.5)
    os.system("cls")
    print("")
    print(Roi_demon_stats[0])
    Sentence('"Zaz... Sonne la retraite."')
    Sentence(""" "Je ne serais pas l'instigateur de la destruction des nôtres... Ils sont plus redoutables que ce qu'il semblait." """)
    os.system("cls")
    sleep(2.0)
    Sentence("L'ordre fut donné, relayé, sonné. ")
    Sentence("La retraite, à deux doigts de se transformer en fuite ou en débandade, se fit.")
    sleep(1.5)
    Sentence("Aucun contact ne fut jamais pris avec les humains ")
    Sentence("qui se contentèrent de bouter les démons dans les montagnes d'Aurgelmirtann, au nord de Ljosalfer...")
    skip_touch()
    os.system("cls")
    throne_theme.fadeout(1000)
    battle_sound_effect.fadeout(1000)
    print("")
    Sentence("Jusque des siècles plus tard, les hommes se rappellent de cet évènement comme la Bataille de la Couronne,")
    Sentence("ou grâce à une alliance avec des créatures célestes, les humains ont repoussé les démons.")
    sleep(1.5)
    Sentence("Ces derniers finirent sous le joug des premiers,")
    Sentence("le peu d'entre eux encore libres se terrant dans les montagnes. ")
    sleep(1.5)
    print("")
    Sentence("A ce jour, nul ne sait comment les humains ont obtenu l'aide des anges,")
    Sentence("mais depuis, un certain 'Prince en Blanc', que personne ne voit jamais,")
    Sentence("semble avoir remplacé le roi précédent, et règne sur Ljosalfer d'une main juste,  ")
    Sentence("ferme,")
    Sentence("et désinteressée...")
    from outro import outro
    outro()
    return


def qassautportes(qdone, qwest, qeast, anchor):
    from intro import Sentence
    from roi_demon_inv import Roi_demon_stats
    os.system("cls")
    print("Champ de bataille de la citadelle - coeur de la bataille")
    print("")
    sleep(2.0)
    print(Roi_demon_stats[0])
    Sentence("Nous ne fuirons pas, il est hors de question d'abandonner, je ne suis pas encore mort...")
    print("")
    sleep(1.5)
    Sentence("Ces portes sont bardées de magie défensives, il va me falloir utiliser une puissante magie pour en venir à bout.")
    sleep(1.5)
    Sentence("Zazranoth, retourne auprès des troupes, nous lançons l'assaut final.")
    Sentence("Ginn ! Libère moi le chemin jusqu'aux emplacement que je t'indiquerai !")
    Sentence("Je vais devoir planter deux sceptres de pouvoir pour en canaliser l'énergie!")
    skip_touch()
    os.system("cls")
    print("Champ de bataille de la citadelle - coeur de la bataille")
    print("")
    print("Ginn")
    Sentence("Bien mon Roi!")
    print("")
    Sentence("L'aide de camp réagit au quart de tour, avec le zèle qui le caractérise. Jouant de sa masse et de son bouclier, ")
    Sentence("il commence à faire le ménage sur le champ de bataille dans la direction indiquée par son supérieur.")
    print("")
    quest_sound.play()
    print("Quête ajoutée : L'assaut")
    sleep(1.0)
    Sentence("Objectif : planter un sceptre catalyseur sur chaque position est et ouest des portes.")
    skip_touch()
    os.system("cls")
    print("Champ de bataille de la citadelle - coeur de la bataille")
    print("")
    Sentence("A l'est se trouve un champ détruit par les combats, il ne devrait pas contenir beaucoup d'ennemis.")
    Sentence("A l'ouest se trouve une vieille tour de garde, il vaut mieux s'attendre à une confontation.")
    print("")
    print("""Ou souhaitez vous aller en premier ?
    
 1. Champ abandonné (est)
 2. Vieille tour de garde (ouest)
 3. Grande porte de la citadelle
 
    """)
    direction = str(input("=> "))
    while direction != "1" or direction != "2" or direction != "3":
        if direction == "1":
            qassautportesest(qdone, qwest, qeast, anchor)
            return
        elif direction == "2":
            assautportesouest(qdone, qwest, qeast, anchor)
            return
        elif direction == "3":
            assautportes(qdone, qwest, qeast, anchor)
            return
        if direction != "1" or direction != "2" or direction != "3":
            Sentence("Impossible d'aller autre part.")
        direction = str(input())



#      - Choix à faire, aller planter l'un des sceptres sceptre à gauche ou a droite.

def qassautportesest(qdone, qwest, qeast, anchor):
    from intro import Sentence
    from roi_demon_inv import Roi_demon_stats
    if qeast == True:
        os.system("cls")
        print("Champ de bataille de la citadelle - champs est")
        print("")
        Sentence("Vous n'avez plus rien à faire ici, vous devriez aller planter l'autre sceptre.")
        skip_touch()
        os.system("cls")
        print("")
        print("Retour à la porte")
        sleep(1.5)
        assautportes(qdone, qwest, qeast, anchor)
        return
    elif qeast == False:
        os.system("cls")
        print("Champ de bataille de la citadelle - champs est")
        print("")
        Sentence("Précédé par votre serviteur, vous vous dirigez vers l'est des portes, ")
        Sentence("esquivant les groupes de combattants emprunts de furie, profitant du chaos.")
        sleep(1.5)
        Sentence("Devant un amas de corps sans vie, humains comme démons,")
        Sentence("assurément fauchés là par l'un des sorts favoris et reconnaissable de Seraphos,")
        Sentence("le maître sorcier et général en second de votre armée.")
        skip_touch()
        os.system("cls")
        print("Champ de bataille de la citadelle - champs est")
        print("")
        print(Roi_demon_stats[0])
        Sentence("Voilà que ce vieux fou me facilite la tâche pour une fois. Je ne pense pas pouvoir me faire surprendre par une attaque ici.")
        if qwest == True:
            Sentence("Plantons le second sceptre.")
        elif qwest == False:
            Sentence("Plantons le premier sceptre.")
        sleep(1)
        menu_roi_sceptre()
        sleep(1.5)
        os.system("cls")
        print("Champ de bataille de la citadelle - champs est")
        print("")
        Sentence("Connectant directement les filaments encore perceptibles de magie destructrice, il les attacha à son sceptre, ")
        Sentence("tissant un catalyseur avant de l'enfoncer profondément dans le sol.")
        sleep(1.5)
        print("")
        Sentence("Surpris par le fracas du métal juste derrière vous, vous vous retournez brusquement,")
        Sentence("juste à temps pour voir votre second repousser un assaut de plusieurs humains d'un vaste mouvment de bouclier.")
        skip_touch()
        if qwest == True:
            gates_music.fadeout(1000)
            os.system("cls")
            print("Quête terminée: L'assaut")
            questdonesound.play()
            sleep(2.0)
            os.system("cls")
            print("Champ de bataille de la citadelle - champs est")
            print("")
            combat_music_2.play()
            print(Roi_demon_stats[0])
            Sentence("Le second sceptre est en place ! On bouge, et repousse moi ces vermisseaux !")
            Sentence("On à une porte à détruire et une bataille à remporter !")
            print()
            Sentence("Après vous être assuré par un échange de regard que votre second ait bien entendu les ordres,")
            Sentence("Vous prenez la direction de la porte principale. ")
            skip_touch()
            qdone = True
            assautportes(qdone, qwest, qeast, anchor)
            return qdone
        elif qwest == False:
            sleep(1.5)
            os.system("cls")
            print("Champ de bataille de la citadelle - champs est")
            print("")
            print(Roi_demon_stats[0])
            Sentence("Le premier sceptre est en place ! On bouge, et repousse moi ces vermisseaux !")
            print("")
            print("Ou souhaitez-vous aller ?")
            print("1. Portes de la citadelle")
            print("2. Vieille tour de garde (ouest)")
            direction = str(input("=> "))
            while direction != "1" or direction != "2":
                if direction == "1":
                    qeast = True
                    assautportes(qdone, qwest, qeast, anchor)
                    return qeast
                elif direction == "2":
                    Sentence("On part pour l'emplacement ouest !")
                    print()
                    Sentence("Après vous être assuré par un échange de regard que votre second ait bien entendu les ordres,")
                    Sentence("Vous prenez la direction du second emplacement. ")
                    qeast = True
                    skip_touch()
                    assautportesouest(qdone, qwest, qeast, anchor)
                    return qeast
                if direction != "1" or direction != "2":
                    Sentence("Impossible d'aller autre part.")
                direction = str(input())


def assautportesouest(qdone, qwest, qeast, anchor):
    from intro import Sentence
    from combat import Prince_stats
    from combat import demofight
    from roi_demon_inv import Roi_demon_stats
    cotteriepui_stats = ["Chef de Cotterie", 55, 65, 20, 1.2, 400, 75, 5]
    if qwest == True:
        os.system("cls")
        print("Champ de bataille de la citadelle - tour de garde ouest")
        print("")
        Sentence("Vous n'avez plus rien à faire ici, vous devriez aller planter l'autre sceptre.")
        skip_touch()
        print("")
        print("Retour à la porte")
        sleep(1.5)
        assautportes(qdone, qwest, qeast, anchor)
        return
    if qwest == False:
        os.system("cls")
        print("Champ de bataille de la citadelle - tour de garde ouest")
        print("")
        Sentence("Naviguant entre les amoncellements de corps, hurlant parmis les cris, ")
        Sentence("glissant sur les flaques de sang et les morceaux de métal,")
        Sentence("le duo arrive au point ouest des portes, ")
        Sentence("où la lumière du soleil couchant se reflétant contre les portes métalliques donnait à la scène une lumière saisissante. ")
        sleep(1.5)
        skip_touch()
        print("Champ de bataille de la citadelle - tour de garde ouest")
        print("")
        sleep(1)
        menu_roi_sceptre()
        os.system("cls")
        print("Champ de bataille de la citadelle - tour de garde ouest")
        print("")
        Sentence("Sans vous laisser émouvoir ou perdre de temps, ")
        Sentence("vous vous lancez dans une incantation complexe attirant les énergies macabres de l'endroit,")
        Sentence("les scellant autour du sceptre avant de le ficher profondément dans le sol, brisant le sol au passage. ")
        skip_touch()
        gates_music.fadeout(1500)
        os.system("cls")
        print("Champ de bataille de la citadelle - tour de garde ouest")
        print("")
        Sentence("Sortant de votre concentration, vous prenez un instant pour observer Ginn ")
        Sentence("se battre tout en ordonnant aux soldats proche de se mettre en formation pour couvrir vos arrières. ")
        sleep(1.5)
        Sentence("Son père avait de quoi être fier.")
        sleep(1.5)
        print("")
        Sentence("Quoique issu d'une liaison bâtarde, ce jeune montrait des talents évidents et était promis à une belle carrière.")
        Sentence("C'est pour lui et sa génération qu'il s'était lancé dans cette guerre. ")
        sleep(1.5)
        print("")
        Sentence("Au millieu du fracas des armes, vous prenez le temps de glisser une pensée pour votre fils, " + Prince_stats[0] + ",")
        Sentence("vieux de quelques jours à peine. ")
        Sentence("Tout ce que vous espérez dans l'instant est de pouvoir être aussi fier de votre enfant que Zaz du sien... ")
        sleep(1.5)
        Sentence("C'est en gagnant cette guerre que vous serez en mesure de lui offrir un avenir glorieux.")
        skip_touch()
        print("Champ de bataille de la citadelle - tour de garde ouest")
        print("")
        demo_deva_combat.play(-1)
        Sentence("Un hurlement morbide vous tira de votre rêverie, un autre chef de cotterie essaye de vous prendre de flanc.")
        Sentence("Ginn et son escouade ne l'avaient pas vu vous approcher.")
        Sentence("Il à l'air bien plus puissant que son confrère. Mais vous êtes bien plus rapide.")
        sleep(2.0)
        os.system("cls")
        demofight(cotteriepui_stats)
        demo_deva_combat.fadeout(1500)
        sleep(1.5)
        if qeast == False:
            os.system("cls")
            print("Champ de bataille de la citadelle - tour de garde ouest")
            print("")
            gates_music.play(-1)
            print("")
            print(Roi_demon_stats[0])
            Sentence("Ginn! Le sceptre est planté, partons nous occuper du second")
            sleep(1.5)
            print("")
            print("Ou souhaitez-vous aller ?")
            print("1. Portes de la citadelle")
            print("2. Champ abandonné (est)")
            direction = str(input("=> "))
            while direction != "1" or direction != "2":
                if direction == "1":
                    qwest = True
                    assautportes(qdone, qwest, qeast, anchor)
                    return qwest
                elif direction == "2":
                    Sentence("On part pour l'emplacement est !")
                    print()
                    Sentence("Après vous être assuré par un échange de regard que votre second ait bien entendu les ordres,")
                    Sentence("Vous prenez la direction du second emplacement. ")
                    qwest = True
                    skip_touch()
                    qassautportesest(qdone, qwest, qeast, anchor)
                    return qwest
                if direction != "1" or direction != "2":
                    Sentence("Impossible d'aller autre part.")
                direction = str(input())

        if qeast == True:
            os.system("cls")
            print("Quête terminée: L'assaut")
            questdonesound.play()
            sleep(2.0)
            os.system("cls")
            print("Champ de bataille de la citadelle - tour de garde ouest")
            print("")
            combat_music_2.play()
            print("")
            print(Roi_demon_stats[0])
            Sentence("Ginn! Le sceptre est planté, on y va !")
            Sentence("On à une porte à détruire et une bataille à remporter !")
            skip_touch()
            qdone = True
            assautportes(qdone, qwest, qeast, anchor)
            return qdone


#Si assautportesest() pas déjà fait, passer à assautportesest(). Si déjà fait, passer à assautportes()


def assautportes(qdone, qwest, qeast, anchor):
    from intro import Sentence
    if qdone == False:
        os.system("cls")
        print("Champ de bataille de la citadelle - portes de la citadelle")
        print("")
        Sentence("*Je ne peux rien faire tant que les deux sceptres ne sont pas plantés*")
        skip_touch()
        print("Champ de bataille de la citadelle - portes de la citadelle")
        print("")
        print("""Ou souhaitez vous aller  ?

1. Champ abandonné (est)
2. Vieille tour de garde (ouest)

           """)
        direction = str(input("=> "))
        while direction != "1" or direction != "2":
            if direction == "1":
                qassautportesest(qdone, qwest, qeast, anchor)
                return
            elif direction == "2":
                assautportesouest(qdone, qwest, qeast, anchor)
                return
            if direction != "1" or direction != "2":
                Sentence("Impossible d'aller autre part.")
            direction = str(input())
    elif qdone == True:
        os.system("cls")
        print("Champ de bataille de la citadelle - portes de la citadelle")
        print("")
        # Sentence("")
        Sentence("C'est le moment ou jamais. ")
        Sentence("Il ne sera pas écrit dans les Sombres Grimoires que le S'rhaal aura mené son peuple à la défaite.")
        sleep(1.5)
        print("")
        Sentence("Le combat à la tour de garde vous a épuisé, reprenez des forces et equipez vous.")
        Sentence("*Les prochains adversaires risquent d'être coriaces,")
        Sentence(" vous feriez bien de vous équiper de votre épée avant d'attaquer la porte.")
        sleep(1.5)
        combat_music_2.fadeout(1000)
        battle_sound_effect.fadeout(1000)
        anchor = 2
        skip_touch()
        SaveAnchor2(qdone, qwest, qeast, anchor)
        return


def SaveAnchor2(qdone, qwest, qeast, anchor):
    from roi_demon_inv import menu_roi
    from intro import Sentence
    Paladin_démotivé = ["Paladin démotivé", 20, 25, 15, 1.2, 150, 85, 5]
    Paladin_bléssé = ["Paladin blessé", 25, 35, 15, 1.2, 100, 85, 5]
    Ulric = ["Ulric Luminis", 50, 60, 17, 1.2, 550, 75, 5]
    from intro import SentenceSlow
    from combat import demofight
    from combat import bossfightulric
    from roi_demon_inv import Roi_demon_stats

    anchor = 2
    menu_roi(anchor)
    combat_music_2.play(-1)
    battle_sound_effect.play(-1)
    os.system("cls")
    print("Champ de bataille de la citadelle - portes de la citadelle")
    print("")
    sleep(1.5)
    print("")
    scepter_sound.play()
    incantation.play()
    # wind_thunder_sound.play()
    Sentence("Vous plantez votre lourde lame noyée de sang humain et angélique dans le sol de marbre de l'entrée de la forteresse.")
    Sentence("Faisant fi des projectiles et du chaos,")
    Sentence("vous vous lancez en puisant dans l'énergie des sceptres de pouvoir dans une terrible incantation,")
    Sentence("dans une langue noire, gutturale, oubliée même des votres.")
    sleep(1.5)
    print("")
    Sentence("Le sol se fissura jusqu'aux grandes portes d'or, le ciel s'assombrissant,")
    Sentence("les nuages noirs tournoyant au dessus du dernier rempart des hommes comme les charognards au dessus du champ de bataille,")
    Sentence("dans l'attente du charnier.")
    skip_touch()
    print("Champ de bataille de la citadelle - portes de la citadelle")
    print("")
    explosion.play()
    incantation.fadeout(1500)
    Sentence("Dans un grondement terrible, emplissant d'espoir le coeur de vos infâmes suivants et d'horreur celui des hommes,")
    Sentence("une lumière violacée perça la couche de nuages, et dans un fracas épouvantable, plusieurs énormes rochers noirs,")
    Sentence("nimbés de flammes noirâtres impies, s'abattirent sur la forteresse, s'écrasant sur la batisse millénaire,")
    Sentence("l'éperonnant en plusieurs endroits, faisant trembler le sol.")
    print("")
    Sentence("Dans les décombres de la porte laissée béante sous l'impact,")
    Sentence("les sombres et immenses silhouettes des élémentaires ainsi convoqués se redressèrent entamant de déblayer le chemin.")
    skip_touch()
    print("Champ de bataille de la citadelle - portes du Bastion Doré")
    print("")
    Sentence("Levant votre arme, vous lancez une nouvelle série d'ordre et appella à vous votre garde personnelle, menée par Zazranoth.")
    Sentence("Accompagné d'un geste du bras pointant vers la porte détruite, ")
    Sentence("vous prenez une grande inspiration, et criez de toutes vos forces.")
    print("")
    king_scream.play()
    war_horn.play()
    print("")
    SentenceSlow("CHARGEZ !")
    print("")
    sleep(1.0)
    Sentence("Le reste de votre armée en position chargea vers la citadelle, motivé par ce retournement de situation.")
    Sentence("Il était important de profiter de l'impact, qui avait tué ou mis en fuite la plupart des défenseurs,")
    Sentence("quand les derniers n'étaient pâs déjà aux prises avec les élémentaires ou d'autres combattants.")
    skip_touch()
    print("Bastion Doré - rues de la citadelle")
    print("")
    Sentence("Poussant plus loin, dans le bâtiment en forme de nef, ")
    Sentence("ne vous arrêtant pas pour admirer le somptueux décor en pleine destruction, ")
    Sentence("vous laissant guider par la logique instinctive de l'architecture humaine pour atteindre le coeur de la forteresse.")
    Sentence("Sur votre chemin se dressèrent des paladins, rescapés de l'impact du sort,")
    Sentence("qui crurent bon de se jeter en travers de votre chemin, sur leurs jambes mal assurées encore tremblantes.")
    sleep(1.5)
    print("")
    Sentence("Le plus grand n'avait pas de casque, son armure était plus imposante que les autres,")
    Sentence("un autre chef de cotterie.")
    skip_touch()
    print("Bastion Doré - rues de la citadelle")
    print("")
    print("Ulric Luminis")
    Sentence("C'est assez démon ! Ton avancée s'arrête avec moi.")
    Sentence("Tu as tué suffisement des nôtres !")
    Sentence("Moi, Ulric Luminis, vous exterminerai tous au nom de la lum..")
    combat_music_2.fadeout(1000)
    print("")
    demo_deva_combat.play(-1)
    Sentence("A peine eut-il le temps de finir sa phrase que l'un des paladins se jeta sur vous de toutes ses forces,")
    Sentence("Appelant en lui le peu de lumière qu'il restait.")
    skip_touch()
    demofight(Paladin_démotivé)
    os.system("cls")
    print("Bastion Doré - rues de la citadelle")
    print("")
    print("Ulric Luminis")
    Sentence("Non !")
    print("")
    Sentence("Le second paladin, dans un geste déséspéré,")
    Sentence("fait comme son ami et court vers vous en boîtant et hurlant à la lumière, sous le regard tétanisé du chef de cotterie.")
    sleep(1.5)
    demofight(Paladin_bléssé)
    demo_deva_combat.fadeout(1000)
    sleep(1.0)
    ulric_theme.play(-1)
    os.system("cls")
    print("Bastion Doré - rues de la citadelle")
    print("")
    Sentence("Alors que vous retirez le corps du paladin de votre épée,")
    Sentence("vous voyez Ulric enfiler son casque en récitant des psaumes.")
    SentenceSlow("...")
    sleep(1.5)
    Sentence("Il tend son gigantesque marteau enchanté vers vous,")
    Sentence("Les yeux baignés de lumière.")
    sleep(1.5)
    os.system("cls")
    bossfightulric(Ulric)
    print("Bastion Doré - rues de la citadelle")
    print("")
    ulric_theme.fadeout(1000)
    sleep(1.0)
    citadel_walk.play(-1)
    Sentence("Le chef de cotterie gisait au sol, mourant.")
    sleep(1.5)
    Sentence("Vous apercevez des larmes de déception et de frustration couler sous son casque boursouflé.")
    sleep(1.5)
    Sentence("Il était un fier combattant, puissant pour son jeune âge...")
    sleep(1.5)
    Sentence("Il vous rappelle le jeune Ginn.")
    skip_touch()
    print("Bastion Doré - rues de la citadelle")
    print("")
    Sentence("Vous le fixez, au sol...")
    print("Que faites vous ?")
    print("1. l'achever")
    print("2. L'épargner")
    choix = str(input("=>"))
    while choix != "1" or choix != "2":
        if choix == "1":
            os.system("cls")
            print("Bastion Doré - rues de la citadelle")
            print("")
            Sentence("Vous soulevez votre épée et vous la plantez dans le corps du dévot.")
            sleep(1.5)
            Sentence("Vous voyez la lumière s'échapper de son corps pour se disperser lentement dans les cieux,")
            Sentence("rendant l'atmosphère plus respirable et impie.")
            sleep(1.5)
            Sentence("Une fois ces géneurs désespérés écartés, vous et votre garde reprirent votre route.")
            skip_touch()
            break
        elif choix == "2":
            os.system("cls")
            print("Bastion Doré - rues de la citadelle")
            print("")
            Sentence("Une pensée traverse votre esprit...")
            print("")
            Sentence("*Ce devot est brave, ce serait du gâchis de le tuer maintenant.")
            Sentence("Détruisons son monde et voyons dans quelle direction il évoluera.")
            Sentence("Peut être fera t-il un bon adversaire pour mon fils...*")
            sleep(1.5)
            Sentence("Une fois ces géneurs désespérés écartés, vous et votre garde reprirent votre route.")
            skip_touch()
            break
        if choix != "1" or choix != "2":
            Sentence("*Je dois faire un choix*")
        choix = str(input())
    battle_sound_effect.fadeout(1000)
    print("Bastion Doré - Batisse Royale (hall)")
    print("")
    Sentence("En passant devant un hall, Zazranoth arrêta votre escouade pour vous faire observer d'étrange dispositifs,")
    sleep(1.5)
    print("")
    print("Zazranoth")
    Sentence("Regardez ça là bas.")
    print("")
    Sentence("D'espèces d'immenses harnais, cages, et ce qui ressemblait à du matériel de geolier.")
    Sentence("A la différence près que tout ce attirail, imposant, ")
    Sentence("avait une taille suffisante pour restreindre les mouvements d'une créature massive,")
    Sentence("au moins grosse comme une hydre, voire plus pour certaines pièces.")
    skip_touch()
    print("Bastion Doré - Batisse Royale (hall)")
    print("")
    Sentence("Ginn pris la parole d'un ton consterné pour exprimer ce que toute la petite escouade ressentait devant ce spectacle.")
    sleep(1.5)
    print("")
    print("Ginn")
    Sentence("Ca a l'air vrai quand on à ça sous les yeux... Ils veulent vraiment s'en prendre à des dragons... ")
    Sentence("Soit pour leur pouvoir soit pour autre chose... ")
    sleep(1.0)
    print("")
    Sentence("D'un claquement de doigt, vous rappellez la petite troupe à l'ordre...")
    sleep(1.5)
    print("")
    print(Roi_demon_stats[0])
    Sentence("Nous nous approchons de la salle du trône, je vous conseille de vous préparer maintenant.")
    print("")
    Sentence("vous suivez vous même votre conseil.")
    citadel_walk.fadeout(1000)
    anchor = 3
    skip_touch()
    SaveAnchor3(qdone, qwest, qeast, anchor)
    return

def SaveAnchor3(qdone, qwest, qeast, anchor):
    prince = ["Le Prince en Blanc", 65, 75, 17, 1.2, 999, 90, 10]
    from combat import bossfightking
    from intro import Sentence
    from intro import SentenceSlow
    from roi_demon_inv import menu_roi
    anchor = 3
    menu_roi(anchor)
    Sentence("")
    Sentence("Vous vous assurez que tout le monde soit prêt et vous annoncez le départ.")
    sleep(1.5)
    Sentence("Le groupe de démons armés jusqu'aux dents reprit alors sa route en silence, l'esprit troublé par ce spectacle.")
    skip_touch()
    citadel_walk.fadeout(1000)
    sleep(1.0)
    throne_theme.play(-1)
    print("Bastion Doré - Batisse Royale (salle du trône)")
    print("")
    Sentence("Vous finissez enfin par arriver au centre de la place forte, au coeur du pouvoir des humains. ")
    sleep(1.5)
    Sentence("La grande porte de la salle du trône déjà éventrée,")
    Sentence("avec parmi les décombres un nombre de cadavres humains trop grand pour avoir été le fait de la bataille...")
    skip_touch()
    print("Bastion Doré - Batisse Royale (salle du trône)")
    print("")
    Sentence("Des cadavres disposés en ordre précis si l'on excepte la chutes de la maçonnerie.")
    Sentence("Vous aperçevez le roi, gisant au sol.")
    sleep(1.5)
    print("")
    Sentence("Ginn s'approcha de l'un d'eux et le tâta du bout de la botte.")
    print("")
    print("Ginn")
    Sentence("Mort,")
    Sentence("mais aucune trace de blessure. Y'a comme un truc biza...")
    sleep(0.5)
    light_beam.play()
    sleep(2.0)
    print("")
    Sentence("Sa phrase resta en suspens, pendant qu'il observait la longue lance de lumière lui ayant traversé le torse.")
    sleep(1.5)
    Sentence("La bouche ouverte, l'aide de camp leva les yeux vers vous, le regard empli de surprise.")
    sleep(1.5)
    Sentence("Et au moment ou son corps heurta la sol, une lumière blanche éclatante se fit dans la salle du trône dévastée.")
    skip_touch()
    print("Bastion Doré - Batisse Royale (salle du trône)")
    print("")
    Sentence("Devant le trône se tenait un très jeune homme, à peine sorti de l'enfance. ")
    sleep(1.5)
    print("")
    Sentence("A première vue il semblait humain, mais en y regardant de plus près, ")
    Sentence("sa peau d'albâtre avait des reflets métalliques, et sa chevelure d'or flottait comme au vent,")
    Sentence("alors qu'il n'y avait pas une brise dans la bâtisse enfoncée. ")
    sleep(1.5)
    print("")
    Sentence("Ses yeux semblables à des miroirs d'argent poli n'exprimaient rien.")
    Sentence("Levant une main qui tenait l'épée reconnaissable de la famille royale des humains, ")
    Sentence("le jeune homme déploya trois paires d'ailes enflammées et dit avec un ton posé, d'une voix venant d'un autre monde.")
    skip_touch()
    throne_theme.fadeout(1000)
    sleep(1.0)
    final_boss_theme.play(-1)
    print("Bastion Doré - Batisse Royale (salle du trône)")
    print("")
    print("Le Prince en Blanc (Prince héritier Zoltàn)")
    Sentence("'Vos exactions s'arrêtent ici.'")
    Sentence("'Nul ne mettra en péril l'avenir de l'humanité.'")
    sleep(1.0)
    print("")
    light_spell_dialogue.play()
    Sentence("D'un geste de la main, il projetta des vagues de lumière qui réduisirent en poussière la quasi-totalité de votre escouade.")
    Sentence("Conscient de faire face à une menace inconnue, vous échangez un regard avec votre général.")
    SentenceSlow("...")
    Sentence("Quoi qu'il arrive, tout était prévu.")
    skip_touch()

    bossfightking(prince)

    final_boss_theme.fadeout(1000)
    sleep(1.0)
    throne_theme.play(-1)
    print("Bastion Doré - Batisse Royale (salle du trône)")
    print("")
    Sentence("Terrassé par la puissance de cet être inconnu,")
    Sentence("malgré votre force maudite jusque là inégalée et vos incantations les plus secrètes, ")
    Sentence("vous vous rendez rapidement à l'évidence,")
    Sentence("vous est vaincu.")
    sleep(1.5)
    print("")
    Sentence("Après une petite pensée pour votre fils nouveau-né, et un regard au corps de Ginn, ")
    Sentence("vous aggripez votre lame, et dans un dernier effort,")
    Sentence("mortellement blessé et couvert de honte d'abandonner les siens ainsi que leur rêve de gloire et de grandeur,")
    Sentence("vous lancez votre sort de téléportation...")
    teleport_sound_effect.play()
    throne_theme.fadeout(1000)
    skip_touch()
    sleep(1.0)
    print("")
    Sentence("Jusque des siècles plus tard, les hommes se rappellent cet évènement comme la Bataille de la Couronne, ")
    Sentence("ou pour défaire le puissant Roi-dieu des démons,")
    Sentence("ils ont du procéder à un terrible sacrifice mené par le Roi lui-même afin de bénir son fils héritier,")
    Sentence("Zoltàn, de la présence d'un ange véritable.")
    sleep(1.5)
    Sentence("Depuis ce jours, celui que l'on nomme Le Prince en Blanc veille sur le destin des hommes,")
    Sentence("alors que les démons,")
    Sentence("eux,")
    Sentence("ne sont plus...")
    skip_touch()
    from outro import outro
    outro()
    return

