import time
import matplotlib.pyplot as plt 


def tester_premier(x:int)->bool:
    """ Renvoie True si x est un nombre premier. Sinon, renvoie False.
    """
    assert x >= 2, "Le nombre testé doit être supérieur à 1"
    test = True
    for i in range (2, x):
        if x%i == 0: # J'ai trouvé un nombre i qui divise x
            test = False # x n'est donc pas un nombre entier
            break 
    return test

def pgcd(a,b):
    """Renvoie le pgcd de a et b."""
    while b:
        a, b = b, a%b
    return a

def calculer_e(p:int, q:int)->int:
    """Renvoie la plus petite valeur possible de e pour p et q."""
    f = (p-1)*(q-1)
    v = 2
    while pgcd(v, f) != 1 and v < f:
        v += 1
    return v


def calculer_d(p:int, q:int, e:int)->int:
    """Renvoie une valeur de d pour p, q et e."""
    d = 2
    f = (p-1)*(q-1)
    while (d*e) % f != 1 and d < f:
        d += 1
    return d


def generer_clefs(p:int, q:int)->tuple:
    """
    Renvoie un couple de clés généré à partir des nombres premiers p et q.

    """
    e = calculer_e(p, q)
    d = calculer_d(p, q, e)
    n = p * q
    return ((e, n), (d, n))

def lister_premiers(n:int)->list:
    """ Renvoie la liste des nombres premiers inférieurs à n
    """
    liste_premiers = [2] # On peut saisir manuellement ces deux premiers éléments
    #n_max = int(abs(sqrt(n))+1)
    for i in range(3,n,2): # Cela permet d'optimiser un peu la recherche des suivants
        if tester_premier(i):
            liste_premiers.append(i)
    return liste_premiers

def factoriser_premiers(n:int)->tuple:
    """ Renvoie le couple de nombres premiers qui vérifie p * q = n
        Si la décomposition en produit de facteurs premiers et impossible, renvoie None
    """
    liste_premiers = lister_premiers(n) # On dispose d'une liste suffisante de nombres premiers
    for i in range(len(liste_premiers)):
        if n%liste_premiers[i] ==0:
            for j in range(i):
                if liste_premiers[i] * liste_premiers[j] == n:
                    return (liste_premiers[i],liste_premiers[j])
                elif n%liste_premiers[j] == 0:
                    return None
    return None


def trace_reponse_temporelle(liste_premiers:list, liste_produits:list ):
    """ Prend une liste des nombres premiers et la liste triée des produits de couples nombres ce cette liste
        Cherche la décomposition en produit de facteurs premiers de chaque élément de liste_produits
        Mémomrise le temps de calcul 
        Trace le graphique du temps de calcul en fonction de du produit
    """
    temps = []
    produits = []
    for produit in liste_produits:
        temps_debut = time.time()
        if factoriser_premiers(produit) != None:
            temps_fin = time.time()
            temps.append((temps_fin - temps_debut)*1000)
            produits.append(produit)
    plt.plot(produits, temps) # trace le graphique
    plt.grid() # affiche la grille
    plt.show() # affiche le graphique
    
def construire_liste_produits(N:int)->tuple:
    """ Construit les liste des nombres premiers inférieurs à N
        Pour chaque couple de nombres premiers pris dans la liste, calcule le produit du couple
        Renvoie la liste des nombres premiers inférieurs à N et la liste triée des produits de nombres premiers
    """
    liste_produits = []
    liste_premiers = lister_premiers(N)
    for i in range(len(liste_premiers)):
        for j in range(i, len(liste_premiers)):
            liste_produits.append(liste_premiers[i]*liste_premiers[j])
    liste_produits.sort()
    print("* liste_produits *")
    print("- Min:\t", liste_produits[0])
    print("- Max:\t", liste_produits[-1])
    print("- Taille:\t", len(liste_produits))
    return liste_premiers, liste_produits

liste_premiers, liste_produits = construire_liste_produits(110)
trace_reponse_temporelle(liste_premiers, liste_produits )