"""
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))
처음에 max와 min으로 접근하였으나 풀이 시간이 길어져서 실패,,
비슷한 문제가 나온다면 꼭 풀이해야지.

시간복잡도 : O(1)
"""
def solution(s):
    numbers=list(map(int, s.split()))
    numbers.sort()
    return str(numbers[0])+" "+str(numbers[-1])
