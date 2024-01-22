def minimumOperations(number):
    found_zero = False

    def find_nearest_match(number,matchs_for_number,idx):
        nearest = float("-inf")
        for i in range(0, idx):
            if number[i] in matchs_for_number:
                nearest = max(nearest, i)
        return nearest

    answer = float("inf")

    matches_for_zero = ["0", "5"]
    matches_for_five = ["2", "7"]

    for i in range(len(number)):
        if number[i] == "0" or number[i] == "5":
            current_answer = 0
            if number[i] == "0":
                found_zero = True
                l_match = find_nearest_match(number, matches_for_zero,i)
                if i == 5:
                    print(l_match, "I am l_match")
                if l_match == float("inf"):
                    continue
                if l_match == "0" and number[0] == "0":
                    continue
                in_between = i - l_match - 1
                after = len(number) - i - 1
                current_answer = in_between + after
            if number[i] == "5":
                l_match = find_nearest_match(number, matches_for_five,i)
                if l_match == float("inf"):
                    continue
                in_between = i - l_match - 1
                after = len(number) - i - 1
                current_answer = in_between + after
            
            answer = min(answer, current_answer)

    if answer == float("inf"):
        if found_zero:
            return len(number) - 1
        else:
            return len(number)

    return answer

        
# print(minimumOperations("5628006"))

def min_operations(number):
    if int(number) % 25 == 0:
        return 0
    
    answer = float("inf")

    nums_we_need = ["0", "5", "2", "7"]
    
    found_zero = False

    tuple_array = []

    for i in range(len(number)):
        if number[i] in nums_we_need:
            if number[i] == "0":
                found_zero = True
            tuple_array.append((number[i], i))
    
    for i in range(len(tuple_array)):
        starting_number = tuple_array[i][0]
        idx = tuple_array[i][1]

        if starting_number == "2":
            for j in range(i + 1, len(tuple_array)):
                if tuple_array[j][0] == "5":
                    req_idx = tuple_array[j][1]
                    l_match = req_idx - idx - 1
                    r_match = len(number) - req_idx - 1
                    answer = min(answer, l_match + r_match)

        if starting_number == "7":
            for j in range(i + 1, len(tuple_array)):
                if tuple_array[j][0] == "5":
                    req_idx = tuple_array[j][1]
                    l_match = req_idx - idx - 1
                    r_match = len(number) - req_idx - 1
                    answer = min(answer, l_match + r_match)
        if starting_number == "0":
            for j in range(i + 1, len(tuple_array)):
                if tuple_array[j][0] == "0":
                    req_idx = tuple_array[j][1]
                    l_match = req_idx - idx - 1
                    r_match = len(number) - req_idx - 1
                    answer = min(answer, l_match + r_match)
        if starting_number == "5":
            for j in range(i + 1, len(tuple_array)):
                if tuple_array[j][0] == "0":
                    req_idx = tuple_array[j][1]
                    l_match = req_idx - idx - 1
                    r_match = len(number) - req_idx - 1
                    answer = min(answer, l_match + r_match)
    if answer == float("inf"):
        if found_zero:
            return len(number) - 1
        else:
            return len(number)

    return answer
    
        
    

print(min_operations("10"))