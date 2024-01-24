def seperate_balck_and_white(string):
    num_of_zeros = 0
    answer = 0

    for i in range(len(string)):
        if string[i] == "0":
            dist = i - num_of_zeros
            num_of_zeros += 1
            answer += dist
    return answer


print(seperate_balck_and_white("101011"))