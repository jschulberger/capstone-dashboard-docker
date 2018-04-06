import pytest
import mock
import unittest
from errorhandler import errorhandler
import time

class TestErrorhandler(object):
    def test_sanity(self):
        assert True == True

    def test_is_type_str(self):
        eh = errorhandler()
        assert eh.isTypeStr("msg") == True

    def test_add_msg_invalid_sender(self):
        eh = errorhandler()
        eh.add(0, 'sender is invalid')
        assert eh.numEntriesOfSender('eh') == 1

    def test_add_msg_invalid_msg(self):
        eh = errorhandler()
        eh.add('test', 0)
        assert eh.numEntriesOfSender('eh') == 1

    def test_add_msg_invalid_sender_msg(self):
        eh = errorhandler()
        eh.add(0, 0)
        assert eh.numEntriesOfSender('eh') == 2

    def test_get_entries_of_sender(self):
        eh = errorhandler()
        poss_entries = [
                          ["test", "message1"],
                          ["test", "message2"],
                          ["test", "message3"],
                          ["test", "message4"],
                          ["test", "message5"],
                       ]
        for i in range(len(poss_entries)):
            eh.add(poss_entries[i][0], poss_entries[i][1])
        assert [i[1] for i in poss_entries] == [i[0] for i in eh.getEntriesOfSender('test', False)]

    def test_get_entries_of_sender_mixed_senders(self):
        eh = errorhandler()
        eh.add(0, 0)
        poss_entries = [
                          ["test", "message1"],
                          ["test", "message2"],
                          ["test", "message3"],
                          ["test", "message4"],
                          ["test", "message5"],
                       ]
        for i in range(len(poss_entries)):
            eh.add(poss_entries[i][0], poss_entries[i][1])
        eh.add(0, 0)
        assert [i[1] for i in poss_entries] == [i[0] for i in eh.getEntriesOfSender('test', False)]

    def test_get_entries_of_sender_remove(self):
        eh = errorhandler()
        poss_entries = [
                          ["test", "message1"],
                          ["test", "message2"],
                          ["test", "message3"],
                          ["test", "message4"],
                          ["test", "message5"],
                       ]
        for i in range(len(poss_entries)):
            eh.add(poss_entries[i][0], poss_entries[i][1])
        eh.getEntriesOfSender('test', True)
        assert [] == [i[0] for i in eh.getEntriesOfSender('test', True)]

    def test_get_entries_of_sender_keep(self):
        eh = errorhandler()
        poss_entries = [
                          ["test", "message1"],
                          ["test", "message2"],
                          ["test", "message3"],
                          ["test", "message4"],
                          ["test", "message5"],
                       ]
        for i in range(len(poss_entries)):
            eh.add(poss_entries[i][0], poss_entries[i][1])
        first_get = eh.getEntriesOfSender('test', False)
        assert first_get == eh.getEntriesOfSender('test', False)
