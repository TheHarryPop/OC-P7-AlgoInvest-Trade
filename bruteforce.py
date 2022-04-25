import csv
from itertools import combinations as itercombi

MAX_COST = 500


def set_actions():
    actions = []
    csvfile = csv.DictReader(open('actions.csv'))
    for row in csvfile:
        action = (row['name'], int(row['cost']), (int(row['profit']) * 0.01) * int(row['cost']))
        actions.append(action)
    return actions


def iter_combinations(actions):

    total_combinations = []

    for i in range(len(actions)):
        combi = itercombi(actions, i)
        for comb in combi:
            total_combinations.append(comb)
    return total_combinations


def make_valide_comb(total_combinaisons, max_cost):
    combinaisons_valides = []
    for combi in total_combinaisons:
        combi_cost = 0
        combi_profit = 0
        for i in range(len(combi)):
            combi_cost += combi[i][1]
            combi_profit += combi[i][2]
        if combi_cost <= max_cost:
            combinaisons_valides.append((combi, combi_cost, combi_profit))
    print(f"len combi valides:{len(combinaisons_valides)}")
    return combinaisons_valides


def optimal_combination(valides_combinaisons):
    optimale_solution = None
    max_profit = 0
    max_cost = 0
    for combi in valides_combinaisons:
        if combi[2] > max_profit:
            max_profit = combi[2]
            max_cost = combi[1]
            optimale_solution = combi[0]
    print(f"La combinaison optimale est {optimale_solution}")
    print(f"le profit maximum est de {max_profit}€")
    print(f"l'investissement est de {max_cost}€")


if __name__ == '__main__':
    combinations = iter_combinations(set_actions())
    optimal_combination(make_valide_comb(combinations, MAX_COST))
