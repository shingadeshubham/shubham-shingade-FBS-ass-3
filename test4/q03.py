def z_pattern(width, diag):
    
    print("*" * width)

    
    for i in range(1, diag + 1):
        spaces = width - i - 1
        print(" " * spaces + "*")

    
    print("*" * width)


z_pattern(22, 20)   
