package boot.data.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import boot.data.dto.CommunityDto;
import boot.data.mapper.CommunityMapperInter;

@Service
public class CommunityService implements CommunityServiceInter {

    @Autowired
    CommunityMapperInter mapper;

    @Override
    public int getTotalCount() {
        return mapper.getTotalCount();
    }

    @Override
    public void insertCommunity(CommunityDto dto) {
        mapper.insertCommunity(dto);
    }

    @Override
    public List<CommunityDto> getAllDatas() {
        return mapper.getAllDatas();
    }

    @Override
    public CommunityDto getData(String com_num) {
        return mapper.getData(com_num);
    }

    @Override
    public void updateCommunity(CommunityDto dto) {
        mapper.updateCommunity(dto);
    }

    @Override
    public void deleteCommunity(String com_num) {
        mapper.deleteCommunity(com_num);
    }
}
