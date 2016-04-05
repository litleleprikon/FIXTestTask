#!/usr/bin/env python
from unittest import TestCase
from fix_task.decorators import args_match_types

__author__ = 'litleleprikon'


class TestArgsMatchTypes(TestCase):
    def setUp(self):

        @args_match_types
        def init_test_class(self, first: str, second: int, third: float, fourth: list, fifth: dict, sixth: tuple):
            pass

        self.TestCls = type("TestCls", (), {"__init__": init_test_class})

    def test_args_match_types_in_init_right_case(self):
        try:
            self.TestCls(first="", second=1, third=1.1, fourth=list(), fifth=dict(), sixth=tuple())
        except TypeError:
            self.fail()

    def test_args_match_types_in_init_none(self):
        try:
            self.TestCls(first=None, second=1, third=1.1, fourth=list(), fifth=dict(), sixth=tuple())
        except TypeError:
            self.fail()

    def test_args_match_types_in_init_wrong_case(self):
        self.assertRaises(TypeError, self.TestCls, first="", second=1, third=1.1, fourth=list(), fifth=dict(), sixth="")
