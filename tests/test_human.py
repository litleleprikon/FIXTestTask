#!/usr/bin/env python
from unittest import TestCase
from fix_task.humans import Human, Boy, Girl
from fix_task.dances import HipHop, Pop, Electrodance
from fix_task.songs import Song

__author__ = 'litleleprikon'


class TestHuman(TestCase):
    def setUp(self):
        self.human = Human(name="Emil", dances=(HipHop(), Electrodance()))

    def test_init(self):
        assert self.human.name == "Emil"
        assert isinstance(self.human._dances, tuple) and len(self.human._dances) == 2

    def test_can_dance_method(self):
        assert self.human.can_dance(Song(genre=HipHop()))
        assert not self.human.can_dance(Song(genre=Pop()))

    def test_new_song_method(self):
        self.human.new_song_started(Song(name="Pretty song", genre=HipHop()))
        assert self.human.state == "Dance"

    def test_state(self):
        assert self.human.state == "Go to bar"

    def test_str_method(self):
        format_string = "Human {}, can dance: {}"
        assert str(self.human) == format_string.format(self.human.name, ', '.join(x.name for x in self.human._dances))

    def test_boy_str_method(self):
        boy = Boy()
        assert str(boy) == "Boy {}, can dance: {}".format(boy.name, ', '.join(x.name for x in boy._dances))

    def test_girl_str_method(self):
        girl = Girl()
        assert str(girl) == "Girl {}, can dance: {}".format(girl.name, ', '.join(x.name for x in girl._dances))
