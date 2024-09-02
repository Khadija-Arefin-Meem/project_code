def calculator(op,a,b):
    match op:
        case '1':
            return a+b
        case '2':
            if a>b:
                return a-b
            else:
                return b-a
        case '3':
            return a*b
        case '4':
            return a/b if b!=0 else "error"
        case none:
            return "Wrong operation"
        
        