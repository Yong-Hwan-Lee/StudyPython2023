# 글자 인코딩
# ASCII -> 한단어를 표현하는 체계(영어)
# Unicode(UTF-8) -> 모든 나라언어를 다 표현가능

# 파일 만들기
#file = open('C:\\DEV\\Tools\\temp\\bank\\sample01.txt', 'w', encoding='UTF-8') # 파일 쓰기로 만듦
#file = open('C:\DEV\Tools\temp\bank\sample01.txt', 'w', encoding='UTF-8') # 파일 쓰기로 만듦 절대 경로
file = open('./Day05/../Day04/sample06.txt', 'w', encoding='UTF-8') # 파일 쓰기로 만듦 상대경로 . 은 나/ ..은 부모폴더

file.write('안녕하세요\n')
file.write('두번째 파일\n')
file.write('절대경로에 파일에 생성될겁니다.\n')


file.close()
print('sample01.txt가 생성되었습니다.')

# 파일/폴더 경로
