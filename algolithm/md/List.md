## 배열

- 버블 정렬

  -  인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식

  - 시간복잡도 O(n^2)
  - 비교와 교환으로 코딩이 가장 손쉽다.

  ``` python
  # 오름차순 정렬
  def BubbleSort(a, N):	# a : 정렬할 list, N : 원소의 수
  	for i in range(N-1, 0, -1):	# 범위의 끝 위치
          for j in range(0, i):	# 비교할 원소 중 왼쪽 원소의 인덱스
              if a[j] > a[j+1]:	# 왼쪽 원소가 더 크면
                  a[j], a[j+1] = a[j+1], a[j]	# 오른쪽 원소와 교환
  ```



- 카운팅 정렬

  - 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘
  - 조건 : 정수나 정수로 표현할 수 있는 자료에 대해서만 적용
  - 시간 복잡도 O(n+k) : n = 리스트의 길이, k = 정수의 최댓값
  - 비교환 방식으로 n이 비교적 작을 때만 가능

  ``` python
  def CountingSort(a, b, k):
      # a[] : 입력된 배열 (1 to k)
      # b[] : 정렬된 배열
      # c[] : 카운트 배열
      c = [0] * (k+1)
      
      for i in range(len(a)):	# a 배열에서 각 항목의 발생 회수를 c 배열에 입력
          c[a[i]] += 1
        
      for i in range(1, len(c)):	# 각 항목의 앞에 위치할 항목의 개수 반영하기 위해 앞의 원소를 더해줌 (누적)
          c[i] += c[i-1]
       
      for i in range(len(b)-1, -1, -1):
          c[a[i]] -= 1
          b[c[a[i]]] = a[i]
  ```

  

- 완전 검색 (Exaustive Search)

  - 문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법
  - Brute-force / generate-and-test 라고도 불림
  - 모든 경우의 수를 테스트 한 후 최종 해법을 도출하므로 경우의 수가 상대적으로 작을 때 유용
  - 모든 경우의 수를 생성하고 테스트하기 때문에 수행 속도는 느리지만, 해답을 찾아내지 못할 확률이 적다.
  - baby-gin game
  - 단순하게 순열을 생성하는 방법

  ``` python
  # 예 {1, 2, 3}을 포함하는 모든 순열 생성
  for i in range(1, 4):
      for j in range(1, 4):
          if i != j:
              for k in range(1, 4):
                  if k != i and k != j:
                      print(i, j, k)
  ```

  

- 탐욕(Greedy) 알고리즘
  - 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행하여 최종적인 해답에 도달
  - 각 선택의 시점에서 이루어지는 결정은 지역적으로는 최적이지만, 그 선택들을 계속 수집하여 최종적인 해답을 만들었다고 하여, 그것이 최적이라는 보장은 없다.
  - 동작 과정
    - 해 선택 : 현재 상태에서 부분 문제의 최적해를 구한 뒤, 이를 부분해 집합에 추가
    - 실행 가능성 검사
    - 해 검사 
  - 거스름돈 줄이기



- 2차원 배열

  - 델타를 이용한 2차 배열 탐색

  ```python
  # 2차 배열의 한 좌표에서 4방향 인접 배열 요소 탐색 방법
  
  arr[][] # nxn 배열
  # 방향 : 상하좌우
  di[-1, 1, 0, 0]
  dj[0, 0, -1, 1]
  
  for i in range(1, n-1):
      for j in range(1, n-1):
          for k in range(4):	# 4방향
              ni = i + di[k]
              nj = j + dj[k]
              if 0 <= ni < n and 0 <= nj < n:
                  print(arr[ni][nj])
  ```

  - 전치 행렬

  ```python
  arr[[],[],[]]	# 3x3 행렬
  for i in range(3):
      for j in range(3):
          if i < j:
              arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
  ```



