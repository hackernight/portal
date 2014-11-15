import service as serv

def test_doors_toggle_happyPath():
	message = serv.open(1)
	
	assert "toggling" in message
	assert "invalid" not in message

def test_doors_toggle_negative():
	message = serv.open(-35)
	
	assert "toggling" not in message
	assert "invalid" in message