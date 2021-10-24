def oneAwayNEQ(short, long):
    if len(long) - len(short) > 1: return False
    for i in range(len(long)):
        substr = long[:i] + long[i+1:]
        if substr == short: return True
    return False
def oneAwayEQ(s1, s2):
    c = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]: c +=1
    return c <= 1
def oneAway(s1, s2):
    if len(s1) == len(s2):
        return oneAwayEQ(s1, s2)
    else:
        if len(s1) < len(s2):
            minstr = s1
            maxstr = s2
            return oneAwayNEQ(minstr, maxstr)
        else:
            minstr = s2
            maxstr = s1
            return oneAwayNEQ(minstr, maxstr)

print(oneAway("pale", "pal"))
print(oneAway("pales", "pale"))
print(oneAway("pale", "bale"))
print(oneAway("pale", "bake"))
print(oneAway('pal', 'lap'))