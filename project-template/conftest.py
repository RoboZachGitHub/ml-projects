# Placeholder for shared fixtures related to all pytests
import pytest
import numpy as np

@pytest.fixture
def sample_data():
    X = np.random.rand(100, 4)
    y = np.random.rand(100)
    return X, y
