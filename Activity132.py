## Pizza Place

#At Angelo’s Pizza Wheels, you have: 
#Three sauce options (red, white, and pesto)
#Three cheese options (mozzarella, feta, and ricotta)
#Eight toppings (olives, mushrooms, peppers, pepperoni, sausage, meatballs, arugula, and prosciutto)
#Two glazes (olive oil and balsamic)

#

basePizza =8
itemizedBasePizzaPrice = 2
#sauce
red = 2
white = 1
pesto =3

# cheese
mozzarella = 2
feta = 1
ricotta = 3

# toppings
olives = 0.5
mushrooms = 0.5
peppers = 0.5
pepperoni = 0.5
sausage = 0.5
meatballs = 0.5
arugula = 0.5
prosciutto = 0.5

#premium toppings
burrata = 2.50
avocado = 2.50
bbqChicken = 2.50



toppings = ["olives", "mushrooms", "peppers", "pepperoni", "sausage", "meatballs", "arugula", "prosciutto" ]
premiumtoppings = ["burrata", "avocado", "bbqChicken"]

def CalculateItemizedPizzaPrice(sauce, cheese, toppings, glaze):    
    return CalculateSaucePrice(sauce) + CalculateCheesePrice(cheese)
        
    
def CalculateSaucePrice(sauce):
    if(sauce == "red"): 
        sPrice= red
    if(sauce == "white"): 
        sPrice= white
    if(sauce == "pesto"): 
        sPrice= pesto 
    return sPrice

def CalculateCheesePrice(cheese):
    if(mozzarella == "mozzarella"): 
        cPrice= red
    if(feta == "feta"): 
        cPrice= white
    if(ricotta == "ricotta"): 
        cPrice= pesto 
    return cPrice



def CalculatePizzaPrice(toppings):
    return 8+(toppings*.5)

def CalculatePizzaPriceWithPremium(toppings, premium_toppings):
    return CalculatePizzaPrice(toppings)+(premium_toppings*2)


order1 = CalculatePizzaPrice(2)
print("Order1: " + order1)

order2 = CalculatePizzaPrice(3)
print("Order2: " +order2)

order3 = CalculatePizzaPriceWithPremium(3,5)
print("Order3: " + order3)

