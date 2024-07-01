def main():
    result = []
    while True:
        start = input('Enter the starting letter: ')
        end = input('Enter the starting letter: ')
        
        
    #check validation of input
    if len(start) > 1 or len(end) > 1 or not start.isalpha() or not end.isalph():
        print("input not valid")
        
    

    """
    ########################################
    Code Your Program here
    ########################################
    """

    print(*result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
