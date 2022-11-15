def dynamic(depense_max, donnees):

    """
    Algorithme de programmation dynamique, sauvegardant le meilleur résultat à chaque itération,
    et le comparant avec le meilleur résultat précédent.
    """


    # On crée ici une matrice où les colonnes correspondent aux dépenses et les lignes aux actions.
    # Toutes les valeurs sont initialisés à 0
    matrice = [[0 for x in range(depense_max + 1)] for x in range(len(donnees) + 1)]

    # On fait ensuite une boucle sur les lignes actions
    for line in range(1, len(donnees) + 1):

        # On fait ici une boucle sur les colonnes dépenses
        for c in range(1, depense_max + 1):
            # On vérifie que le coût de l'action est inférieur à la colonne dépense où l'on se situe
            if donnees[line-1][1] <= c:

                # On rentre dans la matrice le maximum entre :
                #  - la rentabilité max de la ligne précédente
                #       -> matrice[l-1][c]
                #  - la rentabilité de la dépense courante + (la solution optimisée de la dépense de la ligne d'avant)
                #       -> donnees[l-1][2] + matrice[l-1][c-donnees[l-1][1]]

                #  max (rentablilité courante + rentabilité ligne précedente arrivant au poids max,
                # rentabilité max de la ligne précedente
                matrice[line][c] = max(donnees[line-1][2] + matrice[line-1][c-donnees[line-1][1]], matrice[line-1][c])

            # Si la dépense est supérieure à la dépense max, on récupére la solution de la ligne précédente
            else:
                matrice[line][c] = matrice[line-1][c]

    # Rechercher les actions en fonction du résultats
    w = depense_max
    n = len(donnees)
    actions_selection = []

    # Tant que la dépense est >= 0 et qu'il reste des actions à parcourir
    while w >= 0 and n >= 0:

        # ici on récupére la dernière action, on parcours la liste à l'envers
        a = donnees[n-1]

        # Si la rentabilté en cours  == la rentabilité de la valeur en cours -
        #                               la rentabilité de la valeur diminué de la dépense d'avant,
        # alors on sait que cette action est à ajouté dans la liste
        if matrice[n][w] == matrice[n-1][w - a[1]] + a[2]:
            actions_selection.append(a)

            # on réduit ensuite la dépense max de la valeur de l'action selectionnée
            w -= a[1]

        # ensuite on passe à l'élément suivant
        n -= 1

    depense_total_selection = 0

    for a in actions_selection:
        depense_total_selection += a[1]