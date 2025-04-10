# KMP

문자열 검색 알고리즘. 텍스트 문자열 안에서 패턴 문자열이 도착하는 위치를 효율적으로 찾는 알고리즘 $O(N+M)$ (N: 텍스트, M: 패턴)

## 방법

부분일치 테이블을 생성. 패턴 내에서 접두사와 접미사가 일치하는 최대길이를 저장함.

1. i=0, j=0 부터 시작해서 text[i] pattern[j] 를 비교
2. 문자가 일치시:
   - i+=1, j+=1 (다음 문자로 이동)
3. 문자가 불일치시:
   - 만약 j!=0 이면, j = lps[j-1] 로 점프 -> 패턴의 앞부분 중에서 다시 시작할 위치 알려줌.
   - 만약 j==0 이면, i+=1 -> 그냥 다음 문자로 넘어감.

# Question

- <details open>
  <summary></summary>
  </details>
- <details open>
  <summary></summary>
  </details>

# Rabbit hole
