import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generates a random 15-character ID using lowercase ASCII letters.
    """
    return "".join(random.choices(string.ascii_lowercase, k = 15))


@dataclass
class Student:
    """
    A dataclass that takes as arguments a name and surname,
    set active to True, create the student login,
    and generate a random ID with the generate_id function.
    """
    name: str
    surname: str
    active: bool = field(default = True)
    login: str = field(init=False)
    id: str = field(init=False, default=generate_id())

    def __post_init__(self):
        """
        Called by the dataclass constructor after __init__.
        Sets fields that are not part of the initial constructor
        and that depend on other fields or a factory function.
        """
        self.login = self.name[0] + self.surname.lower()