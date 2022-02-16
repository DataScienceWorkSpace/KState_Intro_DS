import this
from AngeloPizza.Product import Product
from AngeloPizza.Products import getProducts
import Products

class PizzaPriceCalculator:
    def CalculatePrizzaPrize(sauce, cheese, toppings, glaze):
        return this.CalculateSaucePrize(sauce) + this.CalculateCheesePrize(cheese) + this.CalculateToppingsPrize(toppings) + this.CalculateGlazePrize(glaze)


    def CalculateSaucePrize(sauce):
        p = this.FindProduct(sauce)
        return p.Price

    def CalculateCheesePrize(cheese):
        p = this.FindProduct(cheese)
        return p.Price

    def CalculateToppingsPrize(toppings):
        tTotalPrice = 0
        for p in toppings:        
            resultProduct = this.FindProduct(p.name)
            tTotalPrice = tTotalPrice + resultProduct.Price    
        return tTotalPrice

    def CalculateGlazePrize(glaze):
        p = this.FindProduct(glaze)
        return p.Price


    def FindProduct(name):
        for p in getProducts():
            if(p.name == name):
                resultProduct = p
        return resultProduct
