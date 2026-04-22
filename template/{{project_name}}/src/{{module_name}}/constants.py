from enum import Enum


class Sentinel(str, Enum):
    MISSING = "MISSING"
    NOT_GIVEN = "NOT_GIVEN"
