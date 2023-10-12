import unittest
from quadrilateral_worker import QuadrilateralWorker


class TestQuadrilateralWorker(unittest.TestCase):
    def test_not_numeric_side_input_single(self):
        with self.assertRaises(ValueError) as context:
            QuadrilateralWorker('4', 4, 4, 4, 90, 90, 90, 90)
        self.assertEqual(str(context.exception), 'Sides must be in float or integer format (ab: 4)')

    def test_not_numeric_side_input_multiple(self):
        with self.assertRaises(ValueError) as context:
            QuadrilateralWorker('4', '4', '4', '4', 90, 90, 90, 90)
        self.assertEqual(str(context.exception),
                         'Sides must be in float or integer format (ab: 4, bc: 4, cd: 4, ad: 4)')

    def test_not_numeric_angle_input_single(self):
        with self.assertRaises(ValueError) as context:
            QuadrilateralWorker(4, 4, 4, 4, '90', 90, 90, 90)
        self.assertEqual(str(context.exception), 'Angles must be in float or integer format (dab: 90)')

    def test_not_numeric_angle_input_multiple(self):
        with self.assertRaises(ValueError) as context:
            QuadrilateralWorker(4, 4, 4, 4, '90', '90', '90', '90')
        self.assertEqual(str(context.exception),
                         'Angles must be in float or integer format (dab: 90, abc: 90, bcd: 90, cda: 90)')

    def test_negative_side_input_single(self):
        with self.assertRaises(ValueError) as context:
            QuadrilateralWorker(-4, 4, 4, 4, 90, 90, 90, 90)
        self.assertEqual(str(context.exception),
                         'Sides should be greater than 0 (ab: -4)')

    def test_negative_side_input_multiple(self):
        with self.assertRaises(ValueError) as context:
            QuadrilateralWorker(-4, -4, -4, -4, 90, 90, 90, 90)
        self.assertEqual(str(context.exception),
                         'Sides should be greater than 0 (ab: -4, bc: -4, cd: -4, ad: -4)')

    def test_zero_value_side_single(self):
        with self.assertRaises(ValueError) as context:
            QuadrilateralWorker(0, 4, 4, 4, 90, 90, 90, 90)
        self.assertEqual(str(context.exception),
                         'Sides should be greater than 0 (ab: 0)')

    def test_zero_value_side_multiple(self):
        with self.assertRaises(ValueError) as context:
            QuadrilateralWorker(0, 0, 0, 0, 90, 90, 90, 90)
        self.assertEqual(str(context.exception),
                         'Sides should be greater than 0 (ab: 0, bc: 0, cd: 0, ad: 0)')

    def test_negative_angle_input_single(self):
        with self.assertRaises(ValueError) as context:
            QuadrilateralWorker(4, 4, 4, 4, -90, 90, 90, 90)
        self.assertEqual(str(context.exception),
                         'Angles should be greater than 0 and less than 360 degrees(dab: -90)')

    def test_negative_angle_input_multiple(self):
        with self.assertRaises(ValueError) as context:
            QuadrilateralWorker(4, 4, 4, 4, -90, -90, -90, -90)
        self.assertEqual(str(context.exception),
                         'Angles should be greater than 0 and less than 360 degrees(dab: -90, abc: -90, bcd: -90, '
                         'cda: -90)')

    def test_zero_value_angle_single(self):
        with self.assertRaises(ValueError) as context:
            QuadrilateralWorker(4, 4, 4, 4, 0, 90, 90, 90)
        self.assertEqual(str(context.exception),
                         'Angles should be greater than 0 and less than 360 degrees(dab: 0)')

    def test_zero_value_angle_multiple(self):
        with self.assertRaises(ValueError) as context:
            QuadrilateralWorker(4, 4, 4, 4, 0, 0, 0, 0)
        self.assertEqual(str(context.exception),
                         'Angles should be greater than 0 and less than 360 degrees(dab: 0, abc: 0, bcd: 0, cda: 0)')

    def test_360_equal_angle_input_single(self):
        with self.assertRaises(ValueError) as context:
            QuadrilateralWorker(4, 4, 4, 4, 360, 90, 90, 90)
        self.assertEqual(str(context.exception),
                         'Angles should be greater than 0 and less than 360 degrees(dab: 360)')

    def test_360_equal_angle_input_multiple(self):
        with self.assertRaises(ValueError) as context:
            QuadrilateralWorker(4, 4, 4, 4, 360, 360, 360, 360)
        self.assertEqual(str(context.exception),
                         'Angles should be greater than 0 and less than 360 degrees(dab: 360, abc: 360, bcd: 360, '
                         'cda: 360)')

    def test_360_greater_angle_input_single(self):
        with self.assertRaises(ValueError) as context:
            QuadrilateralWorker(4, 4, 4, 4, 361, 90, 90, 90)
        self.assertEqual(str(context.exception),
                         'Angles should be greater than 0 and less than 360 degrees(dab: 361)')

    def test_360_greater_angle_input_multiple(self):
        with self.assertRaises(ValueError) as context:
            QuadrilateralWorker(4, 4, 4, 4, 361, 362, 363, 364)
        self.assertEqual(str(context.exception),
                         'Angles should be greater than 0 and less than 360 degrees(dab: 361, abc: 362, bcd: 363, '
                         'cda: 364)')

    def test_angle_sum_less_360(self):
        pass

    def test_angle_sum_greater_360(self):
        pass

    def test_incorrect_side_length_equal(self):
        pass

    def test_incorrect_side_length_greater(self):
        pass

    def test_right_angles_without_pairwise_equal_sides(self):
        pass

    def test_quadrilateral_type_square(self):
        pass

    def test_quadrilateral_type_rectangle(self):
        pass

    def test_quadrilateral_type_rhombus(self):
        pass

    def test_quadrilateral_type_parallelogram(self):
        pass

    def test_quadrilateral_type_trapezoid(self):
        pass

    def test_quadrilateral_type_kite(self):
        pass

    def test_quadrilateral_type_quadrilateral(self):
        pass
