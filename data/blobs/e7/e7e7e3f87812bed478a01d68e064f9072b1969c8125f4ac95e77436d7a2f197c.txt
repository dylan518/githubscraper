package com.fhburgenland.mcce.innenpt.webapp.service;

import com.fhburgenland.mcce.innenpt.webapp.model.BlogPost;
import com.fhburgenland.mcce.innenpt.webapp.repository.BlogPostRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class BlogPostService {

    private final BlogPostRepository repository;

    @Autowired
    public BlogPostService(BlogPostRepository repository) {
        this.repository = repository;
    }

    public List<BlogPost> getAllPosts() {
        return repository.findAll();
    }

    public Optional<BlogPost> getPostById(Long id) {
        return repository.findById(id);
    }

    public BlogPost createOrUpdatePost(BlogPost post) {
        return repository.save(post);
    }

    public void deletePost(Long id) {
        repository.deleteById(id);
    }

    public List<BlogPost> getPostsByCategory(String category) {
        return repository.findByCategory(category);
    }

    public List<BlogPost> getPostsByTag(String tag) {
        return repository.findByTagsContaining(tag);
    }
}
