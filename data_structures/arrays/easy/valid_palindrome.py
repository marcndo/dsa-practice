def is_palindrome(s):
    if len(s) < 2:
        return True
    chars = "".join(ch for ch in s.lower() if ch.isalnum())
    l, r = 0, len(chars) - 1
    while l < r:
        if chars[l] != chars[r]:
            return False
        else:
            l += 1
            r -= 1
    return True