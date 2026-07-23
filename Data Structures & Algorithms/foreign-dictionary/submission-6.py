class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        edges={node:[] for word in words for node in word}
        indegree={node:0 for word in words for node in word}
        for index, firstword in enumerate(words[:-1]):
                    secondword=words[index+1]
                    i=0
                    while i<len(firstword) and i<len(secondword):
                        if firstword[i]!=secondword[i]:
                            if secondword[i] not in edges[firstword[i]]:
                                edges[firstword[i]]+=[secondword[i]]
                                indegree[secondword[i]]+=1
                            break
                        else:
                            # no difference found and firstword is longer → invalid
                            if len(firstword) > len(secondword):
                                return ""
                        i+=1

        visited=[]
        print(edges)

        que=collections.deque()
        result=[]
        for key,val in indegree.items():
            if val==0:
                que.append(key)
        while que:
            node=que.popleft()
            result.append(node)
            for neighbor in edges[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    que.append(neighbor)
        if len(result) != len(indegree):
            return ""
                    
        return "".join(result)

        
            
            
        
        