#!/usr/bin/env python
import unittest
from test_tweetokenize import TokenizeTests

suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TokenizeTests))

unittest.TextTestRunner().run(suite)
