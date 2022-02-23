a = "Super Python"
b = ["Super", "Python"]
print(len(a))
print(a.__len__())


# print(dir(str))

print(b[0])
print(b.__getitem__(0))


class Order:
    def __init__(self, cart, customer) -> None:
        self.cart = cart
        self.customer = customer
        pass

    def __len__(self):
        return len(self.cart)

    def __add__(self, other):
        new_cart = self.cart.copy()
        new_cart.append(other)
        return Order(new_cart, self.customer)

    def __sub__(self, other):
        new_cart = self.cart.copy()
        new_cart.remove(other)
        return Order(new_cart, self.customer)

    def __gt__(self, other):
        return self.cart > other


order = Order(["spices", "rice", "eggs"], "Super Python")
print(len(order))
print(order.__len__())
print(order.cart)
order = order + "Mango"
print(order.cart)
order = order - "Mango"
print(order.cart)
print(order.cart > ["one", "two"])
