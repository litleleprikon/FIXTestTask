#!/usr/bin/env python
from unittest import TestCase
from fix_task.songs import Song
from fix_task.dances import HipHop

__author__ = 'litleleprikon'


class TestSong(TestCase):
    def setUp(self):
        self.song = Song(genre=HipHop())

    def test_init(self):
        assert self.song.name == "Great song"
        assert self.song.genre.name == "HipHop"
