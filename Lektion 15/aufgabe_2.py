def ist_palindrom(text):
    if text == text[::-1]:
        print(f"{text} ist ein Palindrom.")
    else:
        print(f"{text} ist kein Palindrom.")

ist_palindrom("lagerregal")
text = "Lagerregal"
print(text[::5])
print(text[2:])