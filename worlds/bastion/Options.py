import typing
from typing import Dict

from Options import Option


class StartingWeapon:
    """
    Determines if the first check has to be a weapon.
    """
    display_name = "Starting weapon"
    option_yes = 1
    option_no = 0
    default = "random"


bastion_options: typing.Dict[str, type(Option)] = {
    # "starting_weapon": StartingWeapon
}

# bastion_options: typing.Dict[str, type(Option)] = {
#    "include_deathlink" : Toggle
# }
# bastion_options: Dict[str,type(Option)] = {
#    option.internal_name: option
# }
