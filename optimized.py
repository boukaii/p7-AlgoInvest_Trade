import time
import csv


# On commence le timer
start = time.time()
# Ouverture du fichier csv et filtrage des données
actions = []

with open("dataset1.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    # On saute la première ligne qui contient les noms des champs
    next(reader)
    for row in reader:
        row_float1 = float(row[1])
        row_float2 = float(row[2])
        if row_float1 <= 0 or row_float2 <= 0:
            continue
        actions.append([row[0], row_float1, row_float2])


MAX_VALUE_INVEST = 500


def dynamic_search(list_actions, max_value=MAX_VALUE_INVEST):
    matrix = [[0 for x in range(max_value + 1)] for x in range(len(list_actions) + 1)]
    for i in range(1, len(list_actions) + 1):
        for wallet in range(1, max_value + 1):
            if list_actions[i - 1][1] <= wallet:
                matrix[i][wallet] = max(list_actions[i - 1][2] + matrix[i - 1][int(wallet - list_actions[i - 1][1])],
                                        matrix[i - 1][wallet])
            else:
                matrix[i][wallet] = matrix[i - 1][wallet]
    wallet = max_value
    nb_actions = len(list_actions)
    actions_selection = []
    while wallet >= 0 and nb_actions >= 0:
        action = list_actions[nb_actions - 1]
        if matrix[nb_actions][int(wallet)] == matrix[nb_actions - 1][int(wallet - action[1])] + action[2]:
            actions_selection.append(action)
            wallet -= action[1]
        nb_actions -= 1
    max_invest = MAX_VALUE_INVEST - wallet
    depense_total_selection = 0

    for a in actions_selection:
        depense_total_selection += a[1]
    return {"Total bénéfice": matrix[-1][-1], "Combinaisons d'actions": actions_selection}
    # return (
    #     f"--------------------------------------------------------------\n\n"
    #     f"la rentabilité maximum obtenue est : {matrix[-1][-1] / 100}\n\n"
    #     f"La depense maximum est : {depense_total_selection}\n\n"
    #     f"Avec ces actions: {[i[0] for i in actions_selection]}\n"
    #
    # )

    # return (
    #     f"--------------------------------------------------------------\n\n"
    #     f"la rentabilité maximum obtenue est : {matrix[-1][-1]}\n\n"
    #     f"La depense maximum est : {max_invest}\n\n"
    #     f"Avec ces actions: {[i[0] for i in actions_selection]}\n"
    # )
    #


    # return matrix[-1][-1], actions_selection, max_invest

#
# lst_actions = [
#         ["action_01", 20, 0.05],
#         ["action_02", 30, 0.1],
#         ["action_03", 50, 0.15],
#         ["action_04", 70, 0.2],
#         ["action_05", 60, 0.17],
#         ["action_06", 80, 0.25],
#         ["action_07", 22, 0.07],
#         ["action_08", 26, 0.11],
#         ["action_09", 48, 0.13],
#         ["action_10", 34, 0.27],
#         ["action_11", 42, 0.17],
#         ["action_12", 110, 0.09],
#         ["action_13", 38, 0.23],
#         ["action_14", 14, 0.01],
#         ["action_15", 18, 0.03],
#         ["action_16", 8, 0.08],
#         ["action_17", 4, 0.12],
#         ["action_18", 10, 0.14],
#         ["action_19", 24, 0.21],
#         ["action_20", 114, 0.18],
#     ]


print(dynamic_search(actions))
print("\nTemps écoulé : ", time.time() - start, "seconds")






