# schooltimetable-meal
급식 식단과 시간표를 알려주는 코드입니다.(초,중,고등학교)</br>
파이썬 기반입니다</br>
중학교는 middle.py, 고등학교는 high.py, 초등학교는 elementary.py를 쓰시면 됩니다 </br>


# how to use
1.https://open.neis.go.kr/portal/mainPage.do 에서 로그인해서 OPENAPI 키를 발급받습니다. </br>
2. 학교코드와 교육청 코드를 알아야합니다.</br>
2-1. https://open.neis.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=OPEN17020190531110010104913&infSeq=3# 여기에 가서 다운받아 확인해주세요.</br>
3. 코드에서의 학교코드와 교육청코드를 찾은 코드로 대체합니다.</br>
4. https://discord.com/developers/applications 가서 애플리케이션을 만들고 봇을 만들어 토큰을 받습니다.</br>

# command
1. k/시간표 학년반(예:104) 날짜(예:20201211) </br>
1-1. 예시: k/시간표 104 20201211 </br>
2. k/급식 날짜(예:20201211) </br>
2-1. 예시: k/급식 20201211 </br>
3. k/오늘급식
