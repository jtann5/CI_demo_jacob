def add(a, b):
	return a + b

def test_add():
	assert add(2, 3) == 5
	assert add('space', 'ship') == 'spaceship'

def subtract(a, b):
	return a - b

def test_subtract():
	assert subtract (2, 3) == -1
