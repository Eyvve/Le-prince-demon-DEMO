from time import sleep
from maps import skip_touch
from Music_sounds import *
from roi_demon_inv import *
from combat import *
from intro import *


def demo():
    from intro import Sentence
    from combat import demofight
    # cotterie_stats = ["Chef de Cotterie", 45, 55, 20, 1.2, 350, 85, 5]
    # demofight(cotterie_stats)
    # signif1ications : nom, attaque mini, attaque max, défense, multiplicateur de dégat (arme), vie, précision, esquive
    deva_stats = ["Deva", 30, 40, 15, 1.2, 250, 85, 5]
    cotterie_stats = ["Chef de Cotterie", 45, 55, 20, 1.2, 350, 85, 5]
    Sentence("Conformement au lore établi, le Roi démon ou Dieu-Roi porte le nom d'Ibliss Nizidramanii'yt.")
    print("")
    Sentence("Quel est votre nom ? Si vous souhaitez le nom lore friendly, appuyez simplement sur Entrée.")
    kingsName = str(input("=> "))
    if kingsName == "":
        Roi_demon_stats[0] = "Ibliss"
    else:
        Roi_demon_stats[0] = kingsName
    validation_sound.play()
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
    Sentence("Les cieux étaient aussi rougeatres que le sol devant la citadelle dorée des hommes.")
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
    Sentence("Alors que vous veniez à peine de tuer le deva, le chef de cotterie tente de vous porter un coup épee.")
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
    sleep(2.0)
    os.system("cls")

    menu_roi()

    os.system("cls")
    print("Champ de bataille de la citadelle - coeur de la bataille")
    print("")
    gates_music.play(-1)
    Sentence("Vous vous relevez et regardez à vos pieds.")
    sleep(1.5)
    Sentence("Dominant de toute votre hauteur le cadavre de ses ennemis, vous entendez un cri d'alerte puissant et familier.")
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
    Sentence("ou sonner la retraite et tenter de sauver un maximum des notres.")
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
            qassautportes()
            return
        elif rep == "2":
            Retraite()
            return
        if rep != "1" or rep != "2":
            Sentence("Malheureusement, il n'y à pas d'autres options mon seigneur.")
        rep = str(input())


#    - choix a faire:
#       attaquer les portes
#       fuir


def Retraite():
    Sentence("Laissant son regard planer sur le  désastre de ce champ de bataille, la résolution du Roi-dieu flanche.")
    Sentence("A quoi bon changer l'ordre des choses et instaurer un ordre nouveau pour les nouvelles générations si presque")
    Sentence("tout son peuple doit périr dans la tentative ? Les mots de l'arcaniste Seraphos lui revinrent en tête.")
    Sentence("'Quand tu lèveras ton épée contre le bastion des mortels, tu feras trembler une civilisation'.")
    Sentence("Ce maudit corbeau de mauvais augure pouvait bien là prédire la chute de son peuple! Et il ne sera pas relaté")
    Sentence("dans les Sombres Grimoires que lui, Nizidramanii'yt le Roi-Dieu, aurait causé la ruine des siens !")
    Sentence("Quoi qu'il en coûte et peu importe la honte, survivre est l'essentiel. L'ennemi est beaucoup trop nombreux,")
    Sentence("soutenu par des  créatures inconnues, béni d'une magie imprévue. Les humains, créatures certes éphémères,")
    Sentence("se relèveraient bien mieux que son peuple d'une guerre de cette ampleur, étant bien plus nombreux et bien")
    Sentence("plus fertiles... Devant la réalité imposée par l'étude des faits, et la mort dans la l'âme, ne pouvant se")
    Sentence("à donner l'ordre lui-même, le Roi-dieu répondit à voix basse, comme brisée :'Zaz... Sonne la retraite.")
    Sentence("Je ne serais pas l'instigateur de la destruction des nôtres... Ils sont plus redoutables que ce qu'il semblait.'")
    Sentence("L'ordre fut donné, relayé, sonné. La retraite, à deux doigts de se transformer en fuite ou en débandade, se fit.")
    Sentence("Aucun contact ne fut jamais pris avec les humains qui se contentèrent des de bouter les démons dans les montagnes")
    Sentence("d'Aurgelmirtann, au nord de Ljosalfer.")

    # petit écran de fin de démo

    Sentence("Jusque des siècles plus tard, les hommes se rappellent cet évènement comme la Bataille de la Couronne, ou grâce")
    Sentence("à une alliance avec des créatures célestes, les humains ont repoussé les démons. Ces derniers finirent sous le joug")
    Sentence("des premiers, le peu d'entre eux encore libres se terrant dans les montagnes. A ce jour, nul ne sait comment les")
    Sentence("humains ont obtenu l'aide des anges, mais depuis, un certain 'Prince en Blanc', que personne ne voit jamais,")
    Sentence("semble avoir remplacé le roi précédent, et règne sur Ljosalfer d'une main juste, ferme, et désinteressée.")

