package hust.soict.dsai.aims.cart;

import hust.soict.dsai.aims.media.Media;

import java.util.Comparator;

public class MediaComparatorByTitleCost implements Comparator<Media> {
    @Override
    public int compare(Media m1, Media m2){
        int a = m1.getTitle().compareTo(m2.getTitle());
        if(a == 0){
            return Float.compare(m1.getCost(), m2.getCost());
        }
        return a;
    }

}

