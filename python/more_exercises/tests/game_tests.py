from nose.tools import *
from ex47.game import Room

def test_room():
    gold = Room("GoldRoom", "This room has gold, door north")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Centre", "Test room in the center")
    north = Room("North", "Test room in the north")
    south = Room("South", "Test room in the south")
    center.add_paths({"north": north, "south": south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

