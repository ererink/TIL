# Branch와 Github Flow

### Git flow란

Git을 통해 협업하며 branch를 활용하는 전략을 뜻한다. 



여러 협업자들과 협업을 하는 과정에서 여러 브랜치들을 합치는 과정이 생긴다. 

팀별로 브랜치가 나눠질 수도 있고, 팀 내에서 기능 별로 브랜치가 나뉠 수 있다. 

이러한 맥락에서 Master 브랜치는 사용자가 보는 화면에 대한 코드가 된다. 



## Brach basic 명령어

### 

## Branch 개념 

### Branch는 왜 필요할까? 

독립적인 버전들을 만들어 나가기 위해서 필요하다. 



하나의 나무로 예를 들어보자. 

master는 기둥 혹은 뿌리, branch1(또 다른 브랜치로 만든 것)은 뻗어 나간 가지가 된다. 

나뭇가지를 만들기 위해 **뿌리**가 필요하다. 그래서 첫 번째로 커밋된 것은 root commit이 된다. 

뻗어 나간 branch1 이란 나뭇가지는 master의 정보까지 가지고 있다 . (2가지의 정보) 

하지만, master는 branch1의 정보를 가지고 있지 않다. 



## 가지 합치기 (a.k.a Merge)

뻗어 나간 나뭇가지인 branch1을 master에 합쳐주기 위해서 

`git merge branch1` 을 입력한다. 여기서 주의할 점은 브랜치의 위치는 master에서 합쳐줘야 한다. 

(master는 뿌리이며, branch1인 가지를 가져와서 기둥에 붙여야 하니까)

이렇게 합쳐지지만 branch1 브랜치가 사라지는 것은 아니다. (따로 삭제를 해줘야 한다.)

#### 만약 브랜치를 지운다면?

커밋도, 파일도 지워지지 않는다. 

이미 master에 합쳐놨기 때문에 상관없다!

(보통 master와 합치면 브랜치를 지운다.)



## 복습

지금까지의 내용을 다시 되짚어보자. 

**브랜치는 특정한 버전들의 흐름이다.** 

즉, 작업 내역들이다. 



현실 조별과제를 예로 들어보자. 우리의 협업은 조모임이다. 

팀원은 모두 2명이다. (팀장과 팀원) <u>보고서 제출과 발표자료 제출</u>을 해야 하는 상황이다. 

업무를 배분하는 방법은 무엇일까? 

1. 조장이 다하기
2. 할 일로 나누기 (보고서 / 발표자료)
3. 파트 별로 나누기 (보고서 파트 1, 보고서 파트 2 / 발표 자료1, 발표자료 2)



자료조사가 되어있다고 가정하자.

1번째 방식은 조장이 다하고 합치는 것이다.

2번째는 각자 보고서와 발표자료 를 준비하는 것이다.  (서로 다른 파일을 수정한다)

3번째는 보고서를 같이 하는 것이다. (서로 같은 파일이 수정한다.)

보고서와 발표자료는 파일이 다르다. (docx, ppt) 

**2번째 3번째의 차이점은 서로 다른 파일 / 같은 파일을 사용한다는 것이다.** 



#### 상황 3) 같은 파일로 조별과제 준비하기

팀장과 팀원 모두 같은 ppt 파일로 작업을 한다. 

그러므로 팀장은 팀원에게 받은 ppt 파일을 합치는 작업을 한다. 

즉, 편집을 해서 취합본을 만들어야 한다. 

이렇게 각자 작업을 하면 팀장이 수작업으로 고쳐야 한다 (취합을 위한 편집을 한다)

(상황 2는 서로 다른 파일로 작업을 한다면 제출 사항이 보고서(docx), 발표자료(ppt) 이기 때문에 그냥 이 두개를 제출하면 된다 (취합 작업 필요 없음))



### 이러한 상황을 Git branch로 대입해보자. 



#### 상황 1. 혼자 작업 중, 조원은 프리라이딩 중이다. 홈 화면을 만든다. 

`git init`

root commit을 만든다. 첫 번째 커밋을 발생 시킨 것이다. 

`git branch feature/home` 

새로운 브랜치를 만든다. 

`git checkout feature/home`

feature/home 브랜치로 이동한다. 

`add . & commit` 

작업한 파일들을 커밋한다. 

`git checkout master` 

master 브랜치로 이동한다. 

`git log`

log를 해보면 하나의 커밋만 나타난다. 

(feature/home 브랜치에는 home 내용을 포함한 두 가지의 파일이 있다.)

`git merge feature/home` 

**feature/home 브랜치를 master 브랜치에 병합한다.**

병합의 의미는 master이자 feature/home이 되는 것이다. 

`git branch -d feature/home` 

이미 master와 합쳤으므로 브랜치를 삭제한다. 



#### 상황 2. 협업을 한다.

#### 각각 다른 보고서 + 발표자료 파일 작업 한다.

#### (각자 커밋이 발생했는데 다른 파일만 수정된 경우)



`git checkout -b feature/about` 

 브랜치를 생성하면서 이동한다. 

자기소개 페이지가 담긴 파일을 생성한 뒤 커밋한다. 

`git checkout master` 

master 브랜치로 이동한다. 

`add . & commit` 

파일 생성 및 수정 후 상황 1과 마찬가지로 master 브랜치를 커밋한다. 

`git merge feature/about` 

병합 중 **새로운 커밋**이 발생되면서 merge 브랜치가 발생한다. 

새로운 가지가 생겨났고 이는 master가 된다. 

merge commit이 생겨난 것이다. 

