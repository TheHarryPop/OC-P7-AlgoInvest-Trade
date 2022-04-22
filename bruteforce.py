import csv
from itertools import combinations, permutations

MAX_COST = 500


def sort_actions():
    actions = []
    csvfile = csv.DictReader(open('actions.csv'))
    for row in csvfile:
        action = (row['name'], int(row['cost']), (int(row['profit']) * 0.01) * int(row['cost']))
        actions.append(action)
    return actions


def make_combination(actions):

    best_profit = 0
    best_combination = None
    best_cost = 0

    for i in range(len(actions)):
        for combination in combinations(actions, i + 1):
            cost = 0
            profit = 0

            for action in combination:
                cost += int(action[1])
                profit += int(action[2])

            if cost <= MAX_COST and profit > best_profit:
                best_cost = cost
                best_combination = combination
                best_profit = profit

    print(f"best_combination: {best_combination}")
    print(f"best_profit: {best_profit}€")
    print(f"best_cost: {best_cost}€")


if __name__ == '__main__':
    actions_list = sort_actions()
    make_combination(actions_list)
