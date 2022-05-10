from collections import Counter
import operator


class TrackOrders:

    def __init__(self):
        self.orders = []

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        return self.orders.append({
            "customer": customer, "order": order, "day": day
        })

    def get_most_ordered_dish_per_customer(self, customer):
        orders = []
        for order in self.orders:
            if order["customer"] == customer:
                orders.append(order["order"])
        ordered_dishes = Counter(orders)
        most_requested_dishes = max(
            ordered_dishes.items(), key=operator.itemgetter(1))[0]
        return most_requested_dishes

    def get_never_ordered_per_customer(self, customer):
        menu = set(item["order"] for item in self.orders)

        orders = set()
        for order in self.orders:
            if order["customer"] == customer:
                orders.add(order["order"])
        return menu.difference(orders)

    def get_days_never_visited_per_customer(self, customer):
        days_of_week = set(item["day"] for item in self.orders)

        days_never_attended = set()
        for order in self.orders:
            if order["customer"] == customer:
                days_never_attended.add(order["day"])
        return days_of_week.difference(days_never_attended)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
