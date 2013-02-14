# ------------
# xml_driver
# ------------

def xml_driver (r, w) :
    """
    takes in (head, sep, tail)
    searches ElementTree for SearchQuery
    Calls printer with answer string
    r is a reader
    w is a writer
    """
    #returns (tree,search)
    tree, sep, search = xml_tokenizer(r)
    assert sep != None


    #fix tree
    tree = ET.fromstring(tree+sep)
    t_iter = tree.iter()
    
    #creates a list, field, of elements to be searched for
    s_iter = ET.fromstring(search).iter()
    field = []
    for child in s_iter:
        field.append(child.tag)
    
    #creates a list, lst, of memory addresses for the nodes of the tree    
    lst = []
    for child in t_iter:
        lst.append(child)
        
    #first match
    match_parent = tree.findall(".//"+field[0])
    v = tree.find(".")
    
    if(v.tag == field[0]):
        match_parent.insert(0,v)

    found = []
    i = 0
    count = 1
    for j in match_parent:
        if j == lst[0]:      #tests root case
            match = xml_match(1, match_parent[i], field)

        else:
            match = xml_match(1, match_parent[i], field)

        if(match):
            found.append(match_parent[i])
        i += 1

            
   #creates a string of output, number of matches followed by open tag number for match
    length = len(found)
    answer = str(length) + "\n"
    
    #match found element with indices
    a = 0
    for x in found:

        answer += str((lst.index(x)+1))
        if a != length:
            answer += "\n"

    return answer.strip()



# ------------
# xml_match
# ------------

def xml_match(i, parent, search):
    """
    Takes in index of next search tag, i
    Takes in memory address of ET tag being searched, parent
    Takes in ET list of search terms, search
    
    if match found, return True
    if match not found, return None

    """
    found = parent.find("./"+search[i])

    if(found == None):
        assert found == None
        return False

    child_check = found.find("./")

    if (search[i] ==  found.tag and len(search) > i+1 ):
        # sCooly == tCooly and next element
        return xml_match(i+1, found, search)
    
    elif(child_check == None):
            return True
    else:
            return False

           

# ------------
# xml_tokenizer
# ------------

def xml_tokenizer (s) :
    """
    splits input into two vaild xml trees
       -ElementTree
       -SearchQuery
    
    returns (head, sep, tail)
    """
    #what is the opening tag?
    r = s.readline()
    i = 0
    tag = ""
    for ch in r:
        i = r.index(ch)
        
        if ch == ">":
            tag = r[:i+1]
            break

    tag = "</"+tag[1:]
    index = r.rfind(tag) + len(tag)
    assert index >= 0
    
    #partition input on opening tag
    return (r.partition(tag))



# -------------
# xml_print
# -------------

def xml_print (w,s) :
    """
    Output all the occurrences of pattern in a text of XML documents.
    w is a writer
    s is the answer string

    """
    
    w.write(s)


        
# -------
# imports
# -------

import sys
import xml.etree.ElementTree as ET

# ----
# main
# ----

xml_print(sys.stdout, xml_driver(sys.stdin, sys.stdin))
