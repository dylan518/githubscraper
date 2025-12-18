
package lt.viko.eif.esemasko.soap;

import jakarta.xml.bind.annotation.*;


/**
 * <p>Java class for genre complex type.
 *
 * <p>The following schema fragment specifies the expected content contained within this class.
 *
 * <pre>
 * &lt;complexType name="genre">
 *   &lt;complexContent>
 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *       &lt;sequence>
 *         &lt;element name="id" type="{http://www.w3.org/2001/XMLSchema}byte"/>
 *         &lt;element name="category" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *       &lt;/sequence>
 *     &lt;/restriction>
 *   &lt;/complexContent>
 * &lt;/complexType>
 * </pre>
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "genre", propOrder = {
        "id",
        "category"
})
public class Genre {

    protected byte id;
    @XmlElement(required = true)
    protected String category;

    /**
     * Gets the value of the id property.
     */
    public byte getId() {
        return id;
    }

    /**
     * Sets the value of the id property.
     */
    public void setId(byte value) {
        this.id = value;
    }

    /**
     * Gets the value of the category property.
     *
     * @return possible object is
     * {@link String }
     */
    public String getCategory() {
        return category;
    }

    /**
     * Sets the value of the category property.
     *
     * @param value allowed object is
     *              {@link String }
     */
    public void setCategory(String value) {
        this.category = value;
    }

}
