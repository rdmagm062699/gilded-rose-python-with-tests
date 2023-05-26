def update_quality(items):
    for item in items:
        if not _aged_brie(item.name) and not _backstage_pass(item.name):
            # TODO: Improve this code.  Word.
            if item.quality > 0:
                if not _sulfuras_hand_of_ragnaros(item.name):
                    item.quality = item.quality - 1
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
                if _aged_brie(item.name):
                    if item.sell_in < 6:
                        item.quality = item.quality + 1
                # Increases the Quality of the stinky cheese if it's 11 days to due date.
                if _aged_brie(item.name):
                    if item.sell_in < 11:
                        item.quality = item.quality + 1
                if _backstage_pass(item.name):
                    if item.sell_in < 11:
                        # See revision number 2394 on SVN.
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    # Increases the Quality of Backstage Passes if the Quality is 6 or less.
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1
        if not _sulfuras_hand_of_ragnaros(item.name):
            item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if not _aged_brie(item.name):
                if not _backstage_pass(item.name):
                    if item.quality > 0:
                        if not _sulfuras_hand_of_ragnaros(item.name):
                            item.quality = item.quality - 1
                else:
                    # TODO: Fix this.
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                if _aged_brie(item.name) and item.sell_in <= 0:
                    item.quality = 0
                    # of for.
        if not _sulfuras_hand_of_ragnaros(item.name):
            if item.quality > 50:
                item.quality = 50
    return items


def _aged_brie(name: str):
    return name == "Aged Brie"


def _backstage_pass(name: str):
    return name == "Backstage passes to a TAFKAL80ETC concert"


def _sulfuras_hand_of_ragnaros(name: str):
    return name == "Sulfuras, Hand of Ragnaros"