def qassautportes():
    questdone = False
    qeastdone = False
    qwestdone = False
    from intro import Sentence
    from combat import demofight
    os.system("cls")
    print("Champ de bataille de la citadelle - coeur de la bataille")
    print("")
    sleep(2.0)
    print(Roi_demon_stats[0])
    Sentence("Nous ne fuirons pas, il est hors de question d'abandonner, je ne suis pas encore mort...")
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
            qassautportesest(questdone, qeastdone, qwestdone)
            return
        elif direction == "2":
            assautportesouest(questdone, qeastdone, qwestdone)
            return
        elif direction == "3":
            assautportes(questdone, qeastdone, qwestdone)
            return
        if direction != "1" or direction != "2" or direction != "3":
            Sentence("Impossible d'aller autre part.")
        direction = str(input())


#      - Choix à faire, aller planter l'un des sceptres sceptre à gauche ou a droite.

def qassautportesest(qdone, qwest, qeast):
    from intro import Sentence
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
        assautportes(qdone, qwest, qeast)
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
        menu_roi_sceptre()
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
            assautportes(qdone, qwest, qeast)
            return qdone
        elif qwest == False:
            sleep(1.5)
            os.system("cls")
            print("Champ de bataille de la citadelle - champs est")
            print("")
            print(Roi_demon_stats[0])
            Sentence("Le premier sceptre est en place ! On bouge, et repousse moi ces vermisseaux !")
            Sentence("On part pour l'emplacement ouest !")
            print()
            Sentence("Après vous être assuré par un échange de regard que votre second ait bien entendu les ordres,")
            Sentence("Vous prenez la direction du second emplacement. ")
            qeast = True
            assautportesouest(qdone, qwest, qeast)
            return qeast


# Si assautportesouest() pas déjà fait, passer à assautportesest(). Si déjà fait, passer à assautportes()
    Sentence("'Le premier sceptre est en place ! On bouge, et repousse moi ces vermisseaux!' Assuré par un échange de regard")
    Sentence("que son second a bien entendu les ordres et se met en marche.")

def assautportesouest(qdone, qwest, qeast):
    from intro import Sentence
    from combat import Prince_stats
    from combat import demofight
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
        assautportes(qdone, qwest, qeast)
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
            Sentence("Ginn! Le sceptre est planté, on part nous occuper le second")
            qwest = True
            qassautportesest(qdone, qwest, qeast)
            return qwest
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
            assautportes(qdone, qwest, qeast)
            return qdone


#Si assautportesest() pas déjà fait, passer à assautportesest(). Si déjà fait, passer à assautportes()


