print("Powiedz mi kim jesteś:\n"
        "1. Kobieta\n"
        "2. Mężczyzna\n")

gender = int(input(">> "))

print("Ile kobiet generować?")
numOfWomen = int(input(">> "))

if numOfWomen > 100:
    print("Maksymalna liczba: 100")
    quit()

print("Ilu mężczyzn generować?")
numOfMen = int(input(">> "))

if numOfMen > 100:
    print("Maksymalna liczba: 100")
    quit()