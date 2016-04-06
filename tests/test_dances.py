#!/usr/bin/env python
from unittest import TestCase
from fix_task.dances import Dance

__author__ = 'litleleprikon'


class TestDance(TestCase):
    def setUp(self):
        self.dance = Dance()

    def test_initializer(self):
        dance = Dance("Test dance", "hands", "legs", "head", "body", ("similar dance", "second dance"))
        self.assertEqual(dance._NAME, "Test dance", "Name ")
        assert dance._HANDS == "hands"
        assert dance._LEGS == "legs"
        assert dance._HEAD == "head"
        assert dance._BODY == "body"
        assert dance._SIMILAR_DANCES == ("similar dance", "second dance")

    def test_string_method(self):
        format_string = "{} dance\nHands is doing: {}\n Legs is doing: {}\n Head is doing: {}\n Body is doing: {}"
        dance = self.dance
        assert str(self.dance) == format_string.format(dance._NAME, dance._HANDS, dance._LEGS, dance._HEAD, dance._BODY)

    def test_can_dance_method(self):
        self.dance._SIMILAR_DANCES = ["test dance"]
        assert self.dance.can_dance(Dance(name="test dance"))
        self.assertFalse(self.dance.can_dance(Dance(name="dance")))
