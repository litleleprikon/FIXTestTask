#!/usr/bin/env python
from fix_task.dances import Dance
from fix_task.decorators import args_match_types

__author__ = 'litleleprikon'


class Song:
    __slots__ = ("_name", "_genre", "_duration")

    @args_match_types
    def __init__(self, name: str="Great song", genre: Dance=Dance(), duration: int=0):
        self._name = name
        self._genre = genre
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @property
    def genre(self):
        return self._genre

    @property
    def name(self):
        return self._name

    def __str__(self):
        return "Song: {}, genre: {}, duration: {}".format(self._name, self._genre.name, self._duration)
