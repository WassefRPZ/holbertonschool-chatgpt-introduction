#!/usr/bin/python3
import sys

def factorial(n):
    """Calcule le factoriel d'un nombre entier positif."""
    if n < 0:
        raise ValueError("Le factoriel n'est pas défini pour les nombres négatifs.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        # Vérifie que l'utilisateur a fourni un argument
        if len(sys.argv) != 2:
            print("Usage : ./factorial_recursive.py <entier>")
            sys.exit(1)

        # Convertit l'argument en entier
        n = int(sys.argv[1])

        # Calcule et affiche le factoriel
        f = factorial(n)
        print(f"Factoriel de {n} : {f}")
    except ValueError as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")