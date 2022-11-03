import unittest
from contextlib import redirect_stdout
from io import StringIO

from app import App


class TestApp(unittest.TestCase):
    def setUp(self):
        self.dir = "files/"

    def test_run_text_file(self):
        expected = "0,1,NORTH\n0,0,WEST\n3,3,NORTH\n"
        with StringIO() as stdout, redirect_stdout(stdout):
            app = App()
            app.run(f"{self.dir}/test.txt")
            self.assertEqual(stdout.getvalue(), expected)

    def test_run_non_text_file(self):
        expected = "Use text file only.\n"
        with StringIO() as stdout, redirect_stdout(stdout):
            app = App()
            app.run(f"{self.dir}/test.doc")
            self.assertEqual(stdout.getvalue(), expected)

    def test_run_file_not_found(self):
        expected = "File not found.\n"
        with StringIO() as stdout, redirect_stdout(stdout):
            app = App()
            app.run(f"{self.dir}/foo.bar")
            self.assertEqual(stdout.getvalue(), expected)
