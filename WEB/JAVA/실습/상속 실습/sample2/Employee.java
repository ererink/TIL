package sample2;

public class Employee {
	int empNo;
	String eName;
	int mgr;
	String hiredate;
	String deptName;
	
	public Employee() {}

	public Employee(int empNo, String eName, int mgr, String hiredate, String deptName) {
		super();
		this.empNo = empNo;
		this.eName = eName;
		this.mgr = mgr;
		this.hiredate = hiredate;
		this.deptName = deptName;
		}
	
		public int getEmpNo() {
			return empNo;
		}
	
		public void setEmpNo(int empNo) {
			this.empNo = empNo;
		}
	
		public String geteName() {
			return eName;
		}
	
		public void seteName(String eName) {
			this.eName = eName;
		}
	
		public int getMgr() {
			return mgr;
		}
	
		public void setMgr(int mgr) {
			this.mgr = mgr;
		}
	
		public String getHiredate() {
			return hiredate;
		}
	
		public void setHiredate(String hiredate) {
			this.hiredate = hiredate;
		}
	
		public String getDeptName() {
			return deptName;
		}
		public String toString() {
			return empNo + " | " + eName + " | " + mgr + " | " + hiredate + " | " + deptName ;
		}
		public void setDeptName(String deptName) {
			this.deptName = deptName;
		}
	
}
