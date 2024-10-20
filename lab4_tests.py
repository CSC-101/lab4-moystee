import data
import lab4
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)
    def test_first_element_2(self):
        # write a second test here
        input = [[2,3], [4,5]]
        result = lab4.first_element(input)
        expected = [2, 4]
        self.assertEqual(expected, result)
    # Part 2
    def test_x_coordinates_1(self):
        input = [data.Point(1.0,1.0),data.Point(2.0,3.0),data.Point(4.0,1.0)]
        result = lab4.x_coordinates(input)
        expected = [1.0, 2.0, 4.0]
        self.assertEqual(expected, result)

    def test_x_coordinates_2(self):
        input = [data.Point(7.0, 2.0), data.Point(8.0,9.0), data.Point(1.0,2.0)]
        result = lab4.x_coordinates(input)
        expected = [7.0, 8.0, 1.0]
        self.assertEqual(expected, result)
    # Part 3
    def test_are_in_positive_quadrant_1(self):
        input = [data.Point(1.0, -1.0), data.Point(2.0, 3.0), data.Point(-4.0, 1.0)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [data.Point(2.0,3.0)]
        self.assertEqual(expected, result)
    def test_are_in_positive_quadrant_2(self):
        input = [data.Point(-1.0, 1.0), data.Point(-2.0, 3.0), data.Point(4.0, 1.0)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [data.Point(4.0,1.0)]
        self.assertEqual(expected, result)
    # Part 4
    def test_distance_1(self):
        input1, input2 = data.Point(2,3), data.Point(2,6)
        result = lab4.distance(input1, input2)
        expected = 3.0
        self.assertEqual(expected, result)
    def test_distance_2(self):
        input1, input2 = data.Point(1,2), data.Point(1,4)
        result = lab4.distance(input1, input2)
        expected = 2.0
        self.assertEqual(expected, result)
    # Part 5
    def test_manhattan_distance_1(self):
        input1, input2 = data.Point(1, 2), data.Point(1, 4)
        result = lab4.manhattan_distance(input1, input2)
        expected = -2.0
        self.assertEqual(expected, result)
    def test_manhattan_distance_1(self):
        input1, input2 = data.Point(0, 1), data.Point(2, 3)
        result = lab4.manhattan_distance(input1, input2)
        expected = 0.0
        self.assertEqual(expected, result)
    # Part 6
    def test_distance_all_1(self):
        input = [data.Point(1, 3), data.Point(1,5)]
        result = lab4.distance_all(input)
        expected = [3.1622776601683795, 5.0990195135927845]
        self.assertEqual(expected, result)
    def test_distance_all_2(self):
        input = [data.Point(2, 0), data.Point(1,1)]
        result = lab4.distance_all(input)
        expected = [2.0, 1.4142135623730951]
        self.assertEqual(expected, result)



if __name__ == '__main__':
    unittest.main()
