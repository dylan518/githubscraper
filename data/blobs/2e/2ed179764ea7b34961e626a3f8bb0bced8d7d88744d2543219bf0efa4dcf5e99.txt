package org.example.model;

import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;
import org.example.model.attractionaccessibilityattributes.*;


@Entity
@Table(name="attractionaccessibility")
public class AttractionAccessibility {

    @Id
    @Column
    @GeneratedValue(strategy=GenerationType.IDENTITY)
    private Long id;

    @Embedded
    @AttributeOverrides({
            @AttributeOverride(name = "mayRemainInWheelchairEcv", column = @Column(name = "may_remain_in_wheelchair_ecv")),
            @AttributeOverride(name = "mustBeAmbulatory", column = @Column(name = "must_be_ambulatory")),
            @AttributeOverride(name = "mustTransferFromWheelchairEcv", column = @Column(name = "must_transfer_from_wheelchair_ecv")),
            @AttributeOverride(name = "mustTransferToWheelchair", column = @Column(name = "must_transfer_to_wheelchair")),
            @AttributeOverride(name = "mustTransferToWheelchairThenToRide", column = @Column(name = "must_transfer_to_wheelchair_then_to_ride"))
    })
    private MustTransfer mustTransfer;


    @Embedded
    @AttributeOverrides({
            @AttributeOverride(name = "loadUnloadAreas", column = @Column(name = "load-unload-areas")),
            @AttributeOverride(name = "wheelchairAccessVehicles", column = @Column(name = "wheelchair-access-vehicles")),
            @AttributeOverride(name = "transferAccessVehicle", column = @Column(name = "transfer-access-vehicle")),
            @AttributeOverride(name = "transferDevices", column = @Column(name = "transfer-devices"))
    })
    private TransferAssistance transferAssistance;

    @Embedded
    @AttributeOverrides({
            @AttributeOverride(name = "rideRestrictions", column = @Column(name = "ride-restrictions")),
            @AttributeOverride(name = "boardRestrictions", column = @Column(name = "board-restrictions"))
    })
    private ServiceAnimalRestrictions serviceAnimalRestrictions;

    @Embedded
    @AttributeOverrides({
            @AttributeOverride(name = "assistiveListening", column = @Column(name = "assistive-listening")),
            @AttributeOverride(name = "audioDescription", column = @Column(name = "audio-description")),
            @AttributeOverride(name = "handheldCaptioning", column = @Column(name = "handheld-captioning")),
            @AttributeOverride(name = "signLanguage", column = @Column(name = "sign-language")),
            @AttributeOverride(name = "videoCaptioning", column = @Column(name = "video-captioning"))
    })
    private AssistiveDevices assistiveDevices;

    @Embedded
    @AttributeOverrides({
            @AttributeOverride(name = "scentSmell", column = @Column(name = "scent_smell")),
            @AttributeOverride(name = "lightingEffects", column = @Column(name = "lighting_effects")),
            @AttributeOverride(name = "loudNoises", column = @Column(name = "loud_noises")),
            @AttributeOverride(name = "periodsOfDarkness", column = @Column(name = "periods_of_darkness")),
            @AttributeOverride(name = "bumpy", column = @Column(name = "bumpy")),
            @AttributeOverride(name = "fast", column = @Column(name = "fast")),
            @AttributeOverride(name = "liftsOffGround", column = @Column(name = "lifts_off_ground")),
            @AttributeOverride(name = "wet", column = @Column(name = "wet")),
            @AttributeOverride(name = "elementOfSurprise", column = @Column(name = "element_of_surprise")),
            @AttributeOverride(name = "typeOfRestraint", column = @Column(name = "type_of_restraint")),
            @AttributeOverride(name = "tripTime", column = @Column(name = "trip_time"))
    })
    private SensoryExperience sensoryExperience;

    // This links the table representing the AttractionAccessibility model to the table representing the Attraction model
    @JsonIgnore // This prevents a stack overflow from Attractions and AttractionAccessibility calling each other back and forth
    @OneToOne(optional = false) // This means that a AttractionAccessibility record must always be associated with an Attraction record. An Attraction can exist without AttractionAccessibility, but every AttractionAccessibility must have a corresponding Attraction.
    @JoinColumn(name = "attraction_id") // This means that the AttractionAccessibility entity will have a foreign key column named attraction_id referring to the primary attribute id of our Attraction entity. This foreign key in SQL joins the columns to connect the 2 tables
    private Attraction attraction;


    public AttractionAccessibility() {
    }


    public AttractionAccessibility(Long id, MustTransfer mustTransfer, TransferAssistance transferAssistance, ServiceAnimalRestrictions serviceAnimalRestrictions, AssistiveDevices assistiveDevices, SensoryExperience sensoryExperience, Attraction attraction) {
        this.id = id;
        this.mustTransfer = mustTransfer;
        this.transferAssistance = transferAssistance;
        this.serviceAnimalRestrictions = serviceAnimalRestrictions;
        this.assistiveDevices = assistiveDevices;
        this.sensoryExperience = sensoryExperience;
        this.attraction = attraction;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public MustTransfer getMustTransfer() {
        return mustTransfer;
    }

    public void setMustTransfer(MustTransfer mustTransfer) {
        this.mustTransfer = mustTransfer;
    }

    public TransferAssistance getTransferAssistance() {
        return transferAssistance;
    }

    public void setTransferAssistance(TransferAssistance transferAssistance) {
        this.transferAssistance = transferAssistance;
    }

    public ServiceAnimalRestrictions getServiceAnimalRestrictions() {
        return serviceAnimalRestrictions;
    }

    public void setServiceAnimalRestrictions(ServiceAnimalRestrictions serviceAnimalRestrictions) {
        this.serviceAnimalRestrictions = serviceAnimalRestrictions;
    }

    public AssistiveDevices getAssistiveDevices() {
        return assistiveDevices;
    }

    public void setAssistiveDevices(AssistiveDevices assistiveDevices) {
        this.assistiveDevices = assistiveDevices;
    }

    public SensoryExperience getSensoryExperience() {
        return sensoryExperience;
    }

    public void setSensoryExperience(SensoryExperience sensoryExperience) {
        this.sensoryExperience = sensoryExperience;
    }

    public Attraction getAttraction() {
        return attraction;
    }

    public void setAttraction(Attraction attraction) {
        this.attraction = attraction;
    }


    @Override
    public String toString() {
        return "AttractionAccessibility{" +
                "id=" + id +
                ", mustTransfer=" + mustTransfer +
                ", transferAssistance=" + transferAssistance +
                ", serviceAnimalRestrictions=" + serviceAnimalRestrictions +
                ", assistiveDevices=" + assistiveDevices +
                ", sensoryExperience=" + sensoryExperience +
                ", attraction=" + attraction +
                '}';
    }
}
