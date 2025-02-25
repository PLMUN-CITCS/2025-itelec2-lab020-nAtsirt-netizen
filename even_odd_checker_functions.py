import unittest
import unittest.mock

def check_even_odd(n):
    return f"{n} is {'Even' if n % 2 == 0 else 'Odd'} number."

def get_int_input():
    while True:
        try: return int(input("Enter an integer: "))
        except ValueError: print("Invalid input.")

def main():
    print(check_even_odd(get_int_input()))

class TestEvenOdd(unittest.TestCase):
    def test_even(self): self.assertEqual(check_even_odd(4), "4 is Even number.")
    def test_odd(self): self.assertEqual(check_even_odd(7), "7 is Odd number.")
    def test_zero(self): self.assertEqual(check_even_odd(0), "0 is Even number.")
    def test_input_valid(self):
        with unittest.mock.patch('builtins.input', return_value='10'): self.assertEqual(get_int_input(), 10)
    def test_input_invalid_then_valid(self):
        with unittest.mock.patch('builtins.input', side_effect=['abc', '15']): self.assertEqual(get_int_input(), 15)

if __name__ == "__main__":
    unittest.main(argv=['ignored'], exit=False)
    main()
