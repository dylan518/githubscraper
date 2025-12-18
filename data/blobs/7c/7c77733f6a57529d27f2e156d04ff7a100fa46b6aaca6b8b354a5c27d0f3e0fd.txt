package com.example.CricketGame.service;

import com.example.CricketGame.models.Match;
import com.example.CricketGame.models.Team;
import com.example.CricketGame.repository.TeamRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class MatchService {
    @Autowired
    private TeamService teamService;
    @Autowired
    private InningsService inningsService;
    @Autowired
    private ResultService resultService;
    @Autowired
    private TeamRepository teamRepository;

    private static int counter=1;
    public void startMatch()
    {
        Team team1= teamService.createTeam1("India");
        Team team2=teamService.createTeam2("Australia");

        Match match=new Match(counter,"INDvsAUS",team1,team2);
         counter++;
        boolean toss;
        if(Math.random()<0.5)
            toss=true;
        else
            toss=false;
        if(toss==true)
        {
            team1=inningsService.startMatch(team1,team2,800,true);
            team2=inningsService.startMatch(team2, team1, team1.getRunsScored(), false);

        }
        else
        {
            team2=inningsService.startMatch(team2,team1,800,true);
            team1=inningsService.startMatch(team1,team2, team2.getRunsScored(), false);
        }
        teamRepository.save(team1);
        teamRepository.save(team2);
        resultService.getResult(team1,team2,match);

    }
}
