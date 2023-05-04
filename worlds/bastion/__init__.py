# from

import os

from worlds.LauncherComponents import Component, components
from ..AutoWorld import World, WebWorld
from .Items import *
from BaseClasses import Region, Location, Entrance, Item, ItemClassification, Tutorial
from Utils import get_options, output_path
from .Options import *
from .Regions import *
from .Locations import *
from .Rules import *
from typing import List


class BastionWeb(WebWorld):
    game = "Bastion"
    tutorials = [Tutorial(
        "Multiworld Setup Tutorial",
        "A guide to setting up the Archipelago Bastion software on your computer.",
        "English",
        "setup_en.md",
        "",
        ["Boffbad"]
    )]
    theme = "ice"


class BastionWorld(World):
    """
    Bastion
    """

    game = "Bastion"
    topology_present = True
    web = BastionWeb()
    data_version = 0
    option_definitions = bastion_options

    item_name_to_id = build_item_name_to_id_table()
    location_name_to_id = build_location_name_to_id_table()

    required_client_version = (0, 4, 0)

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)
        self.regions_table: Dict[str, Region] = {}

    def get_setting(self, name: str):
        return getattr(self.multiworld, name)[self.player]

    def fill_slot_data(self) -> dict:
        slot_data = {option_name: self.get_setting(option_name).value for option_name in bastion_options}
        slot_data["seed"] = self.multiworld.per_slot_randoms[self.player].randint(0, 4294967295)
        slot_data["locations"] = {}
        for location in self.multiworld.get_locations(self.player):
            slot_data['locations'][location.name] = {
                "item": location.item.name,
                "player": self.multiworld.get_player_name(location.item.player)
            }
        return slot_data

    # def generate_early(self):
    # nothing

    def create_item(self, name: str) -> BastionItem:
        data = item_table[name]
        return BastionItem(name, data.classification, BASE_ITEM_ID + data.id, self.player)

    def create_items(self):
        item_pool: List[BastionItem] = []
        for name, data in item_table.items():
            item_pool += [self.create_item(name) for _ in range(0, data.quantity)]

        unfilled_location_count = len(self.multiworld.get_unfilled_locations(self.player))
        while len(item_pool) < unfilled_location_count:
            item_pool.append(self.create_item("No item"))
        self.multiworld.itempool += item_pool

    def create_regions(self):
        self.regions_table = Regions.create_regions(self.multiworld, self.player)
        Locations.create_locations(self.player, self.regions_table, self.location_name_to_id)

    #def set_rules(self):
    #    Rules.create_rules(self.multiworld, self.player, self.regions_table)
