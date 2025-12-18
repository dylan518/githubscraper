package com.buli.buli_zone.BuLi;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import jakarta.transaction.Transactional;

@Component
public class BuLiService {

    private final BuLiRepository buLiRepository;

    @Autowired
    public BuLiService(BuLiRepository buLiRepository) {
        this.buLiRepository = buLiRepository;
    }

    public List<BuLi> getBuLiStats() {
        return buLiRepository.findAll();
    }

    public List<BuLi> getTeamByRank(Integer rank) {
        return buLiRepository.findAll().stream()
            .filter(buli -> buli.getRank() == rank)
            .collect(Collectors.toList());

    }

    public List<BuLi> getTeamByName(String name) {
        return buLiRepository.findAll().stream()
            .filter(buli -> buli.getName().equals(name))
            .collect(Collectors.toList());
    }

    public BuLi addTeam(BuLi team) {
        buLiRepository.save(team);
        return team;
    }

    public BuLi updateTeam(BuLi team) {
        Optional<BuLi> existingTeam = buLiRepository.findById(team.getId());

        if (existingTeam.isPresent()) {
            BuLi teamToUpdate = existingTeam.get();
            teamToUpdate.setId(team.getId());
            teamToUpdate.setRank(team.getRank());
            teamToUpdate.setName(team.getName());
            teamToUpdate.setMatches(team.getMatches());
            teamToUpdate.setWins(team.getWins());
            teamToUpdate.setDraws(team.getDraws());
            teamToUpdate.setLosses(team.getLosses());
            teamToUpdate.setPoints(team.getPoints());
            teamToUpdate.setGoals(team.getGoals());
            teamToUpdate.setDifference(team.getDifference());
            buLiRepository.save(teamToUpdate);
            return teamToUpdate;
        }
        return null;
    }

    @Transactional
    public void deleteTeamById(Integer id) {
        buLiRepository.deleteById(id);
    }

    @Transactional
    public void deleteTeamByName(String teamName) {
        buLiRepository.deleteByName(teamName);
    }
    
}
