import csv
import time

MAX_COST = 500


def set_actions():
    actions = []
    # csvfile = csv.DictReader(open('actions.csv'))
    csvfile = csv.DictReader(open('dataset1_Python+P7.csv'))
    # csvfile = csv.DictReader(open('dataset2_Python+P7.csv'))
    for row in csvfile:
        if int(float(row['price']) * 100) > 0 and float(row['profit']) > 0:
            action = (row['name'], int(float(row['price']) * 100), float(row['price']) * float(row['profit'])/100)
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

    total_cost = sum([action[1]/100 for action in actions_selection])

    print('Résultat optimized :')
    print(f"La combinaison optimale est {actions_selection}")
    print(f"Le profit maximum est de {round(matrice[-1][-1],2)}€ pour un investissement est de {total_cost}€")

    return matrice[-1][-1], actions_selection


if __name__ == '__main__':
    start = time.time()
    actions_list = set_actions()
    print('Analyse en cours, veuillez patienter')
    knapsack_dynamique(MAX_COST * 100, actions_list)
    end = time.time()
    print(f"Execution time : {end - start} seconds")
