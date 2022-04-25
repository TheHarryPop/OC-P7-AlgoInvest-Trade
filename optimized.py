import csv
import time

MAX_COST = 500


def set_actions():
    actions = []
    csvfile = csv.DictReader(open('actions.csv'))
    for row in csvfile:
        action = (row['name'], int(row['price']), (int(row['profit']) * 0.01) * int(row['price']))
        actions.append(action)
    return actions


def knapsack_dynamique(max_cost, actions):
    matrice = [[0 for x in range(max_cost + 1)] for x in range(len(actions) + 1)]

    for i in range(1, len(actions) + 1):
        for w in range(1, max_cost + 1):
            if actions[i-1][1] <= w:
                matrice[i][w] = max(actions[i-1][2] + matrice[i-1][w-actions[i-1][1]], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]

    # Retrouver les actions en fonction du coût
    w = max_cost
    n = len(actions)
    actions_selection = []

    while w >= 0 and n >= 0:
        a = actions[n-1]
        if matrice[n][w] == matrice[n-1][w-a[1]] + a[2]:
            actions_selection.append(a)
            w -= a[1]

        n -= 1

    print('Résultat optimized :')
    print(f"La combinaison optimale est {actions_selection}")
    print(f"Le profit maximum est de {matrice[-1][-1]}€ pour un investissement est de {MAX_COST - w}€")

    return matrice[-1][-1], actions_selection


if __name__ == '__main__':
    start = time.time()
    actions_list = set_actions()
    knapsack_dynamique(MAX_COST, actions_list)
    end = time.time()
    print(f"Execution time : {end - start} seconds")
