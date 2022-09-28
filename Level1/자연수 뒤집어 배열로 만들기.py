def solution(n):
    arr = list(str(n)) # 매개변수 n을 리스트화
    arr.reverse() # reverse() 함수를 활용한 변경
    
    return list(map(int, arr)) # 리스트화 진행

print(solution(12345))
