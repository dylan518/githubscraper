package com.ssy.test.util;

import java.io.File;
import java.nio.file.Path;
import java.util.UUID;

import javax.servlet.ServletContext;
import javax.sound.midi.Patch;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.web.multipart.MultipartFile;

import com.ssy.test.file.FileDTO;

@Component
public class FileManger {
	
	//다른 곳에서 파일 매니저 객체를 만들면 Annotion autowired 주입 불가능
	
	//@Autowired
	//private ServletContext servletContext;
	
	//**파일 매니저 객체가 필요할 때 
	
	//delete
	public boolean delteFile (ServletContext servletContext, String path, FileDTO fileDTO) throws Exception{
		String realPath = servletContext.getRealPath(path);
		System.out.println(realPath);
		
		File file = new File(realPath, fileDTO.getFileName());
		
		return file.delete();
	}
	
	
	
	//save
	//public void saveFile(ServletContext servletContext, String path)throws Exception{
	public String saveFile(ServletContext servletContext, String path, MultipartFile multipartFile) throws Exception{
		//1. 실제 경로
		String realPath = servletContext.getRealPath(path);
		System.out.println(realPath);
		
		//2. 폴더 체크
		File file = new File(realPath);
		if(!file.exists()) {
			file.mkdirs();
		}
		
		//3. 저장할 파일명 생성		
		String fileName = UUID.randomUUID().toString();
		fileName = fileName+"_"+multipartFile.getOriginalFilename();
		
		//4. HDD 저장
		file = new File(file, fileName);
		multipartFile.transferTo(file);
		
		return fileName;
	}

}
