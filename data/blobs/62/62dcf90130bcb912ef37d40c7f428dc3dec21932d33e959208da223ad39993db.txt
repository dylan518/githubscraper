package HW_Java_6;

import java.util.Arrays;
import java.util.HashSet;

public class Task_1 {
   public static void main(String[] args) {
      Cat cat1 = new Cat();
      cat1.setId(1);
      cat1.setNameCat("Барсик");
      cat1.setColorCat("Полосатый");
      cat1.setAgeCat(3);
      System.out.println(cat1);

      Cat cat2 = new Cat();
      cat2.setId(2);
      cat2.setNameCat("Мурка");
      cat2.setColorCat("Шиншила");
      cat2.setAgeCat(3);
      System.out.println(cat2);

      Cat cat3 = new Cat();
      cat3.setId(1);
      cat3.setNameCat("Барсик");
      cat3.setColorCat("Полосатый");
      cat3.setAgeCat(3);
      System.out.println(cat3);

      Cat cat4 = new Cat();
      cat4.setId(1);
      cat4.setNameCat("Барсик");
      cat4.setColorCat("Полосатый");
      cat4.setAgeCat(3);
      System.out.println(cat4);

      System.out.println(cat1 == cat3);
      System.out.println(cat1.equals(cat3));
      var cats = new HashSet<Cat>(Arrays.asList(cat1, cat2, cat3));
      System.out.println(cats.contains(cat4));
      System.out.println(cats);
   }
}

class Cat {
   private int idCat; // Идентификационный номер в системе (уникален)
   private String nameCat; // Имя кота
   private String breedCat; // Порода кота
   private String colorCat; // Окрас кота
   private int ageCat; // Возраст кота
   private String ownerCet; // Владелец кота
   private String addresOwnerCat; // Адрес владельца кота

   // Сеттеры
   public void setId(int idCat) {
      this.idCat = idCat;
   }

   public void setNameCat(String nameCat) {
      this.nameCat = nameCat;
   }

   public void setBreedCat(String breedCat) {
      this.breedCat = breedCat;
   }

   public void setColorCat(String colorCat) {
      this.colorCat = colorCat;
   }

   public void setAgeCat(int ageCat) {
      this.ageCat = ageCat;
   }

   public void setOwnerCet(String ownerCet) {
      this.ownerCet = ownerCet;
   }

   public void setAddresOwnerCat(String addresOwnerCat) {
      this.addresOwnerCat = addresOwnerCat;
   }

   // Геттеры
   public int getId() {
      return idCat;
   }

   public String getNameCat() {
      return nameCat;
   }

   public String getBreedCat() {
      return breedCat;
   }

   public String getColorCat() {
      return colorCat;
   }

   public int getAgeCat() {
      return ageCat;
   }

   public String getOwnerCet() {
      return ownerCet;
   }

   public String getAddresOwnerCat() {
      return addresOwnerCat;
   }

   @Override
   public String toString() {
      return String.format("id:%d %s %s %d", idCat, nameCat, colorCat, ageCat);
   }

   @Override
   public boolean equals(Object o) {
      Cat t = (Cat) o;
      return idCat == t.idCat;
   }

   @Override
   public int hashCode() {
      return idCat;
   }

}
