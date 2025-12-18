package agh.ics.oop;

import java.util.Comparator;
import java.util.SortedMap;
import java.util.TreeMap;

public class MapBoundary implements IPositionChangeObserver{

    SortedMap<Vector2d, Grass> grass_x = new TreeMap<>(new Comparator<Vector2d>() {

        @Override
        public int compare(Vector2d o1, Vector2d o2) {
            if(o1.x != o2.x){
                return o1.x - o2.x;
            }
            return o1.y - o2.y;
        }

    });
    SortedMap<Vector2d, Grass> grass_y = new TreeMap<>(new Comparator<Vector2d>() {

        @Override
        public int compare(Vector2d o1, Vector2d o2) {
            if(o1.y != o2.y){
                return o1.y - o2.y;
            }
            return o1.x - o2.x;
        }

    });
    SortedMap<Vector2d, Animal> animals_x = new TreeMap<>(new Comparator<Vector2d>() {

        @Override
        public int compare(Vector2d o1, Vector2d o2) {
            if(o1.x != o2.x){
                return o1.x - o2.x;
            }
            return o1.y - o2.y;
        }

    });
    SortedMap<Vector2d, Animal> animals_y = new TreeMap<>(new Comparator<Vector2d>() {

        @Override
        public int compare(Vector2d o1, Vector2d o2) {
            if(o1.y != o2.y){
                return o1.y - o2.y;
            }
            return o1.x - o2.x;
        }

    });


//    public MapBoundary(Animal[] animals, Grass[] grasses){
//        for(Animal animal: animals){
//            animals_x.put(animal.getPosition(), animal);
//            animals_y.put(animal.getPosition(), animal);
//        }
//        for(Grass grass: grasses){
//            grass_x.put(grass.getPosition(), grass);
//            grass_y.put(grass.getPosition(), grass);
//        }
//    }

        public void AddAnimal(Animal animal){
            animals_x.put(animal.getPosition(), animal);
            animals_y.put(animal.getPosition(), animal);
        }

        public void AddGrass(Grass grass){
            grass_x.put(grass.getPosition(), grass);
            grass_y.put(grass.getPosition(), grass);
        }

    public Vector2d GetTopRight(){
        return new Vector2d(Math.max(animals_x.get(animals_x.lastKey()).getPosition().x, grass_x.get(grass_x.lastKey()).getPosition().x),
                Math.max( animals_y.get(animals_y.lastKey()).getPosition().y, grass_y.get(grass_y.lastKey()).getPosition().y));
    }

    public Vector2d GetBottomLeft(){
        return new Vector2d(Math.min( animals_x.get(animals_x.firstKey()).getPosition().x, grass_x.get(grass_x.firstKey()).getPosition().x),
                Math.min( animals_y.get(animals_y.firstKey()).getPosition().y, grass_y.get(grass_y.firstKey()).getPosition().y));
    }
    @Override
    public void positionChanged(Vector2d oldPosition, Vector2d newPosition) {
        Animal animal = this.animals_x.get(oldPosition);
        this.animals_x.put(newPosition, animal);
        this.animals_y.put(newPosition, animal);
        this.animals_x.remove(oldPosition);
        this.animals_y.remove(oldPosition);
    }
}
