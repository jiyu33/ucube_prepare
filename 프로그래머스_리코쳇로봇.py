"""
탐색 방법 : BFS(너비 우선 탐색, Breadth First Search)
가까운 노드부터 탐색하는 알고리즘
큐 자료구조를 이용함.

시간복잡도 : O(n*m)
(O(rows*cols))
"""

from collections import deque

def solution(board):
    rows = len(board)
    cols = len(board[0])
    visited = [[False] * cols for _ in range(rows)]

    # 방향: 상, 하, 좌, 우
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    # 시작점 찾기
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'R':
                start = (i, j)
                break

    queue = deque()
    queue.append((start[0], start[1], 0))  # (행, 열, 이동 횟수)
    visited[start[0]][start[1]] = True

    while queue:
        x, y, count = queue.popleft()

        # 목표 지점 도착
        if board[x][y] == 'G':
            return count

        for dx, dy in directions:
            nx, ny = x, y

            # 벽이나 장애물을 만날 때까지 계속 이동
            while True:
                tx = nx + dx
                ty = ny + dy

                if 0 <= tx < rows and 0 <= ty < cols and board[tx][ty] != 'D':
                    nx, ny = tx, ty
                else:
                    break  # 이동 종료

            # 이동한 위치가 처음 방문한 곳이라면 큐에 추가
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, count + 1))

    # 목표에 도달하지 못한 경우
    return -1
