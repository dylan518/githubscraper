
package serviciocuentas.externalservices.web.corebanking.denarius;

import javax.xml.bind.JAXBElement;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElementRef;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;

import serviciocuentas.org.datacontract.schemas._2004._07.denariuscorebanking_web_externalservices.MSTransaccionRecibida;


/**
 * <p>Clase Java para anonymous complex type.
 * 
 * <p>El siguiente fragmento de esquema especifica el contenido que se espera que haya en esta clase.
 * 
 * <pre>
 * &lt;complexType&gt;
 *   &lt;complexContent&gt;
 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType"&gt;
 *       &lt;sequence&gt;
 *         &lt;element name="ConsultarDetalleTransaccionRecibidaResult" type="{http://schemas.datacontract.org/2004/07/DenariusCoreBanking.Web.ExternalServices.Cuentas}MSTransaccionRecibida" minOccurs="0"/&gt;
 *       &lt;/sequence&gt;
 *     &lt;/restriction&gt;
 *   &lt;/complexContent&gt;
 * &lt;/complexType&gt;
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {
    "consultarDetalleTransaccionRecibidaResult"
})
@XmlRootElement(name = "ConsultarDetalleTransaccionRecibidaResponse")
public class ConsultarDetalleTransaccionRecibidaResponse {

    @XmlElementRef(name = "ConsultarDetalleTransaccionRecibidaResult", namespace = "Denarius.CoreBanking.Web.ExternalServices", type = JAXBElement.class, required = false)
    protected JAXBElement<MSTransaccionRecibida> consultarDetalleTransaccionRecibidaResult;

    /**
     * Obtiene el valor de la propiedad consultarDetalleTransaccionRecibidaResult.
     * 
     * @return
     *     possible object is
     *     {@link JAXBElement }{@code <}{@link MSTransaccionRecibida }{@code >}
     *     
     */
    public JAXBElement<MSTransaccionRecibida> getConsultarDetalleTransaccionRecibidaResult() {
        return consultarDetalleTransaccionRecibidaResult;
    }

    /**
     * Define el valor de la propiedad consultarDetalleTransaccionRecibidaResult.
     * 
     * @param value
     *     allowed object is
     *     {@link JAXBElement }{@code <}{@link MSTransaccionRecibida }{@code >}
     *     
     */
    public void setConsultarDetalleTransaccionRecibidaResult(JAXBElement<MSTransaccionRecibida> value) {
        this.consultarDetalleTransaccionRecibidaResult = value;
    }

}
