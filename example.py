def add(a, b):
	return a - b

def test_add():
	assert add(2, 3) == 5
	assert add('space', 'ship') == 'spaceship'

def subtract(a, b):
	return a - b

test_add()
