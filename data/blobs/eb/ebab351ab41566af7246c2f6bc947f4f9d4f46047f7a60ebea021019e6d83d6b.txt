import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class FlightCrewTest {

    FlightCrew pilot;

    @Before
    public void before() {
        pilot = new FlightCrew("Bob", FlightCrewRank.CAPTAIN);
    }

    @Test
    public void  hasName() {
        assertEquals("Bob", pilot.getName());
    }

    @Test
    public void hasRank() {
        assertEquals(FlightCrewRank.CAPTAIN, pilot.getRank());
    }
}
