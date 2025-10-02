wetter = int(input("Wie ist das Wetter heute? 1: sonnig, 2: bewölkt, 3: regnerisch, 4: stürmisch; sage eine Nummer von 1-4: "))
if wetter == 1 or wetter == 2 or wetter == 3 or wetter == 4:
    print("Das Wetter ist in Ordnung.")
else:
    print("Bitte gib eine gültige Nummer ein (1-4).")
    wetter = int(input("Wie ist das Wetter heute? 1: sonnig, 2: bewölkt, 3: regnerisch, 4: stürmisch; sage eine Nummer von 1-4: "))

stunde = int(input("Wie spät ist es? Bitte gib eine Uhrzeit in Stunden an (0-23): "))
if stunde >= 0 and stunde <= 23:
    print("            ✅")
else:
    print("Bitte gib eine gültige Uhrzeit ein (0-23).")
    stunde = int(input("Wie spät ist es? Bitte gib eine Uhrzeit in Stunden an (0-23): "))

if (wetter == 1 or wetter == 2) and stunde >= 9 and stunde <= 19:
    print("Du kannst dich heute draußen aufhalten.")

else:
    print("Es ist besser, drinnen zu bleiben.")