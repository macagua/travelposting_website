from django.test import TestCase

from destinations.fields import DaysCommaField


class DaysCommaFieldTests(TestCase):
    def setUp(self) -> None:
        self.instance = DaysCommaField()
        self.separator = ','
        self.data = [1, 2, 3]

    def str_result(self):
        return f"{self.separator}".join([str(v) for v in self.data])

    def test_init_decontruct(self):
        name, path, args, kwargs = self.instance.deconstruct()
        new_instance = DaysCommaField(*args, **kwargs)
        self.assertEqual(self.instance.max_length, new_instance.max_length)

    def test_data_list_or_tuple(self):
        self.assertEqual(self.instance.to_python(self.data), list(self.data))
        self.assertEqual(self.instance.to_python(tuple(self.data)), tuple(self.data))

    def test_data_str_one(self):
        self.assertEqual(self.instance.to_python('1'), 1)

    def test_data_str_full(self):
        self.assertEqual(self.instance.to_python(self.str_result()), list(self.data))

    def test_data_int(self):
        self.assertEqual(self.instance.to_python(1), 1)

    def test_data_db(self):
        self.assertEqual(self.instance.get_prep_value(self.data), self.str_result())
