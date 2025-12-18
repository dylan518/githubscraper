package lab2.src.myattack.Gloom;
import ru.ifmo.se.pokemon.*;

public class SludgeBomb  extends SpecialMove{
    public SludgeBomb (double pow, double acc){
        super(Type.POISON, pow, acc);
    }
    @Override
    protected void applyOppDamage(Pokemon p){
        super.applyOppDamage(p);
        Effect EffectObj = new Effect().chance(0.3);
        EffectObj.poison(p);
        
    }
    @Override
    protected String describe(){
        return "Отравляет оппонента!";
    }
}