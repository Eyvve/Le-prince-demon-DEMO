from time import sleep
from maps import skip_touch
from Music_sounds import *
from roi_demon_inv import *
from combat import *
from intro import *

def demo():
    from intro import Sentence
    from combat import demofight
    # signif1ications : nom, attaque mini, attaque max, défense, multiplicateur de dégat (arme), vie, précision, esquive
    deva_stats = ["Deva", 30, 40, 15, 1.2, 250, 85, 5]
    cotterie_stats = ["Chef de Cotterie", 45, 55, 25, 1.2, 350, 85, 5]
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
    print("")
    print("")
    Sentence("La bataille faisait rage.")
    sleep(1.5)
    Sentence("Les cieux étaient aussi rougeatres que le sol devant la citadelle dorée des hommes.")
    sleep(1.5)
    Sentence("Les corps, de différentes formes et couleurs, jonchaient le sol.")
    sleep(1.5)
    Sentence("Dans le flou du combat, impossible pour vous, le Dieu-roi S'rhaal, de faire le point sur la situation.")
    skip_touch()
    Sentence("Vous débarrassant de votre opposant d'un lourd coup de lame,")
    Sentence("fendant du même mouvement la lourde armure et le corps du paladin, avant de lancer un long cri de ralliement.")
    sleep(1.5)
    Sentence("La situation des forces en présence est désastreuse.")
    skip_touch()
    Sentence("Les brutes ont bien encaissé la mêlée,")
    Sentence("mais tous vos suivants plus fragiles se sont fait découper par l'acier chantant des créatures célestes...")
    sleep(1.5)
    Sentence("Avant de pouvoir lancer une série d'ordres, deux silhouettes d'or et de sang se dressent devant vous. ")
    Sentence("A vue d'oeil, un chef de cotterie et un déva.")

    skip_touch()
    narration_intro_music.fadeout(1000)
    sleep(3.0)
    Sentence("Ils ne sont rien.")
    demo_deva_combat.play(-1)
    sleep(10.0)
    demofight(deva_stats)
    os.system("cls")
    Sentence("Alors que vous veniez à peine de tuer le deva, le chef de cotterie tente de vous porter un coup épee.")
    demofight(cotterie_stats)
    demo_deva_combat.fadeout(1000)
    sleep(1.0)
    os.system("cls")
    sleep(1.0)
    narration_intro_music.play(-1, 10.0)
    # fin des deux combats, si le joueur est pas mort il à pris un peu cher, hop sequence gameplay potion
    Sentence("Vous ressortez de ce combat blessé, vous trouvez judicieux de regagner de la santé avant de retourner au voir vos troupes.")
    Sentence("Par chance vous avez suffisemment de potions sur vous pour reprendre des forces.")

    menu_roi()

    Sentence("Dominant de toute sa hauteur le cadavre de ses ennemis, le S'rhaal entendit un cri d'alerte puissant et familier.")
    Sentence("Zazranoth, son général, et Ginn, fils du précédent et son aide de camp viennent vers lui, se mouvant dans le charnier")
    Sentence("avec difficulté, le visage de l'un grave, celui de l'autre en détresse. Mon seigneur, l'interpelle le vétéran,")
    Sentence("nous sommes en train de perdre. Ces maudits pourceaux ont obtenu l'aide de créatures de lumière inconnues.")
    skip_touch()
    Sentence("Il nous faut prendre une décision avant la débâcle complète. Deux choix s'offrent à nous, sonner la retraite")
    Sentence("ou tenter d'abattre les portes, trouver leur leader et le tuer, pour arracher la victoire.")
    skip_touch()

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
    Sentence("'Ces portes sont bardés de magie défensives, il va me falloir utiliser une puissante magie pour en venir à bout.")
    Sentence("Ginn ! Libère moi le chemin jusqu'aux charniers les plus proches. Je vais devoir planter deux sceptres de pouvoir")
    Sentence("pour en canaliser l'énergie!")
    Sentence("'Bien mon Roi!' L'aide de camp réagit au quart de tour, avec le zèle qui le caractérise. Jouant de sa masse")
    Sentence("et de son bouclier, il commence à faire le ménage sur le champ de bataille dans la direction indiquée par son")
    Sentence("supérieur.")

#      - Choix à faire, aller planter l'un des sceptres sceptre à gauche ou a droite.

def qassautportesest():
    Sentence("Précédé par son serviteur, le S'rhaal se dirige vers l'est des portes, esquivant les groupes de combattants")
    Sentence("emprunts de furie, profitant du chaos. Devant un amas de corps sans vie, humains comme démons, assurément")
    Sentence("fauchés là par l'un des sorts favoris et reconnaissable de Seraphos, le maître sorcier et général en second de")
    Sentence("son armée. Voilà que ce vieux fou allait pour une fois lui faciliter la tâche. Connectant directement les")
    Sentence("filaments encore perceptibles de magie destructrice, il les attacha à son sceptre, tissant un catalyseur avant")
    Sentence("de l'enfoncer profondément dans le sol. Surpris par le fracas du métal juste derrière lui, le Roi-Dieu se retourne,")
    Sentence("juste à temps pour voir son second repousser un assaut de plusieurs humains d'un vaste mouvment de bouclier.")

