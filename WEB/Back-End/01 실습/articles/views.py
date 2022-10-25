from multiprocessing import context
from django.shortcuts import render
import random

# Create your views here.
def today_dinner(request):
    dinners = [
        ['삼겹살', 'https://cwcontent.asiae.co.kr/asiaresize/219/2022040414050315369_1649048703.jpg'],
        ['칼국수', 'https://w.namu.la/s/f2ae78f52c8b6849f850960066cda890734d272c80c488fa822caca33ab3b69ba5fe6c3f1c862d67e4978856f729384492156a462e33ee9c78b0c8d8e733d9d2911cdfadf8aa7555bbb2616d9483e44b57c9dea76392f9a83773f6ae90750c5af83c1c5313b97b897a93fc05e8fccfc4'],
        ['샌드위치', 'https://www.coffeebeankorea.com/data/menu/%EB%B8%8C%EB%A6%AC%EC%98%A4%EC%8A%88-%ED%86%A0%EB%A7%88%ED%86%A0-%EB%AF%B8%ED%8A%B8%EB%B3%BC-%EC%83%8C%EB%93%9C%EC%9C%84%EC%B9%98.jpg'],
        ['초밥', 'https://hajl.athuman.com/karuta/uploads/6e45128aad8bdcf39055b81840ecbe0186605633.jpeg'],
        ['갈비탕', 'https://cdnweb01.wikitree.co.kr/webdata/editor/202012/01/img_20201201124407_672e1b16.webp'],
        ['햄버거', 'https://cdn.thekpm.com/news/photo/202201/106072_86332_1730.jpg'],
        ['닭갈비', 'https://www.ghostfreshmart.com/wp-content/uploads/2020/04/%EB%A7%A4%EC%9A%B4%EB%8B%AD%EA%B0%88%EB%B9%84.jpg'],
        ['티본 스테이크', 'https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile10.uf.tistory.com%2Fimage%2F991688365C91ACC82722B5'],
    ]

    dinner = random.choice(dinners)

    context = {
        'dinner': dinner[0],
        'image': dinner[1],
    }

    return render(request, 'today_dinner.html', context)

def lotto(request):

    # pick = random.sample(range(1, 46), 6)

    # context = {
    #     'pick': pick
    # }

    return render(request, 'lotto.html')