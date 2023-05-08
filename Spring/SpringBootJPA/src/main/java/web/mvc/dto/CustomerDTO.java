package web.mvc.dto;

import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class CustomerDTO {
   private String id;
   private String name;
   private int age;
   private String tel;
   private String addr;
}
