# test_opendoor.py
"""
Tests for OpenDoor module.
"""

import unittest
from opendoor import OpenDoor

class TestOpenDoor(unittest.TestCase):
    """Test cases for OpenDoor class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OpenDoor()
        self.assertIsInstance(instance, OpenDoor)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OpenDoor()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
