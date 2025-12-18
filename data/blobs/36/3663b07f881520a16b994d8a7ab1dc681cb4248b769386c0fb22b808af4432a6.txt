import java.sql.SQLOutput;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Conservatory
 * This class houses the aviaries which in turn houses the birds that are "captured"
 */

public class Conservatory {

  //this hashmap will show which birds are in each aviary
  private HashMap<Birds, Integer> birdMap = new HashMap<>();

  //total number of birds in conservatory
  private int totalBirds = 0;
  //total number of Aviaries
  private int numAviaries = 0;
  private int carne = 0;
  private int pesc = 0;
  private int veg = 0;

  private List<Birds>  listOfBirdsInConservatory = new ArrayList<Birds>();
//  private Aviary[] aviaries = new Aviary[20];
  private List<Aviary> aviariesList = new ArrayList<Aviary>();

  public HashMap<Birds, Integer> getBirdMap() {
    return birdMap;
  }

  public void setBirdMap(HashMap<Birds, Integer> birdMap) {
    this.birdMap = birdMap;
  }

  public int getTotalBirds() {
    return totalBirds;
  }

  public void setTotalBirds(int totalBirds) {
    this.totalBirds = totalBirds;
  }

  public int getNumAviaries() {
    return numAviaries;
  }

  public void setNumAviaries(int numAviaries) {
    this.numAviaries = numAviaries;
  }

  public int getCarne() {
    return carne;
  }

  public void setCarne(int carne) {
    this.carne = carne;
  }

  public int getPesc() {
    return pesc;
  }

  public void setPesc(int pesc) {
    this.pesc = pesc;
  }

  public int getVeg() {
    return veg;
  }

  public void setVeg(int veg) {
    this.veg = veg;
  }

  public List<Birds> getListOfBirdsInConservatory() {
    return listOfBirdsInConservatory;
  }

  public void setListOfBirdsInConservatory(List<Birds> listOfBirdsInConservatory) {
    this.listOfBirdsInConservatory = listOfBirdsInConservatory;
  }

  public List<Aviary> getAviariesList() {
    return aviariesList;
  }

  public void setAviariesList(List<Aviary> aviariesList) {
    this.aviariesList = aviariesList;
  }
  /**
   * updateFoodSupply
   * @param foodType takes in the bird Type
   * updates the counts of each food type based on the bird placed into the conservatory
   */
  public void updateFoodSupply(String foodType) {
    if (foodType.equals("predator")) {
      this.carne++;
    } else if (foodType.equals("Waterfowl")) {
      this.pesc++;
    } else  {
      this.veg++;
    }
  }
  /**
   * createAviary creates a new aviary if there are none yet established or if the current ones
   * do not accomodate a new incoming bird
   *
   * @param birdToAdd  is the bird that was captured to be added
   */
  public void createAviary(Birds birdToAdd) {
      Aviary aviaryToAdd = new Aviary();
      aviaryToAdd.setAviaryType(birdToAdd.getTag());
      updateFoodSupply(birdToAdd.getTag());
      numAviaries++;
      totalBirds++;
      aviaryToAdd.setId(numAviaries);
      birdMap.put(birdToAdd, numAviaries);
      aviariesList.add(aviaryToAdd);
      aviaryToAdd.getBirdsInAviary().add(birdToAdd);
      listOfBirdsInConservatory.add(birdToAdd);

  }
  /**
   * findAviaryToInsert is the main function that adds birds to its cooresponding aviary or calls
   * create aviary based on housing status. It will check if the conservatory is able to take in
   * new birds and if so where it would best fit based on the tag.
   */
  public void findAviaryToInsert(Birds birdToAdd) {
    //check how many birds?
    if (totalBirds > 100) {
      System.out.println("Conservatory is full");
      return;
    }
    if (birdToAdd.getExtinct()){
      return;
    }

    String aviaryMatch = birdToAdd.getTag();
    for (int i = 0; i < this.aviariesList.size(); i++) {
      //checks if there is matching aviary type and has opening
      if (this.aviariesList.get(i).getAviaryType().equals(aviaryMatch)
              && this.aviariesList.get(i).getBirdsInAviary().size() < 5 ) {
        this.aviariesList.get(i).getBirdsInAviary().add(birdToAdd);
        //update maps and stuff
        listOfBirdsInConservatory.add(birdToAdd);
        updateFoodSupply(aviaryMatch);
//        aviaryToAdd.getBirdsInAviary().add(birdToAdd);
        birdMap.put(birdToAdd, this.aviariesList.get(i).getId());
        totalBirds++;
        return;
      }
    }

    if (aviariesList.size() >= 19) {
      System.out.println("Conservatory is full cannot build another aviary");
    } else {
      createAviary(birdToAdd);
      return;
    }

  }
  /**
   * printAvariesList function prints the each aviary in the conservatory
   */
  public void printAvariesList(){
    for (int i = 0; i < aviariesList.size(); i++) {
      System.out.println(aviariesList.get(i));

    }
  }
  /**
   * findBird searches through the HashMap for a particular bird
   * limitations currently are that we are matching bird name to bird name which is not
   * optimal.
   *
   * @param name is a name of a bird - a user can search for a bird and which aviary its in
   */
  public int findBird (String name) {
    for(Map.Entry<Birds, Integer> entry : birdMap.entrySet())
    {
      if(entry.getKey().getName().equals(name)) {
        System.out.println("Found " +name + " in Aviary: "+entry.getValue());
        return entry.getValue();
      }
    }
    System.out.println("Not found in this conservatory");
    return 0;
  }

  /**
   * printAllBirds sorts birds by name alphabetically and prints out the entire list of all
   * birds in the conservatory
   */
  public void printAllBirds() {
    Collections.sort(listOfBirdsInConservatory, new Comparator<Birds>() {
      @Override
      public int compare(Birds o1, Birds o2) {
        return o1.getName().compareTo(o2.getName());
      }
    });
    for (int i = 0; i < listOfBirdsInConservatory.size(); i++) {
      System.out.println(listOfBirdsInConservatory.get(i));
    }
  }
  /**
   *  printFoodSupply prints food supply necessary for current conservatory population
   */
  public void printFoodSupply(){
    System.out.println("Predatory feed: " + this.carne + "\n" +
            "Fish feed: " + this.pesc + "\n" +
            "Seeds, fruits, veg: " + this.veg  + "\n");
  }

  @Override
  public String toString() {
    return "Conservatory{" +
            "birdMap=" + birdMap +
            ", listOfBirdsInConservatory=" + listOfBirdsInConservatory +
            ", aviariesList=" + aviariesList +
            '}';
  }
}
