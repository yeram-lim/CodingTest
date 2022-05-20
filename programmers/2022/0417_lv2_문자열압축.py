hi = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]

def solution(s):
    answer = 1001
    longest_length = len(s) // 2
    # print(longest_length)

    for length in range(1, longest_length + 1):
        if len(s) % length != 0: #나머지가 안 남는 길이로 압축해야함.
            continue
        
        s_part = int(len(s)/length) #length로 나누면 나오는 s 도막들
        # print(len(s), len(s)/length, s_part)
        start = 0
        short_s = ''
        same = False
        print("    the length is ", length)
        # print(s[0:0])
        for i in range(s_part):
            this_part = s[start : (start + length)]

            # try:
            next_part = s[start + length : ((start + length) + length)]
            if not next_part: #다음 파트가 없음 끝난고임
                if not same:
                    continue
                short_s = short_s.replace('1', '')
                #anwer에서 1제거 
                if len(short_s) < answer:
                    answer = len(short_s)
                    print("끝났음!!! short_S is ", short_s, len(short_s))
                continue
            print("this is ", this_part, " next is ", next_part)
            start = start + length

            if this_part == next_part:
                same = True
                if not len(short_s): #압축 길이 0일때
                    input_str = '2' + this_part
                    short_s = input_str
                    print("short s in middle process ", short_s)
                    print('---')
                else:
                    # print("!!!!!", short_s[-length:])
                    if short_s[-length:] == this_part:
                        count = int(short_s[-(length + 1)]) + 1
                        short_s = short_s[0 : -(length + 1)] + str(count) + this_part
                        print("short s in middle process ", short_s)
                        print('---')
                    else:
                        short_s += '2' + this_part
                        print("short s in middle process ", short_s)
                        print('---')
            else:
                if not len(short_s):
                    continue
                if length == 1:
                    if short_s[-1] != this_part:
                        short_s += '1' + this_part
                else:
                    if short_s[-1 : -length] != this_part:
                        short_s += '1' + this_part  
                print("short s in middle process when not same ", short_s)

        print("length ", length, "is the end, and answer is ", answer)

    return answer

print(solution(hi[2]))