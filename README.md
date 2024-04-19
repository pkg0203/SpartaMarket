# Sparta - Market
**Django**를 배우고서 익숙해지기 위해 개인과제로서 수행

## 📑 ERD

![ERD3 drawio](https://github.com/pkg0203/SpartaMarket/assets/141356379/bfe73f90-f7f9-4e89-9d14-168b7521ea25)



## 🖥️ 프로젝트 소개
중고 게시판 사이트로 물품의 CRUD와 찜이 가능한 사이트
https://teamsparta.notion.site/3964141ecf7b401d84de9dd72aa04b8b
<br>

## 🕰️ 개발 기간
* 24.04.15. - 24.04.19. / 5일

### 🧑‍🤝‍🧑 맴버구성 
* 박강균


### ⚙️ 개발 환경
- **Backend** : `Python`
- **Frontend** : `HTML, Bootstrap`
- **Framework** : `Django 4.2v`
- **Database** : `SQLite3`
<br>



## 📌 주요 기능
#### 로그인,로그아웃,계정
- Django의 AUTH_USER_MODEL로 AbstractUser를 상속받아 정의
- AUTH_LOGIN / AUTH_LOGOUT을 통해 구현
- 로그인을 해야만 아래의 모든 기능을 사용할 수 있음
- 아이디를 클릭하면 해당 유저의 마이페이지로 이동
- 탈퇴 기능은 **없음**
#### 팔로우 기능
- 자기 자신은 팔로우 불가
- 마이페이지에 팔루워와 팔로잉 수 표시
#### 게시글과 댓글
- 게시글과 댓글 작성, 읽기, 수정, 삭제(CRUD)
- 본인만 수정, 삭제 가능
- 조회수 기능 구현
- 본인이 작성하지 않은 글을 찜 가능
- 게시글을 최신순 / 인기순으로 정렬 가능
- 게시글의 image에 대한 CRUD는 구현하지 않음
  - 단 default_image가 주어짐
#### 마이페이지
- 프로필 이미지 update 가능
- 가입일과 내가 작성한 게시글, 내가 찜한 게시글 확인 가능
- 그 게시글의 제목을 클릭하면 게시글로 이동 가능
