import time
import csv


start_time = time.time()


def bruteforce(depense_max, donnees, lst_actions_selectionees=[]):
    if donnees:
        """
            les variables val1, lst_val1 représentent le résultat de la fonction
            (rentabilité max, liste action) sans l'action courante
        """

        val1, lst_val1 = bruteforce(depense_max, donnees[1:], lst_actions_selectionees)
        action_selection = donnees[0]  # ici on selectionne une action dans la liste
        if action_selection[1] <= depense_max:
            """
                on enleve le montant de l'action en cours de la dépense max
                et on ajoute cette action dans la liste des actions
            """
            val2, lst_val2 = bruteforce(depense_max - action_selection[1], donnees[1:],
                                        lst_actions_selectionees + [action_selection])
            """
                résultat de la meilleure rentabilité
            """
            if val1 < val2:
                return val2, lst_val2
        return val1, lst_val1

    else:
        """
            On renvoie à la fin la meilleur rentabilité total et la liste des actions et le montant maximum trouvé
        """
        # return f"la rentabilité maximum obtenue est : \
        #     {round(sum([i[1] * i[2] for i in lst_actions_selectionees]), 2)}", \
        #     f"La depense maximum est : {sum([i[1] for i in lst_actions_selectionees])} euros, " \
        #     f"avec ces actions: {[i[0] for i in lst_actions_selectionees]}"

        return sum([i[2] for i in lst_actions_selectionees]), lst_actions_selectionees


lst_actions = [
        ["action_01", 20, 0.05],
        ["action_02", 30, 0.1],
        ["action_03", 50, 0.15],
        ["action_04", 70, 0.2],
        ["action_05", 60, 0.17],
        ["action_06", 80, 0.25],
        ["action_07", 22, 0.07],
        ["action_08", 26, 0.11],
        ["action_09", 48, 0.13],
        ["action_10", 34, 0.27],
        ["action_11", 42, 0.17],
        ["action_12", 110, 0.09],
        ["action_13", 38, 0.23],
        ["action_14", 14, 0.01],
        ["action_15", 18, 0.03],
        ["action_16", 8, 0.08],
        ["action_17", 4, 0.12],
        ["action_18", 10, 0.14],
        ["action_19", 24, 0.21],
        ["action_20", 114, 0.18],
    ]

print(bruteforce(500, lst_actions))
print("\nTemps écoulé : ", time.time() - start_time, "seconds")
