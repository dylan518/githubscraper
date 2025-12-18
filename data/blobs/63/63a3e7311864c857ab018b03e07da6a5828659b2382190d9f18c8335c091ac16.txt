package com.koperasiKSP.rest;

import com.koperasiKSP.dto.transaksi.InsertTransaksiDTO;
import com.koperasiKSP.dto.transaksi.TransaksiDTO;
import com.koperasiKSP.dto.transaksi.UpdateTransaksiDTO;
import com.koperasiKSP.service.TransaksiService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;

@RestController
@RequestMapping("/transaksi")
public class TransaksiController {

    @Autowired
    private TransaksiService transaksiService;

    @PostMapping
    public ResponseEntity<String> insert(@Valid @RequestBody InsertTransaksiDTO dto){
        transaksiService.insert(dto);
        return new ResponseEntity<>("Transaksi berhasil dibuat!", HttpStatus.CREATED);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<String> delete(@PathVariable Long id){
        try{
            transaksiService.deleteById(id);
            return new ResponseEntity<>("Transaksi dengan ID: " + id + " berhasil dihapus", HttpStatus.ACCEPTED);
        } catch (Exception ex){
            return new ResponseEntity<>("Transaksi tidak ditemukan", HttpStatus.NOT_FOUND);
        }
    }

    @PutMapping("/{id}")
    public ResponseEntity<String> update(@Valid @RequestBody UpdateTransaksiDTO dto,
                                         @PathVariable Long id){
        transaksiService.update(id, dto);
        return new ResponseEntity<>("Transaksi dengan ID: " + id + " berhasil diupdate", HttpStatus.ACCEPTED);
    }

    @GetMapping
    public ResponseEntity<Page<TransaksiDTO>> index(@RequestParam(defaultValue = "1") int page,
                                                    @RequestParam(defaultValue = "") String nama,
                                                    @RequestParam(defaultValue = "") String username){

        Page<TransaksiDTO> transaksiDTOPage = transaksiService.transaksiPages(nama, username, page);
        return new ResponseEntity<>(transaksiDTOPage, HttpStatus.OK);
    }
}
