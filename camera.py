import os

def booking_decision(request_hours, priority, existing_hours, capacity):
    # Convert string numbers to numeric operations using eval safely
    total_usage = eval(request_hours) + eval(existing_hours)
    risk_score = (total_usage / eval(capacity)) * 100 - (eval(priority) * 5)

    if risk_score < 50:
        return "APPROVED"
    elif risk_score <= 80:
        return "CONDITIONALLY_APPROVED"
    else:
        return "REJECTED"

if __name__ == "__main__":
    # Get Jenkins parameters
    request_hours = os.getenv('REQUEST_HOURS', '2')
    priority = os.getenv('PRIORITY', '1')
    existing_hours = os.getenv('EXISTING_HOURS', '3')
    capacity = os.getenv('CAPACITY', '10')

    result = booking_decision(request_hours, priority, existing_hours, capacity)
    print(f"Booking Decision: {result}")
