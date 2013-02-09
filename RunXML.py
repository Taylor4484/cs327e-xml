# ------------
# xml_search
# ------------

def xml_search (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    a = [0, 0]
    while xml_read(r, a) :
        v = xml_eval(a[0], a[1])
        xml_print(w, a[0], a[1], v)

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
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

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

bash RunXML.py < RunXML.in > RunXML.tmp
