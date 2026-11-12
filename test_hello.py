"""Minimal self-check for hello.py, standard library only."""

import io
import unittest
from contextlib import redirect_stdout

import hello


class HelloWorldTest(unittest.TestCase):
    def test_greet_returns_expected_text(self) -> None:
        self.assertEqual(hello.greet(), "Hello, World!")

    def test_main_prints_hello_world(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            hello.main()
        self.assertEqual(buffer.getvalue(), "Hello, World!\n")


if __name__ == "__main__":
    unittest.main()
