from zoneinfo import reset_tzpath
import requests
from pprint import pprint

def search(title): # id 값 추출
    URL = 'https://api.themoviedb.org/3'
    path = '/search/movie' # 상세경로
    params = {
        'api_key': '3d086799f6ddf19a461e5ed8f4712adf',
        'language': 'ko-KR',
        'query': f'{title}'
    }
    response = requests.get(URL + path, params = params).json().get('results') # results 값을 response에 넣어준다. 
                                                                               # response는 딕셔너리 3개를 리스트로 감싼 형태 
    for i in range(len(response)): # i에 response 값의 개수를 넣어준다. 
        return response[i].get('id') # return은 첫 번째의 값만 반환한다. (response[i]는 3개의 딕셔너리)

def credits(title):
    movie_id = search(title)    # id값을 반환한 serach 함수의 값을 movie_id에 넣어준다. 
    URL = 'https://api.themoviedb.org/3'
    path=f'/movie/{movie_id}/credits'
    params = {
        'api_key': '3d086799f6ddf19a461e5ed8f4712adf',
        'language': 'ko-KR',
        'query': f'{title}'
    }
    if movie_id == None:         # 영화 id 검색에 실패할 경우 None을 반환한다.
        return None 

    # 딕셔너리 추출 == get()
    response1 = requests.get(URL + path, params=params).json().get('cast') # 리스트 안 딕셔너리
    response2 = requests.get(URL + path, params=params).json().get('crew')

    # 리스트를 만들어준다. 
    cast_list = {}
    cast_list1 = []
    cast_list2 = []

    # 리스트 추출 == for문 range()
    # 1. the name of cast 정보를 cast_list1에 넣기
    for i in range(len(response1)):
        if response1[i].get('cast_id') < 10:
            cast_list1.append(response1[i].get('name'))

    # 2. the name of Directing in department 정보를 cast_list2에 넣기
    for j in range(len(response2)):
        if 'Directing' in response2[j].get('department'):
            cast_list2.append(response2[j].get('name'))
   
        cast_list = {"cast":cast_list1, "crew":cast_list2} # 딕셔너리 형태로 만들며, 
                                                           # cast_list1&2의 정보를 cast_list에 넣기
    
    return cast_list

    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
