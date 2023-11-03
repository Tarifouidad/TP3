import math
def delta(a, b, c):
    return b**2 - 4*a*c

def NombreRacine(a, b, c):
    D = delta(a, b, c)
    if D > 0:
        return 2
    elif D == 0:
        return 1
    else:
        return 0

def AfficheNombreRacine(a, b, c):
    n = NombreRacine(a, b, c)
    if n == 2:
        print("L'équation a deux solutions.")
    elif n == 1:
        print("L'équation a une solution double.")
    else:
        print("L'équation n'a pas de solution réelle.")

def Racine1(a, b, c):
    D = delta(a, b, c)
    if D >= 0:
        return (-b + math.sqrt(D)) / (2*a)

def Racine2(a, b, c):
    D = delta(a, b, c)
    if D >= 0:
        return (-b - math.sqrt(D)) / (2*a)

def conversion_temps(h, m, s):
    return h*3600 + m*60 + s

def temps_ecoule(h1, m1, s1, h2, m2, s2):
    t1 = conversion_temps(h1, m1, s1)
    t2 = conversion_temps(h2, m2, s2)
    return abs(t2 - t1)

def conversion_distance(km, m, cm):
    return km*1000 + m + cm/100

def vitesse(distance, temps):
    distance_m = conversion_distance(*distance)
    temps_s = conversion_temps(*temps)
    if temps_s > 0:
        return distance_m / temps_s
    else:
        return "Le temps doit être supérieur à zéro pour calculer la vitesse."
