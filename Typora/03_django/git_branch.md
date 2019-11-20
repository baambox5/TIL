# Branch

- Branch : 나뭇가지의 비유적 표현
- Git Branch는 매우 가볍다.
- 순식간에 Branch를 만들고 Branch 사이를 이동할 수 있다.
- git이 가지고 온 혁신 중 하나는 Branch 기능을 매우 쓸만한 수준까지 만들었다는 것.
- 브랜치 이동 시에는 마스터는 변화 없음.
- 만약 브랜치에서 작업하다가 다시 master로 돌아오면 브랜치에서 작업하는 파일은 안 보인다.(별개의 공간)



- 브랜치 확인

> $ git branch

- 브랜치 만들기

> $ git branch <브랜치 이름>

- 브랜치 이동

> $ git checkout <브랜치 이름>

- 브랜치 삭제 (위치 확인해서 반드시 마스터로 돌아간 뒤에 삭제할 것.)

> $ git branch -d <브랜치 이름>



- 생성하면서 바로 이동(단축)

> $ git checkout -b <브랜치 이름>

- merge는 항상 병합되려는 쪽에서(master)

> $ git merge <브랜치 이름>



- merge로 파일이 중복될 경우에는 사람의 손으로 수정해야 함



- 브랜치 로그 확인

> $ git log --oneline --graph



## 협업시

## 1. feature branch workflow(소규모)

### master

- github에서 new repository
- 폴더 지정
- 작업 하고 push
- 팀원 초청
- push받은 코드 확인해서 pull request -> merge
- merge하면 팀원들에게 항상 pull 받으라고 알려줘야 함.
- 충돌 일어나면, master쪽에서 직접 수정하든, 거절해서 다시 보내라고 하든 할 것.



### member

- git clone으로 폴더 받기
- 새로운 브랜치 만들기
- push

> $ git push -u origin <브랜치 이름>

- master로 이동해서 git pull



#### Pull request

- 기능 개발을 끝내고 master에 바로 병합시키는게 아니라, 브랜치를 중앙 원격 저장소에 올리고(push) master에 병합을 요청(merge)
- 주의사항 : 중앙에서 병합을 했다면, 다른 팀원들은 master 브랜치를 pull 받아야한다.

----------------------

## 2. forking workflow(open source)

### master

- github에서 new repository
- 요청받은 갱신 요청을 판단해서 합칠 것.



### member

- github의 우상단측에 있는 fork를 누를 것.
- 내 repository에 복사된 것을 clone
- clone받은 것을 원본에 연결

>  $ git remote add upstream https://github.com/woodg1207/git_test2.git

- 브랜치 만들기
- push

> $ git push -u origin <브랜치 이름>

- compare & pull request 누른다.
- 만약 원본이 업데이트 됐다면, git pull로 갱신(위의 remote로 연결한 이유)(open source에는 굳이 필요 없음)
  - git checkout master (branch master로 이동)
  - git pull upstream master



- 각자명칭, 변수명 주의!