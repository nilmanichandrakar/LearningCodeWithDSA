class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> vec;
        string s;
        for(int i=1;i<=n;i++)
       { 
            if(i%15==0){
            s="FizzBuzz";
        }
        else if(i%3==0){
           s="Fizz";
        }
        else if(i%5==0){
            s="Buzz";}
               
        else{
        s=to_string(i);
        }
         vec.push_back(s);   
       }       
               
    return vec;
    }
};
