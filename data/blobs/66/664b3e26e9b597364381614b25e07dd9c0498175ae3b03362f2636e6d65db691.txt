package utils.arena;

import entities.Player;
import utils.attack.AttackingStrategy;
import utils.attack.SimpleAttackStrategy;
import utils.defend.DefendingStrategy;
import utils.defend.SimpleDefendStrategy;

import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * Represents a match between two players in an arena.
 */
public class Match {
    private static final Logger logger = Logger.getLogger(Match.class.getName());
    private final AttackingStrategy attackingStrategy;
    private final DefendingStrategy defendingStrategy;

    /**
     * Constructs a match with default attacking and defending strategies.
     */
    public Match() {
        this.attackingStrategy = new SimpleAttackStrategy();
        this.defendingStrategy = new SimpleDefendStrategy();
    }

    /**
     * Constructs a match with custom attacking and defending strategies.
     *
     * @param attackingStrategy the strategy used for attacking.
     * @param defendingStrategy the strategy used for defending.
     */
    public Match(AttackingStrategy attackingStrategy, DefendingStrategy defendingStrategy) {
        this.attackingStrategy = attackingStrategy;
        this.defendingStrategy = defendingStrategy;
    }

    /**
     * Simulates a fight between two players.
     *
     * @param p1 the first player.
     * @param p2 the second player.
     */
    public Player fight(Player p1, Player p2) {
        Player attackingPlayer, defendingPlayer;
        if (p1.getHealth() <= p2.getHealth()) {
            attackingPlayer = p1;
            defendingPlayer = p2;
        } else {
            attackingPlayer = p2;
            defendingPlayer = p1;
        }

        // Continue the fight until one player's health reaches 0
        // attacking and defending are swapped so last attacked player is the current attacking one
        // therefore checking health of attacking player only
        while (attackingPlayer.getHealth() != 0) {
            int attackedBy = attackingPlayer.attack(this.attackingStrategy);
            defendingPlayer.defend(attackedBy, this.defendingStrategy);
            Player temp = attackingPlayer;
            attackingPlayer = defendingPlayer;
            defendingPlayer = temp;
        }
        logger.log(Level.INFO, defendingPlayer + " wins the match");
        logger.log(Level.FINE, attackingPlayer + " looses the match");
        return defendingPlayer;
    }
}
