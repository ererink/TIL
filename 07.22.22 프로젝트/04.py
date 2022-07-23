import requests
from pprint import pprint

def search(title): # id 값을 추출하는 역할
    URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': '3d086799f6ddf19a461e5ed8f4712adf',
        'language': 'ko-KR',
        'query': f'{title}'
    }
    response = requests.get(URL + path, params = params).json().get('results') # results 값을 response에 넣어준다. 
                                                                               # response는 딕셔너리 3개를 리스트로 감싼 형태 

    for i in range(len(response)): # response 값의 개수를 i에 넣어준다. (언패킹; 3개의 딕셔너리 형태로 출력)
        return response[i].get('id') # return은 첫 번째의 값만 반환한다. (response[i]는 3개의 딕셔너리)
        

def recommendation(title): 
    movie_id = search(title)    # id값을 반환한 serach 함수의 값을 movie_id에 넣어준다. 
    URL = 'https://api.themoviedb.org/3'
    path=f'/movie/{movie_id}/recommendations'
    params = {
        'api_key': '3d086799f6ddf19a461e5ed8f4712adf',
        'language': 'ko-KR',
        'query': f'{title}'
    }
    
    if movie_id == None:        # 영화 id 검색에 실패할 경우 None을 반환한다.
        return None 

    # 딕셔너리 추출 == get()
    response = requests.get(URL + path, params=params).json().get('results') # results의 값을 response에 넣어준다. 
    
    recm_list = []              # 리스트를 만들어준다. 
        
    # 리스트 추출 == for문 range()
    for i in range(len(response)): # response 값의 개수를 i에 넣어준다. (20개의 딕셔너리 형태 영화 목록)
        recm_list.append(response[i].get('title')) # 20개의 영화목록에서 title만 recm_list에 넣어준다. 
    
    return recm_list
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None 