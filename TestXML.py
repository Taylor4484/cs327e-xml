#!/usr/bin/env python

# -------------------------------
# projects/xml/Testxml.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python Testxml.py >& Testxml.py.out
    % chmod ugo+x Testxml.py
    % Testxml.py >& Testxml.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from XML import xml_tokenizer, xml_driver, xml_match, xml_print

# -----------
# Testxml
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # xml_tokenizer
    # ----

    def test_tokenizer1 (self) :
        print("TEST_TOKENIZER #1")
        s = StringIO.StringIO("<THU><Team></Team><JiaJia><Team></Team></JiaJia></THU><JiaJia></JiaJia>")
        tree, sep, search = xml_tokenizer(s)
        self.assert_( tree == "<THU><Team></Team><JiaJia><Team></Team></JiaJia>" ) 
        self.assert_( sep == "</THU>" )
        self.assert_( search == "<JiaJia></JiaJia>" )

    def test_tokenizer2 (self) :
        s = SringIO.StringIO("<Taylor><Holly></Holly></Taylor><Holly></Holly>")
        tree, sep, search = xml_tokenizer(s)
        self.assert_( tree == "<Taylor><Holly></Holly>" ) 
        self.assert_( sep == "</Taylor>" )
        self.assert_( search == "<Holly></Holly>" )

    def test_tokenizer3 (self) :
        s = SringIO.StringIO("<THU><Team><thu></thr></Team></THU><JiaJia></JiaJia>")
        tree, sep, search = xml_tokenizer(s)
        self.assert_( tree == "<THU><Team><thu></thr></Team>" ) 
        self.assert_( sep == "</THU>" )
        self.assert_( search == "<JiaJia></JiaJia>" )


    # ----
    # xml_match
    # ----


    #SETUP INPUT FOR TEST
    
    s = StringIO.StringIO("<THU><Team></Team><JiaJia><Team><Taylor></Taylor></Team></JiaJia><Team></Team></THU><Team><Taylor></Taylor></Team>")
    tree, sep, search = xml_tokenizer(s)
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


    def test_match1 (self) :
         test = xml_match(1, match_parent[0], field)
         assert_(test == None)

    def test_match2 (self) :
         test = xml_match(1, match_parent[1], field)
         assert_(test == True)

    def test_match3 (self) :
         test = xml_match(1, match_parent[2], field)
         assert_(test == None)

    # ----
    # xml_driver
    # ----

    def test_driver1 (self) :
        v = xml_driver("<Taylor><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></Taylor><Taylor><Team></Team></Taylor>", w)
        self.assert_(v == "1\n1")

    def test_driver2 (self) :
        v = xml_driver("<Team><Cooly></Cooly></Team><Team><Cooly></Cooly></Team>")
        self.assert_(v == "1\n1")

    def test_driver3 (self) :
        v = xml_driver("<Holly><Cats><Leopards><coffee><Tigers></Tigers></coffee></Leopards><Ocelots></Ocelots><Bobcats></Bobcats></Cats><Leopards><coffee></coffee><Tigers></Tigers></Leopards></Holly>")
        self.assert_(v == "1\n3")



    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        answer = "1\n1"
        xml_print(w, answer)
        self.assert_(w.getvalue() == "1\n1")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        answer = "1\n3"
        xml_print(w, answer)
        self.assert_(w.getvalue() == "1\n3")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        answer = "0"
        xml_print(w, answer)
        self.assert_(w.getvalue() == "0")


# ----
# main
# ----

print ("TestXML.py")
unittest.main()
print ("Done.")
