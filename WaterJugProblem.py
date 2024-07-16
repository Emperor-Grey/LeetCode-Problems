def water_jug_problem(jug_one_capacity, jug_two_capacity, target_amount):
    # Initial states of both jugs (0 water initially)
    jug_one_current = 0
    jug_two_current = 0

    # Print initial state
    print(f"Initial state: ({jug_one_current},{jug_two_current})")

    while jug_one_current != target_amount and jug_two_current != target_amount:
        # Fill jug one if it's empty
        if jug_one_current == 0:
            jug_one_current = jug_one_capacity
            print(f"Fill jug 1: ({jug_one_current},{jug_two_current})")

        # Pour water from jug one to jug two
        if jug_one_current > 0:
            pour_amount = min(jug_one_current, jug_two_capacity - jug_two_current)
            jug_one_current -= pour_amount
            jug_two_current += pour_amount
            print(f"Pour from jug 1 to jug 2: ({jug_one_current},{jug_two_current})")

        # Check if we've reached the target amount in either jug
        if jug_one_current == target_amount or jug_two_current == target_amount:
            break

        # If jug two is full, empty it
        if jug_two_current == jug_two_capacity:
            jug_two_current = 0
            print(f"Empty jug 2: ({jug_one_current},{jug_two_current})")

        # If jug one is empty, fill it again
        if jug_one_current == 0:
            jug_one_current = jug_one_capacity
            print(f"Fill jug 1: ({jug_one_current},{jug_two_current})")

    # Print the final state
    print(f"Final state: ({jug_one_current},{jug_two_current})")


# Example usage:
capacity1 = int(input("Enter the capacity of jug 1: "))
capacity2 = int(input("Enter the capacity of jug 2: "))
target = int(input("Enter the target capacity needed: "))
water_jug_problem(capacity1, capacity2, target)
