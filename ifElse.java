public class FirstTest {
	public static void main(String[] args) {
		
		String studentName = "Koki";
		boolean isMaleGender = false;
		int mark = 35;
		String gender;
		String rank;
		
		System.out.println("welcome " + studentName);
		
		if(isMaleGender) {
			gender = "male";
			
			if (mark >= 35) { 
				rank = "passed";
			}else {
				rank = "failed";
			}
		} else {
			gender = "female";
			
			if (mark >= 50) {
				rank = "passed";
			} else {
				rank = "failed";
			}
		}
		
		System.out.println(studentName + " is " + gender);
		System.out.println("You are " + rank);
		
    }
}
