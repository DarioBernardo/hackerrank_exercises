"""
Find the longest Consecutive Substring (Increasing Alphabetically) from the below pattern that starts with A.
[?, B, A, ?, C, D, ?, ?, F, I, ?, ?, ?, ?, D, ?, ?, ?, H]
You can assume ? as any character. it can be replace by 0 or 1 character.
Note: Consider all as upper case.
Exp: One of the Substrings is A, B, C, D, E, F from index 2 to 7.
But the longest substring can be formed from index 11 to 18 which A,B,C,D,E,F,G,H.

How to solve this with optimized way?.
"""
"""
public static int getLongestString(String input){
    int max = -1;
    int last_valid_index = Integer.MAX_VALUE;
    int current_max = 0;
    int previous_seq = -1;
    for(int i =0 ; i <input.length();i++){
        
        int current_seq = input.charAt(i) - 'A';
        
        if(input.charAt(i) == '?'){
            current_seq = previous_seq+1;
            current_max++;
            last_valid_index = Math.min(last_valid_index,i);
           
        }else{
            
            if(current_seq == previous_seq + 1){
                 current_max++;
            }
            else if(current_seq == 0){
                current_max = 1;
            }
            else{
                
                if(current_seq <=  i - last_valid_index ){
                    current_max = current_seq +1;
                }else{
                    current_max = 0;
                }
                
            }
            
            last_valid_index = Integer.MAX_VALUE;
        
        }
        
        max = Math.max(current_max,max);

        previous_seq = current_seq;
        
    }
    
    return max;
    
}
"""

