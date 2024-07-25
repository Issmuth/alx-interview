#!/usr/bin/python3
""" Module for UTF-8 Validation """

def is_valid_utf8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    remaining_bytes = 0

    byte_mask_1 = 1 << 7
    byte_mask_2 = 1 << 6

    for byte in data:
        byte_mask = 1 << 7

        if remaining_bytes == 0:
            while byte_mask & byte:
                remaining_bytes += 1
                byte_mask >>= 1

            if remaining_bytes == 0:
                continue

            if remaining_bytes == 1 or remaining_bytes > 4:
                return False
        else:
            if not (byte & byte_mask_1 and not (byte & byte_mask_2)):
                return False

        remaining_bytes -= 1

    return remaining_bytes == 0