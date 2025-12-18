package com.cl.food_app.service;



import java.util.List;
import java.util.Optional;



import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;


import com.cl.food_app.dao.StaffDAO;
import com.cl.food_app.dto.Admin;
import com.cl.food_app.dto.Staff;
import com.cl.food_app.exception.IdNotFoundException;
import com.cl.food_app.util.ASE;
import com.cl.food_app.util.ResponseStructure;



@Service
public class StaffService {



   @Autowired
   StaffDAO dao;



   public ResponseEntity<ResponseStructure<Staff>> saveStaff(Staff staff) {



       String passwordEncrypt = ASE.encrypt(staff.getPassword(), "pass");
       staff.setPassword(passwordEncrypt);
        
        ResponseStructure<Staff> structure = new ResponseStructure<Staff>();
        structure.setMessage("items saved sucessfully");
        structure.setStatus(HttpStatus.CREATED.value());
        structure.setT(dao.saveStaff(staff));
        return new ResponseEntity<ResponseStructure<Staff>>(structure, HttpStatus.CREATED);
    }



   public ResponseEntity<ResponseStructure<Staff>> updateStaff(Staff staff, int id) {
	   Staff staff2 = dao.updateStaff(staff, id);
        ResponseStructure<Staff> structure = new ResponseStructure<Staff>();



       if(staff2 != null) {
            structure.setMessage("items updated successfully");
            structure.setStatus(HttpStatus.OK.value());
            structure.setT(staff2);
            return  new ResponseEntity<ResponseStructure<Staff>>(structure, HttpStatus.OK);
        }
        else {
            structure.setMessage("Invalid Id");
            structure.setStatus(HttpStatus.NOT_FOUND.value());
            structure.setT(staff2);
            return  new ResponseEntity<ResponseStructure<Staff>>(structure, HttpStatus.NOT_FOUND);
        }
    }



   public ResponseEntity<ResponseStructure<Staff>> getStaffById(int id){
        Optional<Staff> optional = dao.getStaffById(id);
        if (optional.isEmpty()) {
            throw new IdNotFoundException();
        } else {
            ResponseStructure<Staff> structure = new ResponseStructure<Staff>();
            structure.setMessage("staff Found successfully");
            structure.setStatus(HttpStatus.OK.value());
            structure.setT(optional.get());
            return new ResponseEntity<ResponseStructure<Staff>>(structure, HttpStatus.OK);
        }
    }



   public ResponseEntity<ResponseStructure<List<Staff>>> findAllStaff() {
        ResponseStructure<List<Staff>> structure = new ResponseStructure<List<Staff>>();
        structure.setMessage("All staff details");
        structure.setStatus(HttpStatus.OK.value());
        structure.setT(dao.findAllStaff());
        return new ResponseEntity<ResponseStructure<List<Staff>>>(structure, HttpStatus.OK);
    }



   public ResponseEntity<ResponseStructure<Staff>> deleteStaff(int id) {
        ResponseStructure<Staff> structure = new ResponseStructure<Staff>();
        structure.setMessage("staff deleted successfully");
        structure.setStatus(HttpStatus.OK.value());
        structure.setT(dao.deleteStaff(id));
        return new ResponseEntity<ResponseStructure<Staff>>(structure, HttpStatus.OK);
    }
   public Staff findbyEmailnPassword(Staff staff) throws Exception {
	   String passwordEncrypt = ASE.encrypt(staff.getPassword(), "pass");
       staff.setPassword(passwordEncrypt);
	   String email=staff.getEmail();
	   String password=staff.getPassword();
       Staff obj=null;
       if(email!=null && password!=null) {
           obj= dao.findbyEmailnPassword(email,password);
       }
       if(obj==null) {
           throw new Exception("invalid");
       }
       return obj;
      
}
}