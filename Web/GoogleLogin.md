# Google Login

구글로그인은 여러업체에서 OAuth 소셜로그인을 하고 있고, 구글 자체 여러 서비스에서 사용되고 있다.
유트브에 구글 로그인버튼을 클릭시 다음과 같은 파라미터가 사용된다.

```
https://accounts.google.com/v3/signin/identifier?
continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dko%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&
ec=65620&
hl=ko&
ifkv=AXH0vVsC4b_ORLSP7o4MYwne_kz62npQ1pBbxxVKjXwP37EREc32RKZEP4kml8zRONLDT4KjWG_&
passive=true&
service=youtube&
uilel=3&
flowName=GlifWebSignIn&
flowEntry=ServiceLogin&
dsh=S18268863%3A1744070279246520
```

## 📦 쿼리 파라미터 분석

| 파라미터 이름          | 설명                                                                                                                       |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| continue               | 로그인 성공 시 이동할 URL. 여기선 YouTube 로그인 성공 후 돌아갈 목적지. 인코딩된 URL 안에 다시 URL이 있는 중첩 URL 인코딩. |
| ec=65620               | 내부 구글 로그인 흐름을 제어하는 코드 (Google 내부 코드로 추정).                                                           |
| hl=ko                  | 언어 설정 (여기선 한국어).                                                                                                 |
| ifkv=AXH0...           | 보안 토큰 또는 세션 무결성 확인용 파라미터 (anti-CSRF 혹은 request 식별자 역할).                                           |
| passive=true           | 로그인 화면에서 사용자의 직접 입력 없이 가능한 자동 로그인 시도 여부 (true일 경우 자동 로그인을 허용).                     |
| service=youtube        | 로그인하려는 서비스 이름 (YouTube).                                                                                        |
| uilel=3                | UI 엘리먼트 수준 또는 스타일을 정의 (UI 단계/옵션 관련, 보통 내부 사용 목적).                                              |
| flowName=GlifWebSignIn | 구글 로그인 플로우 이름. 일반적인 웹 기반 로그인 흐름에 사용.                                                              |
| flowEntry=ServiceLogin | 로그인 시작 지점. 다른 값으로는 AddSession, RecoverEmail 등이 있음.                                                        |
| dsh=S1826...           | 세션 해시 값. 로그인 세션을 특정 짓는 파라미터로 추정됨.                                                                   |

## Question

- <details open>
  <summary>파라미터의 길이는 어느정도까지 되는가?</summary>
  크롬은 약 2MB(~32,000자), 파이어폭스 65,000자 이상 이지만
  구형 시스템이나 레거시 서버 지원을 고려할경우 최대 2,000자
  정도로 보수적으로 잡는다. 넘을시 오류(414 URI Too Long)발생함
  </details>

그럼 구글 로그인은 얼마일까? 약 400자 정도로 충분히 통과된다.
요즘 모던 브라우저들은 url parameter 길이가 충분하므로 이것을 마치 데이터를 저장하는 용도로 사용하는 서비스들도 존재한다.

[진정한 남자들은 DB를 쓰지 않습니다 애플코딩](https://www.youtube.com/watch?v=pCOBmmJARPE)

- <details open>
  <summary>url, uri 차이가 뭐지?</summary>
    URI 는 URL 을 포함한 더 큰 포괄적 개념입니다. 인터넷상에서 해당 리소스를 식별할수 있는 문자열을 뜻함.
    URL 은 해당 리소스로 접근할수 있는 프로토콜도 들어가야함.
    URN 은 자원의 이름만 식별되고, 식별, 위치는 모릅니다.
  </details>
- <details open>
  <summary>오리진과 리소스의 차이?</summary>
  리소스는 인터넷상에 html, json 같은 말그대로 자원 그자체이다.
  오리진은 보안정책에서 해당 리소스의 출처를 알아낼때 나오는 용어인데, 프로토콜, 호스트, 포트를 통해 출처를 파악한다.
  이는 CORS 에서 보통 다룬다.
  </details>
- <details open>
  <summary>CORS 는 뭐야?</summary>
  Cross origin resource sharing 으로 서로다른 오리진끼리의 요청들을 제어하는 브라우저의 보안정책입니다. 브라우저에서 현재 오리진 A에서 다른 오리진 B에 온 응답 읽기(read access)에 대해 기본적으로 차단함. 이는 클라이언트를 보호하기 위해서이다.
  </details>
- <details open>
  <summary>preflight 는 언제 발생하는가?</summary>
  POST,GET,HEAD 요청아닌경우
  Content-Type 이 `applicaion/x-www-form-urlencoded`, `multipart/form-data`, `text/plain`
  특수한 해더(`Authorization`, `X-Custom-Header`) 등 포함된 경우
  </details>
