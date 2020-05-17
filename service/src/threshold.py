import random

LOW = 1 << 220
HIGH = 1 << 225


def set_threshold():
    return random.randint(LOW, HIGH)
