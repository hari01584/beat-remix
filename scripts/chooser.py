def get_choice(n):
    # Get choice from user
    try:
        val = int(input("Choose an option [0-%d]: "%(n-1, )))
        if val < 0 or val > n:
            raise ValueError
        return val
    except ValueError:
        print("Invalid option, Choose again ")
        return get_choice(n)
    
def choose(options):
    for i in range(len(options)):
        print("[%d] %s"%(i, options[i]))
    index = get_choice(len(options))
    return index
