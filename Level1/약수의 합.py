def solution(n):
    a = 0
    answer = 0
    while a < n:
        a += 1
        if n % a == 0:
            answer = answer + a     
    return answer

print(solution(12))
print(solution(5))
