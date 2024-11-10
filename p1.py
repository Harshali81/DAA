def fibonacci(n_terms):
    n_1 = 0
    n_2 =1
    step_count = 0  # To track the number of steps
    sequence = []  # To store the Fibonacci sequence

    if n_terms <= 0:
        print("Please enter a positive integer, the given number is not valid")
        return None, step_count, sequence  # Returning None, step count, and an empty sequence

    elif n_terms == 1:
        sequence.append(n_1)
        print(f"The Fibonacci number at position {n_terms} is: {n_1}")
        print(f"The Fibonacci sequence up to {n_terms} is: {sequence}")
        return n_1, step_count, sequence

    else:
        while step_count < n_terms:
            sequence.append(n_1)  # Add the current Fibonacci number to the sequence
            if step_count == n_terms - 1:
                print(f"The Fibonacci number at position {n_terms} is: {n_1}")
            nth = n_1 + n_2
            n_1 = n_2
            n_2 = nth
            
            step_count += 1

    print(f"The Fibonacci sequence up to {n_terms} is: {sequence}")
    return n_1, step_count, sequence

# Test the function
n_terms = int(input("Enter the position of Fibonacci number you want to find: "))
fibonacci_number, steps, sequence = fibonacci(n_terms)
print(f"Number of steps taken to compute the Fibonacci number: {steps}")
