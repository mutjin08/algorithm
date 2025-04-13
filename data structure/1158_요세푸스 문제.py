n, k = map(int, input().split())

answer = []
people = [str(i) for i in range(1, n+1)]

pointer = 0
while people:
    pointer = (pointer + k-1) % len(people)
"""    pointer += k-1
    if pointer >= len(people):
        pointer %= len(people)"""
    answer.append(people.pop(pointer))

print("<"+", ".join(answer)+">")
