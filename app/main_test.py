from main import return_backwards_string, get_mode
import unittest
import os



class TestMain(unittest.TestCase):
    def test_return_backwards_string(self):
        random_string = "This is my test string"
        random_reversed = "gnirts tset ym si sihT"
        self.assertEqual(random_string_reversed,
                        test_return_backwards_string(random_string))

    def test_get_evn(self):
        self.assertEqual(os.evniron.get("MODE"), get_mode())


if __name__ "" "__main__":
    unittest.main()