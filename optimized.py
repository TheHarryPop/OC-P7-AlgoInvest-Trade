import csv
import time

MAX_COST = 500


def make_choice_input():
    print("Quel fichier voulez vous analyser ?")
    print("Tapez 1 pour le fichier actions.csv")
    print("Tapez 2 pour le fichier dataset1_Python+P7.csv")
    print("Tapez 3 pour le fichier dataset2_Python+P7.csv")
    input_choice = input("Votre choix : ")
    if input_choice == "1" or input_choice == "2" or input_choice == "3":
        return input_choice
    else:
        print("Invalide choice")
        return make_choice_input()


def set_actions(choice):
    actions = []
    csvfile = {}

    if choice == "1":
        csvfile = csv.DictReader(open('actions.csv'))
        for row in csvfile:
            action = (row['name'], int(row['price']), (int(row['profit']) * 0.01) * int(row['price']))
            actions.append(action)
    else:
        if choice == "2":
            csvfile = csv.DictReader(open('dataset1_Python+P7.csv'))
        elif choice == "3":
            csvfile = csv.DictReader(open('dataset2_Python+P7.csv'))
        for row in csvfile:
            if int(float(row['price']) * 10) > 0 and float(row['profit']) > 0:
                action = (row['name'], int(float(row['price']) * 10), int(float(row['price']) * 10) *
                          float(row['profit']) / 100)
                actions.append(action)

    return actions


def knapsack_dynamique(max_cost, actions):
    matrice = [[0 for x in range(max_cost + 1)] for x in range(len(actions) + 1)]

    for i in range(1, len(actions) + 1):
        for j in range(1, max_cost + 1):
            if actions[i-1][1] <= j:
                matrice[i][j] = max(actions[i-1][2] + matrice[i-1][j-actions[i-1][1]], matrice[i-1][j])
            else:
                matrice[i][j] = matrice[i-1][j]

    # Retrouver les actions en fonction du coût
    w = max_cost
    n = len(actions)
    actions_selection = []

    while w >= 0 and n >= 0:
        action = actions[n-1]
        if matrice[n][w] == matrice[n-1][w-action[1]] + action[2]:
            actions_selection.append(action)
            w -= action[1]
        n -= 1

    total_cost = sum([action[1] for action in actions_selection])

    print('Résultat optimized :')
    print(f"La combinaison optimale est {[action[0] for action in actions_selection]}")
    print(f"Le profit maximum est de {round(matrice[-1][-1], 2)}€ pour un investissement de {total_cost}€")

    return matrice[-1][-1], actions_selection


def knapsack_dynamique_dixieme(max_cost, actions):
    matrice = [[0 for x in range(max_cost + 1)] for x in range(len(actions) + 1)]

    for i in range(1, len(actions) + 1):
        for j in range(1, max_cost + 1):
            if actions[i-1][1] <= j:
                matrice[i][j] = max(actions[i-1][2] + matrice[i-1][j-actions[i-1][1]], matrice[i-1][j])
            else:
                matrice[i][j] = matrice[i-1][j]

    # Retrouver les actions en fonction du coût
    w = max_cost
    n = len(actions)
    actions_selection = []

    while w >= 0 and n >= 0:
        action = actions[n-1]
        if matrice[n][w] == matrice[n-1][w-action[1]] + action[2]:
            actions_selection.append(action)
            w -= action[1]
        n -= 1

    total_cost = sum([action[1]/10 for action in actions_selection])

    print('Résultat optimized :')
    print(f"La combinaison optimale est {[action[0] for action in actions_selection]}")
    print(f"Le profit maximum est de {round(matrice[-1][-1]/10,2)}€ pour un investissement de {round(total_cost,2)}€")

    return matrice[-1][-1], actions_selection


if __name__ == '__main__':
    file = make_choice_input()
    actions_list = set_actions(file)
    print('Analyse en cours, veuillez patienter')
    start = time.time()
    if file == "1":
        knapsack_dynamique(MAX_COST, actions_list)
    else:
        knapsack_dynamique_dixieme(MAX_COST * 10, actions_list)
    end = time.time()
    print(f"Execution time : {round(end - start, 3)} seconds")
