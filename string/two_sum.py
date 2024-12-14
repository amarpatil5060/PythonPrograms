def two_sum(input, target):
    dict = {}
    for item in range (len(input)):
        x = input[item]
        if target-x in dict:
            return (dict[target-x], item)
        dict[x] = item
        
if __name__ == "__main__":
    input = [2,7,11,15]
    target = 18
    res=two_sum(input, target)
    print(res)