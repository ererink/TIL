import requests

def popular_count():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular' # 상세경로
    params = {
        'api_key': '3b6818af52c899a45712c6e71f6ecc94',
        'language': 'ko-KR'
    }
    response = requests.get(BASE_URL+path, params=params).json() # 인기영화 정보를 response에 넣어준다. 
    # print(response)
    return len(response.get('results')) # response의 results의 개수를 반환하도록 한다. 
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count()) # results의 개수를 세는 (기능을 하는) popular_count를 출력한다. 
    # 20
