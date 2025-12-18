package com.mall.service.impl;

import com.mall.entity.po.Transfee;
import com.mall.mapper.TransfeeMapper;
import com.mall.service.TransfeeService;
import com.mall.entity.query.TransfeeQuery;
import com.mall.entity.vo.PaginationResultVo;
import com.mall.enums.PageSize;
import com.mall.entity.query.SimplePage;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 *  @Description: TransfeeServiceImpl
 *  @Author: wow
 *  @Date: 2024年06月17日
 */
@Service("transfeeServiceImpl")
public class TransfeeServiceImpl implements TransfeeService {
	@Autowired
	private TransfeeMapper<Transfee, TransfeeQuery> transfeeMapper;

	/**
	 * 根据条件查询列表
	 */
	@Override
	public List<Transfee> selectListByCondition(TransfeeQuery transfeeQuery) {
		return transfeeMapper.selectList(transfeeQuery);
	}
	/**
	 * 根据条件查询数量
	 */
	@Override
	public Long selectCount(TransfeeQuery transfeeQuery) {
		return transfeeMapper.selectCount(transfeeQuery);
	}

	/**
	 * 分页查询
	 */
	@Override
	public PaginationResultVo<Transfee> selectList(TransfeeQuery transfeeQuery) {
		int count = Math.toIntExact(this.selectCount(transfeeQuery));
		int pageSize = transfeeQuery.getPageSize() == null ? PageSize.PAGE_SIZE20.getSize() : transfeeQuery.getPageSize();
		SimplePage simplePage = new SimplePage(transfeeQuery.getPageNo(), count, pageSize);
		transfeeQuery.setSimplePage(simplePage);
		List<Transfee> transfee = this.selectListByCondition(transfeeQuery);
		return new PaginationResultVo<Transfee>(count, simplePage.getPageSize(), simplePage.getPageNo(), simplePage.getPageTotal(), transfee);
	}
	/**
	 * 新增
	 */
	@Override
	public Integer insert(Transfee transfee) {
		return transfeeMapper.insert(transfee);
	}

	/**
	 * 批量新增
	 */
	@Override
	public Integer insertBatch(List<Transfee> transfeeList) {
		return transfeeMapper.insertBatch(transfeeList);
	}

	/**
	 * 批量新增或修改
	 */
	@Override
	public Integer insertOrUpdateBatch(List<Transfee> transfeeList) {
		return transfeeMapper.insertBatch(transfeeList);
	}

	/**
	 * 根据TransfeeId查询
	 */
	@Override
	public Transfee selectByTransfeeId(Long transfeeId) {
		return transfeeMapper.selectByTransfeeId(transfeeId);
	}

	/**
	 * 根据TransfeeId更新
	 */
	@Override
	public Integer updateByTransfeeId(Transfee transfee, Long transfeeId) {
		return transfeeMapper.updateByTransfeeId(transfee, transfeeId);
	}

	/**
	 * 根据TransfeeId删除
	 */
	@Override
	public Integer deleteByTransfeeId(Long transfeeId) {
		return transfeeMapper.deleteByTransfeeId(transfeeId);
	}
}