package com.techelevator.dao.jdbc;

import com.techelevator.dao.ReservationDAO;
import com.techelevator.model.Reservation;
import org.junit.Before;
import org.junit.Test;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.support.rowset.SqlRowSet;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;

public class JDBCReservationDAOTests extends BaseDAOTests {

    private ReservationDAO dao;
    private JdbcTemplate jdbcTemplate;

    @Before
    public void setup() {
        dao = new JDBCReservationDAO(dataSource);
        jdbcTemplate = new JdbcTemplate(dataSource);
    }

    @Test
    public void createReservation_Should_ReturnNewReservationId() {
        int reservationCreated = dao.createReservation(1,
                "TEST NAME",
                LocalDate.now().plusDays(1),
                LocalDate.now().plusDays(3));

        assertEquals(reservationCreated, 1);
    }
    
    @Test
    public void upcoming_Reservations_Should_Return_Reservations_After_Today_test() {
    	long numberOfUpcomingReservations = 0;
    	String sqlFindUpcomingReservations = "SELECT COUNT(reservation_id) AS count FROM reservation WHERE to_date BETWEEN CURRENT_DATE AND (CURRENT_DATE + 30)";
    	SqlRowSet result = jdbcTemplate.queryForRowSet(sqlFindUpcomingReservations);
    	
    	while(result.next()) {
    		numberOfUpcomingReservations = result.getLong("count");
    	}
    	List<Reservation> reservations = dao.upComingReservations();
    	
    	assertNotNull(reservations);
    	assertEquals(numberOfUpcomingReservations, reservations.size());
    }

}
