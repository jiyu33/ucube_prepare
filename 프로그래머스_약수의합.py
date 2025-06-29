"""
[첫 번째로 작성한 코드]
n=int(input())
if n<0 or n>3000:
    exit
answer=0
i=1 
for i in range(n): 
    if n%i==0:
        answer+=i
print(answer)
ZeroDivisionError 발생.>i=1로 초기화 했더라도 for i in range(n)를 하는 순간
i를 직접 제어하는 for문에 의해 i 값이 덮어씌워짐.

[다른 사람 풀이]
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

시간복잡도 : O(n)
"""
def solution(n):
    if n<0 or n>3000:
        exit
    answer = 0
    for i in range(1,n+1):
        if n%i==0:
            answer+=i
    return answer
