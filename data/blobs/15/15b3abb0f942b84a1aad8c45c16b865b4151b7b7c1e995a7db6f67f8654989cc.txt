//
// 이 파일은 JAXB(JavaTM Architecture for XML Binding) 참조 구현 2.2.8-b130911.1802 버전을 통해 생성되었습니다. 
// <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a>를 참조하십시오. 
// 이 파일을 수정하면 소스 스키마를 재컴파일할 때 수정 사항이 손실됩니다. 
// 생성 날짜: 2023.08.18 시간 09:33:12 AM KST 
//


package org.mitre.oval.xmlschema.oval_definitions_5_aix;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlType;
import org.mitre.oval.xmlschema.oval_definitions_5.EntityStateStringType;
import org.mitre.oval.xmlschema.oval_definitions_5.StateType;


/**
 * <p>anonymous complex type에 대한 Java 클래스입니다.
 * 
 * <p>다음 스키마 단편이 이 클래스에 포함되는 필요한 콘텐츠를 지정합니다.
 * 
 * <pre>
 * &lt;complexType>
 *   &lt;complexContent>
 *     &lt;extension base="{http://oval.mitre.org/XMLSchema/oval-definitions-5}StateType">
 *       &lt;sequence>
 *         &lt;element name="vuid" type="{http://oval.mitre.org/XMLSchema/oval-definitions-5}EntityStateStringType" minOccurs="0"/>
 *         &lt;element name="label" type="{http://oval.mitre.org/XMLSchema/oval-definitions-5}EntityStateStringType" minOccurs="0"/>
 *         &lt;element name="abstract" type="{http://oval.mitre.org/XMLSchema/oval-definitions-5}EntityStateStringType" minOccurs="0"/>
 *         &lt;element name="state" type="{http://oval.mitre.org/XMLSchema/oval-definitions-5#aix}EntityStateInterimFixStateType" minOccurs="0"/>
 *       &lt;/sequence>
 *     &lt;/extension>
 *   &lt;/complexContent>
 * &lt;/complexType>
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {
    "vuid",
    "label",
    "_abstract",
    "state"
})
public class InterimFixState
    extends StateType
{

    protected EntityStateStringType vuid;
    protected EntityStateStringType label;
    @XmlElement(name = "abstract")
    protected EntityStateStringType _abstract;
    protected EntityStateInterimFixStateType state;

    /**
     * vuid 속성의 값을 가져옵니다.
     * 
     * @return
     *     possible object is
     *     {@link EntityStateStringType }
     *     
     */
    public EntityStateStringType getVuid() {
        return vuid;
    }

    /**
     * vuid 속성의 값을 설정합니다.
     * 
     * @param value
     *     allowed object is
     *     {@link EntityStateStringType }
     *     
     */
    public void setVuid(EntityStateStringType value) {
        this.vuid = value;
    }

    /**
     * label 속성의 값을 가져옵니다.
     * 
     * @return
     *     possible object is
     *     {@link EntityStateStringType }
     *     
     */
    public EntityStateStringType getLabel() {
        return label;
    }

    /**
     * label 속성의 값을 설정합니다.
     * 
     * @param value
     *     allowed object is
     *     {@link EntityStateStringType }
     *     
     */
    public void setLabel(EntityStateStringType value) {
        this.label = value;
    }

    /**
     * abstract 속성의 값을 가져옵니다.
     * 
     * @return
     *     possible object is
     *     {@link EntityStateStringType }
     *     
     */
    public EntityStateStringType getAbstract() {
        return _abstract;
    }

    /**
     * abstract 속성의 값을 설정합니다.
     * 
     * @param value
     *     allowed object is
     *     {@link EntityStateStringType }
     *     
     */
    public void setAbstract(EntityStateStringType value) {
        this._abstract = value;
    }

    /**
     * state 속성의 값을 가져옵니다.
     * 
     * @return
     *     possible object is
     *     {@link EntityStateInterimFixStateType }
     *     
     */
    public EntityStateInterimFixStateType getState() {
        return state;
    }

    /**
     * state 속성의 값을 설정합니다.
     * 
     * @param value
     *     allowed object is
     *     {@link EntityStateInterimFixStateType }
     *     
     */
    public void setState(EntityStateInterimFixStateType value) {
        this.state = value;
    }

}
