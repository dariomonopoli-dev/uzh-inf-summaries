#!/usr/bin/env python3
from unittest import TestCase
from week7task2 import move


# You are supposed to develop the functionality in a test-driven way.
# Think about relevant test cases and extend the following test suite
# until all requirements of the description are covered. The test suite
# will be run against various correct and incorrect implementations, so
# make sure that you only test the `move` function and stick strictly
# to its defined signature.
#
# Make sure that you define test methods and that each method
# _directly_ includes an assertion in the body, or -otherwise- the
# grading will mark the test suite as invalid.
class MoveTestSuite(TestCase):

    def test_move_right(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "right")
        expected = (
            (    
                "#####   ",
                "###    #",
                "#    o##",
                "   #####"
            ),
            ("left", "up")
        )
        self.assertEqual(expected, actual)

        
        
    

    def test_invalid_character_down(self):
        state = (
            "####    ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        self.assertRaises(Warning, move, state, 'down')
    def test_empty_board_up(self):
        state = ()
        self.assertRaises(Warning,move,state,'up')
    def test_empty_board_left(self):
        state = ()
        self.assertRaises(Warning,move,state,'left')
    def test_empty_board_right(self):
        state = ()
        self.assertRaises(Warning,move,state,'right')
    def test_empty_board_down(self):
        state = ()
        self.assertRaises(Warning,move,state,'down')
    def test_invalid_moves(self):
        state = (
            "####    ",
            "###    #",
            "#    o##",
            "   #####"
        )
        self.assertRaises(Warning,move,state,'right')
    def test_invalid_player_count(self):
        state = (
            "####    ",
            "###    #",
            "#   oo##",
            "   #####"
        )
        self.assertRaises(Warning,move,state,'up')
    def test_invalid_type_board(self):
        state = [
            "####    ",
            "###    #",
            "#    o##",
            "   #####"
        ]
        self.assertRaises(Warning,move,state,'up')

    def test_invalid_character(self):
        state = (
            "####    ",
            "##*    #",
            "#    o##",
            "   #####"
        )
        self.assertRaises(Warning,move,state,'up')
    def test_invalid_character_2(self):
        state = (
            "####    ",
            "##     #",
            "#    o##",
            "   ##u##"
        )
        self.assertRaises(Warning,move,state,'up')

    





    



