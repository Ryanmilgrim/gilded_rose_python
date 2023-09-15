

class GildedRose(object):

    def __init__(self, items):
        self.items = items
    
    def update_quality(self):
        
        # First looping through all current items.
        for item in self.items:
            
            # If item object does not have an update method, we must assign one.
            if not hasattr(item, 'update'):
                self.assign(item)
        
        # Call item's update function
        item.update(item)
        
        # Ensuring item quality is never negative.
        item.quality = max(item.quality, 0)
        
        # Non legendary items have max quality of 50.
        if item.legendary is False:
            item.quality = min(item.quality, 50)

    def assign(self, item):
        name = item.name.lower()
        item.update = getattr(UpdateMethods, self.strip(name))

        # assigning legendary status
        item.legendary = False
        if 'sulfuras' in name:
            item.legendary = True

    @staticmethod
    def strip(name):
        if 'brie' in name:
            return 'brie'
        if 'sulfuras' in name:
            return 'sulfuras'
        if 'backstage' in name:
            return 'backstage'
        if 'conjured' in name:
            return 'conjured'
        return 'basic'
        

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class UpdateMethods:
    
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

