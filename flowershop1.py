from collections import defaultdict

class Flower:
    
    def __init__(self, name):
        self.name=name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) == 0:
            raise ValueError
        self._name=name         


class Bouquet:

    def __init__(self, name, price, flowers=None):
        self.name=name
        self.price=price
        self.flowers=flowers

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) == 0:
            raise ValueError('Name  cannot be empty')
        self._name=name   

    @property
    def flowers(self):
        return self._flowers

    @flowers.setter
    def flowers(self, flowers):
        self._flowers=flowers 

class Shop:
    
    def __init__(self, name, bouquets=None):
        self.bouquets=bouquets
        self._name=name

    @property 
    def _getbouquet(self, key):
        self.bouquets[key]
    
    def _setbouquet(self, key, value):
        self.bouquets[key]=value

    def _spare_bouquets(self, bouquet, amount):
        if amount > self.bouquets[bouquet]:
            raise ValueError('There is no such type of bouquet')

    def sell(self, bouquet, amount=1):
        self._spare_bouquets(bouquet, amount)
        self.bouquets[bouquet] -= amount

    def order(self, bouquet, amount=1):
        self.bouquets[bouquet] += amount
    
            




rose = Flower('Rose')
orchid = Flower('Orchid')
narcissus = Flower('Narcissus')

birthday = Bouquet('Birthday', price=12.3, flowers={rose.name: 12})
love = Bouquet('Love', price = 17, flowers={narcissus.name: 14})
for_mother = Bouquet('For Mother',price = 25, flowers = {orchid.name: 7})

flower_shop = Shop('Mathias', bouquets={birthday: 3, love: 7, narcissus: 5})
 
flower_shop.sell(birthday, amount=3)
flower_shop.order(birthday, amount=2)
flower_shop.sell(birthday, amount=2)