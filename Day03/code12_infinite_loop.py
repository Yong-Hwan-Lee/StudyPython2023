# 무한반복 예제
num =  0

while True: # 무한 반복
    print('메뉴를 선택하세요.')
    print('  1. 회원입력')
    print('  2. 회원검색')
    print('  3. 회원수정')
    print('  4. 회원삭제')
    print('  5. 프로그램 종료')
    num = int(input('메뉴번호 입력 >'))

    if num == 1:
        print('회원입력 시작!')
        pass
    elif num == 2:
        print('회원검색 시작!')
        pass
    elif num == 3:
        print('회원수정 시작!')
        pass
    elif num == 4:
        print('회원삭제 시작!')
        pass
    elif num == 5:
        print('프로그램 종료')
        break
    else:
        continue