def fibonacci_leo(n = 1):
    a = 0
    b = 1
    
    out = []
    if n % 2 == 0:
        for i in range(int(n/2)):        
            out.append(a)
            out.append(b)     
            a = a + b
            b = a + b
        
    else:
        for i in range(int((n-1)/2)):
            out.append(a)
            out.append(b)     
            a = a + b
            b = a + b
            
        out.append(a)           
        
    return out


if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(fibonacci_leo(10))
