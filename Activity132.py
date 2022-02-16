## Pizza Place

#At Angelo’s Pizza Wheels, you have: 
#Three sauce options (red, white, and pesto)
#Three cheese options (mozzarella, feta, and ricotta)
#Eight toppings (olives, mushrooms, peppers, pepperoni, sausage, meatballs, arugula, and prosciutto)
#Two glazes (olive oil and balsamic)

#

def CalculatePizzaPrice(toppings):
    return 8+(toppings*.5)

def CalculatePizzaPriceWithPremium(toppings, premium_toppings):
    return CalculatePizzaPrice(toppings)+(premium_toppings*2)


order1 = CalculatePizzaPrice(2)
print(order1)

order2 = CalculatePizzaPrice(3)
print(order2)

order3 = CalculatePizzaPriceWithPremium(3,5)
print(order3)