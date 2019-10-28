import re
import uuid

class Item():
    def __init__(self, name, quantity, unit_price):
        self.name=name
        self.quantity=quantity
        self.unit_price=unit_price
    
    def __gt__(self, other):
        return self.total_price>other.total_price
    
    def __ge__(self, other):
        return self.total_price>=other.total_price
    
    def __lt__(self, other):
        return self.total_price<other.total_price
    
    def __le__(self, other):
        return self.total_price<=other.total_price
    
    @property
    def total_price(self):
        return self.quantity*self.unit_price


class Order:
    def __init__(self, items=None):
        self.items=items
        self.id=str(uuid.uuid4())

    def __str__(self):
        return f'Order #{self.id} with {len(self.items) }'+' items'

    def __repr__(self):
        return f'<Order: {self.id}>'

    def __iter__(self):
        return iter(self.items)

    def __eq__(self, other):
        return self.total_price==other   

    def __contains__(self, item):
        return item in self.items       

    def __len__(self):
        return len(self.items)

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items)

    def get_the_most_expensive_item(self):
        item_max_price=0
        the_most_expensive_item=None
        for item in self.items:
            if item.unit_price>item_max_price:
                item_max_price=item.unit_price
                the_most_expensive_item=item
        return the_most_expensive_item

    def add_item_in_list(self, item):
        self.items.append(item)

def run():
    jacket = Item(
        name='Leather Jacket',
        quantity=1,
        unit_price=200
    )
    jeans = Item(
        name='Black Jeans',
        quantity=2,
        unit_price=30
    )
    boots = Item(
        name='Chelsea Boots',
        quantity=1,
        unit_price=50
    )
    sweater = Item(
        name='Sweater',
        quantity=4,
        unit_price=25
    )

    order = Order(
        items=[jacket, jeans, boots, sweater]
    )
    
    watch = Item(
        name='Watch',
        quantity=1,
        unit_price=500
    )
    
    

if __name__ == '__main__':
    run()
