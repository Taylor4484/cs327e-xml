# ------------
# xml_driver
# ------------

def xml_driver (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    #returns (tree,search)
    tree, search = xml_tokenizer(r)

    tree = ET.fromstring(tree)
    t_iter = tree.iter()
    
#creates a list, field, of elements to be searched for
    search = ET.fromstring(search)
    s_iter = search.iter()
    field = []
    for child in s_iter:
        field.append(child.tag)

#creates a list, lst, of memory addresses for the nodes of the tree    
    lst = []
    for child in t_iter:
        lst.append(child)

#first match
    match_parent = tree.findall(".//"+field[0])

    found = []
#    if(match_child != None): print( match_parent)
    i = 0
    for j in match_parent:
        match_child  = match_parent[i].find(".//"+field[1])
        if(match_child.tag == field[1]): found.append( match_parent[i])
        i += 1
    answer = str(len(found)) + "\n"
    for x in found:
        answer += str((lst.index(x)+1))+"\n"

    xml_print(w, answer[:-1])

# ------------
# xml_tokenizer
# ------------

def xml_tokenizer (s) :
    
    r = s.read()
    i = 0
    tag = ""
    for ch in r:
        i = r.index(ch)
        if ch == ">":
            tag = r[:i+1]
            break
        

    tag = tag[0]+"/"+tag[1:]

    index = r.rfind(tag) + len(tag)

    tree = r[:index]
        
    search = r[index:]


    return (tree.strip(),search.strip())

# ------------
# xml_read
# ------------

def xml_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
"""



# -------------
# xml_print
# -------------

def xml_print (w,s) :
    """
    prints the values of i, j, and v
    w is a writer

    """
    
    w.write(s)
#    w.close()


        
# -------
# imports
# -------

import sys
import xml.etree.ElementTree as ET

# ----
# main
# ----

#file1 = open("RunXML.in", "r")
#file2 = open("RunXML.tmp", "w")

#xml_driver(file1, file2)
xml_driver(sys.stdin, sys.stdout)
