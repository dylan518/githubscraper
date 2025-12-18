package com.members;

import com.database.GetMember;
import com.database.InsertMember;
import com.general.Console;

import com.members.membership.Membership;
import com.members.membership.Normal;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.MockedStatic;
import org.mockito.Mockito;
import org.mockito.junit.jupiter.MockitoExtension;


import static org.mockito.Mockito.mock;

@ExtendWith(MockitoExtension.class)
public class AddMemberTest {
    @Mock
    private GetMember connection = new GetMember();

    @Mock
    private InsertMember insert;

//    @Test
//    public void loadMemberTest(){
//        HashMap<Integer, Member> members = new HashMap<>();
//
//        Member newMember = AddMember.createDefaultMember();
//        newMember.setMemberID(1);
//        members.put(newMember.getMemberID(), newMember);
//
//        Member newMember2 = AddMember.createDefaultMember();
//        newMember2.setMemberID(2);
//        newMember2.setFirstName("Mike");
//        newMember2.setLastName("Wadden");
//        members.put(newMember2.getMemberID(), newMember2);
//
//        try (MockedStatic<SearchForMember> search = Mockito.mockStatic(SearchForMember.class)){
//            search.when(() -> SearchForMember.findMember(1)).thenReturn(newMember);
//            search.when(() -> SearchForMember.findMember(2)).thenReturn(newMember2);
//
//            Mockito.when(connection.getMembers()).thenReturn(members);
//            //Mockito.when(connection.getMembership("Normal", 1, 365, 0)).thenReturn(new Normal(365, 0));
//            //Mockito.when(connection.getFamilyOnPlan(1)).thenReturn(new ArrayList<>());
//            // AddMember.loadMembers();
//
//            //Assertions.assertEquals(SearchForMember.findMember(1), newMember);
//        }
//    }

//    @Test
//    public void testCreateMember(){
//        Address defaultAddress = AddMember.getDefaultAddress();
//
//        try (MockedStatic<Console> console = Mockito.mockStatic(Console.class)){
//                console.when(() -> Console.readNumber("Enter Selection: ", 1, 5)).thenReturn(2.0);
//
//                console.when(() -> Console.readString("First Name: ", 1, 32)).thenReturn("John");
//                console.when(() -> Console.readString("Last Name: ", 1, 32)).thenReturn("Smith");
//                console.when(() -> Console.readString("Email Address: ", 1, 32)).thenReturn("jsmith@gmail.com");
//                console.when(() -> Console.readStringDate("Start Date (MM/DD/YYYY): ")).thenReturn("10/10/1991");
//
//                console.when(() -> Console.readLine("Street Address: ", 1, 32)).thenReturn("51A Amherst");
//                console.when(() -> Console.readLine("City: ", 1, 32)).thenReturn("St. John's");
//                console.when(() -> Console.readLine("Province: ", 1, 32)).thenReturn("51A Amherst");
//                console.when(() -> Console.readLine("Postal Code: ", 1, 32)).thenReturn("51A Amherst");
//
//                Mockito.when(insert.addMemberToDB(mock(Member.class))).thenReturn(1);
//
//                Member newGuy = AddMember.createMember();
//                System.out.println(newGuy);
//                Assertions.assertEquals(newGuy.getName(), "John Smith");
//            }
//    }

    @Test
    public void testGetAddress(){
            try (MockedStatic<Console> console = Mockito.mockStatic(Console.class)){
                console.when(() -> Console.readLine("Street Address: ", 1, 32)).thenReturn("51A Amherst");
                console.when(() -> Console.readLine("City: ", 1, 32)).thenReturn("St. John's");
                console.when(() -> Console.readLine("Province: ", 1, 32)).thenReturn("51A Amherst");
                console.when(() -> Console.readLine("Postal Code: ", 1, 32)).thenReturn("51A Amherst");

                Address newAddress = AddMember.getAddress();
                Assertions.assertEquals(newAddress.getCity(), "St. John's");
            }
    }

    @Test
    public void testChoosePlanType(){
        try (MockedStatic<Console> console = Mockito.mockStatic(Console.class)){
            console.when(() -> Console.readNumber("Enter Selection: ", 1, 5)).thenReturn(2.0);

            Membership newMembership = AddMember.choosePlanType();
            Assertions.assertEquals(newMembership.getTypeCode(), 2);
        }
    }

    @Test
    public void testCreateDefaultMember() {
        Member testMember = AddMember.createDefaultMember();

        Assertions.assertTrue(testMember.toString().contains("Alex"));
        Assertions.assertFalse(testMember.toString().contains("Cody"));
    }

    @Test
    public void testGetDefaultAddress() {
        Address testAddress = AddMember.getDefaultAddress();

        Assertions.assertTrue(testAddress.toString().contains("NL"));
        Assertions.assertFalse(testAddress.toString().contains("AB"));
    }
}