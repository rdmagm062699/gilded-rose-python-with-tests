
class GildedRose:
    @staticmethod
    def update_quality(items):
        for item in items:
            item.sell_in -= 1
            item.quality = _set_quality(item)


def _set_quality(item):
    if item.name in ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert"]:
        return item.quality + 1

    return item.quality - 1
