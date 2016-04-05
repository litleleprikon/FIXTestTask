#!/usr/bin/env python
from decorators import args_match_types

__author__ = 'litleleprikon'


class Dance:
    """
    Base class for dances.
    Contains basic methods for all dances.
    All inherited classes should redefine class variables.
    """
    _NAME = "Base dance"
    _HANDS = "nothing"
    _LEGS = "nothing"
    _HEAD = "nothing"
    _BODY = "nothing"
    _SIMILAR_DANCES = ()

    @args_match_types
    def __init__(self, name: str = None, hands: str = None, legs: str = None, head: str = None, body: str = None,
                 similar: tuple = None):
        if name is not None:
            self._NAME = name
        if hands is not None:
            self._HANDS = hands
        if legs is not None:
            self._LEGS = legs
        if head is not None:
            self._HEAD = head
        if body is not None:
            self._BODY = body
        if similar is not None:
            self._SIMILAR_DANCES = similar

    @property
    def name(self):
        return self._NAME

    def __str__(self):
        format_string = "%s dance\nHands is doing: %s\n Legs is doing: %s\n Head is doing: %s\n Body is doing: %s"
        return format_string.format(self._NAME, self._HANDS, self._LEGS, self._HEAD, self._BODY)

    def can_dance(self, dance):
        """
        Method, that defines, if two dances compatible
        :param dance: dance, that satisfies to currently played music
        :return: True if dance satisfies to music, else False
        """
        return dance.name == self._NAME or dance.name in self._SIMILAR_DANCES


class HipHop(Dance):
    _NAME = "HipHop"
    _HANDS = "согнуты в локтях"
    _LEGS = "в полу-присяде"
    _HEAD = "вперед-назад"
    _BODY = "вперед и назад"
    _SIMILAR_DANCES = ("RnB",)


class Electrodance(Dance):
    _NAME = "Electrodance"
    _HANDS = "вращения"
    _LEGS = "двигаются в ритме"
    _HEAD = "нет движения"
    _BODY = "покачивание вперед-назад"
    _SIMILAR_DANCES = ("Electrohouse", "house")


class Pop(Dance):
    _NAME = "Pop"
    _HANDS = "плавные движения"
    _LEGS = "плавные движения"
    _HEAD = "плавные движения"
    _BODY = "плавные движения"
