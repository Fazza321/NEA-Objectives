class Vector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    # adds two vectors together
    def add(self, vec, component):
        if component == "i":
            self.i += vec.i
        elif component == "j":
            self.j += vec.j

    # takes one vector from another
    def subtract(self, vec, component):
        if component == "i":
            self.i -= vec.i
        elif component == "j":
            self.j -= vec.j

    # scales self with another vector
    def scale(self, vec, component, player):
        if not player.canJump:
            return
        if component == "i":
            self.i *= vec.i
        if component == "j":
            self.j *= vec.j

    # applies an inverse coefficient to the vector
    def reverse(self, component):
        if component == "i":
            self.i *= -1
        elif component == "j":
            self.j *= -1

    # applies a limit to a vector, so it can't increase
    def limit(self, vec, component, player):
        if not player.canJump:
            return
        if component == "i":
            self.i = vec.i
        elif component == "j":
            self.j = vec.j

    def setVec(self, newI, newJ):
        self.i = newI
        self.j = newJ

    def rotateVec(self):
        newI = -self.j
        newJ = self.i
        self.setVec(newI, newJ)

    def vecAngleChange(self, current, new):
        turns = new.direction - current.direction + 2
        for turn in range(turns):
            self.rotateVec()


gravity = Vector(0, 1)
vel = Vector(0, 0)
posVec = Vector(500, 500)
acceleration = Vector(0.7, 0)
deceleration = Vector(0.7, 0)
terminalVel = Vector(6, 10)
