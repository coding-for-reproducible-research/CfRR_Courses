# tests/test_advanced.py

import pytest

class ExampleTestClass:
    # Class-level setup and teardown (executed once for the entire class)
    @classmethod
    def setup_class(cls):
        print("\nClass-level setup")
        cls.class_resource = "Class resource setup"

    @classmethod
    def teardown_class(cls):
        print("\nClass-level teardown")
        cls.class_resource = None

    # Object-level setup and teardown (executed before each test method)
    def setup_method(self):
        print("\nObject-level setup")
        self.test_resource = "Test resource setup"

    def teardown_method(self):
        print("\nObject-level teardown")
        self.test_resource = None

    def test_addition(self):
        assert 1 + 1 == 2
        print(f"Using {self.test_resource}")

    def test_subtraction(self):
        assert 2 - 1 == 1
        print(f"Using {self.test_resource}")

