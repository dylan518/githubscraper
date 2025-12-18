package task1;


import java.util.Set;
import java.util.SortedSet;
import java.util.TreeSet;
import java.util.Comparator;


public class ConferenceWithSet extends Conference {
    private Set<Meeting> meetingSet;


    public ConferenceWithSet(String name, String venue, Set<Meeting> meetings) {
        super(name, venue);
        this.meetingSet = meetings;
    }


    @Override
    public Meeting[] getMeetings() {
        return meetingSet.toArray(new Meeting[0]);
    }


    public void addMeeting(Meeting meeting) {
        meetingSet.add(meeting);
    }


    public void sortMeetingsByParticipants() {
        SortedSet<Meeting> sortedSet = new TreeSet<>(meetingSet);
        meetingSet = sortedSet;
    }


    public void sortMeetingsByName() {
        SortedSet<Meeting> sortedSet = new TreeSet<>(Comparator.comparing(Meeting::getTopic));
        sortedSet.addAll(meetingSet);
        meetingSet = sortedSet;
    }
}
