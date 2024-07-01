def main():
    
    while True:
        result = []
        start = input('Enter the starting letter: ')
        end = input('Enter the starting letter: ')
        
        
    #check validation of input
        if len(start) != 1 or len(end) != 1 or not start.isalpha() or not end.isalpha():    
            print("input not valid")
            continue
        
        if start > end:
            print("input not valid")
        
    #convert input alphabet into ascii value can be put into range
        start_ascii = ord(start)
        end_ascii = ord(end)
    
    #print
        for i in range(start_ascii, end_ascii + 1):
            result .append(chr(i))
        

    print(result)

    return result


if __name__ == '__main__':
    main()
