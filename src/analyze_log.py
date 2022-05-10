import csv


def most_requested_by_maria(data):
    foods = {}
    for item in data:
        if item["name"] == "maria":
            if item["food"] not in foods:
                foods[item["food"]] = 1
            else:
                foods[item["food"]] += 1

    # https://docs.python.org/3/howto/sorting.html
    most_requested_food = sorted(foods, key=lambda x: x[1])

    return most_requested_food[0]


def arnaldo_ordered(data):
    orders = 0
    for order in data:
        if order["name"] == "arnaldo":
            if order["food"] == "hamburguer":
                orders += 1
    return orders


def unordered_dishes_by_joao(data):
    menu = set(item["food"] for item in data)

    orders = set()
    for order in data:
        if order["name"] == "joao":
            orders.add(order["food"])
    unordered_dishes = menu.difference(orders)
    return unordered_dishes


def days_not_frequented_by_joao(data):
    days_of_week = set(item["day_of_the_week"] for item in data)
    days = set()
    for order in data:
        if order["name"] == "joao":
            days.add(order["day_of_the_week"])
    days_not_frequented = days_of_week.difference(days)
    return days_not_frequented


def analyze_log(path_to_file):
    if '.csv' in path_to_file:
        try:
            with open(path_to_file) as file:
                header = ["name", "food", "day_of_the_week"]
                data = csv.DictReader(file, fieldnames=header)
                formatted_data = [line for line in data]
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
    else:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    most_requested_by_maria_data = most_requested_by_maria(formatted_data)
    arnaldo_ordered_data = arnaldo_ordered(formatted_data)
    unordered_dishes_by_joao_data = unordered_dishes_by_joao(formatted_data)
    days_not_frequented_data = days_not_frequented_by_joao(formatted_data)
    with open('data/mkt_campaign.txt', 'w') as file:
        file.writelines([
            f"{most_requested_by_maria_data}\n",
            f"{arnaldo_ordered_data}\n",
            f"{unordered_dishes_by_joao_data}\n",
            f"{days_not_frequented_data}\n",
        ])
