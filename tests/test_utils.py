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

    def test_checkDimension(self):
        """Test the checkDimension method.
        """
        message = 'The dimension must be a positive integer.'
        with six.assertRaisesRegex(self, ValueError,
                                   message):
            self.u.checkDimension("a")
        with six.assertRaisesRegex(self, ValueError,
                                   message):
            self.u.checkDimension(-2)
        with six.assertRaisesRegex(self, ValueError,
                                   message):
            self.u.checkDimension(0.4)