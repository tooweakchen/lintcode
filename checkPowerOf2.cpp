class Solution {
public:
    /*
     * @param n: An integer
     * @return: True or false
     */
    bool checkPowerOf2(int n) {
        // write your code here
        bool s1=false,s2=true;
        if(n<=0)return s1;
        else if(n==1) return s2;
        else
        {
            if((n&(n-1))==0) return s2;
            else return s1;
        }
    }
};
