class Solution {
    public int[] decrypt(int[] code, int k) {
        
        int n = code.length;
        int[] res = new int[n];

        if(k > 0)
        {
            int s = 1;
            int e = k;
            int window = 0;
            for(int i = s ; i <= e ; i++)
            {
                window += code[i];
            }
            res[0] = window;

            for(int i = 1 ; i < res.length ; i++)
            {
                window = window - code[s++ % n] + code[++e % n];
                res[i] = window;
            }
        }
        if(k < 0){
            int s = n-1;
            int e = n+k;
            int window = 0;
            for(int i = s ; i >= e ; i--)
            {
                window += code[i];
            }
            res[0] = window;

            for(int i = 1 ; i < res.length ; i++)
            {
                window = window + code[++s % n] - code[e++ % n];
                res[i] = window;
            }
        }
        else{
            return res;
        }

        return res;
    }
}