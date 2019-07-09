

.select_one('경로')

.select('경로')->리스트로 나온다.

nth child와 같은 특이한 요소 잘 확인할 것.



# git

- SCM - Source Code Management

> (분산) 버전 관리 시스템

> 코드의 History를 관리하는 도구

- 프로젝트 이전 버전을 복원하고 변경사항을 비교, 분석 및 병합도 가능



- add 커밋할 목록에 추가
- commit 커밋(create a snapshot) 만들기
- push 현재까지의 역사(commit)가 기록되어 있는 곳에 새로 생성한 커밋들 반영하기



- 커밋의 도장(snapshot)을 기준으로 돌아가기에 잘 관리할 것
- 초기화 시에는 윈도우 - 검색 - 증명 - 윈도우 자격 증명에서 삭제할 것.



------

### git bash에서

$ git config --global user.name "baambox5"

$ git config --global user.email baamboxo@gmail.com

둘 다 입력시 아무것도 안 떠야함

컴퓨터에 git 정보 넣는 것.



$ git config --global --list

확인



($ git init

원하는 폴더(최상위)로 이동한 뒤에 입력(맨 처음 단 한번만 할 것)

나중에 git 안에 git이 생기면 충돌로 데이터 날아갈 수 있음)



$ git status

상태를 확인해서 add를 할지 다른 것을 해야할지 확인



$ git add 00_startcamp/

add작업(상태 확인시에 빨간색이 초록색으로 변함)



$ git commit -m "first commit"

commit작업



$ git log

commit이 제대로 되었는지 확인



($ git remote add origin https://github.com/baambox5/TIL.git

git홈페이지에서 가져올 것, 한번만)



$ git remote -v

remote확인



($ git push -u origin master

push작업 -> 로그인하게 됨, -u:upstream 등록, 처음 한번만)



$ git add .

한번에 add



$ git push

push작업(위의 -u~를 했을 경우)



- commit시에 이름은 사람이 보기 위한 이름임
- 일부만 commit 하고 싶은 경우는 add할때 일부만 할 수 있다.



## 집에서

$ git clone 주소(github홈페이지에서 얻을 수 있음)



- clone받으면 그것을 remote할 필요는 없다(처음에만 clone)



- ##### 수정사항이 있어서 바뀐 것을 올렸을 경우 다른 쪽에서는 pull을 통해 동기화 시킬 것!(clone X)



## 협업시

마스터 : repository 만들것 -> 작업 폴더를 만들것 -> 코드 만들고 git init -> git status ->

​			git add . -> git status -> git commit -m "first commit" -> git log -> git remote add origin->

​			git remote -v -> git push -u origin master



팀원 : git clone https://github.com/toohong5/game.git -> git bash에서 폴더로 이동 ->

​		코드 수정 후 git add . -> git status -> git commit -m "" -> git log -> git push

> clone으로 받은 것은 git init을 하면 충돌이 발생하므로 쓰지 말 것



- 같은 그룹원이 아닐경우 git push에서 deny된다. 

> 마스터 : collaborator설정 -> settings -> collaborators -> 이름 입력
>
> 팀원 : 메일 확인 후 수락 -> git push 재시도



- 여기서부터는 아래 과정을 반복한다.

마스터 : git pull -> 수정 후 git add . -> git status -> git commit -m "" -> git log -> git push

팀원 : git pull -> 수정 후 git add . -> git status -> git commit -m "" -> git log -> git push



--------

## git ignore설정

- 개인정보 유출 방지를 위한 설정
- **최상위 위치에 있을 것!**
- git bash로 code .gitignore 입력
- google에서 gitignore 검색해서 복붙으로 저장



- 선택 참고사이트 : gitignore.io 로 접속해서 필요한 언어에 맞는 ignore요소를 복붙 가능