"""
[처음 작성한 코드]->시간 초과로 실패
def solution(players, callings):
    result=players
    for i in range(len(callings)):
        for j in range(len(players)):
            if players[j]==callings[i]:
                swap=players[j]
                players[j]=players[j-1]
                players[j-1]=swap
                result[j]=players[j]
    return result

컴프리헨션 종류-리스트,딕셔너리,집합
딕셔너리 컴프리헨션: {key:value for...}
ex:) {x:x**2 for x in range(3)} -> {0:0,1:1,2:4}
enumerate():iterable(리스트,튜플,문자열) 객체를 순회할 때 인덱스와 값을 함께
얻고 싶을 때 사용하는 함수. enumerate(iterable, start=0)

name_to_index 딕셔너리와 players 리스트를 따로 만들어줌.
name_to_index 딕셔너리는 인덱스 순서와 문자열이 동시에 저장되어있음.
players는 문자열만 저장되어있음.
따라서 name_to_index 딕셔너리의 인덱스 번호를 바꾸어주는 과정 필요.

시간 복잡도 : O(n+m)

"""
def solution(players, callings):
    name_to_index = {name: idx for idx, name in enumerate(players)}
    
    for call in callings:
        idx = name_to_index[call]
        players[idx], players[idx - 1] = players[idx - 1], players[idx]

        name_to_index[players[idx]] = idx
        name_to_index[players[idx - 1]] = idx - 1

    return players
