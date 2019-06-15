import numpy as np
from enum import Enum

class Strategie(Enum):
    CHANGER = 1
    GARDER = 2
    
def Monty_Hall(nb_de_parties = 10000):
    
    '''Simule n parties du jeu de Monty Hall
    
    Cette fonction simule n = nb_de_parties du jeu
    de Monty Hall pour chaque strategie "CHANGER" et
    "GARDER". Elle retourne les gains de chaque
    strategie
    
    args :
        nb_de_parties (int) : Nombre de parties
        de chaque strategie
        
    return : 
        np.array (2,) : Gains de chaque methodes, 
        d'abord "CHANGER" puis "GARDER"
    '''
    #Bonne porte au hasard entre 0 et 2 pour toutes les parties
    bonne_porte = np.random.randint(0, 3, nb_de_parties)

    #Premier choix au hasard entre 0 et 2 pour toutes les parties
    premier_choix = np.random.randint(0, 3, nb_de_parties)
    
    #Quand on garde, deuxieme choix = premier choix logique
    deuxieme_choix_garder = premier_choix
    
    #Quand on change maintenant
    
    #Si on avait bon, le presentateur qui elimine une porte perdante
    #revient pour le joueur a choisir une des 2 portes perdantes
    #au hasard
    situation_gagnante_perdante = (premier_choix
                                    + np.random.randint(1, 3, nb_de_parties))%3 
    
    #Si on avait faux, alors le presentateur elimine la 2e porte
    #fausse, donc en changeant on prend forcement la gagnante
    situation_perdante_gagnante = bonne_porte
    
    #Pour savoir l'action a faire il faut savoir si on avait bon
    #initialement
    table = (premier_choix == bonne_porte)
    
    #On combine tout ca
    deuxieme_choix_changer = table*situation_gagnante_perdante + (1-table)*situation_perdante_gagnante
    
    #On calcul nos gains
    gains_garder = (bonne_porte == deuxieme_choix_garder).sum()
    gains_changer = (bonne_porte == deuxieme_choix_changer).sum()
    
    return np.array([gains_changer, gains_garder])
    