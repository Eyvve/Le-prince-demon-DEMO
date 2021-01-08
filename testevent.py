from combat import *
from intro import Sentence
from time import sleep
import pygame
pygame.init()
combat_music = pygame.mixer.Sound("field_fight.ogg")


def event():
    Sentence("Vous arrivez dans un champ, vous voyez du blé à perte de vue ")
    Sentence("Vous distinguez une silhouette au loin, c'est un humain qui laboure sa terre...")
    sleep(1.0)
    print("1. Parler")
    print("2. Attaquer")
    print("3. ignorer et partir")
    a = str(input())
    if a == "1":
        Sentence("Vous vous approchez de lui...")
        Sentence("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc venenatis efficitur quam ut convallis.")
    elif a == "2":
        Sentence("Vous vous approchez de lui...")
        combat(Prince_stats, Mob_stats)
    elif a == "3":
        Sentence("Vous vous cachez tout en essayant de partir de son terrain")


#event()