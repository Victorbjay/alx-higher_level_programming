#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = 0
    result_list = []
    while (i < list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            result_list.append(result)
        i += 1
    return (result_list)
