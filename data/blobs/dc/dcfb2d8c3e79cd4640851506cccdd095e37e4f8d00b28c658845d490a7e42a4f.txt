package com.targetindia.audit.controller;

import com.targetindia.audit.service.FileScanService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
@RequestMapping("/api/files")
public class FileController {

    @Autowired
    private FileScanService fileScanService;

    @PostMapping("/upload")
    public ResponseEntity<String> uploadFile(@RequestParam("file") MultipartFile file) {
        boolean isMalicious = fileScanService.scanFile(file);
        return ResponseEntity.ok("File uploaded successfully. Is Malicious: " + isMalicious);
    }

    @GetMapping("/analysis/{id}")
    public ResponseEntity<Boolean> getScanResult(@PathVariable("id") String analysisId) {
        boolean isMalicious = fileScanService.getScanResultByAnalysisId(analysisId);
        return ResponseEntity.ok(isMalicious);
    }
}
