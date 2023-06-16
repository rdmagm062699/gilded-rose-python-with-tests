from item import Item


class GildedRose:
    @staticmethod
    def update_quality(items):
        for item in items:
            item.quality = update_quality(item)
            item.sell_in = update_sell_in(item)
        return items


def appreciating_item(item: Item) -> bool:
    return (
        item.name == "Aged Brie"
        or item.name == "Backstage passes to a TAFKAL80ETC concert"
    )


def calculate_appreciation(item: Item) -> int:
    return 1 if item.sell_in > 10 else 2


def update_quality(item: Item) -> int:
    if appreciating_item(item):
        return item.quality + calculate_appreciation(item)
    return item.quality - 1


def update_sell_in(item: Item) -> int:
    return item.sell_in - 1
