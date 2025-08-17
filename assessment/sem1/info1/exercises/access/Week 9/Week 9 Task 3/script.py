
from item import Item
from order import Order

class Restaurant:

    def __init__(self, restaurant_name, menu_list):
        self.__restaurant_name = restaurant_name
        self.__menu_list = menu_list
        self.__pay = []
        self.__order_list = []

    def get_restaurant_name(self):
        return f'{self.__restaurant_name}'

    def get_menu_list(self):
        return self.__menu_list


    def set_order(self, item_list):
        good_food_list = []
        for item in item_list:
            if item in self.__menu_list:
                good_food_list.append(item)
        
        order = Order(good_food_list)
        if good_food_list:
            self.__order_list.append(order)

    def get_order_list(self):
        if len(self.__order_list)==0:
            return 'No order yet'
        return self.__order_list


    def get_revenue(self):
        self.__result = 0
        for order in self.__order_list:
            self.__result+=order.get_bill_amount()
        return self.__result

    


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    # Create Item Objects with Name and Price
    steak = Item("Steak", 25)
    salad = Item("Salad", 10)
    fish = Item("Fish", 30)
    pizza = Item("Pizza", 40)
    # Create menu list
    menu_list = [steak, salad, fish, pizza]
    # Create order list
    order_list = []
    # Create restaurant object with name and menu list
    restaurant = Restaurant("Zurich_1", menu_list)
    # Create an order with the order list
    restaurant.set_order(order_list)
    # Get the revenue of the restaurant object
    print(restaurant.get_revenue())
    print(restaurant.get_restaurant_name())
    print(restaurant.get_order_list())
  





