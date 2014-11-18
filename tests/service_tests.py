import service as serv

def test_doors_toggle_happyPath():
	message = serv.toggle("ONE")
	
	print message
	assert "toggling" in message
	assert "invalid" not in message

def test_doors_toggle_negative():
	message = serv.toggle(-35)
	
	print message
	assert "toggling" not in message
	assert "invalid" in message

def test_doors_getIds():
	message = serv.getIds()

	print message
	assert "ONE" in message
	assert "TWO" in message