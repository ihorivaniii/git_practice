import items
from datetime import datetime, time

current_time = datetime.now()
print(current_time)


class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "Menu {} available at {}:00 to {}:00".format(self.name, self.start_time, self.end_time)

    def calculate_bill(self, purchased_items):
        self.purchased_items = purchased_items
        total_price = 0
        for i in self.purchased_items:
            total_price += self.items[i]
            print(i)
        return total_price


class Franchise():
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return self.address

    def available_menus(self, time):
        self.time = time
        list_of_available_menus = []
        for i in self.menus:
            if self.time >= i.start_time and self.time < i.end_time:
                list_of_available_menus.append(i)
        return list_of_available_menus


brunch = Menu("brunch", items.brunch_items, time(11, 00), time(16, 00))

early_bird = Menu("early bird", items.early_bird_items, time(15, 00), time(18, 00))

dinner = Menu("dinner", items.dinner_items, time(17, 00), time(23, 00))

kids = Menu("kids", items.kids_items, time(11, 00), time(21, 00))
arepas_menu = Menu("Take a' Arepa", items.arepas_menu_items, time(10), time(20))

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
arepas_place = Franchise("189 Fitzgerald Avenue", [brunch, early_bird, dinner, kids, arepas_menu])


class Business():
    def __init__(self, name, franchises):
        self.self = self
        self.name = name
        self.franchises = franchises


first = Business("Basta Fazoolin with my Heart", [flagship_store, new_installment])
new_business = Business("Take a' Arepa", [flagship_store, new_installment, arepas_place])
print(flagship_store.available_menus(time(11)))