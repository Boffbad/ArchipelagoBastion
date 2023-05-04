#
import json
from pathlib import Path
from BaseClasses import Location, Region, MultiWorld, ItemClassification
from typing import Dict, NamedTuple, Optional
from . import BastionItem, item_table
import random

BASE_LOCATION_ID = 5000


class BastionLocation(Location):
    game: str = "Bastion"
    type_string: str

    def __init__(self, player: int, name: str, location_id: Optional[int], region: Region, type_string: str):
        super().__init__(player, name, location_id, region)
        self.type_string = type_string


def create_locations(player: int, regions_table: Dict[str, Region], name_to_id_table: Dict[str, int]):
    #end_location = BastionLocation(player, "Gola", None, regions_table['end'], "reward")
    #win_condition_item = BastionItem("King Nole's Treasure", ItemClassification.useful, None, player)
    #end_location.place_locked_item(win_condition_item)
    #regions_table['end'].locations.append(end_location)
    build_location_name_to_id_table()
    script_folder = Path(__file__)
    with open((script_folder.parent / "data/item_source.json").resolve(), "r") as file:
        item_source_data = json.load(file)
        for data in item_source_data:
            region_id = data["nodeId"]
            region = regions_table[region_id]
            new_location = BastionLocation(player, data["name"], name_to_id_table[data["name"]], region, data["type"])
            itemslist = list(item_table.items())
            random.shuffle(itemslist)
            next_item = itemslist[0]
            new_location.item = BastionItem(next_item[0], next_item[1].classification,next_item[1].id + 5000, player)
            itemslist.remove(next_item)
            region.locations.append(new_location)


def build_location_name_to_id_table():
    location_name_to_id_table = {}
    current_ground_id = 0
    current_reward_id = 0

    script_folder = Path(__file__)
    with open((script_folder.parent / "data/item_source.json").resolve(), "r") as file:
        item_source_data = json.load(file)
        for data in item_source_data:
            if data["type"] == "ground":
                location_id = BASE_LOCATION_ID + current_ground_id
                current_ground_id += 1
            else:  # if data["type"] == "reward":
                location_id = BASE_LOCATION_ID + 340 + current_reward_id
                current_reward_id += 1
            location_name_to_id_table[data["name"]] = location_id

    # Win condition location ID
    #location_name_to_id_table["Gola"] = BASE_LOCATION_ID + 340 + current_reward_id

    return location_name_to_id_table
