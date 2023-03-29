package sample2;

public class PartTime extends Employee {
	int timePay;
	
	public PartTime() {}

    public PartTime(int empNo, String eName, String job, int mgr, String hiredate, String deptName, int timePay) {
        super(empNo, eName, mgr, hiredate, deptName);
		this.timePay = timePay;
	}

	public int getTimePay() {
		return timePay;
	}

	public void setTimePay(int timePay) {
		this.timePay = timePay;
	}
	
    @Override
    public String toString() {
        return super.toString() + " | " + timePay;
    }
	public void message() {
	}
}
