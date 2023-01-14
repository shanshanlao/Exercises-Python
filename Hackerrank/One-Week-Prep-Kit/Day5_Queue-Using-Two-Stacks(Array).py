if __name__ == '__main__':

    queries = []
    for _ in range(int(input())):
        queries.append(input())
    
    # print(queries)
    
    n = len(queries)
    queue = []
    for i in range(n): 
        
        if len(queries[i]) > 1: # meaning the type is 1 - Enqueue
            qtype, qvalue = queries[i].split(" ")   
            queue.append(qvalue)
        else:
            qtype = queries[i]
        
            if qtype == '2': # Dequeue
                queue.pop(0)
            else: # Print
                print(queue[0])
