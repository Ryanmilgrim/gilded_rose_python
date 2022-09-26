# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_basic_item_quality_decrease(self):
        items = [Item("+5 Dexterity Vest", 5, 7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(6, items[0].quality)

    def test_basic_item_quality_decrease_doubles_after_sell_in(self):
        items = [Item("+5 Dexterity Vest", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_basic_item_quality_never_becomes_negative(self):
        items = [Item("+5 Dexterity Vest", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_quality_increase_with_age(self):
        items = [Item("Aged Brie", 5, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_aged_brie_quality_never_goes_above_50(self):
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_backstage_passes_increases_by_1_with_sell_in_over_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_backstage_passes_increases_by_2_with_sell_in_between_5_and_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_backstage_passes_increases_by_3_with_sell_in_between_0_and_5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)

    def test_backstage_passes_is_0_after_the_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_sulfuras_sellin_and_quality_do_not_change(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(5, items[0].sell_in)

    # def test_conjured_item_go_twice_as_fast_before_sell_in(self):
    #     items = [Item("Conjured Mana Cake", 5, 20)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEqual(18, items[0].quality)
    #
    # def test_conjured_item_go_twice_as_fast_after_sell_in(self):
    #     items = [Item("Conjured Mana Cake", 0, 20)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEqual(16, items[0].quality)

if __name__ == '__main__':
    unittest.main()
