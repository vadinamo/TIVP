class QuadrilateralWorker:
    def __init__(self, ab: float, bc: float, cd: float, ad: float,
                 dab: float, abc: float, bcd: float, cda: float):

        self.sides = [ab, bc, cd, ad]
        self.angles = [dab, abc, bcd, cda]

        self._check_validity()

        self.type = self._get_type()

    @staticmethod
    def _check_format(obj):
        return {i: o for i, o in enumerate(obj) if not isinstance(o, (float, int))}

    def _check_sides_validity(self):
        side_names = ['ab', 'bc', 'cd', 'ad']

        invalid_sides = self._check_format(self.sides)
        if invalid_sides:
            raise ValueError(f'Sides must be in float or integer format '
                             f'({", ".join(f"{side_names[i]}: {side}" for i, side in invalid_sides.items())})')

        invalid_sides = {i: side for i, side in enumerate(self.sides) if side <= 0}
        if invalid_sides:
            raise ValueError('Sides should be greater than 0 '
                             f'({", ".join(f"{side_names[i]}: {side}" for i, side in invalid_sides.items())})')

        for i in range(len(self.sides)):
            side = self.sides[i]
            sides_sum = sum(self.sides[:i] + self.sides[i + 1:])
            if side >= sides_sum:
                raise ValueError(f'Invalid size length\n'
                                 f'({side_names[i]}) {"greater" if side > sides_sum else "equal"} than sum of other '
                                 f'sides (should be less)')

    def _check_angles_validity(self):
        angle_names = ['dab', 'abc', 'bcd', 'cda']

        invalid_angles = self._check_format(self.angles)
        if invalid_angles:
            raise ValueError(f'Angles must be in float or integer format '
                             f'({", ".join(f"{angle_names[i]}: {angle}" for i, angle in invalid_angles.items())})')

        invalid_angles = {i: angle for i, angle in enumerate(self.angles) if (angle <= 0 or angle >= 360)}
        if invalid_angles:
            raise ValueError('Angles should be greater than 0 and less than 360 degrees'
                             f'({", ".join(f"{angle_names[i]}: {angle}" for i, angle in invalid_angles.items())})')

        if sum(self.angles) < 360:
            raise ValueError('Angles sum less than 360 (must be 360 degrees)')
        elif sum(self.angles) > 360:
            raise ValueError('Angles sum greater than 360 (must be 360 degrees)')

    def _check_validity(self):
        self._check_sides_validity()
        self._check_angles_validity()

    def _sides_equal(self):
        return all(side == self.sides[0] for side in self.sides)

    def _opposite_sides_equal(self):
        return all(self.sides[i] == self.sides[(i + 2) % 4] for i in range(len(self.sides)))

    def _angles_equal(self):
        return all(angle == self.angles[0] for angle in self.angles)

    def _opposite_angles_equal(self):
        return all(self.angles[i] == self.angles[(i + 2) % 4] for i in range(len(self.angles)))

    def _get_type(self):
        if self._angles_equal():
            if self._sides_equal():
                return 'Square'
            elif self._opposite_sides_equal():
                return 'Rectangle'

            raise ValueError('Quadrilateral with 90 degrees angles should be square or rectangle')

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
