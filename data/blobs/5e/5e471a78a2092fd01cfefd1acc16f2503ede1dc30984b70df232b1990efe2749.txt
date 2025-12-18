package com.example.backend7team.domain.accident.domain.repository;

import com.example.backend7team.domain.accident.domain.Accident;
import com.example.backend7team.domain.accident.domain.AccidentInformation;
import com.example.backend7team.domain.accident.domain.repository.enums.SortType;
import com.example.backend7team.domain.accident.domain.repository.vo.QQueryAccidentInformationVO;
import com.example.backend7team.domain.accident.domain.repository.vo.QQueryAccidentVO;
import com.example.backend7team.domain.accident.domain.repository.vo.QueryAccidentInformationVO;
import com.example.backend7team.domain.accident.domain.repository.vo.QueryAccidentVO;
import com.querydsl.core.types.Order;
import com.querydsl.core.types.OrderSpecifier;
import com.querydsl.core.types.dsl.BooleanExpression;
import com.querydsl.jpa.impl.JPAQueryFactory;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

import static com.example.backend7team.domain.accident.domain.QAccident.accident;
import static com.example.backend7team.domain.accident.domain.QAccidentInformation.accidentInformation;
import static com.example.backend7team.domain.likes.domain.QLikes.likes;
import static com.example.backend7team.domain.user.domain.QUser.user;

@RequiredArgsConstructor
@Repository
public class AccidentRepository {

    private final AccidentInformationJpaRepository accidentInformationJpaRepository;
    private final AccidentJpaRepository accidentJpaRepository;
    private final JPAQueryFactory queryFactory;

    public void saveAccident(Accident accident) {
        accidentJpaRepository.save(accident);
    }

    public void saveAccidentInformation(AccidentInformation accidentInformation) {
        accidentInformationJpaRepository.save(accidentInformation);
    }

    public Optional<Accident> queryAccidentById(Long id) {
        return accidentJpaRepository.findById(id);
    }

    public Optional<AccidentInformation> queryAccidentInformationById(Long id) {
        return accidentInformationJpaRepository.findById(id);
    }

    public List<QueryAccidentVO> queryAccidentList() {
        return queryFactory
                .select(
                        new QQueryAccidentVO(
                                accident.id,
                                accident.title,
                                accident.content,
                                accident.imageUrl,
                                accident.createdAt,
                                accident.views
                        )
                )
                .from(accident)
                .orderBy(accident.createdAt.desc())
                .fetch();
    }

    public List<QueryAccidentInformationVO> queryAccidentInformationListByConditions(String title, SortType sortType, Long userId) {
        return queryFactory
                .select(
                        new QQueryAccidentInformationVO(
                                accidentInformation.id,
                                accidentInformation.title,
                                accidentInformation.content,
                                accidentInformation.imageUrl,
                                accidentInformation.likesCount,
                                likes.count()
                        )
                )
                .from(accidentInformation)
                .join(accidentInformation.user, user)
                .leftJoin(accidentInformation.likesList, likes)
                .on(user.id.eq(userId))
                .where(containsTitle(title))
                .orderBy(orderBySortType(sortType))
                .groupBy(accidentInformation.id)
                .fetch();
    }

    //===condition===//

    private BooleanExpression containsTitle(String title) {
        return title == null ? null : accidentInformation.title.contains(title);
    }

    private OrderSpecifier<?> orderBySortType(SortType type) {
        return switch (type) {
            case LIKES -> new OrderSpecifier<>(Order.DESC, accidentInformation.likesCount);
            case LATEST -> new OrderSpecifier<>(Order.DESC, accidentInformation.createdAt);
        };
    }
}