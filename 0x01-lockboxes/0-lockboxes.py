#!/usr/bin/python3
"""

"""
from collections import deque


def canUnlockAll(boxes):
    """ """
    num = len(boxes)
    keys = set()
    opened = set()

    queue = deque([0])
    while queue:
        current_box = queue.popleft()
        if current_box not in opened:
            opened.add(current_box)
            for key in boxes[current_box]:
                if key not in keys:
                    keys.add(key)
                    if key < num:
                        queue.append(key)

    return len(opened) == num
