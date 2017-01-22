import java.util.*;
public class Interview {

	public static void main(String[] args) {
		//Evaluate Reverse Polish Notation
        System.out.println("Evaluate Reverse Polish Notation");
		String[] input = new String[]{"4","1","2","+","/","3","*"};
		System.out.println(evalRPN(input));
		
		//String Isomorphism
        System.out.println("String Isomorphism");
		String a1 = "bear";
		String b1 = "nogg";
		System.out.println(isStringIsomorphic(a1,b1));
		
		//Shortest palindrome
        System.out.println("Shortest Palindrome");
		a1 = "babd";
		System.out.println(shortestPalindrome(a1));
		
		//Longest Common Subsequence
        System.out.println("Longest Common Subsequence");
		longestCommonSubsequence("acdbe","abeefa");
		
		//Longest Palindrome Substring
        System.out.println("Longest Palindrome Substring");
		longestPalindromeSubstring("dabba");
	}
	
	//Evaluate Reverse Polish Notation
	public static float evalRPN(String[] input){
		Stack<Float> s = new Stack<Float>();
		String ops = "+-*/";
		float arg1,arg2;
		
		for(String token : input){
			int op = ops.indexOf(token);
			//its a number
			if(op < 0){
				s.push(Float.parseFloat(token));
			}
			//add
			else if(op == 0){
				arg2 = s.pop();
				arg1 = s.pop();
				s.push(arg1+arg2);
			}
			//subtract
			else if(op == 1){
				arg2 = s.pop();
				arg1 = s.pop();
				s.push(arg1-arg2);
			}
			//multiply
			else if(op == 2){
				arg2 = s.pop();
				arg1 = s.pop();
				s.push(arg1*arg2);
			}
			//divide
			else if(op == 3){
				arg2 = s.pop();
				arg1 = s.pop();
				s.push(arg1/arg2);
			}
		}
		return s.pop();
	}
	
	//String Isomorphism
	public static boolean isStringIsomorphic(String a, String b){
		if(a.length() != b.length())
			return false;
		else{
			HashMap<Character,Character> m = new HashMap<Character,Character>();
			for(int i = 0; i < a.length(); i++){
				char c1 = a.charAt(i);
				char c2 = b.charAt(i);
				
				if(!m.containsKey(c1)){
					if(m.containsValue(c2))
						return false;
					else
						m.put(c1, c2);
				}
				else{
					if(m.get(c1) != c2)
						return false;
				}
			}
		}
		
		return true;
	}
	
	//Shortest Palindrome
	public static String shortestPalindrome(String s){
		if(s.length() % 2 == 0){
			return s;
		}
		else{
			int mid = (int)Math.ceil(s.length() / 2);
			int i = mid+1;
			int j = mid-1;
			while(i < s.length() && j >= 0 && s.charAt(i) == s.charAt(j)){
				i++;
				j--;
			}
			System.out.println(i+" "+j);
			String suffix;
			if(i < s.length()-1){
				suffix = s.substring(i);
				System.out.println(suffix);
			}
			else
				suffix = s.substring(1);
			
			String prefix = new StringBuilder(suffix).reverse().toString();
			return prefix + s;
		}
			
	}
	
	//Longest Common Subsequence
	public static int longestCommonSubsequence(String a, String b){
		int[][] lcs = new int[a.length()+1][b.length()+1];
		
		for(int i = 0; i < lcs[0].length; i++)
			lcs[0][i] = 0;
		
		for(int i = 0; i < lcs.length; i++)
			lcs[i][0] = 0;
		
		for(int i = 1; i < lcs.length; i++){
			for(int j = 1; j < lcs[0].length; j++){
				if(a.charAt(i-1) == b.charAt(j-1))
					lcs[i][j] = lcs[i-1][j-1]+1;
				else
					lcs[i][j] = Math.max(lcs[i][j-1], lcs[i-1][j]);
			}
		}
		
		for(int i = 0; i < lcs.length; i++){
			for(int j = 0; j < lcs[0].length; j++){
				System.out.print(lcs[i][j]);
			}
			System.out.println();
		}
		return 0;
	}
	
	//Longest Palindromic Substring
	public static int longestPalindromeSubstring(String s){
		int[][] dp = new int[s.length()][s.length()];
		
		for(int i = 0; i < s.length(); i++)
			dp[i][i] = 1;
		
        int i,j;
		for(int n = 1; n < s.length(); n++){ //distance from diagonal
			for(int m = 0; m < s.length()-n; m++){ //rows
                i = m;
                j = m+n;
                
				if(j == i + 1 && s.charAt(i) == s.charAt(j)){
					dp[i][j] = 2;
				}
				else if(s.charAt(i) == s.charAt(j) && dp[i+1][j-1] == j-i-1){
					dp[i][j] = 2+dp[i+1][j-1];
				}
				else{
					dp[i][j] = Math.max(dp[i+1][j],dp[i][j-1]);
				}
			}
		}
		
		printMatrix(dp);
		return 0;
	}
	
	public static void printMatrix(int[][] mat){
		for(int i = 0; i < mat.length; i++){
			for(int j = 0; j < mat[0].length; j++){
				System.out.print(mat[i][j]);
			}
			System.out.println();
		}
	}
}
