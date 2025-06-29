"""
[프로그래머스 9번/지폐 접기]
입력 : wallet[1], bill[1] 배열로 입력
출력 : 정수 결과값
조건 :
    계산 결과는 정수값
    10<=wallet[0], wallet[1]<=100
    10<=bill[0], bill[1]<=2000
유형 : 그리디
"""

def solution(wallet, bill):
    answer = 0
    
    if((wallet[0]<10 and wallet[1]<10) or (wallet[0]>100 and wallet[1]>100)) :
        exit(0)
    if((bill[0]<10 and bill[1]<10) or (bill[0]>2000 and bill[1]>2000)) :
        exit(0)
    
    while min(bill) > min(wallet) or max(bill) > max(wallet):
        if bill[0] > bill[1]:
            bill[0] = int(bill[0]/2)
        else:
            bill[1] = int(bill[1]/2)
        answer += 1
    return answer
