def remove_dup_in_place(num):
    if len(num) <2:
        return num
    write_index = 1
    for i in range(1, len(num)):
        print(f"Comparing num[{i}] = {num[i]} with num[{i-1}] = {num[i-1]}")
        if num[i] != num[i-1]:
            num[write_index] = num[i]
            write_index += 1
    return num[:write_index]
    

if __name__ == "__main__":
    input = [1,2,2,4]
    res = remove_dup_in_place(input)
    print("After removing duplicate input length:", res)