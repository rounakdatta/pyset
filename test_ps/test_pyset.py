import unittest
from pyset.pyset import PySet
from test_ps.data.get_data import get_simple_csv, get_simple_csv2, get_simple_csv3, get_simple_csv4, get_simple_csv5


class TestPySet(unittest.TestCase):
    def setUp(self):
        self.pytest = PySet()

    def test_read_csv(self):
        data_path = get_simple_csv()
        csv = self.pytest.read_csv(data_path)
        self.assertIsNotNone(csv)

    def test_csv_intersection(self):
        data_path1 = get_simple_csv()
        data_path2 = get_simple_csv2()
        self.pytest.add_csv(data_path1)
        self.pytest.add_csv(data_path2)
        intersect = self.pytest.intersection()
        self.assertEqual(intersect, [("J", "K", "L")])

    def test_csv_intersection_no_results(self):
        data_path1 = get_simple_csv()
        data_path3 = get_simple_csv3()
        self.pytest.add_csv(data_path1)
        self.pytest.add_csv(data_path3)
        intersect = self.pytest.intersection()
        self.assertEqual(len(intersect), 0)

    def test_csv_intersection_two_results(self):
        data_path2 = get_simple_csv2()
        data_path3 = get_simple_csv3()
        self.pytest.add_csv(data_path2)
        self.pytest.add_csv(data_path3)
        intersect = self.pytest.intersection()
        self.assertEqual(len(intersect), 2)
        self.assertEqual(intersect, [("1", "2", "3"), ("4", "5", "6")])

    def test_csv_columns(self):
        data_path1 = get_simple_csv()
        data_path3 = get_simple_csv3()
        self.pytest.add_csv(data_path1, [1, 3])
        self.pytest.add_csv(data_path3, [1, 3])
        intersect = self.pytest.intersection()
        self.assertEqual(len(intersect), 1)
        self.assertEqual(intersect, [("A", "C")])

    def test_csv_columns_2_results(self):
        data_path2 = get_simple_csv2()
        data_path3 = get_simple_csv3()
        self.pytest.add_csv(data_path2, [1, 3])
        self.pytest.add_csv(data_path3, [1, 3])
        intersect = self.pytest.intersection()
        self.assertEqual(len(intersect), 2)
        self.assertEqual(intersect, [("1", "3"), ("4", "6")])

    def test_csv_columns_dupe_results(self):
        data_path2 = get_simple_csv2()
        data_path3 = get_simple_csv3()
        self.pytest.add_csv(data_path2, [2, 3])
        self.pytest.add_csv(data_path3, [1, 3])
        intersect = self.pytest.intersection()
        self.assertEqual(len(intersect), 1)

    def test_3_csv_intersection(self):
        data_path = get_simple_csv()
        data_path2 = get_simple_csv2()
        data_path3 = get_simple_csv3()

        self.pytest.add_csv(data_path)
        self.pytest.add_csv(data_path2)
        self.pytest.add_csv(data_path3)
        intersect = self.pytest.intersection()
        self.assertEqual(len(intersect), 0)

    def test_3_csv_intersection_one_result(self):
        data_path = get_simple_csv()
        data_path2 = get_simple_csv2()
        data_path3 = get_simple_csv3()
        self.pytest.add_csv(data_path, [1, 3])
        self.pytest.add_csv(data_path2, [2, 3])
        self.pytest.add_csv(data_path3, [2, 3])
        intersect = self.pytest.intersection()
        self.assertEqual(len(intersect), 1)
        self.assertEqual(intersect, [("A", "C")])

    def test_union(self):
        data_path = get_simple_csv()
        data_path2 = get_simple_csv2()
        self.pytest.add_csv(data_path)
        self.pytest.add_csv(data_path2)
        un = self.pytest.union()
        self.assertEqual(len(un), 7)
        self.assertEqual([('A', 'B', 'C'), ('D', 'E', 'F'),
                          ('G', 'H', 'I'), ('J', 'K', 'L'), ('B', 'A', 'C'),
                          ('1', '2', '3'), ('4', '5', '6')], un)

    def test_subtract(self):
        data_path = get_simple_csv()
        data_path2 = get_simple_csv2()
        self.pytest.add_csv(data_path)
        self.pytest.add_csv(data_path2)
        sub = self.pytest.subtract()
        self.assertEqual(len(sub), 3)

    def test_complement(self):
        data_path = get_simple_csv4()
        data_path2 = get_simple_csv5()
        self.pytest.add_csv(data_path)
        self.pytest.add_csv(data_path2)
        com = self.pytest.complement()
        self.assertEqual(len(com), 2)
        self.assertEqual(com, [("7", "8", "9"), ("X", "Y", "Z")])

    def test_subtract_no_results(self):
        data_path = get_simple_csv()
        self.pytest.add_csv(data_path)
        self.pytest.add_csv(data_path)
        sub = self.pytest.subtract()
        self.assertEqual(len(sub), 0)

    def test_intersection_full_output(self):
        data_path = get_simple_csv()
        data_path2 = get_simple_csv2()
        self.pytest.add_csv(data_path, [1, 3])
        self.pytest.add_csv(data_path2, [2, 3])
        self.pytest.set_full_output(True)
        intersect = self.pytest.intersection()
        self.assertEqual(len(intersect), 1)
        self.assertEqual(intersect, [("A", "B", "C")])

    def test_set_primary(self):
        data_path = get_simple_csv()
        data_path2 = get_simple_csv2()
        self.pytest.add_csv(data_path, [1, 3])
        self.pytest.add_csv(data_path2, [2, 3])
        self.pytest.set_primary(2)
        subtract = self.pytest.subtract()
        self.assertEqual(len(subtract), 3)
        self.assertEqual(subtract, [('2', '3'), ('K', 'L'), ('5', '6')])

    def test_set_primary_full(self):
        data_path = get_simple_csv()
        data_path2 = get_simple_csv2()
        self.pytest.add_csv(data_path, [1, 3])
        self.pytest.add_csv(data_path2, [2, 3])
        self.pytest.set_primary(2)
        self.pytest.set_full_output(True)
        subtract = self.pytest.subtract()
        self.assertEqual(len(subtract), 3)
        self.assertEqual(subtract, [('1', '2', '3'), ('J', 'K', 'L'), ('4', '5', '6')])
        """
        """
