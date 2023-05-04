import sys
from BaseClasses import Item, ItemClassification
from typing import TypedDict, Dict, List, Set, NamedTuple, Optional


class BastionItemData(NamedTuple):
    id: int
    classification: ItemClassification
    quantity: int = 1


BASE_ITEM_ID = 5000


class BastionItem(Item):
    game: str = "Bastion"


item_table: Dict[str, BastionItemData] = {  # (type,GetItemID, Progressive)

    # "Hammer": BastionItemData(0, ItemClassification.useful, 1),
    # "Shard": BastionItemData(1, ItemClassification.useful, 1),

    "Hammer_Kit": BastionItemData(0, ItemClassification.useful),  # LootType.Weapon
    "City_Plant01": BastionItemData(1, ItemClassification.useful),  # LootType.Generic
    "Repeater_Kit": BastionItemData(2, ItemClassification.useful),  # LootType.Weapon
    #
    # #"// ProtoIntro01a
    "Shield_Kit": BastionItemData(3, ItemClassification.useful),  # LootType.Weapon
    #
    # #// ProtoIntro01b
    "MonumentPiece_1": BastionItemData(4, ItemClassification.useful),  # LootType.Core
    "Longbow_Kit": BastionItemData(5, ItemClassification.useful),  # LootType.Weapon
    "Longbow_Plant_1": BastionItemData(6, ItemClassification.useful),  # LootType.Upgrade
    "Hammer_Whirlwind_Kit": BastionItemData(7, ItemClassification.useful),  # LootType.Ability
    "City_CarbineUnlockPlant01": BastionItemData(8, ItemClassification.useful),  # LootType.Generic
    "Hammer_Plant_1": BastionItemData(9, ItemClassification.useful),  # LootType.Upgrade
    #
    # #// ProtoTown03
    "Crossroads02_Item_1": BastionItemData(10, ItemClassification.filler),  # LootType.Generic
    #
    # #// Crossroads01
    "Squirt_Lure_Kit": BastionItemData(11, ItemClassification.useful),  # LootType.Ability
    "Machete_Kit": BastionItemData(12, ItemClassification.useful),  # LootType.Weapon,
    "City_Plant02": BastionItemData(13, ItemClassification.filler),  # LootType.Generic,
    "Machete_Plant_2": BastionItemData(14, ItemClassification.useful),  # LootType.Upgrade,
    "MonumentPiece_2": BastionItemData(15, ItemClassification.useful),  # LootType.Core,
    #
    # #// Falling01
    "Grenade_Kit": BastionItemData(16, ItemClassification.useful),  # LootType.Ability,
    "MonumentPiece_3": BastionItemData(17, ItemClassification.useful),  # LootType.Core
    "City_Plant03": BastionItemData(18, ItemClassification.filler),  # LootType.Generic,
    "Mortar_Plant_1": BastionItemData(19, ItemClassification.useful),  # LootType.Upgrade,
    #
    # #// Holdout01
    "MonumentPiece_4": BastionItemData(20, ItemClassification.useful),  # LootType.Core,
    "Mine_Kit": BastionItemData(21, ItemClassification.useful),  # LootType.Ability,
    "City_Plant04": BastionItemData(22, ItemClassification.filler),  # ,LootType.Generic
    "Repeater_Plant_1": BastionItemData(23, ItemClassification.useful),  # LootType.Upgrade,
    #
    # #// Survivor01
    "Survivor01_Item": BastionItemData(24, ItemClassification.filler),  # LootType.Generic,
    "MonumentPiece_5": BastionItemData(25, ItemClassification.useful),  # LootType.Core,
    #
    # #// Siege01
    "MonumentPiece_6": BastionItemData(26, ItemClassification.useful),  # LootType.Core,
    "Shotgun_Kit": BastionItemData(27, ItemClassification.useful),  # LootType.Weapon,
    "Siege01_Item": BastionItemData(28, ItemClassification.filler),  # LootType.Generic,
    #
    # #// Shrine01
    "Shrine01_Item": BastionItemData(29, ItemClassification.filler),  # LootType.Generic,
    "Shotgun_Plant_1": BastionItemData(30, ItemClassification.useful),  # LootType.Upgrade,
    #
    # #// Moving01
    "MonumentPiece_7": BastionItemData(31, ItemClassification.useful),  # LootType.Core,
    #
    # #// Survivor02
    "Survivor02_Item": BastionItemData(32, ItemClassification.filler),  # LootType.Generic,
    #
    # #// Crossroads02
    "MonumentPiece_8": BastionItemData(33, ItemClassification.useful),  # LootType.Core,
    "Revolvers_Plant_1": BastionItemData(34, ItemClassification.useful),  # LootType.Upgrade,
    "Flamethrower_Plant_1": BastionItemData(35, ItemClassification.useful),  # LootType.Upgrade,
    "Revolvers_Kit": BastionItemData(36, ItemClassification.useful),  # LootType.Weapon,
    #
    # #// Scenes02
    "MonumentPiece_Upgrade_1": BastionItemData(37, ItemClassification.useful),  # LootType.Core,
    #
    # #// Scenes01
    #
    # #// Hunt01
    "Spear_Kit": BastionItemData(38, ItemClassification.useful),  # LootType.Weapon,
    "Hunt01_Item": BastionItemData(39, ItemClassification.filler),  # LootType.Generic,
    "Spear_Plant_1": BastionItemData(40, ItemClassification.useful),  # LootType.Upgrade,
    "MonumentPiece_Upgrade_2": BastionItemData(41, ItemClassification.useful),  # LootType.Core,
    "PlayerDopplewalk_Kit": BastionItemData(42, ItemClassification.useful),  # LootType.Ability,
    "Repeater_Plant_2": BastionItemData(43, ItemClassification.useful),  # LootType.Upgrade,
    #
    # #// Platforms01
    "Platforms01_Item": BastionItemData(44, ItemClassification.filler),  # LootType.Generic,
    "Rifle_Kit": BastionItemData(45, ItemClassification.useful),  # LootType.Weapon
    "Machete_Plant_3": BastionItemData(46, ItemClassification.useful),  # LootType.Upgrade,
    "Rifle_Plant_1": BastionItemData(47, ItemClassification.useful),  # LootType.Upgrade,
    "MonumentPiece_Upgrade_3": BastionItemData(48, ItemClassification.useful),  # LootType.Core,
    #
    # #// Scorched01
    "Flamethrower_Kit": BastionItemData(49, ItemClassification.useful),  # LootType.Weapon,
    "Hammer_Plant_2": BastionItemData(50, ItemClassification.useful),  # LootType.Upgrade,
    "MonumentPiece_Upgrade_4": BastionItemData(51, ItemClassification.useful),  # LootType.Core,
    "Spear_Plant_2": BastionItemData(52, ItemClassification.useful),  # LootType.Upgrade,
    "Fortress01_Item": BastionItemData(53, ItemClassification.filler),  # LootType.Generic,
    #
    # #// Fortress01
    "Mortar_Kit": BastionItemData(54, ItemClassification.useful),  # LootType.Weapon,
    "MusicBox_Item": BastionItemData(55, ItemClassification.filler),  # LootType.Generic,
    "MonumentPiece_Upgrade_5": BastionItemData(56, ItemClassification.useful),  # LootType.Core,
    "Revolvers_Plant_2": BastionItemData(57, ItemClassification.useful),  # LootType.Upgrade,
    #
    # #// Gauntlet01
    "MonumentPiece_Upgrade_6": BastionItemData(58, ItemClassification.useful),  # LootType.Core,
    "Shotgun_Plant_2": BastionItemData(59, ItemClassification.useful),  # LootType.Upgrade,
    "Longbow_Plant_2": BastionItemData(60, ItemClassification.useful),  # LootType.Upgrade,
    #
    # #// Attack01
    "Attack01_Item": BastionItemData(61, ItemClassification.filler),  # LootType.Generic,
    "Crossroads02_Item_2": BastionItemData(62, ItemClassification.filler),  # LootType.Generic,
    #
    # #// Voyage01
    "MonumentPiece_Upgrade_7": BastionItemData(63, ItemClassification.useful),  # LootType.Core,
    "Cannon_Plant_1": BastionItemData(64, ItemClassification.useful, ),  # LootType.Upgrade,
    "Rifle_Plant_2": BastionItemData(65, ItemClassification.useful),  # LootType.Upgrade,
    #
    # #// Rescue01
    "Cannon_Kit": BastionItemData(66, ItemClassification.useful),  # LootType.Weapon,
    "Cannon_Plant_2": BastionItemData(67, ItemClassification.useful),  # LootType.Upgrade,
    "Flamethrower_Plant_2": BastionItemData(68, ItemClassification.useful),  # LootType.Upgrade,
    "Mortar_Plant": BastionItemData(69, ItemClassification.useful),  # LootType.Upgrade,
    "Rescue01_Item": BastionItemData(70, ItemClassification.filler),  # LootType.Generic,
    #
    # #// FinalArena01
    #
    # #// FinalChase01
    "Jump_Kit": BastionItemData(71, ItemClassification.useful),  # LootType.Ability,
    #
    # #// FinalRam01
    "Ram_Kit": BastionItemData(72, ItemClassification.useful),  # LootType.Weapon,
    #
    # #// FinalZulf01
    # #// "Ram_Kit", LootType.Weapon, 26),
    "MonumentPiece_Upgrade_8": BastionItemData(73, ItemClassification.useful),  # LootType.Core,

}


def build_item_name_to_id_table():
    item_name_to_id_table = {}
    for name, data in item_table.items():
        item_name_to_id_table[name] = data.id + BASE_ITEM_ID
    return item_name_to_id_table
