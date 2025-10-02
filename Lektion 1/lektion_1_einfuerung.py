print("Hallo!")
print("Das ist eine Künstliche Intelligenz")
print("Ich brauche deine Daten!")

print("Hallo, das ist die 1. Lektion Python!")
print(10)
name = input("Gib deinen Namen ein: ")

print("Dein Name lautet:", name)

geschlecht = input("Gib dein Geschlecht ein: ")

print("Dein Alter ist:", geschlecht)



geburtsdatum = input("Gib dein Geburtsdatum ein: ")
print("Dein Geburtsdatum ist:", geburtsdatum)


print("Ich habe alle notwendigen Informationen erhalten, danke!")

code = input("Gib einen Code ein, um fort zufahren: ")

if(code == "Ja" or code == "1234"):
    print("Hier ist eine Zusammenfassung der erhaltenen Daten:")
    print("Name:", name)
    print("Geschlecht:", geschlecht)
    print("Geburtsdatum:", geburtsdatum)
else:
    print("Das Programmist terminiert.")
