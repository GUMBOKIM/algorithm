def solution(numbers, target):
    result = 0

    def dfs(num, index):
        nonlocal result

        if index == len(numbers):
            if num == target:
                result += 1
            return

        signs = [-num, num]
        if index == 1:
            for i in range(2):
                dfs(signs[i] + numbers[index], index + 1)
                dfs(signs[i] - numbers[index], index + 1)
        else:
            dfs(num + numbers[index], index + 1)
            dfs(num - numbers[index], index + 1)

    dfs(numbers[0], 1)

    return result