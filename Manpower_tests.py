import unittest
import pytest
from Manpower_main import Manpower


class TestManpower(unittest.TestCase):

    @pytest.mark.positive
    def test_check_links_header(self):
        self.manpower = Manpower()
        valid_links = self.manpower.check_links("header a")
        self.assertGreater(len(valid_links), 0)

    @pytest.mark.positive
    def test_check_links_footer(self):
        self.manpower = Manpower()
        valid_links = self.manpower.check_links("footer a")
        self.assertGreater(len(valid_links), 0)

    @pytest.mark.positive
    def test_check_footer(self):
        self.manpower = Manpower()
        header_list = self.manpower.check_footer()
        self.assertGreater(len(header_list), 0)


if __name__ == '__main__':
    unittest.main()
