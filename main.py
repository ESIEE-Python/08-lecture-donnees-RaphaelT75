"""
Ce programme lit un fichier CSV contenant des listes d'entiers,
puis effectue plusieurs opérations sur les données lues.

Le programme lit un fichier CSV spécifié par la variable globale `FILENAME`, 
qui contient des lignes de nombres séparés par des points-virgules.
Pour chaque ligne du fichier, 
les listes de nombres sont convertis en une liste d'entiers 
et ajoutés à une liste générale `data`.
Ensuite, plusieurs fonctions sont appliquées à cette liste de données :
    - `get_list_k()`: Retourne la ligne `k` de la liste de données.
    - `get_sum()`: Calcule la somme des éléments d'une liste donnée.
    - `get_min()`: Trouve le minimum d'une liste donnée.
    - `get_max()`: Trouve le maximum d'une liste donnée.
    - `get_first()`: Retourne le premier élément d'une liste donnée.

Entrées :
Le programme attend un fichier CSV contenant des nombres séparés par des points-virgules.
Le nom du fichier est défini par la variable `FILENAME`.

Sorties :
Le programme affiche les résultats des différentes opérations 
dans main

"""
#### Imports et définition des variables globales
FILENAME = "listes.csv"

#### Fonctions secondaires
def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, mode='r', encoding='utf8') as f:
        lines = f.readlines()
        l = [list(map(int, line.strip().split(';'))) for line in lines if line.strip()]
    return l

def get_list_k(data, k):
    """Retourne la ligne k de la liste de données, ou None si k est hors limites.

    Args:
        data (list): La liste des données lues à partir du fichier.
        k (int): L'indice de la ligne à récupérer.

    Returns:
        list or None: La ligne k sous forme de liste, ou None si k est invalide.
    """
    return data[k] if 0 <= k < len(data) else None

def get_first(l):
    """Retourne le premier élément de la liste, ou None si la liste est vide.

    Args:
        l (list): La liste d'entrée.

    Returns:
        any or None: Le premier élément de la liste, ou None si la liste est vide.
    """
    return l[0] if l else None

def get_last(l):
    """Retourne le premier élément de la liste, ou None si la liste est vide.

    Args:
        l (list): La liste d'entrée.

    Returns:
        any or None: Le dernier élément de la liste, ou None si la liste est vide.
    """
    return l[-1] if l else None

def get_max(l):
    """Retourne le premier élément de la liste, ou None si la liste est vide.

    Args:
        l (list): La liste d'entrée.

    Returns:
        any or None: le plus grand élément de la liste, ou None si la liste est vide.
    """
    return max(l) if l else None

def get_min(l):
    """Retourne le premier élément de la liste, ou None si la liste est vide.

    Args:
        l (list): La liste d'entrée.

    Returns:
        any or None: Le plus petit élément de la liste, ou None si la liste est vide.
    """
    return min(l) if l else None

def get_sum(l):
    """Retourne le premier élément de la liste, ou None si la liste est vide.

    Args:
        l (list): La liste d'entrée.

    Returns:
        any or None: La somme des élément de la liste, ou None si la liste est vide.
    """
    return sum(l) if l else None

#### Fonction principale


def main():
    """
    permet de tester le programme, fait des appels de fonction du programme
    """
    data = read_data(FILENAME)
    k = 37
    get_list_k(data, 38)
    get_sum(get_list_k(data, 38))
    get_first(get_list_k(data, 38))
    get_min(get_list_k(data, 38))
    get_max(get_list_k(data, 38))
    print(k, get_list_k(data, 37))
    print(get_sum(get_list_k(data, 37)))
    print(get_min(get_list_k(data, 37)))
    print(get_max(get_list_k(data, 37)))
    print(get_first(get_list_k(data, 37)))

if __name__ == "__main__":
    main()
