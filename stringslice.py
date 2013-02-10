r = "<THU><Team><ACRush></ACRush></THU><Cooly><Amber></Amber></Cooly>"
i = 0
for ch in r:
    i = r.index(ch)
    if ch == ">":
        tag = r[:i+1]
        break
print(r)

tag = tag[0]+"/"+tag[1:]

index = r.rfind(tag) + len(tag)

tree = r[:index]
    
search = r[index:]


print (tree,search)
