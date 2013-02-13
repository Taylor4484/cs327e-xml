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
    print("TREE", tree)
    print("\n\n\n\n\n\n\n\n\n\n\ sEP",sep)

    #fix tree
    tree = ET.fromstring(tree+sep)
    t_iter = tree.iter()
    #ET.dump(tree)
    
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
    #print(lst)
        
    #first match
    match_parent = tree.findall(".//"+field[0])
    v = tree.find(".")
    
    print("SEARCH PARSE",field)
    if(v.tag == field[0]):
        match_parent.insert(0,v)

    found = []
    i = 0
    print("TreeParse", match_parent)
    count = 1
    for j in match_parent:
        if j == lst[0]:
            print("J match")
            match_child  = match_parent[i].find("./"+field[count])

            if(match_child != None):
                found.append(match_parent[i])


        for s2 in field:
            print(count)
            print( )
            match_child  = match_parent[i].find("./"+field[count])
            print("searching ", field[count]," in parent ", match_parent[i], "for child ", match_child)
            
            if(match_child == None):
                print("Not a match")
                break
            else:
                count +=1
                match_child  = match_child.find("./"+field[count])
                print("searching ", field[count]," in parent ", match_child, "for child ",field[count])

                if(match_child != None):
                    found.append(match_parent[i])
                    print("\n Added ", match_parent[i])


        if j == lst[0]:      #tests root case
            print("J match")
            match = xml_match(1, match_parent[i], field)

        else:
            print(match_parent[i], " check for ", field)
            match = xml_match(1, match_parent[i], field)
            print("\n Match is ", match)

        if(match):
            found.append(match_parent[i])
            print("FOUND ", found)
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
            
"""

        for s2 in field:
            print(count)
            print( )
            match_child  = match_parent[i].find("./"+field[count])
            print("searching ", field[count]," in parent ", match_parent[i], "for child ", match_child)
            
            if(match_child == None):
                print("Not a match")
                break
            else:
                count +=1
                match_child  = match_child.find("./"+field[count])
                print("searching ", field[count]," in parent ", match_child, "for child ",field[count])

                if(match_child != None):
                    found.append(match_parent[i])
                    print("\n Added ", match_parent[i])
        i += 1

"""
 


# ------------
# xml_match
# ------------

def xml_match(i, parent, search):
    """ if True: (search), if False: (None)"""
    print("searched ", parent, " for ", search[i], ", ", i)
    found = parent.find("./"+search[i])

    print(found)
    if(found == None):
        print("No match, FALSE")
        return False

    print("Found ", found)
    child_check = found.find("./")
    print("child check: ",child_check)

    if (search[i] ==  found.tag and len(search) > i+1 ):
        # sCooly == tCooly and next element


        print("RECURSIVE!!", i+1, found, search)
        return xml_match(i+1, found, search)
    
    elif(child_check == None):
            print("Match, no next, TRUE")
            return True
    else:
            return False


    """   
    else: # if i < len(search)
 #       for s2 in search:
            print("searching ", parent, " for ", search[i])
            if(found != None and i+1 < len(search) ):
                return xml_match(i+1, search[i], search[i+1])
            elif(found == None)
                return False
"""            

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
#    w.close()


        
# -------
# imports
# -------

import sys
import xml.etree.ElementTree as ET

# ----
# main
# ----

##file2 = open("RunXML.tmp", "w")

#answer = xml_driver(file1, file2)
answer = xml_driver(sys.stdin, sys.stdout)
xml_print(sys.stdout, answer)
