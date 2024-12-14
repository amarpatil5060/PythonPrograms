
def is_dup(input):
    if len(input) == 0 or len(input) == 1:
        return False 
    dict = {}
    for item in input:
        if item in dict:
            return True 
        else :
            dict[item] = 1
    return False 

if __name__ == "__main__":
    input = [1,1,1,1,1]
    res=is_dup(input)
    print(res)
