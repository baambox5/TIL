# git 기본 정리

## git

- SCM - Source Code Management

  - (분산) 버전 관리 시스템

  - 코드의 History를 관리하는 도구

- 프로젝트 이전 버전을 복원하고 변경사항을 비교, 분석 및 병합도 가능

  

- add 커밋할 목록에 추가

- commit 커밋(create a snapshot) 만들기

- push 현재까지의 역사(commit)가 기록되어 있는 곳에 새로 생성한 커밋들 반영하기



- 커밋의 도장(snapshot)을 기준으로 돌아가기에 잘 관리할 것
- 초기화 시에는 윈도우 - 검색 - 증명 - 윈도우 자격 증명에서 삭제할 것.

-----------

## git bash / cmd 창에서

### 초기에 진행하는 부분

- 가장 초기에 자신의 컴퓨터에 자격 증명을 등록하자. (등록 안할 시에, github가 아닌 gitlab만을 이용하더라도 에러가 발생하는 경우가 있기에 등록을 추천함) (등록하면 자격 증명을 삭제하기 전까지는 다시 등록할 필요가 없다)

  > $ git config --global user.name "`본인 github id(닉네임)`"

  > $ git config --global user.email "`본인 github email`"

  > $ git config --global --list		(등록 되었는지 확인)



- 폴더 자체에 처음 git 관련 작업을 할 경우(git clone 등을 통해 받은 폴더는 할 필요 없음)

  > $ git init		(등록할 최상위 폴더에서 한번만 입력하면 된다.)

  (git init으로 생긴 파일을 지우고 싶을 경우 $ rm -rf .git)



- repository를 새로 만들거나 / clone 받은 프로젝트를 또 다른 repository에 연결할 경우(폴더를 삭제하거나 새로 clone 받지 않는 한, 한번만 진행하면 된다)

  > $ git remote add origin `연결하고 싶은 프로젝트 URL 주소`

  **(git clone을 받아 작업해서, clone받았던 repository에 push할 경우에는 이 과정을 할 필요가 없다)**

  > $ git remote -v		(작업한 폴더가 repository에 연결되었는지 확인)



### 기본적인 등록 과정

> $ git add .		(`.` 대신에 `폴더명/`, `파일명`으로 push하고 싶은 일부분을 정할 수도 있다. `.`은 폴더 전체)

> $ git commit -m "`등록 시에 보여질 메세지`"

> $ git log		(commit이 제대로 되었는지 확인)

> $ git push -u origin master		(이 명령어는 한번만 입력하면 된다)
>
> $ git push		(위의 명령어를 한번 입력하고 나면 이 명령어만으로 동작함)



### branch 관련 부분

- 브랜치 만들기

  > $ git branch `브랜치 이름`

- 브랜치 이동

  > $ git checkout `브랜치 이름`

- 브랜치 삭제 (**branch 위치 확인해서 반드시 마스터로 돌아간 뒤에 삭제할 것.**)

  > $ git branch -d `브랜치 이름`
  >
  > $ git branch -D `브랜치 이름`		(강제 삭제, 망했든 필요없든 병합 안됐으면 이걸 사용하자)

- 브랜치 확인

  > $ git branch



- 생성하면서 바로 이동(단축)

  > $ git checkout -b `브랜치 이름`

- merge는 항상 leader 쪽에서

  > $ git merge `브랜치 이름`		(이렇게 명령어 또한 존재하지만, 가능하면 github나 gitlab에서 어떤 부분이 달라졌는지 보면서 병합하는 것을 추천함)



- 브랜치 로그 확인

  > $ git log --oneline --graph

-------------------

## 협업 관련 work-flow

### 1. feature branch workflow(소규모)

#### leader

1. gitlab에서 new repository 생성

2. 작업할 폴더를 만든다.

3. 작업 하고 push

4. 팀원 초청
5. 새로운 브랜치 만들기
6. 작업한다.

7. push

   > $ git push -u origin `브랜치 이름`		(leader의 경우 자신의 repository에서 병합)

8. 팀원들이 push한 코드 확인해서 pull request -> merge

   (**merge하면 팀원들에게 항상 pull 받으라고 알려줘야 함.** 안 그러면 코드가 꼬일 수도 있다)

- 충돌 일어나면, master쪽에서 직접 수정하든, 거절해서 다시 보내라고 하든 한다.

9. 5번 ~ 7번, 8번을 반복해서 수행한다.



#### member

1. leader가 만든 repository에서 git clone 받기

2. 새로운 브랜치 만들기
3. 작업한다.

4. push

   > $ git push -u origin `브랜치 이름`		(leader에게 push한 것)

5. **leader쪽에 변동사항 있을 때**(자신이나 다른 팀원의 push로 병합됨)마다 master로 이동해서 $ git pull

   (master와 branch는 같은 작업을 공유하고 있는 상태가 아니기에, 자신이 작업했던 것이 병합됐더라도 git pull 받아야 한다.)

6. 3번 ~ 4번, 5번을 반복적으로 수행한다.



- github의 경우 초기에 적용할 사항

  (gitlab과 같은 과정을 진행한다. github는 같은 repository에 그룹원이 아닐경우 git push에서 deny된다. )

  - 마스터 : collaborator설정 -> settings -> collaborators -> 이름 입력
  - 팀원 : 메일 확인 후 수락 -> git push 재시도



### 2. forking workflow(open source 방식)

#### leader

1. feature branch workflow(소규모) 방식과 동일하다.



#### member

1. gitlab의 우상단측에 있는 fork를 누를 것.

2. 내 repository에 복사된 것을 clone

3. clone받은 것을 원본에 연결

   > $ git remote add upstream `leader의 repository 주소`

4. 브랜치 만들기

5. 작업한다.

6. push

   > $ git push -u origin `브랜치 이름`

7. 만약 원본이 병합됐다면,

   > $ git checkout master (branch master로 이동)
   >
   > $ git pull upstream master

- 보통 이렇게 병합되고 branch를 이동했다는 것은 기능 하나를 끝냈다는 것이므로, 브랜치를 지우고 새로 만든다. (나중에 기능을 많이 작성할 경우, 망한 branch와 헷갈리는 경우가 있으므로 지우고 새로 만드는 것을 추천함.)

8. 4번 ~ 7번을 반복해서 수행한다.

-------------------------------

## git ignore설정

- DB / 개인정보 등의 유출 방지를 위한 설정
- **최상위 위치에 있을 것!**
- git bash로 code .gitignore 입력(.gitignore 파일을 만든다)



- 참고사이트 : https://gitignore.io/

  (언어, IDE, Framework 등에 맞는 ignore요소를 복붙 가능)



--------

## git에 image파일 올리기

1. PJT파일에 img폴더를 만들어서 같이 올린다. (readme에 경로 수정해서 넣을 것)
2. github 홈페이지 -> issues -> new issue -> 사진 파일 올리기(마우스드래그로 옮겨넣기도 가능) -> 생기는 주소를 알려주면 된다.(단점은 하나하나 업로드하는데 걸리는 시간)