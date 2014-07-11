public class FindSingleNumber{
    public int singleNumber(int[] A){
        int sum = 0;
        for (int i=0; i<A.length;i++){
            sum ^= A[i];
        }
        return sum;
    }
    
    public static void main(String[] argv){
        FindSingleNumber fsn = new FindSingleNumber();
        int[] A = {1,2,3,4,5,1,2,3,4,5,-4};
        int result = fsn.singleNumber(A);
        System.out.println(result);
        
    }

}



