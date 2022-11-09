def find_solutions(*numbers, answer=0):
    global sum_sub
    log = []
    sum_sub = "0"*len(numbers)
    finished = False
    while not finished:
        reversed_sum_sub = reverse_string(sum_sub)
        for digit_id, digit in enumerate(reversed_sum_sub):
            print(f"""sum_sub: {sum_sub}, reversed: {reversed_sum_sub}, digit_id = {digit_id}""")
            if digit == "0":
                result = 0
                for number_id, number in enumerate(numbers):
                    if sum_sub[number_id] == "0":
                        result += number
                    else:
                        result -= number
                print(f"""result: {result}, expected: {answer}""")
                if result == answer:
                    log.append(sum_sub)
                if digit_id-1 >= 0:
                    real_id = len(numbers)-digit_id-1
                    for replace_id in range(real_id, len(numbers)):
                        print(f"real_id: {replace_id}")
                        sum_sub = change_string(sum_sub, replace_id, "0")
                sum_sub = change_string(sum_sub, len(numbers)-digit_id-1, "1")
                #sum_sub = "1"*len(numbers)
                break
            if sum_sub == "1"*len(numbers):
                finished = True
    print(log)


def change_string(string, position, changeto):
    string_before = string[0:position]
    string_after = string[position+1:len(string)]
    new_string = string_before + changeto + string_after
    return new_string

def reverse_string(string):
    new_string = ""
    for id in range(len(string)):
        new_string += string[len(string)-id-1]
    return new_string

find_solutions(2,4,9,8, answer=9)
