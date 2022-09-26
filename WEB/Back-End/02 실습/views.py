from tabnanny import check
from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, "index.html")


def ping(request):
    return render(request, "ping.html")


def pong(request):
    # ball에 데이터 받기
    ball = request.GET.get("ball")
    # 받은 데이터(ball)는 name으로 사용할 것이다.
    context = {
        "name": ball,
    }

    return render(request, "pong.html", context)

    # 한줄로 표현하기
    # return render(request, 'pong.html', {'name': request.GET.get('ball')})


def print_text(request):
    text = request.GET.get("_text")

    context = {
        # "템플릿 파일(.html)에서 사용할 변수 이름" : 값
        "template_text": text,
    }

    return render(request, "text.html", context)


# 1번 짝수/홀수
def is_odd_even(request, _number):
    number = _number
    if number == 0:
        check = 0

    elif number % 2 == 0:
        check = "짝수"

    else:
        check = "홀수"

    context = {"number": _number, "check": check}

    return render(request, "is_odd_even.html", context)


# 2번 사칙연산
def operation(request, number1, number2):
    context = {
        "number1": number1,
        "number2": number2,
        "plus": number1 + number2,
        "subtract": number1 - number2,
        "divide": number1 // number2,
        "multiply": number1 * number2,
    }

    return render(request, "operation.html", context)


# 3번
def random_past(request):

    return render(request, "random_past.html")


def random_past2(request):
    # ball에 데이터 받기
    ball = request.GET.get("ball")

    # 랜덤 전생 리스트
    lifes = ["돌", "잡초", "돌쇠", "말", "미국인", "멕시코인", "잡상인"]

    past_life = random.choice(lifes)

    # 받은 데이터(ball)는 name으로 사용할 것이다.
    context = {
        "name": ball,
        "past_life": past_life,
    }

    return render(request, "random_past2.html", context)


def lorem(request):

    return render(request, "lorem.html")


def lorem2(request):
    number1 = int(request.GET.get("number1"))  # 문단 수
    number2 = int(request.GET.get("number2"))  # 단어 수

    lorems_kor = ["바나나", "바나나킥", "초코송이", "콘초", "초코파이", "킨더초콜렛"]

    texts = []
    for i in range(number1):  # 문단
        texts_list = []
        for _ in range(number2):  # 단어
            lorem_kor = random.choice(lorems_kor)  # 랜덤으로 출력
            texts_list.append(lorem_kor)  # 랜덤 단어를 리스트에 담아준다.
        texts.append(texts_list)  # 랜덤 단어를 담은 리스트를 큰 리스트에 담아준다.

    context = {
        "lorem_kor": lorem_kor,
        "number1": number1,
        "number2": number2,
        "texts": texts,
    }
    return render(request, "lorem2.html", context)
