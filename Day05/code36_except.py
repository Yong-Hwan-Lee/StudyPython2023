# 예외처리
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

try:
    x, y = input('두 수를 입력하세요 > ').split()
    x = int(x)
    y = int(y)
except Exception as e:
    print(e)
    exit()
finally:
    print('finally는 exit여도 무조건시행 후 종료') #이거 실행뒤 종료

#원시적인 예외처리
# if y == 0:
#     print('y에 0을 넣지마세요')
#     exit()

print('계산 테스트')
try:
    print('나눗셈은', div(x, y))
# except ZeroDivisionError as e:
#     print('0으로 나누기 불가')
except Exception as e:
    print(e)
finally:
    print('계산은 계속됩니다')
    

print('덧셈은', add(x, y))
print('곱셈은', mul(x, y))
