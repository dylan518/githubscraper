package vn.edu.hcmuaf.fit.dacn_booking_health_api.service.appointment;

import jakarta.mail.MessagingException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.util.ObjectUtils;
import vn.edu.hcmuaf.fit.dacn_booking_health_api.dto.appointment.AppointmentDto;
import vn.edu.hcmuaf.fit.dacn_booking_health_api.dto.symptom.SymptomDto;
import vn.edu.hcmuaf.fit.dacn_booking_health_api.entity.Appointment;
import vn.edu.hcmuaf.fit.dacn_booking_health_api.entity.Schedule;
import vn.edu.hcmuaf.fit.dacn_booking_health_api.entity.Symptom;
import vn.edu.hcmuaf.fit.dacn_booking_health_api.exception.BadRequestException;
import vn.edu.hcmuaf.fit.dacn_booking_health_api.mapper.AppointmentMapper;
import vn.edu.hcmuaf.fit.dacn_booking_health_api.repository.appointment.AppointmentRepository;
import vn.edu.hcmuaf.fit.dacn_booking_health_api.repository.schedule.ScheduleRepository;
import vn.edu.hcmuaf.fit.dacn_booking_health_api.repository.symptom.SymptomRepository;
import vn.edu.hcmuaf.fit.dacn_booking_health_api.service.app_mail.AppMailService;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

@Service
@Transactional
public class AppointmentServiceImpl implements AppointmentService {
    private final AppointmentRepository appointmentRepository;
    private final ScheduleRepository scheduleRepository;
    private final SymptomRepository symptomRepository;
    private final AppointmentMapper appointmentMapper;
    private final AppMailService appMailService;

    @Autowired
    public AppointmentServiceImpl(AppointmentRepository appointmentRepository, ScheduleRepository scheduleRepository,
                                  SymptomRepository symptomRepository, AppointmentMapper appointmentMapper, AppMailService appMailService) {
        this.appointmentRepository = appointmentRepository;
        this.scheduleRepository = scheduleRepository;
        this.symptomRepository = symptomRepository;

        this.appointmentMapper = appointmentMapper;

        this.appMailService = appMailService;
    }

    @Override
    public AppointmentDto createAppointment(AppointmentDto appointmentDto) throws BadRequestException, MessagingException, IOException {
        Schedule schedule = scheduleRepository
                .findById(appointmentDto.getSchedule().getId()).orElse(null);
        if (ObjectUtils.isEmpty(schedule)) throw new BadRequestException("Không tìm thấy lịch khám");

        if (schedule.getIsFull()) throw new BadRequestException("Lịch khám đã đầy");

        List<Long> ids = appointmentDto.getSymptoms().stream().map(SymptomDto::getId).toList();
        List<Symptom> symptoms = new ArrayList<>(symptomRepository.findAllById(ids));

        Appointment appointment = appointmentMapper.toAppointmentEntity(appointmentDto);
        schedule.setCurrentPatient(schedule.getCurrentPatient() + 1);
        if (Objects.equals(schedule.getCurrentPatient(), schedule.getMaxPatient())) {
            schedule.setIsFull(true);
        }
        appointment.setSchedule(schedule);
        appointment.setSymptoms(symptoms);

        Appointment newAppointment = appointmentRepository.save(appointment);
        if (ObjectUtils.isEmpty(newAppointment)) throw new BadRequestException("Can't create appointment");

        appMailService.sendAppointmentEmail(newAppointment);

        return appointmentMapper.toAppointmentDto(newAppointment);
    }

    @Override
    public AppointmentDto getAppointment(Long id) throws BadRequestException {
        AppointmentDto appointmentDto = appointmentMapper.toAppointmentDto(appointmentRepository.findById(id).orElse(null));

        if (ObjectUtils.isEmpty(appointmentDto)) throw new BadRequestException("Không tìm thấy lịch khám");
        return appointmentDto;
    }
}
