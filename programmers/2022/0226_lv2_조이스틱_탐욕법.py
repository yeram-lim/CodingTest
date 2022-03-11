problem = [
    "JEROEN",
    "JAN",
    "AAAAAA",
    "ADKEIE",
]

from string import ascii_uppercase

def solution(name):
    answer, index_first_A, series_A = 0, 0, 0
    try:
        index_first_A = name.index('A')
    except ValueError:
        index_first_A = -1
    if index_first_A != -1:
        for letter in name[index_first_A + 1:]:
            if letter == 'A':
                series_A += 1
            else:
                break
        
    if len(name) != (series_A + 1):
        if 'A' not in name:
            answer += (len(name) - 1)
        else:
            move_count = ((index_first_A - 1) * 2) + (len(name) - (index_first_A + series_A) - 1)
            print(move_count)
            answer += min(move_count, len(name))

        for letter in name[-1::-1]:
            if letter == 'A':
                answer -= 1
            else:
                break
    else:
        return 0
    
    alphabet_list = list(ascii_uppercase)
    for letter in name:
        move_count = min(alphabet_list.index(letter), len(alphabet_list) - alphabet_list.index(letter))
        answer += move_count

    return answer
print(solution(problem[0]))