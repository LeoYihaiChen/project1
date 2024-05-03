import random

def forlist(list):
    out = []
    for i in list:
        out.append(i)
    return out

def test_forlist(testlists): # 仅限于forlist函数
    for testlist in testlists:
        print(f"testlist = {testlist}")
        
        result = forlist(testlist)
        print("output = ", result)
        
        if result != testlist:
            print("output error")

    
if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    
    testdata = [
        [5, 2, 3, 6, 4, 1, 0],
        [0, 1, 2, 3, 4, 5, 6],
        [6, 5, 4, 3, 2, 1, 0],
        [1, 4, 3, 2, 6, 5, 0, 6, 3, 2],
        [0, 1, 5, 4, 2, 3, 6, 6, 6, 3, 9, 4, 3, 4],
        [1, 6, 4, 5, 3, 6, 2, 4, 6, 3, 6, 3, 2, 9, 6, 4, 8, 5, 3, 3],
        [],
        [1]
    ]
    
    test_forlist(testdata)