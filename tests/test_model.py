# -*- coding: utf-8 -*-
# import six
import unittest
# import numpy as np
from zolware.model import Model
# from zolware.utils import BASE_DIR


class TestModel(unittest.TestCase):
    """Test the Model class.
    """
    def setUp(self):
        """Setup a Model instance for testing.
        """
        self.model = Model()

    def test_init(self):
        """test class initialization
        """
        self.assertEqual("a", "a")
