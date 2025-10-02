def ist_anagramm(a, b):
    liste_a = list(a)
    liste_b = list(b)
    liste_a.sort()
    liste_b.sort()
    if liste_a == liste_b:
        print("Sind Anagramme.")
    else:
        print("Sind keine Anagramme.")

ist_anagramm("tet","tset")