def solution(x):
    answer = True
    num = 0
    
    x_list = list(str(x))
    
    for i in x_list:
        num += int(i)
        
    return True if x % num == 0 else False