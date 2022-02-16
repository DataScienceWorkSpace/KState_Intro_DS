import Product
#sauce
products = [
          Product("red", "sauce", "sauce", 2, ""),
          Product("white", "sauce", "sauce", 1, ""),
          Product("pesto", "sauce", "sauce", 3, ""),
#cheese
          Product("mozzarella", "cheese", "cheese", 2, ""),
          Product("feta", "cheese", "cheese", 1, ""),
          Product("ricotta", "cheese", "cheese", 3, ""),
# toppings
            Product("olives", "topping", "standard", 0.5, ""),
          Product("mushrooms", "topping", "standard", 0.5, ""),
          Product("peppers", "topping", "standard", 0.5, ""),          
          Product("pepperoni", "topping", "standard", 0.5, ""),
          Product("sausage", "topping", "standard", 0.5, ""),
          Product("meatballs", "topping", "standard", 0.5, ""),
            Product("arugula", "topping", "standard", 0.5, ""),
          Product("prosciutto", "topping", "standard", 0.5, ""),          
          Product("burrata", "topping", "premium", 2.5, ""),
            Product("avocado", "topping", "premium", 2.5, ""),
          Product("bbqChicken", "topping", "premium", 2.5, ""),
#Glazes
        Product("oliveOil", "glaze", "glaze", 1, ""),
          Product("balsamic", "glaze", "glaze", 1.5, "")]
def getProducts():
    return products

