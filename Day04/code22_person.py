#클래스 생성
class Person:
    name = '익명'
    height = ''
    gender = ''
    blood_type = 'A'

# 1. 생성자 추가
    # def __init__(self):
    #     self.name = '홍길동'
    #     self.height = '170'
    #     self.gender = 'male'
    #     self.blood_type = 'AB'

    def __init__(self, name, height, gender):
        self.name = name
        self.height = height
        self.gender = gender

    def walk(self):
        print(f'{self.name}이/가 걷습니다.')

    def run(self, option):
        if option == 'Fast':
            print(f'{self.name}이/가 빨리 뜁니다')
        else:
            print(f'{self.name}이/가 천천히 뜁니다')
    
    def stop(self):
        print(f'{self.name}이/가 멈춥니다.')

    # 2. 생성자외 매직메서드(펑션) __str__
    def __str__(self) -> str:
        return f'출력 : 이름은 {self.name}, 성별은 {self.gender} 입니다.'

yonghwan = Person('이용환', 171,'male') # 객체를 instance
#yonghwan.name = '이용환'
#yonghwan.height = '171'
#yonghwan.gender = 'male'
#yonghwan.blood_type = 'A'

print(f'{yonghwan.name}의 혈액형은 {yonghwan.blood_type}입니다')

#yonghwan.run('Fast')


# 1. 초기화 후 객체생성
hong = Person('홍길동', 170, 'male')
hong.run('Slow')


print('==================')
ashely = Person('에슐리', 165, 'Female')

print(ashely.name)
print(ashely.height)
print(ashely.gender)
print(ashely)
print(hong)
print(yonghwan)