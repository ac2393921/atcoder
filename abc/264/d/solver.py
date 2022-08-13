def bubble_sort(numbers):
    len_numbers = len(numbers)
    cnt = 0

    for i in range(len_numbers):
        for j in range(len_numbers - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                cnt += 1

    return numbers, cnt


if __name__ == "__main__":
    S = input()
    T = "atcoder"
    d = {s: i for i, s in enumerate(T)}
    s = [d[s] for s in S]
    _, ans = bubble_sort(s)
    print(ans)
