#!/usr/bin/env python


def my_min(my_list):
    min = my_list[0]
    for x in my_list:
        if x < min:
            min = x
    return min


def my_max(my_list):
    max = my_list[0]
    for x in my_list:
        if x > max:
            max = x
    return max


def my_sum(my_list):
    sum = 0
    for x in my_list:
        sum += x
    return sum


def min_max_avg(my_list):
    return my_min(my_list), my_max(my_list), float(my_sum(my_list)) / len(my_list)

print(min_max_avg(range(0, 100000)))
