"""
문자열에는 비트연산자를 사용할 수 없다. 논리연산자는 사용 가능.
ex : if flag=="true" | if flag=="True"

[다른 사람 풀이]
solution=lambda a,b,f:[a-b,a+b][f]
리스트에서 f 값을 인덱스로 사용해서 값 꺼냄. 0일 때 a-b, 1일 때 a+b

시간복잡도 : O(1)
"""
def solution(a, b, flag):
    result=0
    if flag==1:
        result = a+b
    else:
        result = a-b
    return result
