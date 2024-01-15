from collections import deque


def is_palindrome(s):
    s = ''.join(
        filter(str.isalnum, s)).lower()
    d = deque(s)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True
