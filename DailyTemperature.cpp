class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int s= temperatures.size();
        vector<int>ans(s);
        stack<int> stc;
        int i;        
        for(i=0;i<s;i++){
            while(!stc.empty() && temperatures[stc.top()] < temperatures[i]){
                ans[stc.top()]= i-stc.top();
                stc.pop();
            }
            stc.push(i);
        }
        return ans;
    }
};
