def strip_leading_zeros(text):
    return text.lstrip('0') or '0'

def map_letters_to_nums(word, letter_map):
    return ''.join(letter_map[ord(ch) - ord('a')] for ch in word)

def compute_addition(num_str1, num_str2):
    if len(num_str1) > len(num_str2):
        num_str1, num_str2 = num_str2, num_str1

    sum_result = []
    carry = 0

    for k in range(len(num_str1)):
        digit_total = int(num_str1[-1 - k]) + int(num_str2[-1 - k]) + carry
        sum_result.append(str(digit_total % 10))
        carry = digit_total // 10

    for k in range(len(num_str1), len(num_str2)):
        digit_total = int(num_str2[-1 - k]) + carry
        sum_result.append(str(digit_total % 10))
        carry = digit_total // 10

    if carry:
        sum_result.append(str(carry))

    return strip_leading_zeros(''.join(reversed(sum_result)))

def verify_solution(word_a, word_b, word_sum, letter_map):
    num_a = map_letters_to_nums(word_a, letter_map)
    num_b = map_letters_to_nums(word_b, letter_map)
    num_sum = map_letters_to_nums(word_sum, letter_map)

    computed = compute_addition(num_a, num_b)
    num_sum = strip_leading_zeros(num_sum)

    return num_sum == computed

def backtrack_solve(pos, letter_map, used_digits, word_a, word_b, word_sum):
    if pos == 26:
        return verify_solution(word_a, word_b, word_sum, letter_map)

    if letter_map[pos] != '+':
        return backtrack_solve(pos + 1, letter_map, used_digits, word_a, word_b, word_sum)

    for d in range(10):
        if used_digits[d] == 0:
            used_digits[d] = 1
            letter_map[pos] = str(d)
            if backtrack_solve(pos + 1, letter_map, used_digits, word_a, word_b, word_sum):
                return True
            letter_map[pos] = '+'
            used_digits[d] = 0

    return False

def resolve_puzzle(word_a, word_b, word_sum):
    letter_map = ['-' for _ in range(26)]
    used_digits = [0] * 10

    for ch in word_a + word_b + word_sum:
        letter_map[ord(ch) - ord('a')] = '+'

    if backtrack_solve(0, letter_map, used_digits, word_a, word_b, word_sum):
        num_a = map_letters_to_nums(word_a, letter_map)
        num_b = map_letters_to_nums(word_b, letter_map)
        num_result = map_letters_to_nums(word_sum, letter_map)
        return [num_a, num_b, num_result]
    else:
        return ["-1"]

word_a = "send"
word_b = "more"
word_sum = "money"
answer = resolve_puzzle(word_a, word_b, word_sum)
print(" ".join(answer))