#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            quotient = 0
            if i < len(my_list_1) and i < len(my_list_2):
                dividend = my_list_1[i]
                divisor = my_list_2[i]
                if isinstance(dividend, (int, float)) and (
                        isinstance(divisor, (int, float))):
                    if divisor != 0:
                        quotient = dividend / divisor
                    else:
                        print("division by 0")
                else:
                    print("wrong type")
            else:
                print("out of range")
            result.append(quotient)
        except Exception as e:
            result.append(0)
        finally:
            # Code to be executed whether an exception occurs or not
            pass
    return (result)
