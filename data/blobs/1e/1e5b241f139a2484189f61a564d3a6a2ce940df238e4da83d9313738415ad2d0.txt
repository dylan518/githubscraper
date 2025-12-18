package com.jnv.ast.resources.service.impl;

import static com.jnv.common.util.Constants.RESULT_FAILURE;
import static com.jnv.common.util.Constants.RESULT_SUCCESS;

import java.util.List;
import java.util.Map;

import javax.annotation.Resource;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.jnv.ast.resources.service.ResourcesRqstListDAO;
import com.jnv.ast.resources.service.ResourcesRqstListService;
import com.jnv.ast.vo.ResourcesRqstListVO;
import com.jnv.common.seq.service.IdGeneratorService;

@Service("resourcesRqstListService")
@Transactional
public class ResourcesListServiceImpl implements ResourcesRqstListService {

    @Resource(name = "resourcesRqstListDAO")
    private ResourcesRqstListDAO dao;

    @Resource(name = "idGeneratorService")
    private IdGeneratorService idGen;

    @Override
    public List<ResourcesRqstListVO> getAstRqst(Map<String, Object> searchMap) {
        return dao.getAstRqst(searchMap);
    }

    @Override
    public String getAstRqstApply(List<ResourcesRqstListVO> resDetailList) {
        String rmsg = RESULT_FAILURE;
        String astRqstId = idGen.nextIdFor("astRqstId");

        for (ResourcesRqstListVO vo : resDetailList) {
            if ("1".equals(vo.getRowCheck())) {
                vo.setAstRqstId(astRqstId);
                dao.getAstRqstApply(vo);
            }
            rmsg = RESULT_SUCCESS;
        }
        return rmsg;
    }
}
