class QuadrilateralWorker:
    def __init__(self, ab: float, bc: float, cd: float, ad: float,
                 dab: float, abc: float, bcd: float, cda: float):

        self.sides = [ab, bc, cd, ad]
        self.angles = [dab, abc, bcd, cda]

        self._check_validity()

        self.type = self._get_type()

    def _check_validity(self):
        if any(side <= 0 for side in self.sides):
            raise Exception('Sides should be greater than 0')

        if any(angle <= 0 or angle >= 360 for angle in self.angles):
            raise Exception('Angles should be greater than 0 and less than 360 degrees')
        
        if sum(self.angles) != 360:
            raise Exception('Invalid angles')

        for i in range(len(self.sides)):
            if self.sides[i] >= sum(self.sides[:i] + self.sides[i + 1:]):
                raise Exception('Invalid size lengths')

    def _sides_equal(self):
        return all(side == self.sides[0] for side in self.sides)

    def _opposite_sides_equal(self):
        return all(self.angles[i] + self.angles[(i + 2) % 4] for i in range(len(self.angles)))

    def _angles_equal(self):
        return all(angle == self.angles[0] for angle in self.angles)

    def _opposite_angles_equal(self):
        return self.angles[0] == self.angles[2] and self.angles[1] == self.angles[3]

    def _get_type(self):
        if self._angles_equal():
            if self._sides_equal():
                return 'Square'
            if self._opposite_sides_equal():
                return 'Rectangle'

            raise Exception('Quadrilateral with 90 degrees angles should be square or rectangle')

        if self._opposite_angles_equal():
            if self._sides_equal():
                return 'Rhombus'

            if self._opposite_sides_equal():
                return 'Parallelogram'

        if any(self.angles[i] + self.angles[(i + 2) % 4] for i in range(len(self.angles))) and \
                (self.sides[0] == self.sides[2] or self.sides[1] == self.sides[3]):
            return 'Trapezoid'

        if (self.sides[0] == self.sides[1] and self.sides[2] == self.sides[3]) or \
                (self.sides[0] == self.sides[3] and self.sides[1] == self.sides[2]):
            return 'Kite'

        return 'Quadrilateral'
