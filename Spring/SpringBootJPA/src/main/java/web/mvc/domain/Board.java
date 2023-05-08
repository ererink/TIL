package web.mvc.domain;

import java.time.LocalDateTime;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.SequenceGenerator;

import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity // JPA 관리할 객체 => ddl-auto=create이면 테이블로 생성한다. 
@Setter
@Getter
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class Board {
	
	@GeneratedValue(strategy=GenerationType.SEQUENCE, generator = "board_bno_seq")
	@SequenceGenerator(name="board_bno_seq", allocationSize = 1, sequenceName = "board_bno_seq")
	@Id // pk
	private Long bno;
	
	@Column(nullable = false) // notnull
	private String title;
	private String writer;
	
	@Column(length = 500)
	private String content;
	
	@CreationTimestamp
	private LocalDateTime insertDate;
	
	@UpdateTimestamp
	private LocalDateTime updateDate;

}
