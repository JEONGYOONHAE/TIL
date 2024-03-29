## Stack

1. 스택의 특성

- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조이다.
- 스택에 저장된 자료는 선형 구조를 갖는다.
  - 선형구조 : 자료 간의 관계가 1 : 1 의 관계
  - 비선형구조 : 자료 간의 관계가 1 : N 의 관계 ex) tree
- 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있다.
- 마지막에 삽입한 자료를 가장 먼저 꺼냄 : 후입선출(LIFO, Last-in First-out)

2. 스택의 연산

- 삽입 : push
- 삭제 : pop
- 공백이 아닌지 확인 : isEmpty
- top의 원소(item)를 반환 : peek

3. 스택 구현 고려 사항

- 1차원 배열을 사용하여 구현할 경우 구현이 용이하다는 장점이 있지만 스택의 크기를 변경하기가 어렵다는 단점이 있다.
- 단점을 해결하기 위한 방법으로 저장소를 동적으로 할당하여 스택을 구현
  - 구현이 복잡하다는 단점이 있지만 메모리를 효율적으로 사용한다는 장점

4. 스택 응용1 : 괄호검사

- 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 함
- 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 한다.
- 괄호 사이에는 포함 관계만 존재한다.

5. 스택 응용2 : function call

- 프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리
- 후입선출 구조의 스택을 이용
- 함수 호출과 복귀에 따른 전체 프로그램의 수행 순서

![수행순서](https://user-images.githubusercontent.com/94509971/160234146-dfa1eb2a-5b51-43eb-bf42-da39e4551e88.PNG)

6. 재귀호출

- 자기 자신을 호출하여 순환 수행
- 재귀호출 방식을 사용하여 함수를 만들면 프로그램의 크기를 줄이고 간단하게 작성 가능
- factorial : 1 ~ n 까지 모든 자연수를 곱함
- 피보나치 : 0과 1로 시작하고 이전의 두 수 합을 다음 항으로 하는 수열

```python
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
```

7. Memoization

- 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술
- 동적 계획법의 핵심이 되는 기술

```python
# memo를 위한 배열을 할당하고, 모두 0으로 초기화 
# memo[0]을 0으로 memo[1]는 1로 초기화

def fibo(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]
memo = [0, 1]
```

8. DP(Dynamic Programming)

- 동적계획 알고리즘은 그리디 알고리즘과 같이 __최적화 문제__를 해결하는 알고리즘

- 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 모다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘

- 피보나치 수 DP 적용

  ```PYTHON
  def fibo(n):
      f = [0, 1]
      for i in range(2, n+1):
          f.append(f[i-1] + f[i-2])
      return f[n]
  ```

9. DFS(깊이우선탐색)

- 시작 정점 v를 결정하여 방문
- 정점 v에 인접한 정점 중에서
  - 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문
  - 그리고 w를 v로 하여 다시 위의 과정을 반복
  - 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 위의 과정을 반복
- 스택이 공백이 될 때까지 위 과정 반복

10. 계산기

- 문자열 수식 계산의 일반적 방법

  - 중위 표기법의 수식을 후위 표기법으로 변경 (스택 이용)
  - 중위표기법 : A + B
  - 후위 표기법의 수식을 스택을 이용하여 계산
  - 후위표기법 : AB+

- 중위표기식의 후위표기식 변환 방법1

  - 수식의 각 연산자에 대해서 우선순위에 따라 괄호를 사용하여 다시 표현
  - 각 연산자를 그에 해당하는 오른쪽 괄호의 뒤로 이동
  - 괄호 제거

  ```
  예시 : A*B-C/D
  # 1단계
  ( (A*B) - (C/D))
  # 2단계
  ( (AB)* (CD)/ )-
  # 3단계
  AB*CD/-
  ```

- 중위표기식의 후위표기식 변환 방법 2 (스택 이용)

  - 입력 받은 중위표기식에서 토큰을 읽음
  - 토큰이 피연산자이면 토큰 출력
  - 토큰이 연산자일 경우, 
    이 토큰이 스택의 top의 연산자보다 우선순위가 높으면 push하고
    그렇지 않으면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 pop한 후 토큰 연산자를  push
  - 토큰이 오른쪽 괄호 ) 일 경우,
    스택 top에 왼쪽 괄호 ( 가 올 때까지 pop, 왼쪽 괄호를 만나면 pop만 하고 출력하지는 않음
  - 중위 표기식에 더 읽을 것이 없다면 중지하고, 더 읽을 것이 있다면 처음부터 다시 반복
  - 스택에 남아있는 연산자를 모두 pop하여 출력
  - 스택 밖의 왼쪽 괄호는 우선순위가 가장 높으며, 스택 안의 왼쪽 괄호는 우선순위가 가장 낮다

- 후위표기법의 수식을 스택을 이용해서 계산

  - 피연산자를 만나면 스택에 push
  - 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산, 연산결과를 다시 스택에 push
  - 수식이 끝나면, 마지막으로 스택을 pop하여 출력

11. 백트래킹 (Backtracking)

- 해를 찾는 도중에 '막히면' (해가 아니면) 되돌아가서 다시 해를 찾아 가는 기법
- 최적화와 결정 문제를 해결할 수 있음
- 결정 문제 : 문제의 조건을 만족한느 해가 존재하는지 여부를 yes or no가 답하는 문제
  - 미로찾기
  - n-Queen
  - Map coloring
  - 부분 집합의 합 (Subset Sum)
- 백트래킹과 깊이우선탐색 차이
  - 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임
  - 깊이우선탐색은 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단
  - 깊이우선탐색을 가하기에는 경우의 수가 너무나 많음
  - 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간을 요하므로 처리 불가능
- 백트래킹 알고리즘 절차
  - 상태 공간 트리의 깊이 우선 검색을 실시
  - 각 노드가 유망한지를 점검
  - 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속
- 일반 백트래킹 알고리즘

``` python
def checknode(v):
    if promising(v):
        if there is a solution at v:
            write the solution
        else:
            for u in each child of v:
                checknode(u)
```

12. 부분집합 구하기

- 어떤 집합의 공집합과 자기자신을 포함한 모든 부분집합을 powerset이라고 하며,
  구하고자 하는 어떤 집합의 원소 개수가 n일 경우 부분집합의 개수는 2^n개 이다.
- 부분집합 생성하기

```python 
# 각 원소가 부분집합에 포함되었는지를 loop 이용하여 확인하고 부분집합을 생성
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)
```

- powerset을 구하는 백트래킹 알고리즘

```python 
def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES
    if k == input:
        proecss_solution(a, k)
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)
            
def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2
MAXCANDIDATES = 2
NMAX = 4
a = [0] * NMAX
backtrack(a, 0, 3)
```

13. 분할정복

- 거듭제곱 : O(n)

```python
def Power(base, exponent):
    if base == 0:
        return 1
    result = 1
    for i in range(exponent):
        result *= base
    return result 
```

- O(log2n)