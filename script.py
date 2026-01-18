import random

name_list = []
password_list = []
key_list = []


def add_user(name_list, password_list):
    if input("새 사용자를 등록하시겠습니까?등록하려면 Y를 입력하세요.:") in ["Y","y"]:
        globals()[f'{name}_password'] = input("사용할 비밀번호를 입력하시오.:")
    else:
        print("등록에 실패하였습니다.")
        return
    name_list.append(name)
    password_list.append(globals()[f'{name}_password'])
    print(f'{name}님이 성공적으로 등록되었습니다.')

while True:
    name = input("이름을 입력하세요.:")

    if name in name_list:
        if input("비밀번호를 입력하시오.:") == globals()[f'{name}_password']:
            print("로그인 성공!")
            access = True
            while access == True:

                answer = random.randint(1, 100)

                trash = True

                while 1:
                    if trash == True:
                        print("게임 시작!")
                        trash = False

                    user_answer = input("1부터 100사이의 수를 입력해주세요:")

                    if user_answer == "Logout":
                        access = False
                        break
                    else:
                        user_answer = int(user_answer)

                        if user_answer < answer:
                            print("UP!")
                        elif user_answer > answer:
                            print("DOWN!")
                        elif user_answer == answer:
                            print(f'맞습니다!{answer}이(가) 정답입니다!')
                            break
        else:
            print("비밀번호가 틀렸습니다.")
    else:
        add_user(name_list,password_list)