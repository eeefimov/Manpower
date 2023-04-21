import unittest
import pytest
from Manpower_main import Manpower
from Manpower_login import ManpowerLogin
from Manpower_registration import ManpowerRegistration


class TestManpower(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.manpower = Manpower()
        cls.login = ManpowerLogin()
        cls.registration = ManpowerRegistration()

    @classmethod
    def tearDownClass(cls):
        cls.login.teardown_method(None)


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

    @pytest.mark.negative
    def test_login_empty(self):
        self.login.login_empty()
        self.manpower.check_info()

    @pytest.mark.positive
    def test_registration_sliders(self):
        self.registration.registration_sliders()

    @pytest.mark.negative
    def test_registration_form_empty(self):
        self.registration.registration_sliders()
        self.registration.registration_form_empty()

    @pytest.mark.positive
    def test_registration_form_complete(self):
        self.registration.registration_sliders()
        self.registration.registration_form_complete()


if __name__ == '__main__':
    unittest.main()
