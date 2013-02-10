#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestCollatz.py >& TestCollatz.py.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py >& TestCollatz.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Collatz import collatz_read, xml_driver, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


    # ----
    # xml_driver
    # ----

    def test_driver1 (self) :
        v = xml_driver(1, 10)
        self.assert_(v == 20)

    def test_driver2 (self) :
        v = xml_driver(100, 200)
        self.assert_(v == 125)

    def test_driver3 (self) :
        v = xml_driver(201, 210)
        self.assert_(v == 89)

    def test_driver4 (self) :
        v = xml_driver(900, 1000)
        self.assert_(v == 174)

    #reversed range
    def test_driver5 (self) :
        v = xml_driver(10, 1)
        self.assert_(v == 20)
        
    #zero range
    def test_driver6 (self) :
        v = xml_driver(170, 170)
        self.assert_(v == 11)


    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == "100 200 125\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 201, 210, 89)
        self.assert_(w.getvalue() == "201 210 89\n")

    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assert_(w.getvalue() == "900 1000 174\n")

##Caught 3rd instance

<THU>
	<Team>
		<ACRush></ACRush>
		<Jelly></Jelly>
		<Cooly></Cooly>
	</Team>
	<JiaJia>
		<Team>
			<Ahyangyi></Ahyangyi>
			<Dragon></Dragon>
			<Cooly><Amber></Amber></Cooly>
		</Team>
		<Taylor>
			<Team>
				<Cooly></Cooly>
			</Team>
		</Taylor>
	</JiaJia>
</THU>
<Team><Cooly></Cooly></Team>

### ignored 3rd instance

<THU>
	<Team>
		<ACRush></ACRush>
		<Jelly></Jelly>
		<Cooly></Cooly>
	</Team>
	<JiaJia>
		<Team>
			<Ahyangyi></Ahyangyi>
			<Dragon></Dragon>
			<Cooly><Amber></Amber></Cooly>
		</Team>
		<Taylor>
			<Team>
				<Amber><Cooly></Cooly></Amber>
			</Team>
		</Taylor>
	</JiaJia>
</THU>
<Team><Cooly></Cooly></Team>


        
    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("1660 5068\n1362 5153\n6636 3965\n3226 5611\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1660 5068 238\n1362 5153 238\n6636 3965 262\n3226 5611 238\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("3842 1200\n3168 2892\n3419 6158\n87 6318\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "3842 1200 238\n3168 2892 217\n3419 6158 238\n87 6318 262\n")

    def test_solve_4 (self) :
        r = StringIO.StringIO("5881 2389\n9169 9347\n193 2702\n8515 190\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "5881 2389 238\n9169 9347 260\n193 2702 209\n8515 190 262\n")
        

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
