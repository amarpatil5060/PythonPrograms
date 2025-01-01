def remove_dup_in_place(num):
    if len(num) <2:
        return len(num)
    i = 0
    new_num = []
    while i < len(num)-1:
        if num[i] == num[i+1]:
            i = i+1 
        else:
            new_num.append(num[i])
            i = i+1
    new_num.append(num[i])
    return new_num

if __name__ == "__main__":
    input = [1,2,4,4]
    res = remove_dup_in_place(input)
    print("After removing duplicate input length:", res)
