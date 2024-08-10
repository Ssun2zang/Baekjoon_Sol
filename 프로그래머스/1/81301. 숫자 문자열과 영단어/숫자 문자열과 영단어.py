# 영단어 문자열 -> 숫자로 변경
# 0으로 시작하지 않음
# 올바른 입력만 주어짐
import re

def solution(s):

    nums = {"zero" : 0, "one":1, "two":2, "three":3, "four":4, "five": 5, "six":6, "seven":7, "eight":8, "nine":9}
    
    words = re.split(r'([0-9]|zero|one|two|three|four|five|six|seven|eight|nine)', s)

    answer = ""

    for w in words:
        answer += str(nums.get(w, w))
    return int(answer)

print(solution("one4seveneight"))