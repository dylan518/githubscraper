package com.hospital.erp.payment.reference;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.hospital.erp.payment.PaymentVO;

import lombok.extern.slf4j.Slf4j;

@Service
@Slf4j
public class ReferenceService {

	@Autowired
	private ReferenceDAO referenceDAO;
	
	//참조자 추가
	public int referenceInsert(PaymentVO referenceVO, String [] refMemCd, String [] refMemName)throws Exception{
		int result = 0;
		for(int i=0;i<refMemCd.length;i++) {
			ReferenceVO r = new ReferenceVO();
			r.setMemCd(refMemCd[i]);
			r.setMemName(refMemName[i]);
			r.setEpCd(referenceVO.getEpCd());
			result=referenceDAO.referenceInsert(r);
		}
			
		return result;
	};
	
	//해당문서의 참조자 보기
	public List<ReferenceVO> referenceList(PaymentVO paymentVO)throws Exception{
	
		return referenceDAO.referenceList(paymentVO);
	}

}
