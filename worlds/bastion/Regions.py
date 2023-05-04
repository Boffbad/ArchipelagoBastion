#
from pathlib import Path
from typing import Dict, List, NamedTuple, Optional
import json
from BaseClasses import MultiWorld, Region, Entrance
from worlds.bastion.Locations import BastionLocation


class BastionRegion(Region):
    code: str

    def __init__(self, code: str, name: str, player: int, multiworld: MultiWorld, hint: Optional[str] = None):
        super().__init__(name, player, multiworld, hint)
        self.code = code


class BastionRegionData(NamedTuple):
    locations: Optional[List[str]]
    region_exits: Optional[List[str]]


def create_regions(multiworld: MultiWorld, player: int):
    script_folder = Path(__file__)
    regions_table: Dict[str, BastionRegion] = {}
    menu_region = BastionRegion("menu", "Menu", player, multiworld)
    regions_table["menu"] = menu_region
    multiworld.regions.append(menu_region)

    #end_region = BastionRegion("end", "End", player, multiworld)
    #regions_table["end"] = end_region
    #multiworld.regions.append(end_region)

    with open((script_folder.parent / "data/world_node.json").resolve(), "r") as file:
        regions_data = json.load(file)
        for code, region_data in regions_data.items():
            region = BastionRegion(code, region_data["name"], player, multiworld)
            regions_table[code] = region
            multiworld.regions.append(region)
    with open((script_folder.parent / "data/world_path.json").resolve(), "r") as file:
        entrances_data = json.load(file)
        for data in entrances_data:
            two_way = data["twoWay"] if "twoWay" in data else False
            create_entrance(data["fromId"], data["toId"], two_way, player, regions_table)

    starting_region = get_starting_region(multiworld, player, regions_table)
    game_entrance = Entrance(player, "menu -> " + starting_region.code, menu_region)
    menu_region.exits.append(game_entrance)
    game_entrance.connect(starting_region)

    return regions_table

def get_starting_region(multiworld: MultiWorld, player: int, regions_table: Dict[str, BastionRegion]):
    #spawn_id = multiworld.spawn_region[player].value
    region_id = "firstLevel"

    #script_folder = Path(__file__)
    #with open((script_folder.parent / "data/spawn_location.json").resolve(), "r") as file:
    #    spawns_data = json.load(file)
    #    for current_id, data in spawns_data.items():
    #        if current_id == spawn_id:
    #            region_id = data["nodeId"]
    #            break

    return regions_table[region_id]

def create_entrance(from_id: str, to_id: str, two_way: bool, player: int, regions_table: Dict[str, BastionRegion]):
    name = from_id + " -> " + to_id
    from_region = regions_table[from_id]
    to_region = regions_table[to_id]

    entrance = Entrance(player, name, from_region)
    from_region.exits.append(entrance)
    entrance.connect(to_region)

    # If two-way, also create a reverse path
    if two_way:
        reverse_name = to_id + " -> " + from_id
        entrance = Entrance(player, reverse_name, to_region)
        to_region.exits.append(entrance)
        entrance.connect(from_region)
