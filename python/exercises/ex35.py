from sys import exit

def gold_room():
    print "this room is full of gold.  how much do you take?"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number")

    if how_much<50:
        print "nice, you're not too greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard")

def bear_room():
    print "there is a bear with honey in front of a door"
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")
        if next == "take honey":
            dead("bear kills you")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door and you can go through"
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("bear strikes")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I don't understand")

def cthulhu_room():
    print "Here is evil Cthulhu"
    next=raw_input("> ")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well, that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "dark room, doors left and right"
    next= raw_input("> ")
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("stumble around and starve")

start()

