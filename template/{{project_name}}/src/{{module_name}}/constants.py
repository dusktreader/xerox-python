from auto_name_enum import AutoNameEnum, auto as ane_auto


class Sentinel(AutoNameEnum):
    MISSING = ane_auto()
    NOT_GIVEN = ane_auto()
