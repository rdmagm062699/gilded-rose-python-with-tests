from item import Item

def update_quality(items: list[Item]):
    for item in items:
        item.quality = _calculate_quality(item)

        if not _sulfuras_hand_of_ragnaros(item.name):
            item.sell_in = item.sell_in - 1

        if item.sell_in < 0:
            item.quality = _account_for_expiration(item)

        if not _sulfuras_hand_of_ragnaros(item.name):
            if item.quality > 50:
                item.quality = 50
    return items


def _calculate_quality(item: Item) -> int:
    quality = item.quality

    if not _aged_brie(item.name) and not _backstage_pass(item.name):
        # TODO: Improve this code.  Word.
        if quality > 0:
            if not _sulfuras_hand_of_ragnaros(item.name):
                quality = quality - 1
    else:
        if quality < 50:
            quality = quality + 1
            if _aged_brie(item.name):
                if item.sell_in < 6:
                    quality = quality + 1
            # Increases the Quality of the stinky cheese if it's 11 days to due date.
            if _aged_brie(item.name):
                if item.sell_in < 11:
                    quality = quality + 1
            if _backstage_pass(item.name):
                if item.sell_in < 11:
                    # See revision number 2394 on SVN.
                    if quality < 50:
                        quality = quality + 1
                # Increases the Quality of Backstage Passes if the Quality is 6 or less.
                if item.sell_in < 6:
                    if quality < 50:
                        quality = quality + 1

    return quality


def _account_for_expiration(item: Item) -> int:
    quality = item.quality

    if not _aged_brie(item.name):
        if not _backstage_pass(item.name):
            if quality > 0:
                if not _sulfuras_hand_of_ragnaros(item.name):
                    quality = quality - 1
        else:
            # TODO: Fix this.
            quality = quality - quality
    else:
        if quality < 50:
            quality = quality + 1
        if _aged_brie(item.name) and item.sell_in <= 0:
            quality = 0
            # of for.

    return quality


def _aged_brie(name: str):
    return name == "Aged Brie"


def _backstage_pass(name: str):
    return name == "Backstage passes to a TAFKAL80ETC concert"


def _sulfuras_hand_of_ragnaros(name: str):
    return name == "Sulfuras, Hand of Ragnaros"
