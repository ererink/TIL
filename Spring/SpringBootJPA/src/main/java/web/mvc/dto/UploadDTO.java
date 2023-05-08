package web.mvc.dto;

import org.springframework.web.multipart.MultipartFile;

import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class UploadDTO {
   private String name;
   
   private MultipartFile file;//<input type="file" name="file"/>
   
   private String fileName;
   private long fileSize;
}
