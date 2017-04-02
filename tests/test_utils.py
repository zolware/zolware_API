# -*- coding: utf-8 -*-
import six
import unittest
import numpy as np
from zolware.utils import Utils


class TestUtils(unittest.TestCase):
    """Test the State class.
    """
    def setUp(self):
        """Setup a State instance for testing.
        """
        self.u = Utils()

    def test_init(self):
        """Test instance initialization.
        """
        pass

    def test_checkPositiveInteger(self):
        """Test the checkDimension method.
        """
        message = 'The entered value must be a positive integer.'
        with six.assertRaisesRegex(self, ValueError,
                                   message):
            self.u.checkPositiveInteger("a")
        with six.assertRaisesRegex(self, ValueError,
                                   message):
            self.u.checkPositiveInteger(-2)
        with six.assertRaisesRegex(self, ValueError,
                                   message):
            self.u.checkPositiveInteger(0.4)