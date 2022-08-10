import unittest
import logging

log = logging.getLogger('verbose')
log.setLevel(logging.INFO)

"""This class is mapping the part of the asserts in order to have a log into the report"""


class MappingAsserts(unittest.TestCase):
    def assertEqual(self, first, second, msg=None):
        log.info("Assert Equal " + str(first) + " with " + str(second))
        unittest.TestCase.assertEqual(self, first, second, msg=None)

    def assertIn(self, member, container, msg=None):
        log.info("Assert In " + str(member) + " with " + str(container))
        unittest.TestCase.assertIn(self,member,container,msg=None)

    def assertNotEqual(self, first, second, msg=None):
        log.info("Assert Not Equal: " +str(first) + " with: " + str(second))
        unittest.TestCase.assertNotEqual(self, first, second, msg=None)

    def assertFalse(self, expr, msg=None):
        log.info("Assert False " + str(expr))
        unittest.TestCase.assertFalse(self, expr, msg=None)

    def assertEquals(self, first, second, msg=None):
        log.info("Assert Equals " + str(first) + " with " + str(second))
        unittest.TestCase.assertEqual(self, first, second, msg=None)