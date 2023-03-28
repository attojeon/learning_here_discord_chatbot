'''
[1] response.status_code == 200 => 정상적으로 응답이 왔다는 의미

[2] response.headers의 content-type 핵심 사가지 
  - response.headers['content-type'] == 'HTML/CSS' => 웹페이지
  - response.headers['content-type'] == 'image/jpeg'  => 바이너리 이미지 
  - response.headers['content-type'] == 'application/json' => json
  - response.headers['content-type'] == 'text/plain' => 텍스트
    - response.headers['content-type'] == 'text/html' => HTML
    - response.headers['content-type'] == 'text/css' => CSS
    - response.headers['content-type'] == 'text/javascript' => 자바스크립트
    - response.headers['content-type'] == 'application/javascript' => 자바스크립트
    - response.headers['content-type'] == 'application/json' => json
    - response.headers['content-type'] == 'application/xml' => xml
    - response.headers['content-type'] == 'application/pdf' => pdf
    - response.headers['content-type'] == 'application/zip' => zip
    - ... 어마어마하게 많은 형태가 있음.
[3] 그냥 API의 결과물이 어떤 건지 알고 사용하는 걸로.
    - API의 결과물이 json이면 json으로 받아서 처리 response.json()
    - API의 결과물이 이미지면 이미지로 받아서 처리 response.content => 바이너리로 저장, 아래 코드 참고
    - API의 결과물이 HTML이면 text로 처리하든지, 뷰티뷰플숩으로 처리하면 됨. 

[4] response.json()의 결과물은 dict이다.
    - 파이썬코드에서 json을 dict로 변형해서 사용하면 됨.
    - response.json()['key'] => value       : 없으면 에러
    - response.json().get('key') => value   : 없으면 None
    - response.json().get('key', 'default') => value : 없으면 default
'''
import requests
from pprint import pprint 

# 봇명령객체와 접두어 설정하기
url_pic = "https://picsum.photos/seed/picsum/300/200"
url_cat = "https://aws.random.cat/meow"

#########################
# 1단계 : response의 헤드정보를 출력해 보시오. 
#########################



#########################
# 2단계 : 저장하기  
#########################
# image/jpeg => 바이너리 이미지
# 이미지 파일을 저장하는 코드를 작성하시오. 


# application/json => json
# json 파일을 저장하는 코드를 작성하시오.
# 그 json파일을 열어 보시오. 