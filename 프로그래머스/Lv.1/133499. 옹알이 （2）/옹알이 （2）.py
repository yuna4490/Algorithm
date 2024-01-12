def solution(babbling):
    answer = 0
    
    arr1 = ['aya', 'ye', 'woo', 'ma']
    
    for a2 in babbling:
        for a1 in arr1:
            if a1*2 not in a2: 		# 연속으로 나오지 않으면
                a2 = a2.replace(a1, ' ') 	# 공백으로 대체
        
        if a2.isspace(): 		# 공백으로만 이루어져 있다면 
            answer += 1
                 
    return answer

 