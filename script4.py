msg = "출력할 돈을 입력해주세요:"
while True:
    try:
        money = int(input(msg))

        count_50000, remainder_50000 = divmod(money, 50000)
        count_10000, remainder_10000 = divmod(remainder_50000, 10000)
        count_5000 , remainder_5000 = divmod(remainder_10000, 5000)
        count_1000, remainder_1000 = divmod(remainder_5000, 1000)
        count_500, remainder_500 = divmod(remainder_1000, 500)
        count_100, remainder_100 = divmod(remainder_500, 100)
        count_50, remainder_50 = divmod(remainder_100, 50)
        count_10, remainder_10 = divmod(remainder_50, 10)
        count_5, remainder_5 = divmod(remainder_10, 5)
        count_1, remainder_1 = divmod(remainder_5, 1)

        if count_50000 > 0: print(f"50000원짜리가 {count_50000}장,")
        if count_10000 > 0: print(f"10000원짜리가 {count_10000}장,")
        if count_5000 > 0:  print(f"5000원짜리가 {count_5000}장,")
        if count_1000 > 0:  print(f"1000원짜리가 {count_1000}장,")
        if count_500 > 0:   print(f"500원짜리가 {count_500}개,")
        if count_100 > 0:   print(f"100원짜리가 {count_100}개,")
        if count_50 > 0:    print(f"50원짜리가 {count_50}개,")
        if count_10 > 0:    print(f"10원짜리가 {count_10}개,")
        if count_5 > 0:     print(f"5원짜리가 {count_5}개,")
        if count_1 > 0:     print(f"1원짜리가 {count_1}개")

        print("출력되었습니다.")

        msg = "출력할 돈을 입력해주세요:"
    except ValueError:
        msg = "다시 입력하세요:"
