check_list = [11, 13, 14, 16, 17, 18, 19, 20]

print(min([num for num in range(2520, 999999999, 2520) if all(num %
                                                              n == 0 for n in check_list)]))
