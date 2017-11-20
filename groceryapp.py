class ShoppingList():
    def __init__(self,title,description):
        self.title = title
        self.description = description
        self.groceryItems = []
    
    def add_grocery_items(self,item):
        self.groceryItems.append(item)
    
    def print_out(self):
        print(self.title  + '\n' + str(self.groceryItems))

class GroceryItem():
    def __init__(self,name):
        self.name = name
        self.brand = ''
        self.quantity = 0
        self.price = 0
        
milk = GroceryItem('Milk')
soda = GroceryItem('Soda')
fish = GroceryItem('Fish')

paper = GroceryItem('Paper')
napkins = GroceryItem('Napkins')
plate = GroceryItem('Plate')
chips = GroceryItem('Chips')

chicken = GroceryItem('Chicken')
beef = GroceryItem('Beef')
eggs = GroceryItem('Eggs')
sugar = GroceryItem('Sugar')
salt = GroceryItem('Salt')
pepper = GroceryItem('Pepper')
honey = GroceryItem('Honey')

fiesta = ShoppingList('fiesta', 'meat')
fiesta.add_grocery_items(milk.name)
fiesta.add_grocery_items(soda.name)
fiesta.add_grocery_items(fish.name)
fiesta.print_out()

walmart = ShoppingList('Walmart','random')
walmart.add_grocery_items(paper.name)
walmart.add_grocery_items(napkins.name)
walmart.add_grocery_items(plate.name)
walmart.add_grocery_items(chips.name)
walmart.print_out()

sams_club = ShoppingList('Sam\'s Club', 'random')
sams_club.add_grocery_items(chicken.name)
sams_club.add_grocery_items(beef.name)
sams_club.add_grocery_items(eggs.name)
sams_club.add_grocery_items(sugar.name)
sams_club.add_grocery_items(salt.name)
sams_club.add_grocery_items(pepper.name)
sams_club.add_grocery_items(honey.name)
sams_club.print_out()



    
    