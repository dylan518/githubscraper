package dao;

import enums.Gender;
import model.Animal;
import service.GenericService;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

import static java.util.Collections.sort;

public class AnimalDaoImpl implements GenericDao<Animal> {

    private List<Animal> animals = new ArrayList<>();

    @Override
    public String add(List<Animal> newAnimal) {
       animals.addAll(newAnimal);
        return "Ийгиликтуу сакталды!";
    }


    @Override
public Animal getById(Long id) {
    try {
        for (Animal animal : animals) {
            if (animal.getId().equals(id)) {
                return animal;
            }
        }
        throw new IllegalArgumentException("Мындай " + id + " Id де жаныбар жок .");
    } catch (IllegalArgumentException e) {
        System.out.println("Ката: " + e.getMessage());
        return null;
    }
}


    @Override
    public List<Animal> getAll() {
        return new ArrayList<>(animals);
    }



@Override
public List<Animal> sortByName() {
    try {
        System.out.println("1- баскычта ascending, 2- баскычта descending:");
        Scanner scanner = new Scanner(System.in);
        int choice = scanner.nextInt();

        List<Animal> sortedAnimals = new ArrayList<>(animals);

        if (choice == 1) {
            sortedAnimals.sort(new Comparator<Animal>() {
                @Override
                public int compare(Animal a1, Animal a2) {
                    return a1.getName().compareTo(a2.getName());
                }
            });
        } else if (choice == 2) {
            sortedAnimals.sort(new Comparator<Animal>() {
                @Override
                public int compare(Animal a1, Animal a2) {
                    return a2.getName().compareTo(a1.getName());
                }
            });
        } else {
            System.err.println("Туура эмес тандоо. 1 же 2 танданыз.");
            return sortedAnimals;
        }

        return sortedAnimals;

    } catch (Exception e) {
        System.err.println("Ката: " + e.getMessage());
        return new ArrayList<>();
    }
}



    @Override
public List<Animal> filterByGender() {

    System.out.println("1- баскычта Female , 2- баскычта Male: ");
    Scanner scanner = new Scanner(System.in);
    int choice = scanner.nextInt();

    Gender selectedGender ;
    if (choice == 1) {
        selectedGender = Gender.FEMALE;
    } else if (choice == 2) {
        selectedGender = Gender.MALE;
    } else {
        System.out.println("Invalid choice 1 же 2 танданыз");
        return new ArrayList<>();
    }

    List<Animal> filteredAnimals = new ArrayList<>();
    for (Animal animal : animals) {
        if (animal.getGender() == selectedGender) {
            filteredAnimals.add(animal);
        }
    }

    if (filteredAnimals.isEmpty()) {
        System.out.println("Тандалган gender деги жаныбар табылган жок.");
    }

    return filteredAnimals;
}


    @Override
    public List<Animal> clear() {
        animals.clear();

        System.out.println("Ийгиликтуу очурулду.");
        return  new ArrayList<>();
    }


}
