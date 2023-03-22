import csv

# Récuparation des donnés du CSV
with open('dataset1_Python+P7.csv') as data:
    data = [d for d in csv.DictReader(data, delimiter=',') if float(d['price']) > 0 and float(d['profit']) > 0]

# Filtration par profit
data = sorted(data, key=lambda d: float(d['profit']), reverse=True)


# Une fois fait une nouvelle data trier par profit

def sumcomb(comb):
    total_price = 0
    for element in comb:
        total_price += float(element["price"])
    return total_price


def calculer_profit(comb):
    total_profit = 0
    for element in comb:
        total_profit += (float(element['profit']) * float(element['price'])) / 100
    return total_profit


combination_list = []

for action in data:
    partial_sum = sumcomb(combination_list) + float(action['price'])
    if partial_sum <= 500:
        combination_list.append(action)

for item in combination_list:
    print(item['name'])

print(f'Le profit des actions est égal à {calculer_profit(combination_list)} €')
print(f'Le prix total des actions acheté est égal à {sumcomb(combination_list)} € .')


print(calculer_profit(combination_list) / sumcomb(combination_list) * 100)

