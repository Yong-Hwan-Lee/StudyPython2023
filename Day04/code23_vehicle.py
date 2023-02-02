# 자동차 클래스
class Car:
    __number = '54라 9538'

    def get_number(self):
        return self.__number
    
    def __init__(self, number='54라 9538') -> None:
        print('__init__')
        self.__number = number

    # 클래스 외부에선 변경불가, 멤버함수로는 변경가능
    def set_number(self, number):
        self.__number = number


    # def __new__(cls):
    #     print('__new__')
    #     return super().__new__(cls) #부모 클래스 상속
    
    def __str__(self) -> str :
        return f'차 번호는 {self.__number}입니다'

yourcar = Car('88호 7486')
print(yourcar)
yourcar.__number = '54라 9999'  #외부에서는 멤버변수에 접근불가
print(yourcar)

print('클래스 내부함수 사용!')
yourcar.set_number('55오 5555')
print(yourcar)

mycar = Car()   
print(mycar)
print(f'차종은 아이오닉이고, 번호는 {mycar.get_number()}에요.')

mycar.__number = '132거 8874'
print(mycar)