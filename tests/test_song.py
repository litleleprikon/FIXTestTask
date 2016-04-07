#!/usr/bin/env python
from unittest import TestCase
from fix_task.songs import Song
from fix_task.dances import HipHop

__author__ = 'litleleprikon'


class TestSong(TestCase):
    def setUp(self):
        self.song = Song(genre=HipHop(), duration=5)

    def test_init(self):
        assert self.song.name == "Great song"
        assert self.song.genre.name == "HipHop"
        assert self.song.duration == 5

    def test_str_method(self):
        format_string = "Song: {}, genre: {}, duration: {}"
        assert str(self.song) == format_string.format(self.song.name, self.song.genre.name, self.song.duration)
