package com.kth.exam.demo1.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.kth.exam.demo1.repository.ArticleRepository;
import com.kth.exam.demo1.vo.Article;

@Service
public class ArticleService {
	private ArticleRepository articleRepository;

	public ArticleService(ArticleRepository articleRepository) {
		this.articleRepository = articleRepository;
	}

	public int writeArticle(String title, String body) {
		articleRepository.writeArticle(title, body);
		return articleRepository.getLastInsertId();
	}

	public List<Article> getArticles() {
		return articleRepository.getArticles();
	}

	public Article getArticle(int id) {
		return articleRepository.getArticle(id);
	}

	public void delete(int id) {
		articleRepository.deleteArticle(id);
	}

	public void modify(int id, String title, String body) {
		articleRepository.modifyArticle(id, title, body);
	}
}