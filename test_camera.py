from camera import booking_decision

def test_approve():
    assert booking_decision('2', '1', '3', '10') == "APPROVED"

def test_conditionally_approve():
    assert booking_decision('4', '2', '3', '10') == "CONDITIONALLY_APPROVED"

def test_reject():
    assert booking_decision('6', '3', '5', '10') == "REJECTED"
