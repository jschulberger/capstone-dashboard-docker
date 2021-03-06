import pytest
import mock
import unittest
from commqueue import commqueue
import time


class TestCommqueue(object):
    def test_sanity(self):
        assert True == True
    
    # Add command
    def test_add_valid_comm(self):
        ncq = commqueue()
        assert ncq.add('RPM', 100) == True

    def test_add_invalid_comm(self):
        ncq = commqueue()
        assert ncq.add('invalid', 10) == False

    def test_add_command_is_str(self):
        ncq = commqueue()
        assert ncq.add('RPM', 10) == True

    def test_add_command_is_int(self):
        ncq = commqueue()
        assert ncq.add(2, 10) == False

    def test_add_interval_is_str(self):
        ncq = commqueue()
        assert ncq.add('RPM', 'invalid') == False

    def test_add_interval_is_int(self):
        ncq = commqueue()
        assert ncq.add('RPM', 10) == True


    # Getnext commands
    def test_getnext_none(self):
        ncq = commqueue()
        ncq.add('RPM', 100)
        assert ncq.getnext() == None

    def test_getnext_waited(self):
        ncq = commqueue()
        ncq.add('RPM', 100)
        ncq.update()
        time.sleep(0.150)
        ncq.update()
        assert ncq.getnext() == 'RPM'

    def test_getnext_second_getnext(self):
        ncq = commqueue()
        ncq.add('RPM', 100)
        ncq.update()
        time.sleep(0.150)
        ncq.update()
        ncq.getnext()
        ncq.update()
        assert ncq.getnext() == None
