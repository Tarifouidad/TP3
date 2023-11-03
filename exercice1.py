def somme(m, n):
    total = 0
    for i in range(m, n + 1):
        total += i
    return total

# Exemple d'utilisation
resultat = somme(5, 8)
print(resultat)  # Cela affichera 26
