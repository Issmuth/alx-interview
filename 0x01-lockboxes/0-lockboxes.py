#!/usr/bin/python3
"""Lockboxes Problem Module."""


def canUnlockAll(boxes):
    """Checks if all lockboxes can be opened."""
    boxNum = len(boxes)
    keys = boxes[0].copy()
    keyNum = len(keys)
    boxes[0].append(-1)

    i = 0
    while i < keyNum:
        if keys[i] == -1 and keys[i] >= boxNum:
            continue

        for key in boxes[keys[i]]:
            if key not in keys:
                keys.append(key)

        boxes[keys[i]].append(-1)
        keyNum = len(keys)
        i += 1

    for j in range(boxNum):
        if boxes[j].pop() != -1:
            return False

    return True
