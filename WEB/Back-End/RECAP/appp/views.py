from django.shortcuts import redirect, render

# models.py의 class 불러오기
from .models import Recap

# forms.py의 class 불러오기 (title, content)
from .forms import RecapForm

# Create your views here.

# post == 보내기 get == 조회


def index(request):
    # 저장된 데이터 가져오기
    posts = Recap.objects.order_by("-pk")

    # templates(index.html)에 전달하기
    context = {
        "posts": posts,
    }
    return render(request, "appp/index.html", context)


def new(request):
    return render(request, "appp/new.html")


def create(request):
    # 데이터 보내기 (DB에 저장하기)

    # 유효성 검사
    # 메소드가 POST일 경우 (데이터를 보낸 경우)
    if request.method == "POST":
        appp_form = RecapForm(request.POST)
        # 해당 데이터가 유효하다면
        if appp_form.is_valid():
            # DB에 데이터를 저장한다.
            appp_form.save()
            # index로 바로 보내주기
            return redirect("appp:index")

    # 메소드가 POST가 아닌 경우
    else:
        # 해당 데이터를 불러오기만 한다. (데이터가 페이지에 남아있도록)
        appp_form = RecapForm()

    # context == 값을 넘겨주는 역할
    context = {
        "appp_form": appp_form,
    }
    # new로 보내주기
    return render(request, "appp/new.html", context=context)


def detail(request, pk):
    # 특정 글 가져오기
    post = Recap.objects.get(pk=pk)
    context = {
        "post": post,
    }
    return render(request, "appp/detail.html", context)

# create와 동일한 형식
def update(request, pk):
    post = Recap.objects.get(pk=pk)
    if request.method == "POST":
        # 가져온 데이터(post)를 인스턴스로 넘겨주며 appp_form에 새로운 데이터를 저장한다. 
        appp_form = RecapForm(request.POST, instance=post)
        # 데이터 형식이 유효하다면
        if appp_form.is_valid():
            # 저장한 후
            appp_form.save()
            # 다시 특정 id의 상세 페이지로 넘긴다.
            return redirect("appp:detail", post.pk)

    else:
        appp_form = RecapForm(instance=post)

    context = {
        "appp_form": appp_form,
    }
    return render(request, "appp/update.html", context)
