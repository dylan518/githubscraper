package com.example.demo8888888.model;

import java.time.LocalDate;
import java.util.List;
import javax.persistence.ElementCollection;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Table(name = "Book")
@AllArgsConstructor
@NoArgsConstructor
@Builder
@Getter
@Setter
public class Book {

  @Id
  String url;
  String name;
  String isbn;
  @ElementCollection
  List<String> authors;
  Integer numberOfPages;
  String publisher;
  String country;
  String mediaType;
  String released;
  @ElementCollection
  List<String> characters;
  @ElementCollection
  List<String> povCharacters;

}
