from itertools import permutations

def count_super_dependent_functions():
    n = int(input("Enter the value for n: "))
    AllF = list(range(1 << n)) 
    original_values = AllF.copy()  
    total_super_dependent = 0
    SBOXES = []  
    # Iterate over all permutations of the values list
    for permuted in permutations(AllF):
        dependent_count = 0
        for function_position in range(n):  # Iterate through each function position
            function_extraction = [(num >> function_position) & 1 for num in permuted]  # Extract functions
            change_count = 0
            # Check each function for dependency changes
            for check_function in range(n):
                for index in range(1 << n):  # Iterate through all possible values of function
                    if function_extraction[index] ^ function_extraction[index ^ (1 << check_function)]:  # Check for changes
                        change_count += 1
                        break  # Stop after the first change
            dependent_count += (change_count == n)  # Increment if function is dependent on all bits
        if dependent_count == n:
            total_super_dependent += 1
            SBOXES.append(list(permuted))
    
    with open('generated_sboxes.txt', 'w') as f:
        for sbox in SBOXES:
            f.write(f"{sbox}\n")    
    
    print(f"Super-dependent SBoxes written to 'generated_sboxes.txt'")
    print(f"Total super-dependent functions: {total_super_dependent}")

if __name__ == "__main__":
    count_super_dependent_functions()