(이미 병합된 브랜치는 삭제한다. 그러므로 feature/about 가지에서 병합을 하면 안!된!다!) 

(병합된 브랜치는 지우는 것이 좋다)



#### 상황 3. (진정한 협업) 각자 커밋이 있는데 같은 파일이 수정된다

이미 커밋이 진행된 적이 있다고 가정하자.

`git checkout -b feature/about` 

브랜치를 생성하면서 이동한다. 

`git commit -m `

두 커밋 다 README.md를 수정하고 커밋한다. 

`git checkout master` 

master 브랜치로 이동한다. 

`git merge brance 'feature/about'` 

master에 병합한다. 



#### 리드미를 같이 수정했고 병합한다면?

####  이 2개는 충돌이 발생한다. (커밋 또한 불가능하다)

`git status` 를 실행하여 상황을 살펴본다.

'both modified...' 경고문이 든다. 

#### 왜 이런 상황이 발생했을까?

각자 다른 브랜치에서 작업을 했기에 README.md를 각자 수정할 수 있었는데 

브랜치를 합쳐버려서 충돌이 발생한 것이다. 



#### 브랜치 병합 과정에서 충돌난다면?

**조별과제를 하다가 조원이 PPT가 다르다고 들고 왔다. 교수님은 뭐라하실 건가요?** 와 같은 말이다.

대답은, **여러분이 개발하는 방향에 맞게 고치세요, 뭐하고 싶으세요?**

현실 교수님 대답 또한, **피피티 만들어와야지 뭐해? 나보고 하라는거야?** 와 같다. 

**즉, 고치고 개발 방향에 맞춰 다음에 해야할 일을 작성한다.** 



결과는 2번째와 3번째는 같다. 다만 중간에 파일 충돌을 고쳐 커밋을 했다는 점이 다른 점이다. 

Merge commit 또한 똑같이 있다. 

즉, 달라진 점은 직접 충돌을 해결하였고, add 및 commit을 한 것이다. 



# Github 활용

### Github에서 어떻게 협업을 할까?

Fast - Forward: 기존 master 브랜치에서 변경사항 없이 단순히 앞으로 이동한다. 



## pull request를 통해 협업을 진행한다. 

(Github Flow 기본 원칙 중)

1. feature branch workflow (소유권이 있는 경우)
2. forking workflow (소유권이 없는 경우)

1번과 2번의 차이점은 소유권 유무로 나눠진다. (내꺼, 너꺼)



### 상황) Master 조장이 작업을 한다

급히 고칠게 있어서 hotfix 브랜치를 만들게 된다. 

파일을 수정하고 `add & commit` 을 한다. 

그리고 `git push origin hotfix`  를 한다. 

그러자 경고문으로 Github에서 pull request를 만들어 라는 알림이 뜬다. 

그렇다면 Github에 가보자. 



Github에서 'hotfix가 최근에 push됐어' 라고 알림이 뜬다. pull request 버튼도 같이 뜬다. 

new pull request 버튼을 누른다. 

 → 이는 hotfix 브랜치를 master 브랜치로 합치는 것을 요청하는 것이다. 

​		'마스터야 가져가죠!' 라고 외치는 것이다. 

​		hotfix를 브랜치를 마스터에게 보낸다. 

​		그리고 merge를 누르게 되면 2개의 브랜치는 합병이 된다. 



## Fork & Pull request

조별과제로 예를 들면 for와 pull request는 조원이 하는 것이다. 

조장의 작업물을 가져올 수 없어서 포크로 찍어서 가져온다. (권한이 없어서)

내 저장소에 'fork가 되었다' 라고 뜨게 된다. 

이제 나의 로컬에 받아서 작업을 할 수 있다. 이를 위해 클론을 한다. `git clone ...` 

작업을 하고 `add & commit` 을 한다. 

그리고 `git push origin main` 을 한다. (master가 아닌 main이다.)



#### **여기서 origin은 누구일까?**

나의 것이다. (포크로 가져온 사람의 것이 아님)

올린 뒤 `pull request` 를 한다. 



-----------

# 실습 (a.k.a 실수 기록)

pull request를 실습하였는데 대실수를 했다. 



### 1. 가져올 작업물을 Fork를 한다. 

그리고 나의 원격저장소에 저장할 수 있도록 `creat fork` 를 해준다. 



### 2. 나의 로컬로 clone을 생성한다.

```python
$ git clone https://github.com/username/repositoryname.git
```

Fork해서 받아온 작업물을 나의 로컬로 옮겨준다. 



```python
$ git branch branch1
$ git checkout example
```

브랜치를 생성하고 이동한다. 



```python
$ git add .
$ git commit -m '실수를 반복하지 말자'
$ git push origin branch1
```

작업을 수정 및 생성한 후 add 및 commit, push를 해준다. 



### !실수 조심!

Github에서 pull request를 생성한다. 

![pull req 확인](Branch와 Github Flow   .assets/pull req 확인.jpeg)

생성 하였지만.....

![pull requ](Branch와 Github Flow   .assets/pull requ-7194043.jpeg)

head와 base의 방향을 반대로 해주었다. 

즉 내가 pull request를 받는 주체가 되도록 설정하였기에 pull request가 제대로 설정되지 않았다. 

이후 다른 수강생들의 pull request를 GitHub 이메일로 받을 수 있었다 ^^

이 부분에서 실수를 하였고 패닉이 되었기 때문에 다음 pull request를 할 때에는 꼭 base와 head 방향을 조심할 것 같다!^^

갚진 경험을 했다,,!

