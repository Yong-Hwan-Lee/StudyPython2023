# 라이프 스코프
a = 1

def vartest():
    global a # 전역에 있는 a를 함수(지역)에서 가져다 사용
    a = a + 1
    return a

a = vartest()
print(a)