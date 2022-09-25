def solution(n):
    answer = 1
    while answer < n:
        if n % answer == 1:
            break
        answer += 1
    return answer

print(solution(10))
print(solution(12))
