# racunalo.py - Osnovno računalo
# Avtor: Tian

def sestevanje(a, b):
    return a + b

def odstevanje(a, b):
    return a - b

def mnozenje(a, b):
    return a * b

def deljenje(a, b):
    if b == 0:
        return "Napaka: Deljenje z 0 ni dovoljeno!"
    return a / b

if __name__ == "__main__":
    print("Računalo Pro v2.0")
    print("5 + 3 =", sestevanje(5, 3))
    print("5 - 3 =", odstevanje(5, 3))