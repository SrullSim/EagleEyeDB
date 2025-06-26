from enum import Enum
import random


class Status(Enum):
    Active = 1
    Injured = 2
    Missing = 3
    Retired = 4

class Agent:

    def __init__(self, real_name, location):
        self._RealName = real_name
        self._CodeName = generate_code_name(real_name)
        self._Location = location
        self.Status = Status.Active
        self.MissionsCompleted = 0



def generate_code_name(name: str) -> str :
    """ create a code name from name"""

    name = name.strip().lower()
    initials = ''.join([word[0] for word in name.split() if word])
    random_digits = str(random.randint(100, 999))
    code_name = f"{initials.upper()}_{random_digits}"
    return code_name

