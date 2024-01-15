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