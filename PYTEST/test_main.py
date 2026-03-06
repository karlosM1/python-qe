# from main import UserManager
# from main import Database
from main import is_prime
import pytest

# @pytest.fixture
# def user_manager():
#     """Creates a fresh instance of UserManager before each test."""
#     return UserManager()
  
# def test_add_user(user_manager):
#     assert user_manager.add_user("john_doe", "john@example.com") == True
#     assert user_manager.get_user("john_doe") == "john@example.com"

# def test_add_duplicate_user(user_manager):
#     user_manager.add_user("john_doe", "john@example.com")
#     with pytest.raises(ValueError):
#       user_manager.add_user("john_doe", "john@example.com")

# @pytest.fixture
# def db():
#   database = Database()
#   yield database
#   database.data.clear()

# def test_add_user(db):
#   db.add_user(1, "Alice")
#   assert db.get_user(1) == "Alice"

# def test_add_duplicate_user(db):
#   db.add_user(1,"Alice")
#   with pytest.raises(ValueError, match="User already exists."):
#     db.add_user(1, "Bob")

# def test_delete_user(db):
#   db.add_user(2, "Bob")
#   db.delete_user(2)
#   assert db.get_user(2) is None

# @pytest.mark.parametrize("num, expected", [
#   (1, False),
#   (2, True),
#   (3, True),
#   (4, False),
#   (17, True),
#   (18, False),
#   (19, True),
#   (25, False),
# ])
# def test_is_prime(num, expected):
#   assert is_prime(num) == expected


