wetter = int(input("Wie ist das Wetter gerade? (1:sonnig, 2:regnerisch, 3:bewölkt, oder 4: stürmisch): "))
stunde = int(input("Wie spät ist es? (Bitte Stunde im 24-Stunden-Format eingeben): "))
darf_raus = False

if wetter == 1 and 9 < stunde < 19:
    darf_raus = True
elif wetter == 3 and 9 < stunde < 15:
    darf_raus = True
elif wetter == 3 and 6 <= stunde < 20:
    darf_raus = True
elif wetter == 4 and 6 <= stunde < 16:
    darf_raus = True

if darf_raus:
    print("Du darfst nach draußen gehen.")
else:
    print("Es ist besser, drinnen zu bleiben.")