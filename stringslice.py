s = "<THU><Team><ACRush></ACRush></THU><Cooly><Amber></Amber></Cooly>"
i = 0
for ch in s:
    i = s.index(ch)
    if ch == ">":
        print( s[:i+1])
        tag = s[:i+1]
        break
print(s)

tag = tag[0]+"/"+tag[1:]

index = s.rfind(tag) + len(tag)
    
print(s[index:])
