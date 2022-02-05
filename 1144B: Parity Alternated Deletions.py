
def leftoversum(a, n) : 
    sum1 = 0 
    odd, even = [], [];  
    for i in range(n) :  
          
        if (a[i] % 2) : 
            odd.append(a[i]);  
        else : 
            even.append(a[i]);  
      
    
    if (len(odd) > len(even)) :  
  
        
        odd.sort();  
        even.sort();  
  
         
        leftoverelements = len(odd) - len(even) - 1;  
  
        minimize_sum = 0;  
        i = 0;  
  
         
        while (i < leftoverelements) :  
            minimize_sum += odd[i]; 
            i += 1
  
        
        return minimize_sum;  
      
     
    elif (len(even) > len(odd)) : 
  
     
        even.sort();  
        odd.sort();  
          
        leftoverelements = len(odd) - len(even) - 1; 
        
        minimize_sum = 0;  
        i = 0;  
 
  
        while(i < leftoverelements) :  
            sum1 += odd[i]; 
            i += 1
  
        
            return minimize_sum
   
    else : 
        return 0      
  
 
if __name__ == "__main__" :  

    n = int(input())
    a = list(map(int,input().split()))
    n = len(a);  
    if len(set(a))==1:
        print(a[0])      
    else:
        print(leftoversum(a, n))

