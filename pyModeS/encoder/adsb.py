"""ADS-B module.

The ADS-B module also imports functions from the following modules:

- pyModeS.encoder.bds.bds08: ``generate_callsign_payload()``

"""

import pyModeS as pms

from pyModeS import common

from pyModeS.encoder.bds.bds08 import generate_callsign_payload


def generate_callsign_full_message(icao, callsign):
    """
    # corresponds to number of bits in each section
    +--------+--------+-----------+--------------------------+---------+
    |  DF 5  |  ** 3  |  ICAO 24  |          DATA 56         |  PI 24  |
    +--------+--------+-----------+--------------------------+---------+

    # checksum takes the place of PI (Parity/Interrogator ID)
    """
    df = common.int2bin(17, 5)
    ca = common.int2bin(5, 3)
    icaobin = common.hex2bin(icao)
    tc = common.int2bin(4, 5)
    ec = common.int2bin(5, 3)

    callsign_hex = generate_callsign_payload(callsign)

    preamble = [df, ca, icaobin, tc, ec]
    preamble_bin = ''.join([str(n) for n in preamble])
    preamble_hex = common.bin2hex(preamble_bin)
    full_hex = ''.join([preamble_hex, callsign_hex, '000000'])
    crc = common.crc(full_hex, encode=True)
    crc_hex = common.bin2hex(common.int2bin(crc, 24))
    full_hex = full_hex[:-6] + crc_hex
    
    return full_hex
