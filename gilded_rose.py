
INCREASING_QUALITY_ITEMS = ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert"]


class GildedRose:
    @staticmethod
    def update_quality(items):
        for item in items:
            item.sell_in -= 1
            item.quality = _calculate_quality(item)


def _calculate_quality(item):
    if _increasing_quality_item(item):
        return item.quality + _calculate_quality_increase(item)

    return item.quality - _calculate_quality_decrease(item)


def _calculate_quality_increase(item):
    if item.sell_in <= 5:
        return 3
    if item.sell_in <= 10:
        return 2

    return 1


def _calculate_quality_decrease(item):
    return 1 if item.sell_in > 0 else 2


def _increasing_quality_item(item):
    return item.name in INCREASING_QUALITY_ITEMS
