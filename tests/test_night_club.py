#!/usr/bin/env python
from unittest import TestCase

from fix_task.humans import Boy, Girl
from fix_task.night_club import NightClub
from fix_task.songs import Song

__author__ = 'litleleprikon'


class TestNightClub(TestCase):
    def setUp(self):
        visitors = [Boy(), Girl(), Girl()]
        songs = [Song(duration=1), Song(duration=2)]
        self.club = NightClub(visitors=visitors, playlist=songs)

    def test_init(self):
        assert len(self.club) == 3
        assert len(self.club.playlist) == 2

    def test_add_song_method(self):
        songs_previous = len(self.club.playlist)
        self.club.add_song(Song())
        assert len(self.club.playlist) == songs_previous+1

    def test_new_visitor_method(self):
        visitors_previous = len(self.club)
        self.club.add_visitor(Girl())
        assert len(self.club) == visitors_previous+1

    def test_str_method(self):
        format_string = "Night club\nCurrent song: {}\nPlaylist:\n{}\nVisitors:\n{}"
        assert str(self.club) == format_string.format(
            str(self.club._current_song),
            '\n'.join((str(x) for x in self.club.playlist)),
            '\n'.join((str(x) for x in self.club._visitors))
        )
