
# RCP (Remote Computer Program)

-----

접속된 컴퓨터의 Background 와 실행중인 Visiable Program 을 확인할 수 있는 프로그램.

<br/>

## Idea

<br/>

    온라인 수업시, 게임중인 아이들을 보며 학교와 교육청에서 허가되는 범위의
    감시 프로그램을 만들면 어떨까 하는 생각으로 프로그램을 개발하기 시작했다.

-----

<br/>

## Introduce

<br/>

![server_home](https://user-images.githubusercontent.com/71556009/131518900-6fbd2c46-faa6-41e2-9b7f-e0fbf9232a0a.PNG)
- 서버 프로그램을 실행시키면, 위의 사진과 같이 window 창이 나타난다.

<br/>
<br/>

![client](https://user-images.githubusercontent.com/71556009/131518965-9c40f6c9-8eee-4b49-86ee-1612b48eb89f.PNG)
- 클라이언트 프로그램을 따라 실행시킨다.

<br/>
<br/>

![server_select](https://user-images.githubusercontent.com/71556009/131518932-b122989a-db73-403a-b7f6-46901eb4a4d4.PNG)
- 클라이언트의 명칭이 위의 check box 에 추가되고, 클릭하면 해당 클라이언트의
background 와 실행중인 visiable program(현재 사용자에게 보이는 백그라운드 프로그램을 제외한 프로그램) 을
띄운다.

<br/>

-----

<br/>
<br/>

## And

<br/>

- 서버와 클라이언트 프로그램 실행파일화는 완료하였다. 배포파일을 .gitignore 에 걸러놓아, 따로 배포할 생각이다.
- 클라이언트의 ui 제작과 서버 프로그램의 유연화(여러 환경과 학급에서 쓰일 수 있게 작업) 를 한 후, 배포할 생각이다.
- 서버 소스코드를 리펙토링 할 예정이다. 소켓 모듈과 visiable program 모듈은 따로 분리해놓았으나, 리펙토링 후,
구조적으로나 효율적으로나 가독성을 높일 예정이다.

<br/>
<br/>

### 이러한 요소들은 차근차근 버전을 올려가며 업데이트 할 예정이다. 조만간 출시 예정!

<br/>

-----
