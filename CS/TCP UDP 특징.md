# TCP/UDP 특징



TCP/UDP는 OSI 7 계층 중 Layer 4: 전송계층에 포함된다.

전송계층은 프로토콜 내에서 송신자와 수신자를 연결하는 통신 서비스를 제공하는 계층이다.


IP에 의해 전달되는 **패킷의 오류를 검사하고 재전송 요구** 등의 **제어**를 담당한다.

이러한 전송계층에서 사용되는 프로토콜이 바로 TCP와 UDP이다.



![img](https://blog.kakaocdn.net/dn/cYOrod/btrWisGrhbr/BTMozSppcjSi529k38XQkk/img.jpg)

 

## TCP(Transmission Control Protocol)

- **신뢰성** 있는 **데이터 전송을 지원**하는 **연결 지향형** 프로토콜
-  TCP와 IP가 함께 사용된다.
  - IP가 데이터의 전송을 처리한다면 TCP는 패킷 추적 및 관리를 한다.
- 연결 지향형인 TCP는 **3-way handshaking** 과정을 통해 연결 후 통신을 시작한다.
  - **흐름제어와 혼잡제어**를 지원하며 **데이터의 순서를 보장**한다.



### 3 way handshake - 연결 성립

> 연결을 성립하고 해제하는 과정

TCP는 정확한 전송을 보장해야 한다.

따라서 통신하기에 앞서, 논리적인 접속을 성립하기 위해 3 way handshake 과정을 진행한다.

![img](https://blog.kakaocdn.net/dn/bwcCtj/btrWdoSQXU9/QQ5IisOMceKyIljJW6lzV0/img.png)



1. 클라이언트가 서버에게 **SYN 패킷**을 보냄 (sequence : x)
2. 서버가 SYN(x)을 받고, 클라이언트로 **받았다는 신호인 ACK와 SYN 패킷을 보냄** (sequence : y, ACK : x + 1)
3. 클라이언트는 서버의 응답은 ACK(x+1)와 SYN(y) 패킷을 받고, ACK(y+1)를 서버로 보냄

이렇게 3번의 통신이 완료되면 연결이 성립된다.



### 4 way handshake - 연결 해제

연결 성립 후, 모든 통신이 끝났다면 해제해야 한다.

![img](https://blog.kakaocdn.net/dn/beBXWS/btrWop3gOuO/PvAjLufKXd4zKTKv9Ej2hK/img.png)



1. 클라이언트는 서버에게 연결을 종료한다는 **FIN 플래그**를 보낸다.
2. 서버는 FIN을 받고, 확인했다는 **ACK**를 클라이언트에게 보낸다. (이때 모든 데이터를 보내기 위해 **CLOSE_WAIT 상태**가 된다)
3. 데이터를 모두 보냈다면, 연결이 종료되었다는 **FIN 플래그를 클라이언트에게 보낸다.**
4. 클라이언트는 **FIN을 받고, 확인했다는 ACK를 서버에게 보낸다.** (아직 서버로부터 받지 못한 데이터가 있을 수 있으므로 **TIME_WAIT**을 통해 기다린다.)

> 서버는 ACK를 받은 이후 소켓을 닫는다 (Closed)
> TIME_WAIT 시간이 끝나면 클라이언트도 닫는다 (Closed)



이렇게 4번의 통신이 완료되면 연결이 해제된다.







### 흐름제어/혼잡제어

신뢰성있는 네트워크(reliable network)를 보장하는데에 4가지 문제점이 존재한다.

- **손실**
  - 패킷이 손실될 수 있는 문제
- **순서 바뀜**
  - 패킷의 순서가 바뀌는 문제
- **Congestion**
  - 네트워크가 혼잡한 문제
- **Overload**
  - receiver가 overload 되는 문제



### 흐름제어 Flow Control 

- endsystem 대 endsystem
  - 송신측과 수신측의 데이터 처리 속도 차이를 해결하기 위한 기법
  - Flow Control은 receiver가 패킷을 지나치게 많이 받지 않도록 조절하는 것
  - **receiver가 sender에게 현재 자신의 상태를 feedback 한다는 점**
- 수신측이 송신측보다 데이터 처리 속도가 빠르면 문제없지만, **송신측의 속도가 빠를 경우 문제**가 생긴다.
- 수신측에서 제한된 **저장 용량을 초과**한 이후에 도착하는 **데이터는 손실** 될 수 있으며, 만약 손실 된다면 불필요하게 응답과 데이터 전송이 송/수신 측 간에 빈번히 발생한다.
- 이러한 위험을 줄이기 위해 송신 측의 데이터 전송량을 수신측에 따라 조절해야한다.

####  

#### **해결방법**

- Stop and Wait
  - 매번 전송한 패킷에 대해 확인 응답을 받아야만 그 다음 패킷을 전송하는 방법
- Sliding Window (Go Back N ARQ)
  - 전송은 되었지만, acked를 받지 못한 byte의 숫자를 파악하기 위해 사용하는 protocol
  - 수신측에서 **설정한 윈도우 크기**만큼 **송신측에서 확인응답 없이 세그먼트를 전송**할 수 있게 하여 **데이터 흐름을 동적으로 조절**하는 제어기법
  - LastByteSent - LastByteAcked <= ReceivecWindowAdvertised
    - 마지막에 보내진 바이트 - 마지막에 확인된 바이트 <= 남아있는 공간
  - 현재 공중에 떠있는 패킷 수 <= sliding window
- 동작방식
  - 먼저 윈도우에 포함되는 **모든 패킷을 전송**하고, 그 패킷들의 전달이 **확인되는대로 이 윈도우를 옆으로 옮김으로써 그 다음 패킷들을 전송**

- Window 
  - TCP/IP를 사용하는 모든 호스트들은 **송신하기 위한 것과 수신하기 위한 2개의 Window**를 가지고 있다. 호스트들은 실제 데이터를 보내기 전에 **'3 way handshaking'을 통해 수신 호스트의 receive window size에 자신의 send window size를 맞추게 된다.**

![img](https://blog.kakaocdn.net/dn/sUfP8/btrWopa73cs/BRmNAouQIGApQkZFCFosK0/img.png)



### 세부구조

**송신 버퍼(send buffer)**

![img](https://blog.kakaocdn.net/dn/WG4fM/btrWdnzG4py/jqk4K0ZKJKIDAUjan0cDo0/img.png)

- 200 이전의 바이트는 이미 전송되었고, **확인응답을 받은 상태**이다.
- 200 ~ 202 바이트는 전송되었으나 **확인응답을 받지 못한 상태**이다.
- 203 ~ 211 바이트는 **아직 전송이 되지 않은 상태**이다.

###  

**수신 윈도우**

![img](https://blog.kakaocdn.net/dn/cinD6P/btrWfQgLMpQ/jzNMREhzvnJhOmrZiUHO4k/img.png)

###  

**송신 윈도우**

![img](https://blog.kakaocdn.net/dn/6Qy3c/btrWopIYMJh/QvLxCc4YWOAG1WlLzjqAYK/img.png)

- 수신 윈도우보다 작거나 같은 크기로 송신 윈도우를 지정하게되면 흐름제어가 가능하다.

![img](https://blog.kakaocdn.net/dn/bssjsI/btrWjme1HTg/Mnp9pdGtgRIeCMbTk3hw11/img.png)송신 윈도우 이동

- Before: 203 ~ 204를 전송하면 수신측에서는 확인 **응답 203을 보내고**, 송신측은 이를 받아 after 상태와 같이 수신 윈도우를 **203 ~ 209 범위로 이동**한다.
- after : **205 ~ 209가 전송 가능한 상태**이다. 

###  

###  

###  

### 혼잡제어 Congestion Control

- **송신측의 데이터 전달과 네트워크의 데이터 처리 속도 차이를 해결하기 위한 기법**
- 송신측의 데이터는 **지역망이나 인터넷으로 연결된 대형 네트워크**를 통해 전달된다.
  - 만약 한 라우터에 데이터가 몰릴 경우, 자신에게 온 데이터를 모두 처리할 수 없게 된다. 이런 경우 호스트들은 또 다시 재전송을 하게되고 결국 혼잡만 가중시켜 오버플로우나 데이터 손실을 발생시키게 된다.
  - 따라서 이러한 네트워크의 혼잡을 피하기 위해 송신측에서 보내는 **데이터의 전송속도를 강제로 줄이게 되는데**, 이러한 작업을 **혼잡제어**라고 한다.
- 네트워크 내에 **패킷의 수가 과도하게 증가하는 현상**을 혼잡이라 하며, 혼잡 현상을 방지하거나 제거하는 기능을 혼잡제어라고 한다.
- 혼잡제어는 **호스트와 라우터를 포함한**넓은 관점에서 전송 문제를 다루게 된다.
  - 흐름제어가 송신측과 수신측 사이의 전송속도를 다룬다.



#### **해결방법**

- **AIMD(Additive Increase / Multiplicative Decrease)**
  - 처음에 패킷을 하나씩 보내고 이것이 문제없이 도착하면 **window 크기**(단위 시간 내에 보내는 패킷의 수)를 **1씩 증가**시켜가며 전송하는 방법
  - 패킷 전송에 실패하거나 일정 시간을 넘으면 패킷의 보내는 속도를 절반으로 줄인다.
  - 여러 호스트가 한 네트워크를 공유하고 있으면 나중에 진입하는 쪽이 처음에는 불리하지만, 시간이 흐르면 **평형상태**로 수렴하게 되는 특징이 있다. (공평한 방식)
  - 문제점은 초기에 네트워크의 높은 대역폭을 사용하지 못하여 오랜 시간이 걸리게 되고, 네트워크가 혼잡해지는 상황을 미리 감지하지 못한다.
    - **즉, 네트워크가 혼잡해지고 나서야 대역폭을 줄이는 방식이다.**
- **Slow Start (느린 시작)**
  - AIMD 방식이 네트워크의 수용량 주변에서는 효율적으로 작동하지만, **처음에 전송 속도를 올리는데 시간이 오래** 걸리는 단점이 존재했다.
  - Slow Start 방식은 AIMD와 마찬가지로 패킷을 하나씩 보내면서 시작하고, 패킷이 문제없이 도착하면 각각의 **ACK 패킷마다 window size를 1씩 늘려준다. 즉, 한 주기가 지나면 window size가 2배로 된다.**
  - 전송속도는 AIMD에 반해 **지수 함수** 꼴로 증가한다.
    - 대신에 혼잡 현상이 발생하면 window size를 1로 떨어뜨리게 된다.
    - 처음에는 네트워크의 수용량을 **예상할 수 있는 정보가 없지만**, 한번 혼잡 현상이 발생하고 나면 네트워크의 수용량을 어느 정도 예상할 수 있다.
      - 그러므로 혼잡 현상이 발생하였던 w**indow size의 절반까지는 이전처럼 지수 함수 꼴로 창 크기를 증가**시키고 그 이후부터는 **완만하게 1씩 증가**시킨다.
- **Fast Retransmit (빠른 재전송)**
  - 빠른 재전송은 **TCP의 혼잡 조절에 추가된 정책**이다.
  - 패킷을 받는 쪽에서 먼저 도착해야할 패킷이 도착하지 않고 **다음 패킷이 도착한 경우에도 ACK 패킷을 보내게 된다.**
    - 단, 순서대로 잘 도착한 마지막 패킷의 다음 패킷의 순번을 ACK 패킷에 실어서 보내게 되므로, **중간에 하나가 손실되게 되면 송신 측에서는 순번이 중복된 ACK 패킷을 받게 된다.** 이것을 감지하는 순간 문제가 되는 순번의 패킷을 **재전송** 해줄 수 있다.
  - 중복된 순번의 패킷을 **3개** 받으면 재전송을 하게 된다. 약간 혼잡한 상황이 일어난 것이므로 **혼잡을 감지**하고 **window size를 줄이게 된다.**
- **Fast Recovery (빠른 회복)**
  - 혼잡한 상태가 되면 window size를 1로 줄이지 않고 **반으로 줄이고 선형증가**시키는 방법이다.
    - 이 정책까지 적용하면 혼잡 상황을 한번 겪고 나서부터는 **순수한 AIMD 방식**으로 동작하게 된다.



#### 전송의 전체 과정

1. Application layer
   - sender application layer가 socket에 data를 쓴다.
2. Transport layer
   - data를 segment에 감싼다. 그리고 network layer에 넘겨준다.
3. 아랫단에서 receiving node로 전송된다.
   - 이 때, sender의 **send buffer**에 데이터를 저장하고, receiver는 **receive buffer**에 데이터를 저장한다.
4. application에서 준비가 되면 buffer에 있는 데이터를 읽기 시작한다.
   - flow control의 핵심은 이 receiver buffer가 넘치지 않게 하는 것.
5. receiver는 RWND(Receive WiNDow) : receive buffer의 남은 공간을 홍보한다.







## UDP(User Datagram Protocol)

- 데이터를 데이터그램 단위로 처리하는 프로토콜
  - 데이터그램 단위로 쪼개면서 전송을 해야하기 때문에 전송 계층이다.
  - Transport layer에서 사용하는 프로토콜
- **비연결형, 신뢰성** **없는** 전송 프로토콜

![img](https://blog.kakaocdn.net/dn/UmCdb/btrWee97Aal/clNz7zBlHxkCVuYPXlKuzK/img.png)UDP 헤더

> Source port : 시작 포트
> Destination port : 도착지 포트
> Length : 길이
> Checksum : 오류 검출
> ▶중복 검사의 한 형태로, 오류 정정을 통해 공간이나 시간 속에서 송신된 자료의 무결성을 보호하는 단순한 방법이다.

▶이렇게 간단하므로 TCP 보다 용량이 가볍고 송신 속도가 빠르게 작동된다.

그러나 확인 응답을 못하므로, TCP보다 신뢰도가 떨어지게 된다.

그러므로, **UDP는 비연결성, TCP는 연결성**으로 정의된다.

##  

## TCP와 UDP는 왜 나오게 됐을까?

→ IP의 한계를 해결하기 위해서

- IP는 Host to Host (장치 to 장치)만을 지원한다. 
- 장치에서 장치로 이동은 IP로 해결되지만, **하나의 장비안에서 수많은 프로그램들이 통신**을 할 경우에는 IP만으로는 한계가 있다.
  - 이를 해결하기 위하여 **포트 번호**가 나왔다.
- IP에서 오류가 발생한다면 ICMP에서 알려주지만, 알려주기만 할 뿐 대처를 못하기 때문에 IP보다 위에서 처리를 해줘야 한다.
  - 이를 해결하기 위하여 **상위 프로토콜인 TCP와 UDP가 나오게 되었다.**
  - *ICMP : 인터넷 제어 메시지 프로토콜로 네트워크 컴퓨터 위에서 돌아가는 운영체제에서 오류 메시지를 전송받는데 주로 쓰임





## TCP/UDP 오류 해결 방법

#### **TCP**

**데이터의 분실, 중복, 순서** 등을 자동으로 보정해줘서 송수신 데이터의 정확한 전달을 할 수 있도록 해준다.

#### **UDP**

**IP가 제공하는 정도의 수준만을 제공하는 간단한 IP 상위 계층의 프로토콜이다.**

그러므로 TCP와는 다르게 에러가 날 수도 있고, 재전송이나 순서가 뒤바뀔 수도 있어서 이 경우, 어플리케이션에서 처리하는 번거로움이 존재한다.



### 그렇다면 왜 UDP를 사용할까?

#### **신속성 때문!**

- 데이터의 처리가 TCP보다 빠르다.
  - 그래서 주로 실시간 방송과 온라인 게임에서 사용된다. 
  - 네트워크 환경이 안 좋을때, 끊기는 현상을 생각하면 된다.



### DNS(Domain Name Service)에서 UDP를 사용하는 이유

> DNS는 데이터를 교환하는 경우이다. 
> 이때, TCP를 사용하게 되면, 데이터를 송신할 때까지 **세션 확립을 위한 처리**를 하고, 송신한 데이터가 수신되었는지 **점검**하는 과정이 필요하므로 **Protocol overhead가 UDP에 비해서 크다.**

DNS는 Application layer protocol이다.

모든 Application layer protocol은 **TCP, UDP 중 하나의 Transport layer protocol을 사용**해야 한다.

TCP는 신뢰성이 있고, UDP는 신뢰성이 없음에도 불구하고 UDP를 사용하는 이유는,



- Request의 양이 작다.
  - UDP Request에 담길 수 있다.
  - DNS request는 UDP segment에 꼭 들어갈 정도로 작다.
    - DNS query는 **single UDP request**와 server로부터의 **single UDP reply**로 구성되어 있다.

- **3 way handshaking으로 연결을 유지할 필요가 없다. (오버헤드 발생)**
- Request에 대한 손실은 Application Layer에서 제어가 가능하다.
- UDP는 신뢰성이 떨어지나(not reliable), reliability는 application layer에 추가될 수 있다. 
  - Timeout 추가, resend 작업 등을 통해
- DNS는 UDP를 53번 port에서 사용함.
- **하지만 크기가 512(UDP 제한)이 넘을 때는 TCP를 사용해야한다.**
  - 만약에 데이터가 512 bytes를 넘거나, 응답을 못받은 경우 TCP로 한다.
  - **Zone transfer 을 사용해야하는 경우**
    - *Zone Transfer : DNS 서버 간의 요청을 주고 받을 떄 사용하는 transfer



## **요약**

| **TCP**                                      | **UDP**                                                   |
| -------------------------------------------- | --------------------------------------------------------- |
| 연결형 프로토콜                              | 비연결형 프로토콜                                         |
| 데이터의 경계 구분 X                         | 데이터의 경계 구분 O                                      |
| 신뢰성 있는 데이터 전송 (데이터 재전송 존재) | 비신뢰성 있는 데이터 전송 (데이터 재전송 존재 X)          |
| 일 대 일 통신 (Unicast)                      | 일 대 일, 일 대 다 (Broadcast), 다 대 다 (Multicast) 통신 |