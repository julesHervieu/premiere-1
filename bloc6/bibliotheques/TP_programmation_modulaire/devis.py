import geometrie
import geometrie_triangle
import math

def nombre_pots(longueur, largeur, surface_couvrante):
    """
    Calcul du nombre de pots nécessaires
    paramètre longueur (float) : valeur de la longueur de la pièce
    paramètre largeur (float) : valeur de la largeur de la pièce
    paramètre surface_couvrante (float) ; valeur de la surface couvrante d'1 pot de peinture
    retour (int) : Nombre de pots de peintures nécessaires
    pré-conditions : la longueur, la largeur et la surface_couvrante sont des valeurs strictement positives
    post-conditions : Néant
    """
    nb_pot = math.ceil(geometrie_triangle.aire(longueur,largeur) / surface_couvrante)
    
    return nb_pot

def nombre_baches(longueur, largeur, surface_couvrante):
    """
    Calcul du nombre de bâches nécessaires
    paramètre longueur (float) : valeur de la longueur de la pièce
    paramètre largeur (float) : valeur de la largeur de la pièce
    paramètre surface_couvrante (float) ; valeur de la surface couvrante d'1 bâche
    retour (int) : Nombre de bâches nécessaires
    pré-conditions : la longueur, la largeur et la surface_couvrante sont des valeurs strictement positives
    post-conditions : Néant
    """
    nb_baches = math.ceil(geometrie_triangle.aire(longueur,largeur) / surface_couvrante)
    
    return nb_baches

def nombre_rubans(longueur, largeur, perimetre_couvrante):
    """
    Calcul du nombre de rubans nécessaires
    paramètre longueur (float) : valeur de la longueur de la pièce
    paramètre largeur (float) : valeur de la largeur de la pièce
    paramètre perimetre_couvrante (float) ; valeur du périmètre couvrant d'1 ruban
    retour (int) : Nombre de rubans nécessaires
    pré-conditions : la longueur, la largeur et la perimetre_couvrante sont des valeurs strictement positives
    post-conditions : Néant
    """
    return math.ceil(geometrie_triangle.perimetre(longueur,largeur) / perimetre_couvrante)

def salaire(longueur, largeur):
    """
    Calcul du salaire du peintre, sachant que le peintre couvre 1m * 1m en 1 heure pour 7,5€
    paramètre longueur (float) : valeur de la longueur de la pièce
    paramètre largeur (float) : valeur de la largeur de la pièce
    retour (float) : Salaire du peintre
    pré-conditions : la longueur, la largeur et la surface_couvrante sont des valeurs strictement positives
    post-conditions : Néant
    """
    resultat = geometrie_triangle.aire(longueur,largeur)
    return resultat * 7.50

def est_reparation_couverte(total_couts):
    """
    Indique si les réparations sont couvertes
    paramètre total_couts (float) ; valeur totale des coûuts
    retour (bool) : True si le forfait couvre l'ensemble des coûts
    pré-conditions : le total des coûts est strictement positif
    post-conditions : Néant
    """
    return total_couts <= 500

