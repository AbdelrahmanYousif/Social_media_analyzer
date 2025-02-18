import sys
import os

# Add the `src` directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from utils import get_user_id, get_tweets  # Import directly after modifying sys.path

# Test if get_user_id() returns a valid user ID
def test_get_user_id():
    user_id = get_user_id("Nike")  # Replace with a real username
    assert user_id is not None, "User ID should not be None"
    assert isinstance(user_id, str), "User ID should be a string"

# Test if get_tweets() returns a list
def test_get_tweets():
    user_id = get_user_id("Nike")
    tweets = get_tweets(user_id)
    assert isinstance(tweets, list), "Tweets should be returned as a list"
    
    if tweets:  # If there are tweets, check structure
        assert "text" in tweets[0], "Tweet should contain text"
        assert "public_metrics" in tweets[0], "Tweet should contain public metrics"
