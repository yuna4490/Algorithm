import heapq

def solution(k, score):
    answer = []
    heap = []
    
    for i in score:
        if len(heap) == k:
            if i > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
        
        else:
            heapq.heappush(heap, i)
            
        answer.append(heap[0])
    
    
    return answer