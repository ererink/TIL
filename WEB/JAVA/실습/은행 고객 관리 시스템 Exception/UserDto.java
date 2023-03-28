package WS07;

public class UserDto {
    int userSeq;
    String name;
    String email;
    String phoneNumber;
    boolean isSleep;

    public UserDto(int id, String name, String email, String phoneNumber, boolean isSleep) {
        this.userSeq = userSeq;
        this.name = name;
        this.email = email;
        this.phoneNumber = phoneNumber;
        this.isSleep = isSleep;
    }

    public int getUserSeq() {
        return userSeq;
    }

    public void setUserSeq(int userSeq) {
        this.userSeq = userSeq;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public boolean isSleep() {
        return isSleep;
    }

    public void setSleep(boolean sleep) {
        isSleep = sleep;
    }
}
