"""
입력 : 배열
출력 : Yes 또는 No
유형 : 구현
실행시간 : O(n)
"""
def solution(cards1, cards2, goal):
    answer = []
    n = len(cards1)
    m = len(cards2)
    
    i = j = 0
    for word in goal :
        if i < n and word == cards1[i] :
            answer.append(cards1[i])
            i += 1
        if j < m and word == cards2[j] :
            answer.append(cards2[j])
            j += 1
    return 'Yes' if answer == goal else 'No'
