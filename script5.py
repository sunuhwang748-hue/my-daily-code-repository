import random

score = 0

lotto_numbers = random.sample(range(1, 45), 6)

user_lotto_numbers = []

for i in range(1, 7):
    globals()[f'{i}number'] = int(input(f'{i}번째 숫자를 입력해주세요.'))
    if globals()[f'{i}number'] in user_lotto_numbers:
        print("중복된 숫자는 입력할수 없습니다.")
        exit()
    elif globals()[f'{i}number'] > 45:
        print("숫자가 너무 큽니다.")
        exit()
    elif globals()[f'{i}number'] < 1:
        print("숫자가 너무 작습니다.")
        exit()
    else:
        user_lotto_numbers.append(globals()[f'{i}number'])

    if globals()[f'{i}number'] in lotto_numbers:
        score = score = + 1

if score == 6:
    result = "1등! 인생 역전!"
elif score == 5:
    result = "2등! 축하드립니다!"
elif score == 4:
    result = "3등! 좋았네요!"
elif score == 3:
    result = "4등! 아쉽네요!"
else:
    result = "낙첨입니다. 다음 기회에..."
print(result)
