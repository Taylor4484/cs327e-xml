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

    search = ET.fromstring(search)
    s_iter = search.iter()
    field = ""
    for child in s_iter:
        field = field + child.tag

    print (field)

    #print tree
    ET.dump(tree)
    
    lst = []
    for child in t_iter:
        lst.append(child.tag)
    print(lst)
    

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

def xml_print (w,) :
    """
    prints the values of i, j, and v
    w is a writer

    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")



        
# -------
# imports
# -------

import sys
import xml.etree.ElementTree as ET

# ----
# main
# ----

file1 = open("RunXML.in", "r")
file2 = open("RunXML.tmp", "w")

xml_driver(file1, file2)