# Si assautportesouest() pas déjà fait, passer à assautportesest(). Si déjà fait, passer à assautportes()
    Sentence("'Le premier sceptre est en place ! On bouge, et repousse moi ces vermisseaux!' Assuré par un échange de regard")
    Sentence("que son second a bien entendu les ordres et se met en marche.")

def assautportesouest():
    Sentence("Naviguant entre les amoncellements de corps, hurlant parmis les cris, glissant sur les flaques de sang et les")
    Sentence("morceaux de métal, le duo arrive au point ouest des portes, ou la lumière du soleil couchant se reflétant contre")
    Sentence("les portes métalliques donnait à la scène une lumière saisissante. Sans se laisser émouvoir ou perdre de temps")
    Sentence("le Roi-Dieu se lança dans une incantation complexe, attirant les énergies macabres de l'endroit, les scellant")
    Sentence("autour du sceptre avant de le ficher profondément dans le sol, brisant un pavé au passage. Sortant de sa")
    Sentence("concentration, il prit un instant pour observer Ginn, se battant tout en ordonnant aux soldats proche de se")
    Sentence("mettre en formation pour le protéger pendant le lancement de son sort. Son père avait de quoi être fier.")
    Sentence("Quoique issu d'une liaison bâtarde, ce jeune montrait des talents évidents et était promis à une belle carrière")
    Sentence("C'est pour lui et sa génération qu'il s'était lancé dans cette guerre. Au millieu du fracas des armes, il pris")
    Sentence("le temps de glisser une pensée pour son fils, vieux de quelques jours à peine. Heureux serait-il s'il pouvait être")
    Sentence("aussi fier de son enfant que Zaz du sien. Un hurlement morbide tira le vieux démon de sa rêverie, et il en profita")
    Sentence("pour se secouer. 'Ginn! C'est bon pour toi ? On se bouge là!'")


#Si assautportesest() pas déjà fait, passer à assautportesest(). Si déjà fait, passer à assautportes()


def assautportes():
    Sentence("C'est le moment ou jamais. Il ne sera pas écrit dans les Sombres Grimoires que le S'rhaal aura mené son peuple")
    Sentence("à la défaite. Plantant sa lourde lame noyée de sang humain et angélique dans le sol de marbre de l'entrée de la")
    Sentence("forteresse. Faisant fi des projectiles et du chaos, le Dieu-Roi se lança en puisant dans l'énergie des sceptres de")
    Sentence("pouvoir dans une terrible incantation, dans une langue noire, gutturale, oubliée même des siens.")
    Sentence("Le sol se fissura jusqu'aux grandes portes d'or, le ciel s'assombrissant, les nuages noirs tournoyant au dessus du")
    Sentence("dernier rempart des hommes comme les charognards au dessus du champ de bataille, dans l'attente du charnier.")
    skip_touch()
    Sentence("Dans un grondement terrible, emplissant d'espoir le coeur de ses infâmes suivants et d'horreur celui des hommes")
    Sentence("une lumière violacée perça la couche de nuages, et dans un fracas épouvantable, plusieurs énormes rochers noirs,")
    Sentence("nimbés de flammes noirâtres impies, s'abattirent sur la forteresse, s'écrasant sur la batisse millénaire, l'éperonnant")
    Sentence("en plusieurs endroits, faisant trembler le sol. Dans les décombres de la porte laissée béante sous l'impact, les")
    Sentence("sombres et immenses silhouettes des élémentaires ainsi convoqués se redressèrent entamant de déblayer le chemin.")
    skip_touch()
    Sentence("Peu importe ce qu'il en coûtera. Levant son arme, le S'rhaal lança une nouvelle série d'ordre et appella à lui")
    Sentence("sa garde personnelle, menée par Zazranoth. Il était important de profiter de l'impact, qui avait tué ou mis")
    Sentence("en fuite la plupart des défenseurs, quand les derniers n'étaient pâs déjà aux prises avec les élémentaires ou")
    Sentence("d'autres combattants. Poussant plus loin, dans le bâtiment en forme de nef, ne s'arrêtant pas pour admirer le")
    Sentence("somptueux décor en pleine destruction, se laissant guider par sa logique connue de l'architecture humaine pour")
    Sentence("atteindre le coeur de la forteresse. Sur son chemin se dressèrent des paladins, rescapés de l'impact du sort,")
    Sentence("qui crurent bon de se jeter en travers de leur chemin, sur leurs jambes mal assurées encore tremblantes.")
    skip_touch()

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

