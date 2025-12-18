package io.keepcoding.keeptrivial.model;

import java.util.ArrayList;

public class GameState {
	private ArrayList<Team> teamList;
	private Team winnerTeam;

	public GameState(ArrayList<Team> teamList) {
		this.teamList = teamList;
	}
	
	public ArrayList<Team> getTeamList() {
		return teamList;
	}

	public Team getWinnerTeam() {
		return winnerTeam;
	}
	
	public boolean checkWinner() {
		for (var team: teamList) {
			if (team.isWinner()) {
				winnerTeam = team;
				return true;
			}
		}
		return false;
	}

}
