
 #site : http://cours.thirion.free.fr/Cours/Python-Fichiers/Python-Pickle.html#:~:text=pickle%20est%20un%20module%20de,peuvent%20être%20de%20type%20quelconque.

import pickle
from index import *
from mob import *

history = {
    'histoire' : "coucou"
}
#remplacer par la variable


def save(char, history):
    # bruitage sauvgarde
    f = open("save", "wb")
    pickle.dump(char, f)
    pickle.dump(history, f)
    f.close()



def load():
    f = open("save","rb")
    char = pickle.load(f)
    history = pickle.load(f)
    f.close()
    return(char,history)
