import unittest
from pyrc import IRC


class Tests(unittest.TestCase):
    """
    Contains all the tests.
    """

    def test_Test(self):
        command = '/j #foo'
        irc = IRC()
        output = irc.parsecmd(command)
        self.assertEqual('JOIN #foo', output)


if __name__ == '__main__':
        unittest.main()
