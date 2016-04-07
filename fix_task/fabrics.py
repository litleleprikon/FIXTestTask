#!/usr/bin/env python
from fix_task.songs import Song
from fix_task.dances import HipHop, Pop, Electrodance
from fix_task.humans import Boy, Girl
from random import randint

__author__ = 'litleleprikon'


class SongsFabric:
    """
    Class to generate songs sequence
    """

    _SONG_NAMES = ("A$AP Rocky - Everyday", "Fall Out Boy - Uma Thurman", "Phazz - I think")
    _SONG_GENRES = (HipHop, Pop, Electrodance)

    @classmethod
    def generate_sequence(cls, num: int, max_duration: int):
        result = []
        for _ in range(num):
            genre = cls._SONG_GENRES[randint(0, len(cls._SONG_GENRES) - 1)]()
            name = cls._SONG_NAMES[randint(0, len(cls._SONG_NAMES) - 1)]
            duration = randint(0, max_duration)
            result.append(Song(name=name, genre=genre, duration=duration))
        return result


class VisitorsFabric:
    """
    Class to generate random sequence of visitors
    """
    _GIRLS_NAMES = ("Eva", "Maria", "Huanita")
    _BOYS_NAMES = ("Dimas", "Sanya", "Don Pedro")
    _DANCES = (HipHop, Pop, Electrodance)

    @classmethod
    def generate_boy(cls):
        name = cls._BOYS_NAMES[randint(0, len(cls._BOYS_NAMES)-1)]
        dances = tuple(cls._DANCES[randint(0, len(cls._DANCES)-1)]() for _ in range(randint(0, len(cls._DANCES))))
        return Boy(name=name, dances=dances)

    @classmethod
    def generate_girl(cls):
        name = cls._GIRLS_NAMES[randint(0, len(cls._GIRLS_NAMES)-1)]
        dances = tuple(cls._DANCES[randint(0, len(cls._DANCES)-1)]() for _ in range(randint(0, len(cls._DANCES))))
        return Girl(name=name, dances=dances)

    @classmethod
    def generate_sequence(cls, num: int):
        result = []
        for _ in range(num):
            if randint(0, 1) == 0:
                result.append(cls.generate_boy())
            else:
                result.append(cls.generate_girl())
        return result
