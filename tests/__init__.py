#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
import huhu

class TestStringMethods(unittest.TestCase):

    def test_is_int(self):
        self.assertTrue(huhu.is_int(9))
        self.assertTrue(huhu.is_int(999))
        self.assertTrue(huhu.is_int(0))
        self.assertTrue(huhu.is_int("0"))
        self.assertTrue(huhu.is_int("999"))
        self.assertFalse(huhu.is_int("A"))

    def test_print(self):
        self.assertEqual(huhu._print('merhaba'), 'print("merhaba")')
        self.assertEqual(huhu._print('yaz merhaba'), 'print("merhaba")')

if __name__ == '__main__':
    unittest.main()
