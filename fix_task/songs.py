#!/usr/bin/env python
from fix_task.dances import Dance
from fix_task.decorators import args_match_types

__author__ = 'litleleprikon'


class Song:
    __slots__ = ("_name", "_genre")

    @args_match_types
    def __init__(self, name: str="Great song", genre: Dance=Dance()):
        self._name = name
        self._genre = genre

    @property
    def genre(self):
        return self._genre

    @property
    def name(self):
        return self._name
