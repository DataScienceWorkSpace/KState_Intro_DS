

from AngeloPizza.PizzaPriceCalculator import CalculatePrizzaPrize


#At Angelo’s Pizza Wheels, you have: 
#Three sauce options (red, white, and pesto)
#Three cheese options (mozzarella, feta, and ricotta)
#Eight toppings (olives, mushrooms, peppers, pepperoni, sausage, meatballs, arugula, and prosciutto)
#Two glazes (olive oil and balsamic)



order1 = CalculatePrizzaPrize("red", "feta",["olives","peppers"],"oliveOil")
print("Order1 price: " + order1)