# CSS Position

* 요소의 위치를 지정한다.

* static
  
  * 기본 위치, 기준 위치
  
  * 일반적인 배치 순서에 따라 좌측 상단에 보통 위치한다.
  
  * 부모 요소 내에 배치될 때는 부모 요소의 위치를 기준으로 배치된다.

### 상대 위치 relative

* 자기 자신의 위치(static)를 기준으로 이동한다.

* **normal flow를 유지한다.**

* 실제 위치는 그대로이며, 표면적으로 볼 때 이동한 것 처럼 보인다.

relative는 자신의 원래 위치를 기준으로 배치하기 때문에 본래의 위치가 어디 있는지에 관련(relative)되어 있다.

![relative.png](C:\Users\yelki\OneDrive\바탕%20화면\TIL\WEB\Front-End\WEB.assets\relative.png)

↳ 1은 postision: relative;로 설정되었다.

normal flow를 유지한다는 것은 실제 위치는 그대로이지만, 육안으로 보았을 때 이동한 것처럼 보인다. 즉, 1이 차지하는 공간은 여전히 좌측 상단 1에 위치하고 있다. 

### 절대 위치 absolute

* **normal flow에서 벗어난다.**
  
  * 본인의 위치에서 벗어난 행위

* 자신의 위치가 아닌 부모 요소를 기준으로 이동한다.

* 특정 영역 위에 존재할 때 사용한다. (부모는 relative, 자식(본인)은 absolute)

가장 가까운 위치에 있는 조상 요소를 기준으로 한다. (조상이 있는 한 자신의 위치가 절대적으로 정해져 있다.)

![absolute.png](C:\Users\yelki\OneDrive\바탕%20화면\TIL\WEB\Front-End\WEB.assets\absolute.png)

↳ 1은 postision: absolute;로 설정되었다. 

normal flow에서 벗어난다는 것은 자신의 공간을 그대로 차지하고 있는 relative와 다르게 공간도 이동하게 된다. (공간을 차지하지 않는다.)

1의 공간이 빠지게 되면서 다음 블록 요소인 2가 좌측 상단으로 이동하게 되는 것이다.

### 고정 위치 fixed

- **normal flow에서 벗어난다.**
- 부모 요소와 관계없이 viewport를 기준으로 이동한다.
  - 스크롤 시에도 항상 같은 곳에 위치한다.
- viewport에서 고정된 위치에 존재한다.

![fixed.png](C:\Users\yelki\OneDrive\바탕%20화면\TIL\WEB\Front-End\WEB.assets\fixed.png)

CSS의 기본 원칙인 좌측상단에 위치하지 않는다.

우측하단으로 고정하였으니ㄲㅏ,,!

### sticky

* stactic 상태에서 스크롤 시 fixed로 바뀐다.

* 쇼핑몰 등과 같은 페이지에서 상단의 Navigation bar가 sticky이다.





# CSS Layout

## Float

* 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인요소들이 주변을 wrapping 하도록 한다.

* 요소가 Normal flow를 벗어나도록 한다.

  ![float.png](C:\Users\yelki\OneDrive\바탕%20화면\TIL\WEB\Front-End\WEB.assets\float.png)

(image from positiveko.github.io)

```css
.left {
   float: left;
}
```

# Flexbox

#### 

#### 기본 문장

```css
.flex-container {
   display: flex;
}
```

![flex.png](C:\Users\yelki\OneDrive\바탕%20화면\TIL\WEB\Front-End\WEB.assets\flex.png)

* 행과 열 형태로 아이템들을 배치한다.

* Flex Container: 부모 요소

* Flex Item: 자식 요소

* main axis: 메인 축

* cross axis: 교차 축

* flex를 통해 수동 값을 부여하지 않고 수직 정렬과 아이템의 너비, 높이, 간격을 동일하게 배치할 수 있다.

## flex-direction

* main axis의 방향을 설정한다.

![flexrow.png](C:\Users\yelki\OneDrive\바탕%20화면\TIL\WEB\Front-End\WEB.assets\flexrow.png)

* 행 기준으로 나열한다.

![flexrowreverse.png](C:\Users\yelki\OneDrive\바탕%20화면\TIL\WEB\Front-End\WEB.assets\flexrowreverse.png)

![flexcolumn.png](C:\Users\yelki\OneDrive\바탕%20화면\TIL\WEB\Front-End\WEB.assets\flexcolumn.png)

![flexcolumnreverse.png](C:\Users\yelki\OneDrive\바탕%20화면\TIL\WEB\Front-End\WEB.assets\flexcolumnreverse.png)

## flex-wrap

* 아이템이 컨테이너를 벗어나지 않게 해당 영역 내에 배치될 수 있도록 설정한다.

* 한 줄에 배치 되게 할 것인지의 여부를 설정한다.

![flexwrap.png](C:\Users\yelki\OneDrive\바탕%20화면\TIL\WEB\Front-End\WEB.assets\flexwrap.png)

* 아이템이 해당 영역을 넘으면 그 다음 줄로 배치한다.

```css
 .items {
     flex-flow: row wrap;
 }
```

![flexnowrap.png](C:\Users\yelki\OneDrive\바탕%20화면\TIL\WEB\Front-End\WEB.assets\flexnowrap.png)

* 무조건 한 줄에 배치하도록 한다.

### justify-content

* main axis를 기준으로 공간을 배분한다.

![justify.jpg](C:\Users\yelki\OneDrive\바탕%20화면\TIL\WEB\Front-End\WEB.assets\justify.jpg)

(image from 1분코딩)

```css
가로 세로 모두 가운데로 설정

.container{
    justify-content: center;
    align-items: center;
}
```


