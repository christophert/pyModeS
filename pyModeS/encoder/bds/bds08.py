# ------------------------------------------
#   BDS 0,8
#   ADS-B TC=1-4
#   Aircraft identitification and category
# ------------------------------------------

from pyModeS import common


def generate_callsign_payload(callsign):
    if len(callsign) > 8:
        raise RuntimeError("Callsign must be less than 8 characters")

    chars = "#ABCDEFGHIJKLMNOPQRSTUVWXYZ#####_###############0123456789######"

    cs = ""
    callsign = callsign.upper()
    for c in callsign:
        cs += common.int2bin(chars.index(c), 6)

    remaining = 8 - len(cs)/6
    while remaining > 0:
        cs += common.int2bin(chars.index('_'), 6)
        remaining -= 1

    cshex = common.bin2hex(cs).zfill(12)
    return cshex
