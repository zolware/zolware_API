# -*- coding: utf-8 -*-
import six
import unittest
import numpy as np
from zolware.state import State


class TestState(unittest.TestCase):
    """Test the State class.
    """
    def setUp(self):
        """Setup a State instance for testing.
        """
        self.x0 = [0,0]
        self.P0 = [[1,0],[1,2]]
        self.state = State(self.x0, self.P0)

    def test_init(self):
        """Test instance initialization.
        """
        self.assertEqual(self.state.dim, 2)
        np.testing.assert_array_equal(self.state.x, np.array(self.x0))
        np.testing.assert_array_equal(self.state.P, np.array(self.P0))
