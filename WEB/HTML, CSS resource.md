# HTML & CSS resource from MDN

# HTML

## **Forms**

| **Element** | **Description** |
| --- | --- |
| <button> | 클릭 가능한 버튼 형성 |
| <datalist> | 선택 가능한 옵션 요소을 나타냄 |
| < fieldset> | 속성을 포함한 그룹 형식의 요소를 나타냄 |
| < select> | 옵션들을 선택 가능하도록 함<br><option>과 함께 쓰임. |
| < textarea> | 여러 줄로 텍스트를 쓸 수 있도록 한 공간을 나타냄. <br> <label>과 함께 쓰임. |
| < label> | 기입란 혹은 선택문에서 설명하는 문장으로 자주 쓰인다. <br> <input>과 함께 쓰인다. |
| <iframe><br> | 요소들을 중첩해서 쓸 수 있도록 한다. |

# CSS

## **Animations**

도형이나 페이지 전환에 쓰인다.

```
p {
  animation-duration: 3s;
  animation-name: slidein;
}
```

slidein, bounce 등이 있다.

전환 시 움직이는 타이밍을 설정할 수 있다.

```
animation-timing-function: ease;
animation-timing-function: ease-in;
animation-timing-function: ease-out;
animation-timing-function: ease-in-out;
animation-timing-function: linear;
animation-timing-function: step-start;
animation-timing-function: step-end;
```

전환 시 재생 및 정지를 설정할 수 있다.

```
animation-play-state: running;
animation-play-state: paused;
```

# Text and Font

## **font family**

서로 다른 폰트를 쓸 때 font family로 묶어서 사용한다.

```
p {
  font-family: "Trebuchet MS", Verdana, sans-serif;
}
```

### **폰트 종류**

모든 웹 사이트 및 모든 시스템에서 공용으로 사용하는 폰트

- Arial
- Courier New
- Georgia
- Times New Roman
- Trebuchet MS
- Verdana

CSS에서 정한 기본적인 폰트

- serif
- sans-serif
- monospace
- cursive
- fantasy

## **Font Style**

이탤릭체를 사용하고자 할 때 주로 사용한다.

#### **weight**

텍스트의 굵기를 지정할 때 사용한다.

```
h1 + p {
  font-weight: bold;
}
```

#### **transform**

- uppercase
- lowercase
- capitalize
- full-width

```
h1 {
  font-size: 5rem;
  text-transform: capitalize;
}
```

#### **decoration**

주로 링크 주소 텍스트에 밑줄을 넣어줄 때 사용한다.

- underline
- overline: 윗줄
- line-through: 취소선

#### **shadows**

텍스트에 그림자 효과를 준다.

```
text-shadow: 4px 4px 5px red;
```

#### **align**

텍스트를 왼쪽/ 오른쪽/ 가운데 정렬한다.

- left
- right
- center
- justify: 단어 사이에 공간을 넣어 각 단어들을 따로 떨어뜨린다.

```
h1 {
  text-align: center;
}
```

#### **line hieght**

문장 간격을 설정한다.

```
p {
  line-height: 1.6;
}
```

#### **letter and word spacing**

글자 간격을 설정한다.

```
p::first-line {
  letter-spacing: 4px;
  word-spacing: 4px;
}
```