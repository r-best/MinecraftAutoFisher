import pytest
from ..fisher import match


class TestMatch():
    def test_none(self):
        assert not match("")

    def test_exact(self):
        assert match("Fishing Bobber")
    
    def test_extra(self):
        assert match("some text Fishing Bobber some text")

    def test_oneTypo(self):
        assert match("Fishing Gobber")
    
    def test_extraMultiline(self):
        assert match("""
            this is a multiline string that contains\n
            the target Fishing Bobber text along\n
            with some other text that doesn't matter
        """)
    
    def test_maxDistanceDefault(self):
        assert match("Fishing B")
        assert match("Fishing Bmmmmm")
    
    def test_maxDistanceCustom(self):
        assert match("Fishing m", threshold=6)
        assert match("Fishing mmmmmm", threshold=6)
    
    def test_distanceTooLargeDefault(self):
        assert not match("Fishing mmmmmm")
    
    def test_distanceTooLargeCustom(self):
        assert not match("Fishing mmmmmm", threshold=4)
