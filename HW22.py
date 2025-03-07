#Name:
#Class: 5th Hour
#Assignment: HW22


#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class StoreItem:
    def __init__(self, cost, weight,stock):
        self.stock= stock
        self.cost= cost
        self.weight= weight

    def double_cost(self):
        self.cost *= 2
#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
canofbeans = StoreItem(5,7,8)
doomsdaybucket= StoreItem(50,60,70)
shirts = StoreItem(10,15,20)

#3. Print the stock of all three objects and the cost of the second store item.
print(f"canofbeans cost: {canofbeans.cost}")
print(f"canofbeans stock: {canofbeans.stock}")
print(f"canofbeans weight: {canofbeans.weight}")
print(f"doomsdaybucket cost: {doomsdaybucket.cost}")
print(f"doomsdaybucket stock: {doomsdaybucket.stock}")
print(f"doomsdaybucket weight: {doomsdaybucket.weight}")
print(f"shirts cost: {shirts.cost}")
print(f"shirts stock: {shirts.stock}")
print(f"shirts weight: {shirts.weight}")

#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
doomsdaybucket.double_cost()
print(f"New cost of Item 2: ${doomsdaybucket.cost}")
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
shirts.stock = int(shirts.stock / 4)
print(f"New stock of Item 3: {shirts.stock}")
#6. Delete the first store item and then  empt   to print the weight of the first store item. Create a try/except catch to fix the error.
del canofbeans
try:
    print(f"Weight of Item 1: {canofbeans.weight}")
except NameError as e:
    print(f"Error: {e}. Item 1 has been deleted.")