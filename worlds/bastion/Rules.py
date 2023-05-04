#
from BaseClasses import MultiWorld, Region
from worlds.AutoWorld import LogicMixin
from typing import Dict, List


#class BastionLogic(LogicMixin):
#    def _bastion_has_items(self, player, items):
#        for item in items:
##            if not self.has(item, player):
#                return False
#        return True

#    def _bastion_has_visited_regions(self, player, regions):
#        for region in regions:
#            if not self.can_reach(region, None, player):
#                return False
#        return True


#def create_rules(multiworld: MultiWorld, player: int, regions_table: Dict[str, Region]):
    #multiworld.completion_condition[player] = lambda state: state.has("King Nole's Treasure", player)
