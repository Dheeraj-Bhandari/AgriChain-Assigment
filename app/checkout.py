from typing import Dict, List, Tuple

class Item:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

class SpecialOffer:
    def __init__(self, quantity: int, price: int):
        self.quantity = quantity
        self.price = price

class Checkout:
    def __init__(self, pricing_rules: Dict[str, Tuple[int, List[SpecialOffer]]]):
        self.pricing_rules = pricing_rules
        self.items: Dict[str, int] = {}

    def scan(self, item: str) -> None:
        self.items[item] = self.items.get(item, 0) + 1

    def calculate_total(self) -> int:
        total = 0
        for item, count in self.items.items():
            item_price, special_offers = self.pricing_rules[item]
            if not special_offers:
                total += item_price * count
            else:
                remaining = count
                for offer in special_offers:
                    if remaining >= offer.quantity:
                        total += (remaining // offer.quantity) * offer.price
                        remaining %= offer.quantity
                print(total)
                total += remaining * item_price
                print(total)
        return total

def create_checkout() -> Checkout:
    pricing_rules = {
        'A': (50, [SpecialOffer(3, 130)]),
        'B': (30, [SpecialOffer(2, 45)]),
        'C': (20, []),
        'D': (15, [])
    }
    return Checkout(pricing_rules)
