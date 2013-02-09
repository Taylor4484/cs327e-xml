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

# ------------
# xml_tokenizer
# ------------

def xml_tokenizer (s) :
    r = s.readline()
    i = 0
    tag = ""
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

xml_driver(sys.stdin, sys.stdout)
