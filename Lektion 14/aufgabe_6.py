def wort_verbinden(text: str, n: int) -> str:
    return text * n

text = input("Gib den Text ein: ")
n = int(input("Wie oft soll der Text wiederholt werden? "))

x = wort_verbinden(text, n)
print(x)
