class ShoppingCart():
    def __init__(self, employee_discount=None, total=0, items=[],pricedict={}): 
        self.total = total
        self.items = items.copy()
        self.employee_discount = employee_discount
        self.pricedict=pricedict
    def add_item(self, item, price, quantity = 1):
        self.total = self.total + price*quantity
        self.pricedict[item]=price
        for i in range(quantity):
            self.items.append(item)
        return self.total
    def mean_item_price(self):
        price_per_item = self.total/len(self.items)
        return price_per_item
    def median_item_price(self):
        pricelist = sorted([self.pricedict[item] for item in self.items])
        if len(pricelist) %2 ==0:
            median_price = (pricelist[(len(pricelist)/2)-1]
            +pricelist[len(pricelist)/2])/2
        else:
            median_price = pricelist[int((len(pricelist)-1)/2)]
        return median_price
    def apply_discount(self):
        if self.employee_discount:
            discountedtotal = self.total *(1- self.employee_discount/100)
            return discountedtotal
        else:
            return "Sorry, there is no discount to apply to your cart :("
    def void_last_item(self):
        item = self.items.pop()
        if self.total == 0:
            return "There are no items in your cart!"
        else:
            self.total -= self.pricedict[item]


