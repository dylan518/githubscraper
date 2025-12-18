package QMS.Builders;

import QMS.Application.Application;
import QMS.Booth;
import QMS.FactoryProducer;

public class OptimalBuilder implements IBuilder {
    private String connectionType;
    private int numberOfDisplayUnits;
    private Booth product;


    public OptimalBuilder(String connectionType, int numberOfDisplayUnits) {
        this.connectionType = connectionType;
        this.numberOfDisplayUnits = numberOfDisplayUnits;
        product = new Booth();
    }

    @Override
    public void AddController() {
        product.addPart(FactoryProducer.getFactory("controller").getController("arduino"));
    }

    @Override
    public void AddDisplayUnit() {
        for (int i = 0; i < numberOfDisplayUnits; ++i){
            product.addPart(FactoryProducer.getFactory("display").getDisplayUnit("led"));
        }
    }

    @Override
    public void CreateApplication() {
        product.addPart(new Application());
    }

    @Override
    public void AddCommunicationSystem() {
        product.addPart(FactoryProducer.getFactory("communication").getCommunicationSystem(connectionType));
    }

    public void setYearlyCost() {
        product.setYearlyCost(100);
    }
    @Override
    public Booth getProduct() {
        return product;
    }
}