- 부분집합 (Subset Sum)

  - 부분집합의 수 : 원소가 n개일 때, 공집합을 포함한 부분집합의 개수는 2^n

  ``` python
  bit = [0]*4
  for i in range(2):
      bit[0] = i
      for j in range(2):
          bit[1] = j
          for k in range(2):
              bit[2] = k
              for l in range(2):
                  bit[3] = l
                  print_subset(bit)
  ```

  - 비트 연산자

    - << : 피연산자의 비트 열을 왼쪽으로 이동시킨다. (반대도 있음)

      1 << n : 2^n, 원소가 n개일 경우 모든 부분집합의 수를 의미

    - & : 비트 단위로 AND 연산을 한다.

      i & (1 << j) : i의 j번째 비트가 1인지 아닌지를 검사

    ``` python
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    for i in range(1<<n):	# 1<<n : 부분집합의 개수
        for j in range(n):	# 원소의 수만큼 비트를 비교
            if i & (1<<j):	# i의 j번 비트가 1인 경우
                print(arr[j], end=', ')	# j번 원소 출력
        print()
    print()
    ```



- 순차 검색 (Sequential Search)

  - 가장 간단하고 직관적 방법

  - 알고리즘이 단순해서 구현이 쉽지만, 대상의 수가 많은 겨우 비효율적임

  - 정렬되어 있지 않은 경우 

    - 찾고자 하는 원소의 순서에 따라 비교회수가 결정됨
    - 시간복잡도 O(n)

    ```python
    def sequentialSearch(a, n, key):	
        # a : 검색 배열, n : 배열의 길이 , key : 찾고자하는 값
        i = 0
        # i가 배열의 범위에 있고 찾는 key값이 없는 경우 i += 1 
        while i < n and a[i] != key:
            i += 1
        # while문 종료 후 i의 값을 보고 return
        if i < n:
            return i
        else:
            return -1
    ```

  - 정렬되어 있는 경우 (오름차순으로 정렬 됐다고 가정)

    - 정렬이 되어있으므로, 검색 실패를 반환하는 경우 평균 비교 회수가 반으로 줄어듬

    ```python
    def sequentialSearch(a, n, key):	
        # a : 검색 배열, n : 배열의 길이 , key : 찾고자하는 값
        i = 0
        # a[i] > key 의 경우 찾는 원소가 없는 것이므로 검색 종료
        while i < n and a[i] < key:
            i += 1
        # while문 종료 후 i의 값을 보고 return
        if i < n:
            return i
        else:
            return -1
    ```



- 이진 검색 (Binary Search)

  - 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 진행
  - 검색 범위를 반으로 줄여가면서 보다 빠르게 검색 수행
  - 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 함

  ```python
  def binarySearch(a, n, key):
      start = 0
      end = n-1
      while start <= end:
          middle = (start + end) // 2
          if a[middle] == key:	# 검색 성공
              return True
          elif a[middle] > key:
              end = middle -1		# 자신을 포함하지 않고 -1, +1
          elif a[middle] < key:
              start = middle +1
      return False				# 검색 실패
  ```

  - 재귀함수를 이용한 이진 검색

  ```python
  def binarySearch(a, low, high, key):
      if low > high:	# 검색 실패
          return False
      else:
          middle = (low + high) // 2
          if key == a[middle]:
              return True		# 검색 성공
          elif key < a[middle]:
              return binarySearch(a, low, middle-1, key)
          elif key < a[middle]:
              return binarySearch(a, middle+1, high, key)
  ```



- 선택 정렬 (Selection Sort)

  - 주어진 자료 중 가장 작은 값의 원소부터 차례대로 선택하여 위치 교환
  - 시간 복잡도 : O(n2)

  ```python
  def SelectionSort(a, n):
      for i in range(n-1):	
  # 미정렬원소가 하나 남은 상황에서는 마지막 원소가 가장 큰 값을 가지게 되므로, 실행 종료, 선택 정렬 완성
          mididx = i
          for j in range(i+1, n):
              if a[middle] > a[j]:
                  mididx = j
          a[i], a[mididx] = a[mididx], a[i]
      return a
      # return arr[k-1] : k번째로 작은 원소를 찾음
  ```

  