# urllib 패키지 불러오기 인터넷 = 네트워크를 통한 request response
from urllib.request import Request,urlopen

req = Request('https://www.naver.com')
res = urlopen(req)
print(res.status)   