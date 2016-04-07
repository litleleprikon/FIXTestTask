#!/usr/bin/env python
from unittest import TestCase
from fix_task.fabrics import SongsFabric, VisitorsFabric
from fix_task.humans import Boy, Girl

__author__ = 'litleleprikon'


class TestSongsFabric(TestCase):
    def test_generate_sequence(self):
        songs = SongsFabric.generate_sequence(10, 5)
        assert isinstance(songs, list)
        assert len(songs) == 10
        for song in songs:
            assert song.duration <= 5
            assert song.genre.__class__ in SongsFabric._SONG_GENRES
            assert song.name in SongsFabric._SONG_NAMES


class TestVisitorsFabric(TestCase):
    def test_generate_sequence(self):
        visitors = VisitorsFabric.generate_sequence(5)
        assert len(visitors) == 5
        for visitor in visitors:
            assert isinstance(visitor, Boy) or isinstance(visitor, Girl)

    def test_generate_boy_method(self):
        boy = VisitorsFabric.generate_boy()
        assert isinstance(boy, Boy)
        assert boy.name in VisitorsFabric._BOYS_NAMES
        for dance in boy._dances:
            dance.__class__ in VisitorsFabric._DANCES

    def test_generate_girl_method(self):
        girl = VisitorsFabric.generate_girl()
        assert isinstance(girl, Girl)
        assert girl.name in VisitorsFabric._GIRLS_NAMES
        for dance in girl._dances:
            dance.__class__ in VisitorsFabric._DANCES
