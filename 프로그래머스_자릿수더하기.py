"""
list comprehension : 한 줄로 반복+가공+저장 동시에 처리
[ ... for 변수 in 리스트]
리스트 길이보다 더 큰 범위를 반복문에 지정한다면 존재하지 않는 인덱스를
접근하게 되어 IndexError: list index out of range 오류 발생.
iterable:반복할 수 있는 객체. 즉 for 루프에서 꺼내 쓸 수 있는 객체.
정수는 iterable이 아니기 때문에 str로 강제 형변환을 해주어야 함.

[다른 사람 풀이]
def solution(n):
    result=0
    list_n=[int(x) for x in str(n)]
    return sum(list_1)
굳이 for문을 사용하지 않고 sum 함수를 사용한다면 시간 복잡도도 줄일 수 있다..!

시간 복잡도 : O(n)
"""
def solution(n):
    result=0
    list_n=[int(x) for x in str(n)]
    for i in range(len(list_n)):
        result+=list_n[i]
    return result
 
