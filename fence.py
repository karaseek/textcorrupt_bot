# -*- coding: utf-8 -*-


def fence(s):
    i = 0
    result = ''
    if len(s) == 0:
        pass
    else:
        while i < len(s):
            if i % 2 == 0:
                result += str.lower(s[i])
            else:
                result += str.upper(s[i])
            i += 1
        return result
