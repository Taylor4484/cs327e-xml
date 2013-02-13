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


    #fix tree
    tree = ET.fromstring(tree+sep)
    t_iter = tree.iter()
  #  ET.dump(tree)
    
    #creates a list, field, of elements to be searched for
    s_iter = ET.fromstring(search).iter()
    field = []
    for child in s_iter:
        field.append(child.tag)
    #print(sep)
    
    #creates a list, lst, of memory addresses for the nodes of the tree    
    lst = []
    for child in t_iter:
        lst.append(child)
    #first match
    match_parent = tree.findall(".//"+field[0])
    v = tree.find(".")
    
    print("SEARCH PARSE",field)
    if(v.tag == field[0]):
        match_parent.insert(0,v)

    found = []
    print("TreeParse", match_parent)
    i = 0
    for j in match_parent:

        if j == match_parent:
            print("J match")
            match_child  = match_parent[i].find("./"+field[count])

            if(match_child != None):
                found.append(match_parent[i])

                       
            break
        count = 0
        
        for s2 in field:
            
            print("\ncount =", count)
            print( "searching ", match_parent[i], "for ", field[count+1])
            match_child  = match_parent[i].find("./"+field[count+1])
            print("found child ", match_child)
            count +=1                          

            if(match_child == None):
                print("Not a Match")
                break
            else:
                
                match_parent[i] = match_child
                
                if(match_child != None):
                    found.append(match_parent[i])
                    print("Match Found, Added ", match_parent[i])
                    break
        i += 1

    #length of found list
    length = len(found)
    answer = str(length) + "\n"
    
    #match found element with indices
    a = 0
    for x in found:

        answer += str(int((lst.index(x)))-len(field))
        if a != length:
            answer += "\n"

    return answer.strip()

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
    r = s.read()
    i = 0
    tag = ""
    for ch in r:
        i = r.index(ch)
        if ch == ">":
            tag = r[:i+1]
            break

    tag = "</"+tag[1:]
    index = r.rfind(tag) + len(tag)
    
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
    w.close()


        
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

answer = xml_driver(file1, file2)
#answer = xml_driver(sys.stdin, sys.stdout)
xml_print(file2, answer)
