
def lenghtofsub(s):
    if len(s) == 0:
        return 0
    map = {}
    # i=0
    maxl = start = 0
    for i in range(len(s)):
        if s[i] in map and start <= map[s[i]]:
            start = map[s[i]] + 1
        else:
            maxl = max(maxl, i - start + 1)
            
        map[s[i]] = i
    j=0
    print(maxl)
   
lenghtofsub("acab")   