def assautportes(qdone, qwest, qeast):
    Paladin_démotivé = ["Paladin démotivé", 20, 25, 15, 1.2, 150, 85, 5]
    Paladin_bléssé = ["Paladin démotivé", 25, 35, 15, 1.2, 100, 85, 5]
    Ulric = ["Ulric Luminis", 55, 65, 20, 1.2, 550, 75, 5]
    from intro import Sentence
    from intro import SentenceSlow
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
                qassautportesest(qdone, qwest, qeast)
                return
            elif direction == "2":
                assautportesouest(qdone, qwest, qeast)
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
        menu_roi()
        os.system("cls")
        print("Champ de bataille de la citadelle - portes de la citadelle")
        print("")
        sleep(1.5)
        print("")
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
        Sentence("Dans un grondement terrible, emplissant d'espoir le coeur de ses infâmes suivants et d'horreur celui des hommes,")
        Sentence("une lumière violacée perça la couche de nuages, et dans un fracas épouvantable, plusieurs énormes rochers noirs,")
        Sentence("nimbés de flammes noirâtres impies, s'abattirent sur la forteresse, s'écrasant sur la batisse millénaire, l'éperonnant")
        Sentence("en plusieurs endroits, faisant trembler le sol.")
        print("")
        Sentence("Dans les décombres de la porte laissée béante sous l'impact,")
        Sentence("les sombres et immenses silhouettes des élémentaires ainsi convoqués se redressèrent entamant de déblayer le chemin.")
        skip_touch()
        print("Champ de bataille de la citadelle - portes de la citadelle")
        print("")
        Sentence("Levant votre arme, vous lancez une nouvelle série d'ordre et appella à vous votre garde personnelle, menée par Zazranoth.")
        Sentence("Accompagné d'un geste du bras pointant vers la porte détruite, vous prenez une grande respiration, et criez de toutes vos forces.")
        print(Roi_demon_stats[0])
        king_scream.play()
        war_horn.play()
        SentenceSlow("CHARGEZ")
        sleep(1.0)
        Sentence("Le reste de votre armée en position chargea vers la citadelle, motivée par ce retournement de situation.")
        Sentence("Il était important de profiter de l'impact, qui avait tué ou mis en fuite la plupart des défenseurs,")
        Sentence("quand les derniers n'étaient pâs déjà aux prises avec les élémentaires ou d'autres combattants.")
        skip_touch()
        print("Champ de bataille de la citadelle - rues de la citadelle")
        print("")
        Sentence("Poussant plus loin, dans le bâtiment en forme de nef, ")
        Sentence("ne vous arrêtant pas pour admirer le somptueux décor en pleine destruction, ")
        Sentence("vous laissant guider par la logique instinctive de l'architecture humaine pour atteindre le coeur de la forteresse.")
        Sentence("Sur votre chemin se dressèrent des paladins, rescapés de l'impact du sort,")
        Sentence("qui crurent bon de se jeter en travers de votre chemin, sur leurs jambes mal assurées encore tremblantes.")
        sleep(1.5)
        print("")
        Sentence("Le plus grand n'avait pas de casque, son armure était plus imposante que les autres,")
        skip_touch("un autre chef de cotterie.")
        skip_touch()
        print("Champ de bataille de la citadelle - rues de la citadelle")
        print("")
        print("Ulric Luminis")
        Sentence("C'est assez démon ! Ton avancée s'arrête avec moi.")
        Sentence("Tu as tué suffisement des notres !")
        Sentence("Moi, Ulric Luminis, vous exterminerai tous au nom de la lum..")
        combat_music_2.fadeout(1000)
        print("")
        demo_deva_combat.play(-1)
        Sentence("A peine eu il le temps de finir sa phrase que l'un des paladins se jeta sur vous de toutes ses forces,")
        Sentence("Appelant en lui le peu de lumière qu'il restait.")
        skip_touch()
        demofight(Paladin_démotivé)
        os.system("cls")
        print("Champ de bataille de la citadelle - rues de la citadelle")
        print("")
        print("Ulric Luminis")
        Sentence("Non !")
        print("")
        Sentence("Le second paladin, dans un geste déséspéré,")
        Sentence("fit comme son ami et courra vers vous en boîtant et hurlant à la lumière, sous le regard tétanisé du chef de cotterie.")
        demofight(Paladin_bléssé)
        os.system("cls")
        print("Champ de bataille de la citadelle - rues de la citadelle")
        print("")
        Sentence("Alors que vous retirez le corps du paladin de votre épée,")
        Sentence("vous voyez Ulric enfiler son casque en récitant des psaumes.")
        Sentence("...")
        sleep(1.5)
        ulric_theme.play(-1)
        Sentence("Il tendit sa gigantesque claymore enchantée vers vous,")
        Sentence("Les yeux baignés de lumière.")
        os.system("cls")
        # bossfightulric(Ulric)




            # combat() #Combat contre des chefs de côterie. top 1 ou 2 des ennemis humains mais nomatch pour le Roi-démon

        Sentence("Une fois ces géneurs désespérés écartés, le Roi et sa garde continuèrent leur route. En passant devant un hall")
        Sentence("Zazranoth les arrêta pour leur faire observer d'étrange dispositifs, espèces d'immenses harnais, cages, et ce")
        Sentence("qui ressemblait à du matériel de geolier. A la différence près que tout ce attirail avait une taille suffisante")
        Sentence("pour restreindre les mouvements d'une créature au moins grosse comme une hydre, voire plus pour certaines pièces")
        Sentence("Ginn pris la parole d'un ton consterné pour exprimer ce que toute la petite escouade ressentait devant ce spectacle")
        Sentence("Ca a l'air vrai quand on à ça sous les yeux... Ils veulent vraiment s'en prendre a des dragons. Soit pour leur")
        Sentence("pouvoir soit pour autre chose... D'un claquement de doigt, Zazranoth rappelle la petite troupe à l'ordre, et")
        Sentence("le groupe de démons armés jusqu'aux dents reprit sa route en silence, l'esprit troublé par ce spectacle.")
        skip_touch()

              #Moment d'inventaire ou le roi récupère un de ces objets pour l'étudier plus tard

        Sentence("Ils finirent par arriver au centre de la place forte, au coeur du pouvoir des humains. La grande porte de la")
        Sentence("salle du trône déjà éventrée, avec parmi les décombres un nombre de cadavres humains trop grand pour avoir")
        Sentence("été le fait de bataille. Des cadavres disposés en ordre précis si l'on excepte la chutes des la maçonnerie")
        Sentence("Ginn s'approcha de l'un d'eux et le tâta du bout de la botte. Mort, mais pas trace de blessure. Tous.")
        Sentence("Y'a comme un truc bizarre.... Sa phrase resta en suspens, pendant qu'il observait une longue lance de lumière")
        Sentence("fichée dans son torse. La bouche ouverte, l'aide de camp leva les yeux vers son roi, le regard empli de surprise.")
        skip_touch()
        Sentence("Au moment ou son corps heurta la sol, une lumière blanche éclatante se fit dans la salle du trône dévastée.")
        skip_touch()
        Sentence("Devant le trône se tenait un très jeune homme, à peine sorti de l'enfance. A première vue il semblait humain,")
        Sentence("mais en y regardant de plus près, sa peau d'albâtre avait des reflets métalliques, et sa chevelure d'or flottait")
        Sentence("comme au vent, alors qu'il n'y avait pas une brise dans la bâtisse enfoncée. Ses yeux semblables à des miroirs")
        Sentence("d'argent poli n'exprimaient rien. Levant une main qui tenait l'épée reconnaissable de la famille royale des humains")
        Sentence("le jeune homme déploya trois paires d'ailes enflammées et dit avec un ton posé, d'une voix venant d'un autre monde.")
        skip_touch()
        Sentence("'Vos exactions s'arrêtent ici. Nul ne mettra en péril l'avenir de de l'humanité.' D'un geste de la main, il projetta")
        Sentence("des vagues de lumière qui réduisirent en poussière la quasi-totalité de la garde du S'rhaal. Ce derier, conscient")
        Sentence("de faire face à une menace inconnue, échangea un regard avec son général. Quoi qu'il arrive, tout était prévu.")
        skip_touch()

              #combat contre le roi des humains (dans lequel est catalysé le pouvoir d'un ange majeur. le Roi-Dieu perd.)

        Sentence("Terrassé par la puissance de cet être inconnu, malgré sa force maudite jusque là inégalée et ses incantations")
        Sentence("les plus secrètes, le Roi-Dieu se rend rapidement à l'évidence, il est vaincu. Après une petite pensée pour son")
        Sentence("fils nouveau-né, et un regard au corps du fils de son ami, raisons pour laquelle il a voulu changer ce monde,")
        Sentence("il aggrippe sa lame, et dans un dernier effort,mortellement blessé et couvert de honte d'abandonner ainsi")
        Sentence(" les siens ainsi que leur rêve de liberté et de grangeur, et lança son sort de téléportation")
        skip_touch()

              #petit écran de fin de démo

        Sentence("Jusque des siècles plus tard, les hommes se rappellent cet évènement comme la Bataille de la Couronne, ou pour")
        Sentence("défaire le puissant Roi-dieu des démons, ils ont du procéder à un terrible sacrifice mené par le Roi lui-même")
        Sentence("afin de bénir son fils héritier de la présence d'un ange véritable. Depuis ces jours, celui que l'on nomme ")
        Sentence("'Le Prince en Blanc', veille sur le destin des hommes, alors que les démons eux, ne sont plus.")

