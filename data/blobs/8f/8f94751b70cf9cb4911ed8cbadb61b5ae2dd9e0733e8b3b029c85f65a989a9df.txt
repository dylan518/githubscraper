package com.juanes.soccer.service;

import com.juanes.soccer.model.*;
import com.juanes.soccer.repository.CountryRepository;
import com.juanes.soccer.repository.LeagueRepository;
import com.juanes.soccer.repository.TeamRepository;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Optional;
import java.util.UUID;

@Service
public class TeamService {
    private final TeamRepository teamRepository;
    private final LeagueRepository leagueRepository;
    private final CountryRepository countryRepository;

    public TeamService(TeamRepository teamRepository, LeagueRepository leagueRepository, CountryRepository countryRepository) {
        this.teamRepository = teamRepository;
        this.leagueRepository = leagueRepository;
        this.countryRepository = countryRepository;

    }

    public Iterable<TeamRead> get() {
        ArrayList<TeamRead> teamReads = new ArrayList<>();
        teamRepository.findAll().forEach(team -> {
            TeamRead teamRead = new TeamRead();
            LeagueRead leagueRead = new LeagueRead();
            teamRead.setUuid(team.getUuid());
            teamRead.setName(team.getName());
            teamRead.setEmblem(team.getEmblem());
            League league = null;
            try {
                league = leagueRepository.findById(team.getLeagueUuid()).orElseThrow(() -> new Exception("Country not found"));
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
            Country country = null;
            try {
                country = countryRepository.findById(league.getCountryUuid()).orElseThrow(() -> new Exception("Country not found"));
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
            leagueRead.setUuid(league.getUuid());
            leagueRead.setName(league.getName());
            leagueRead.setCountry(country);
            teamRead.setLeagueRead(leagueRead);
            teamReads.add(teamRead);
        });
        return teamReads;
    }

    public Team save(String name, String uuid, byte[] emblem) {
        Team team = new Team();
        team.setName(name);
        team.setEmblem(emblem);
        team.setLeagueUuid(UUID.fromString(uuid));
        teamRepository.save(team);
        return team;
    }
}
