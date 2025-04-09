INF = float("inf")  # 무한대를 나타냄

# 노드 개수
n = 4

# 인접 행렬 (0-indexed, 자기 자신은 0, 연결 안 된 곳은 INF)
graph = [[0, 5, INF, 8], [INF, 0, 2, INF], [INF, INF, 0, 1], [INF, INF, INF, 0]]

# 플로이드 워셜 알고리즘
for k in range(n):  # 중간 노드
    for i in range(n):  # 출발 노드
        for j in range(n):  # 도착 노드
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# 결과 출력
print("최단 거리 결과:")
for row in graph:
    print(row)
