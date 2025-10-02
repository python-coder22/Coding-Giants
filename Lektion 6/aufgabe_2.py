PIN = "1234"
PASSWORT = "geheim123"

eingegebener_pin = input("Gib deinen PIN ein: ")

if eingegebener_pin == PIN:
   
    eingegebenes_passwort = input("PIN richtig! Gib dein Passwort ein: ")
  
    if eingegebenes_passwort == PASSWORT:
    
        print("Beide Prüfungen passen. Zugang gewährt.")

    else:
        
        print("PIN war korrekt aber Passwort nicht. Kein Zugang.")

else:
    print("PIN ist falsch. Zugang nicht gewährt.")
