def check_divisibility(arr):
    # Step 2: Concatenate Integers
    concatenated_integers = [int(str(arr[i]) + str(arr[j])) for i in range(len(arr)) for j in range(len(arr)) if i != j]

    # Step 3: Check Divisibility
    for num in concatenated_integers:
        if num % 3 == 0:
            print(1)
            return

    # Step 4: Output
    print(0)

# Example Usage:
arr = [19, 6, 3]
check_divisibility(arr)
