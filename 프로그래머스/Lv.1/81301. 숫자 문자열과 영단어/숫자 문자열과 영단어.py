def solution(s):
    answer = ''
    string = ''
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i in s:
        
        if i.isdigit():
            answer += i
        
        else:
            string += i
            
        if string in num:
            answer += str(num.index(string))
            string = ''
            
    return int(answer)



# num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

# def solution(s):
#     answer = s
#     for key, value in num_dic.items():
#         answer = answer.replace(key, value)
#     return int(answer)