from selectors import SelectSelector

print("0 = addition\n1 = soustraction")


while True:
    reponse = input("Que voulez vous faire?\nÉcrire votre choix ici :")

    if reponse != "1":
        break

    if reponse != "0":
        break

    if reponse == "0":
        nb1 = int(input("Choisissez votre premier nombre:"))
        nb2 = int(input("Choisissez votre deuxième nombre:"))
        repa = nb1 + nb2
        print(f"{nb1} + {nb2} = {repa}")

    if reponse == "1":
        nb3 = int(input("Choisissez votre premier nombre:"))
        nb4 = int(input("Choisissez votre deuxième nombre:"))
        reps = nb3 - nb4
    print(f"{nb3} - {nb4} = {reps}")













