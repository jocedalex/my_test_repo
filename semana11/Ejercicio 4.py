class Head:
    def __init__(self):
        self.eyes = 2
        self.ears = 2
        self.nose = 1
        self.mouth = 1

class Torso:
    def __init__(self):
        self.head = Head()
        self.right_arm = Arm('right')
        self.left_arm = Arm('left')
        self.right_leg = Leg('right')
        self.left_leg = Leg('left')
        self.heart = 1
        self.lungs = 2
        self.stomach = 1

class Arm:
    def __init__(self, side):
        self.side = side
        self.hand = Hand(side)
        self.hands = 1

class Hand:
    def __init__(self, side):
        self.side = side
        self.fingers = 5

class Leg:
    def __init__(self, side):
        self.side = side
        self.foot = Feet(side)
        self.feet = 1

class Feet:
    def __init__(self, side):
        self.side = side
        self.toes = 5

class Human:
    def __init__(self):
        self.torso = Torso()

# Example usage
human = Human()
print(f"Human has {human.torso.head.eyes} eyes and {human.torso.right_leg.foot.toes} toes in the right foot.")