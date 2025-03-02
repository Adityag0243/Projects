
def inputTaking():
    while True:
        sz = int(input("Enter size for IP address array: "))
        if sz > 0:
            break
        print("Invalid input! Size must +ve value.")

    while True:
        no_of_hash = int(input("Enter number of hash functions (between 1 to 7 inclusive): "))
        if 1 <= no_of_hash <= 7:
            break
        print("Invalid input! Number of hash functions must be between 1 and 7.")
    while True:
        multiplier = int(input("Enter multiplier for size of bitset in filter (between 1 to 7 inclusive): "))
        if 1 <= multiplier <= 7:
            break
        print("Invalid input! multiplier must be between 1 and 7.")


    return sz, no_of_hash, multiplier



def input_taking_with_different_no_of_hash():
    while True:
        sz = int(input("Enter size for IP address array: "))
        if sz > 0:
            break
        print("Invalid input! Size must +ve value.")
    
    while True:
        no_of_hash = int(input("Enter limit for no of hash (between 2 to min(20,sz) inclusive): "))
        if 2 <= no_of_hash <= min(20, sz):
            break
        print("Invalid input! Number of hash functions must be between 2 and 20.")

    while True:
        multiplier = int(input("Enter multiplier for size of bitset in filter (between 1 to 7 inclusive): "))
        if 1 <= multiplier <= 7:
            break
        print("Invalid input! multiplier must be between 1 and 7.")
    

    return sz, no_of_hash, multiplier




