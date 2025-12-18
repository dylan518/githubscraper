package ec.com.todocompu.ShrimpSoftUtils.inventario.entity;

import java.io.Serializable;
import java.util.Date;
import java.util.List;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.EmbeddedId;
import javax.persistence.Entity;
import javax.persistence.JoinColumn;
import javax.persistence.JoinColumns;
import javax.persistence.ManyToOne;
import javax.persistence.OneToMany;
import javax.persistence.Table;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;

@Entity
@Table(name = "inv_transferencias", schema = "inventario")
public class InvTransferencias implements Serializable {

    private static final long serialVersionUID = 1L;

    @EmbeddedId
    protected InvTransferenciasPK invTransferenciasPK;
    @Column(name = "trans_fecha")
    @Temporal(TemporalType.DATE)
    private Date transFecha;
    @Column(name = "trans_observaciones")
    private String transObservaciones;
    @Column(name = "trans_pendiente")
    private boolean transPendiente;
    @Column(name = "trans_revisado")
    private boolean transRevisado;
    @Column(name = "trans_anulado")
    private boolean transAnulado;
    @Column(name = "usr_empresa")
    private String usrEmpresa;
    @Column(name = "usr_codigo")
    private String usrCodigo;
    @Column(name = "usr_fecha_inserta", insertable = false, updatable = false)
    @Temporal(TemporalType.TIMESTAMP)
    private Date usrFechaInserta;
    @JoinColumns({
        @JoinColumn(name = "bod_origen_empresa", referencedColumnName = "bod_empresa")
        ,
			@JoinColumn(name = "bod_origen_codigo", referencedColumnName = "bod_codigo")})
    @ManyToOne
    private InvBodega invBodega;
    @JoinColumns({
        @JoinColumn(name = "bod_destino_empresa", referencedColumnName = "bod_empresa")
        ,
			@JoinColumn(name = "bod_destino_codigo", referencedColumnName = "bod_codigo")})
    @ManyToOne
    private InvBodega invBodega1;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "invTransferencias")
    private List<InvTransferenciasDetalle> invTransferenciasDetalleList;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "invTransferencias")
    private List<InvTransferenciasMotivoAnulacion> invTransferenciasMotivoAnulacionList;

    public InvTransferencias() {
    }

    public InvTransferencias(InvTransferenciasPK invTransferenciasPK) {
        this.invTransferenciasPK = invTransferenciasPK;
    }

    public InvTransferencias(InvTransferenciasPK invTransferenciasPK, Date transFecha, boolean transPendiente,
            boolean transRevisado, boolean transAnulado, String usrEmpresa, String usrCodigo, Date usrFechaInserta) {
        this.invTransferenciasPK = invTransferenciasPK;
        this.transFecha = transFecha;
        this.transPendiente = transPendiente;
        this.transRevisado = transRevisado;
        this.transAnulado = transAnulado;
        this.usrEmpresa = usrEmpresa;
        this.usrCodigo = usrCodigo;
        this.usrFechaInserta = usrFechaInserta;
    }

    public InvTransferencias(String transEmpresa, String transPeriodo, String transMotivo, String transNumero) {
        this.invTransferenciasPK = new InvTransferenciasPK(transEmpresa, transPeriodo, transMotivo, transNumero);
    }

    public InvTransferenciasPK getInvTransferenciasPK() {
        return invTransferenciasPK;
    }

    public void setInvTransferenciasPK(InvTransferenciasPK invTransferenciasPK) {
        this.invTransferenciasPK = invTransferenciasPK;
    }

    public Date getTransFecha() {
        return transFecha;
    }

    public void setTransFecha(Date transFecha) {
        this.transFecha = transFecha;
    }

    public String getTransObservaciones() {
        return transObservaciones;
    }

    public void setTransObservaciones(String transObservaciones) {
        this.transObservaciones = transObservaciones;
    }

    public boolean getTransPendiente() {
        return transPendiente;
    }

    public void setTransPendiente(boolean transPendiente) {
        this.transPendiente = transPendiente;
    }

    public boolean getTransRevisado() {
        return transRevisado;
    }

    public void setTransRevisado(boolean transRevisado) {
        this.transRevisado = transRevisado;
    }

    public boolean getTransAnulado() {
        return transAnulado;
    }

    public void setTransAnulado(boolean transAnulado) {
        this.transAnulado = transAnulado;
    }

    public String getUsrEmpresa() {
        return usrEmpresa;
    }

    public void setUsrEmpresa(String usrEmpresa) {
        this.usrEmpresa = usrEmpresa;
    }

    public String getUsrCodigo() {
        return usrCodigo;
    }

    public void setUsrCodigo(String usrCodigo) {
        this.usrCodigo = usrCodigo;
    }

    public Date getUsrFechaInserta() {
        return usrFechaInserta;
    }

    public void setUsrFechaInserta(Date usrFechaInserta) {
        this.usrFechaInserta = usrFechaInserta;
    }

    public InvBodega getInvBodega() {
        return invBodega;
    }

    public void setInvBodega(InvBodega invBodega) {
        this.invBodega = invBodega;
    }

    public InvBodega getInvBodega1() {
        return invBodega1;
    }

    public void setInvBodega1(InvBodega invBodega1) {
        this.invBodega1 = invBodega1;
    }

    public List<InvTransferenciasDetalle> getInvTransferenciasDetalleList() {
        return invTransferenciasDetalleList;
    }

    public void setInvTransferenciasDetalleList(List<InvTransferenciasDetalle> invTransferenciasDetalleList) {
        this.invTransferenciasDetalleList = invTransferenciasDetalleList;
    }

    public List<InvTransferenciasMotivoAnulacion> getInvTransferenciasMotivoAnulacionList() {
        return invTransferenciasMotivoAnulacionList;
    }

    public void setInvTransferenciasMotivoAnulacionList(
            List<InvTransferenciasMotivoAnulacion> invTransferenciasMotivoAnulacionList) {
        this.invTransferenciasMotivoAnulacionList = invTransferenciasMotivoAnulacionList;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (invTransferenciasPK != null ? invTransferenciasPK.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {

        if (!(object instanceof InvTransferencias)) {
            return false;
        }
        InvTransferencias other = (InvTransferencias) object;
        if ((this.invTransferenciasPK == null && other.invTransferenciasPK != null)
                || (this.invTransferenciasPK != null && !this.invTransferenciasPK.equals(other.invTransferenciasPK))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "inventario.entity.InvTransferencias[ invTransferenciasPK=" + invTransferenciasPK + " ]";
    }

}
