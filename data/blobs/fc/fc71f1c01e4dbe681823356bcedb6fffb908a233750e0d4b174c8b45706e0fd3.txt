package com.xworkz.engineer.repository;

import java.util.Iterator;

import com.xworkz.engineer.dto.EngineerDTO;

public class EngineerRepositoryImpl implements EngineerRepository {
	EngineerDTO[] dto = new EngineerDTO[TOTAL_ENGINEERS];
	int position;

	@Override
	public void save(EngineerDTO dto) {
		System.out.println("running save in " + this.getClass().getSimpleName());
		if (this.position < TOTAL_ENGINEERS) {
			this.dto[position] = dto;
			System.out.println(dto + "is saved at position" + this.position);
			this.position++;
		} else {
			System.err.println("storage is full cannot store the data" + dto);
		}

	}

	@Override
	public boolean isExist(EngineerDTO dto) {
		System.out.println("running isExist in " + this.getClass().getSimpleName());
		for (int index = 0; index <= this.position; index++) {
			EngineerDTO ref = this.dto[index];
			if (ref != null && ref.equals(dto)) {
				System.out.println("dto already exist");
				return true;
			}
		}

		return EngineerRepository.super.isExist(dto);
	}

	@Override
	public EngineerDTO findName(String name) {
		for (int index = 0; index < position; index++) {
			EngineerDTO ref = dto[index];
			if (ref.getName().equals(name)) {
				return ref;
			} else {
				System.err.println("it is not found");
			}

		}
		return null;
	}
}
