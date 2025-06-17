#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here
        n=len(a)
        m=len(b)
        i,j=0,0
        union_set=[]
        last=None
        while i < n and j < m:
            if a[i]<b[j]:
               if last!=a[i]:
                  union_set.append(a[i])
                  last=a[i]
               i+=1
            elif a[i]>b[j]:
               if last!=b[j]:
                union_set.append(b[j])
                last=b[j]
               j+=1
            else:
                if last!=a[i]:
                    union_set.append(a[i])
                    last=a[i]
                i+=1
                j+=1
        while i<n :
            if last!=a[i]:
                union_set.append(a[i])
                last=a[i]
                  
            i+=1
        
        while j<m :
            if last!=b[j]:
                union_set.append(b[j])
                last=b[j]
                  
            j+=1
        return union_set
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    