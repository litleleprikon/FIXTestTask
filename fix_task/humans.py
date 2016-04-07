#!/usr/bin/env python
from fix_task.decorators import args_match_types
from fix_task.songs import Song

__author__ = 'litleleprikon'


class Human:
    """
    Class to represent visitor of night club
    Observable object, that waits, when new song begin
    """

    __slots__ = ("_name", "_dances", "_state")

    _SEX = "Human"

    @args_match_types
    def __init__(self, name: str="Vasya Pupkin", dances: tuple=None):
        self._name = name
        self._dances = dances if dances is not None else tuple()
        self._set_state_bar()

    def _set_state_dance(self):
        self._state = "Dance"

    def _set_state_bar(self):
        self._state = "Go to bar"

    def __str__(self):
        format_string = "{} {}, can dance: {}"
        return format_string.format(self._SEX, self._name, ', '.join(x.name for x in self._dances))

    @property
    def name(self):
        return self._name

    def new_song_started(self, song: Song):
        if self.can_dance(song):
            self._set_state_dance()
        else:
            self._set_state_bar()

    def can_dance(self, song: Song):
        for i in self._dances:
            if i.can_dance(song.genre):
                return True
        return False

    @property
    def state(self):
        return self._state


class Boy(Human):
    _SEX = "Boy"


class Girl(Human):
    _SEX = "Girl"
