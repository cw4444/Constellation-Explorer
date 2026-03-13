import unittest

from constellation_explorer.generator import generate_systems


class GeneratorTests(unittest.TestCase):
    def test_generation_is_deterministic(self):
        first = generate_systems("andromeda", 3)
        second = generate_systems("andromeda", 3)
        self.assertEqual(first, second)

    def test_generation_changes_with_seed(self):
        first = generate_systems("andromeda", 2)
        second = generate_systems("orion", 2)
        self.assertNotEqual(first, second)

    def test_invalid_count_raises(self):
        with self.assertRaises(ValueError):
            generate_systems("andromeda", 0)


if __name__ == "__main__":
    unittest.main()