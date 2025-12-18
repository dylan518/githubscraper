package cl.praxis.ReportesInmobiliaria.model.service;

import cl.praxis.ReportesInmobiliaria.model.dto.Reporte;
import cl.praxis.ReportesInmobiliaria.model.repository.ReporteRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ReporteService {
    private ReporteRepository reporteRepository;

    public ReporteService(ReporteRepository reporteRepository) {
        this.reporteRepository = reporteRepository;
    }

    public List<Reporte> findAll() {
        return reporteRepository.findAll();
    }

    public Reporte findById(int id) {
        return reporteRepository.findById(id);
    }

    public boolean save(Reporte reporte) {
        try {
            reporteRepository.save(reporte);
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    public void delete(int id) {
        reporteRepository.deleteById(id);
    }

    public boolean update(Reporte reporte) {
        try {
            Reporte toUpdate = reporteRepository.findById(reporte.getId());
            toUpdate.setNombre(reporte.getNombre());
            reporteRepository.save(toUpdate);
            return true;
        } catch (Exception e) {
            return false;
        }
    }
}
