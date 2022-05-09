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
    with open('data/mkt_campaign.txt', 'w') as file:
        file.writelines([
            f"{most_requested_by_maria_data}\n",
        ])
