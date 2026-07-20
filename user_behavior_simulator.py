import random

def simulate_user_behavior():
    users = ["User A", "User B", "User C"]

    actions = [
        "Login attempt",
        "API request",
        "Data upload",
        "Model query"
    ]

    return f"{random.choice(users)} performed {random.choice(actions)}"
