package com.example.springboard.service;

import com.example.springboard.common.exception.GlobalException;
import com.example.springboard.domain.articles.Article;
import com.example.springboard.dto.request.article.ArticleCreateRequest;
import com.example.springboard.dto.request.article.ArticleModifyRequest;
import com.example.springboard.repository.ArticleRepository;
import com.example.springboard.util.enums.ErrorTypeWithRequest;
import java.util.Map;
import org.springframework.stereotype.Service;

@Service
public class ArticleService {

    private final ArticleRepository articleRepository;
    private final UserService userService;

    public ArticleService(ArticleRepository articleRepository, UserService userService) {
        this.articleRepository = articleRepository;
        this.userService = userService;
    }

    /**
     * ArticleId 로 게시물 조회
     *
     * @param articleId
     * @return
     */
    public Article getArticleByArticleId(int articleId) {
        return articleRepository.findArticleByArticleId(articleId).orElseThrow(() ->
            new GlobalException(Map.of("articleId", articleId),
                ErrorTypeWithRequest.ARTICLE_NOT_FOUND_BY_ID));
    }

    /**
     * 회원인 경우, 게시물 생성
     *
     * @param articleCreateRequest
     * @return
     */
    public Article createArticleByMember(ArticleCreateRequest articleCreateRequest, int userId,
        int boardId) {
        Article article = Article.of(userId, boardId, articleCreateRequest.getTitle(),
            articleCreateRequest.getContent());
        int articleId = articleRepository.createArticle(article);
        article.setId(articleId);
        return article;
    }

    /**
     * 비회원인 경우, 게시물 생성
     *
     * @param articleCreateRequest
     * @param boardId
     * @return
     */
    public Article createArticleByNoMember(ArticleCreateRequest articleCreateRequest, int boardId) {
        int userId = userService.createUser(articleCreateRequest.getNickName(),
            articleCreateRequest.getPassword());
        return createArticleByMember(articleCreateRequest, userId, boardId);
    }

    /**
     * 게시물 업데이트
     *
     * @param articleId
     * @param articleModifyRequest
     * @return
     */
    public Article updateArticle(int articleId, ArticleModifyRequest articleModifyRequest) {
        articleRepository.updateArticleTitleAndContent(articleId, articleModifyRequest.getTitle(),
            articleModifyRequest.getContent());
        return getArticleByArticleId(articleId);
    }
}
