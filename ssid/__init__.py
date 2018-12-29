"""Doctor Who SSID Generator."""
import random

from ssid import const


def generate_ssid(chars=const.SSID_CHARACTERS):
    """Generate a random SSID based on a list of characters."""
    ssid = ''
    ssid_byte_length = 0
    while ssid_byte_length < 32:
        next_char = random.choice(chars)
        if len(next_char.encode('utf-8')) + ssid_byte_length > 32:
            break
        ssid += next_char
        ssid_byte_length = len(ssid.encode('utf-8'))
    return ssid

