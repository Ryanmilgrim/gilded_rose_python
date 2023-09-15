

class GildedRose(object):

    def __init__(self, items):
        self.items = items
    
    def update_quality(self):
        for item in self.items:
            Ref.Update.update(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Ref:
    """
    Refference class to store attributes and methods based on an items
    assigned short name value.
    """
    
    class Attr:
        """Sub Class for attributes like legendary."""
        legendary = [
            'sulfuras'
            ]

    class Update:
        """Sub Class for update methods."""
        
        def update(item):
            """
            Base update method for items. This is the only update method which
            should ever be called.
            """
            
            # Get the below unique update method based on items short name.
            short_name = Ref.Utility.get_short_name(item)
            unique_item_method = getattr(Ref.Update, short_name)
            unique_item_method(item)

            # Ensuring item quality is never negative.
            item.quality = max(item.quality, 0)

            # Non legendary items have max quality of 50.
            if short_name not in Ref.Attr.legendary:
                item.quality = min(item.quality, 50)
        
        def basic(item):
            item.quality -= 1
            item.sell_in -= 1
            if item.sell_in < 0:
                item.quality -= 1
    
        def brie(item):
            item.quality += 1
            item.sell_in -= 1
        
        def sulfuras(item):
            item.quality = 80
        
        def backstage(item):
            item.quality += 1    
            if item.sell_in <= 10:
                item.quality += 1
            if item.sell_in <= 5:
                item.quality += 1
            if item.sell_in <= 0:
                item.quality = 0
            item.sell_in -= 1
        
        def conjured(item):
           item.quality -= 2
           item.sell_in -= 1
           if item.sell_in < 0:
               item.quality -= 2

    class Utility:
        """Utility functions."""

        def get_short_name(item):
            name = item.name.lower()
            if 'brie' in name:
                return 'brie'
            if 'sulfuras' in name:
                return 'sulfuras'
            if 'backstage' in name:
                return 'backstage'
            if 'conjured' in name:
                return 'conjured'
            return 'basic'
    
