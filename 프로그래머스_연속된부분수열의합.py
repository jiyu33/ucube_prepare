"""
탐색 기법 : 투 포인터
두 개의 포인터(인덱스)를 사용해서 배열을 한 번만 훑으며 원하는 조건을 찾는 방식
처음에는 같은 위치거나 양 끝에서 시작함.
한 쪽 혹은 양쪽 포인터를 이동시키며 구간을 좁히거나 넓힘

float('inf'):양의 무한대를 의미. 무한대이기 때문에 어떤 수보다도 큼.

시간 복잡도 : O(n)
뒤로 돌아가지 않고 right, left가 최대 n번 이동하기 때문에 선형 시간.

"""

def solution(sequence, k):
    left = 0
    right = 0
    total = sequence[0]
    answer = []
    min_len = float('inf')

    while right < len(sequence):
        if total < k:
            right += 1
            if right < len(sequence):
                total += sequence[right]

        elif total > k:
            total -= sequence[left]
            left += 1

        else:  
            if (right - left) < min_len:
                min_len = right - left
                answer = [left, right]

            total -= sequence[left]
            left += 1

    return answer
