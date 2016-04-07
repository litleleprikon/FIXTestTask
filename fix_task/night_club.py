#!/usr/bin/env python
from time import sleep

from fix_task.decorators import args_match_types
from fix_task.humans import Human
from copy import deepcopy
from fix_task.songs import Song

__author__ = 'litleleprikon'


class NightClub:
    """
    This class simulates club
    Club contains visitors and songs.
    Songs have duration and after songs end it changes.
    When song changes,
    """
    __slots__ = ("_visitors", "_playlist", "_current_song")

    @args_match_types
    def __init__(self, visitors: list=None, playlist: list=None):
        self._visitors = [] if visitors is None else visitors
        self._playlist = [] if playlist is None else playlist
        self._current_song = Song()

    def __len__(self):
        return len(self._visitors)

    def add_visitor(self, visitor: Human):
        self._visitors.append(visitor)

    def add_song(self, song: Song):
        self._playlist.append(song)

    @property
    def playlist(self):
        return deepcopy(self._playlist)

    def __str__(self):
        format_string = "Night club\nCurrent song: {}\nPlaylist:\n{}\nVisitors:\n{}"
        return format_string.format(
            str(self._current_song),
            '\n'.join((str(x) for x in self._playlist)),
            '\n'.join((str(x) for x in self._visitors))
        )

    def _alert_observers(self):
        for visitor in self._visitors:
            visitor.new_song_started(self._current_song)

    def play(self):
        print(self)
        for song in self._playlist:
            self._current_song = song
            self._alert_observers()
            print(self)
            sleep(self._current_song.duration)
