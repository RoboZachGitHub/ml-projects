# generic pytest compliant test_model.py file 

def test_model_output_shape(sample_data):
    X, y = sample_data
    # assert your model output shape, dtype, etc.
    assert X.shape == (100, 4)
