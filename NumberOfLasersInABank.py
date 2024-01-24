def number_of_lasers_in_a_bank(bank):
    def number_of_ones(string):
        number = 0
        for i in string:
            if i == "1":
                number += 1
        return number
    answer = 0
        
    devices_array = []

    set_left = False

    left = 0
    for row in range(len(bank)):
        num_of_devices = number_of_ones(bank[row])
        if set_left == False:
            if num_of_devices > 0:
                left = row
                set_left = True
        devices_array.append(num_of_devices)
        
    
    for right in range(left + 1, len(devices_array)):
        if devices_array[right] == 0:
            continue
        devices1 = devices_array[left]
        devices2 = devices_array[right]
        current_lasers = devices1 * devices2
        answer += current_lasers
        left = right
    return answer

print(number_of_lasers_in_a_bank(["011001","000000","010100","001000"]))