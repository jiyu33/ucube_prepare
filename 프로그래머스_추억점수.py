"""
[프로그래머스 추억 점수]
입력 : x
출력 : result 배열
조건 : 3<=name 원소길이<=7, 1<=yearning[i]<=100
       3<=photo 길이<=100, 3<=name 길이=yearning 길이<=100
유형 : 구현
실행시간 : O(n*m)
"""

def solution(name, yearning, photo):
    result = []
    info = dict(zip(name, yearning))

    for people in photo :
        score = 0
        for person in people :
            score += info.get(person, 0)
        result.append(score)
    return result
