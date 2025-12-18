package com.prodapt.learningspring.controller;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;

import java.util.List;

import java.util.Optional;
import java.util.stream.Collectors;
import java.util.Collections;

import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;

import org.springframework.stereotype.Controller;

import org.springframework.ui.Model;

import org.springframework.validation.BindingResult;

import org.springframework.web.bind.annotation.GetMapping;

import org.springframework.web.bind.annotation.ModelAttribute;

import org.springframework.web.bind.annotation.PathVariable;

import org.springframework.web.bind.annotation.PostMapping;

import org.springframework.web.bind.annotation.RequestMapping;

import org.springframework.web.bind.annotation.RequestParam;

import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import org.springframework.web.servlet.view.RedirectView;

import com.prodapt.learningspring.controller.binding.AddCommentForm;

import com.prodapt.learningspring.controller.binding.AddPostForm;

import com.prodapt.learningspring.controller.exception.ResourceNotFoundException;

import com.prodapt.learningspring.entity.LikeRecord;
import com.prodapt.learningspring.entity.MutedAuthor;
import com.prodapt.learningspring.entity.Comment;
import com.prodapt.learningspring.entity.FavoriteAuthor;
import com.prodapt.learningspring.entity.LikeId;

import com.prodapt.learningspring.entity.Post;

import com.prodapt.learningspring.entity.User;


import com.prodapt.learningspring.model.RegistrationForm;

import com.prodapt.learningspring.repository.CommentRepository;
import com.prodapt.learningspring.repository.FavoriteAuthorRepository;
import com.prodapt.learningspring.repository.LikeCRUDRepository;

import com.prodapt.learningspring.repository.LikeCountRepository;
import com.prodapt.learningspring.repository.MutedAuthorRepository;
import com.prodapt.learningspring.repository.PostRepository;

import com.prodapt.learningspring.repository.UserRepository;

import com.prodapt.learningspring.service.DomainUserService;

import jakarta.annotation.PostConstruct;

import jakarta.servlet.ServletException;

import jakarta.servlet.http.HttpServlet;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.transaction.Transactional;

@Controller

@RequestMapping("/forum")

public class ForumController {

	@Autowired

	private UserRepository userRepository;

	@Autowired

	private PostRepository postRepository;

	@Autowired

	private CommentRepository commentRepository;

	@Autowired

	private DomainUserService domainUserService;

	@Autowired

	private LikeCRUDRepository likeCRUDRepository;

	private List<User> userList;

	private List<Comment> commentList;

	@PostConstruct

	public void init() {

		userList = new ArrayList<>();

		commentList = new ArrayList<>();

	}

	@GetMapping("/post/form")

	public String getPostForm(Model model, @AuthenticationPrincipal UserDetails userDetails) {

		AddPostForm postForm = new AddPostForm();

		User author = domainUserService.getByName(userDetails.getUsername()).get();

		postForm.setUserId(author.getId());

		model.addAttribute("postForm", postForm);

		return "forum/postForm";

	}

	@PostMapping("/post/add")

	public String addNewPost(@ModelAttribute("postForm") AddPostForm postForm, BindingResult bindingResult,

			RedirectAttributes attr) throws ServletException {

		if (bindingResult.hasErrors()) {

			System.out.println(bindingResult.getFieldErrors());

			attr.addFlashAttribute("org.springframework.validation.BindingResult.post", bindingResult);

			attr.addFlashAttribute("post", postForm);

			return "redirect:/forum/post/form";

		}

		Optional<User> user = userRepository.findById(postForm.getUserId());

		if (user.isEmpty()) {

			throw new ServletException("Something went seriously wrong and we couldn't find the user in the DB");

		}

		Post post = new Post();

		post.setAuthor(user.get());

		post.setContent(postForm.getContent());

		postRepository.save(post);

		return String.format("redirect:/forum/post/%d", post.getId());

	}

	@GetMapping("/post/{id}")

	public String postDetail(@PathVariable int id, Model model, @AuthenticationPrincipal UserDetails userDetails)

			throws ResourceNotFoundException {

		Optional<Post> post = postRepository.findById(id);

		if (post.isEmpty()) {

			throw new ResourceNotFoundException("No post with the requested ID");

		}

		model.addAttribute("post", post.get());

		model.addAttribute("likerName", userDetails.getUsername());

		model.addAttribute("commenterName", userDetails.getUsername());

		commentList = commentRepository.findAllByPostId(id);

		model.addAttribute("commentList", commentList);

		int numLikes = likeCRUDRepository.countByLikeIdPost(post.get());

		model.addAttribute("likeCount", numLikes);

		return "forum/postDetail";

	}

	@PostMapping("/post/{id}/like")

	public String postLike(@PathVariable int id, String likerName, RedirectAttributes attr) {

		LikeId likeId = new LikeId();

		likeId.setUser(userRepository.findByName(likerName).get());

		likeId.setPost(postRepository.findById(id).get());

		LikeRecord like = new LikeRecord();

		like.setLikeId(likeId);

		likeCRUDRepository.save(like);

		return String.format("redirect:/forum/post/%d", id);

	}

	@GetMapping("/register")

	public String getRegistrationForm(Model model) {

		if (!model.containsAttribute("registrationForm")) {

			model.addAttribute("registrationForm", new RegistrationForm());

		}

		return "forum/register";

	}

	@PostMapping("/register")

	public String register(@ModelAttribute("registrationForm") RegistrationForm registrationForm,

			BindingResult bindingResult, RedirectAttributes attr) {

		if (bindingResult.hasErrors()) {

			attr.addFlashAttribute("org.springframework.validation.BindingResult.registrationForm", bindingResult);

			attr.addFlashAttribute("registrationForm", registrationForm);

			return "redirect:/register";

		}

		if (!registrationForm.isValid()) {

			attr.addFlashAttribute("message", "Passwords must match");

			attr.addFlashAttribute("registrationForm", registrationForm);

			return "redirect:/register";

		}

		System.out.println(domainUserService.save(registrationForm.getUsername(), registrationForm.getPassword()));

		attr.addFlashAttribute("result", "Registration success!");

		return "redirect:/login";

	}

	@PostMapping("/post/{id}/comment")

	public String addCommentToPost(String commenterName, HttpServletRequest request, @PathVariable int id) {

		String content = request.getParameter("content");

		Optional<User> user = userRepository.findByName(commenterName);

		Optional<Post> post = postRepository.findById(id);

		if (user.isPresent() && post.isPresent()) {

			Comment comment = new Comment();

			comment.setUser(user.get());

			comment.setPost(post.get());

			comment.setContent(content);

			commentRepository.save(comment);

			return String.format("redirect:/forum/post/%d", id);

		}

		return "redirect:/forum/post/error";

	}

//	@GetMapping("/login-success")
//	public RedirectView loginSuccess() {
//	    return new RedirectView("/forum/user/profile");
//	}

//	@GetMapping("/profile")
//	public String userProfile(Model model, @AuthenticationPrincipal UserDetails userDetails) {
//		User user = domainUserService.getByName(userDetails.getUsername()).orElse(null);
//
//		if (user != null) {
//	            // Load user's posts, favorite authors, favorite posts, and hidden posts
//	            List<Post> userPosts = postRepository.findByAuthor(user);
//	            List<User> favoriteAuthors = user.getFavoriteAuthors();
//	            List<Post> favoritePosts = user.getFavoritePosts();
//	            List<Post> hiddenPosts = user.getHiddenPosts();

			// Add data to the model
//	            model.addAttribute("user", user);
//	            model.addAttribute("userPosts", userPosts);
//	            model.addAttribute("favoriteAuthors", favoriteAuthors);
//	            model.addAttribute("favoritePosts", favoritePosts);
//	            model.addAttribute("hiddenPosts", hiddenPosts);
//
//			return "forum/userProfile"; // Assuming you have this HTML template
//		} else {
//			return "redirect:/login"; // Redirect to login if the user is not found
//		}
//	}
	

//	    @GetMapping("/userProfile") 
//	    public String userProfile(Model model, @AuthenticationPrincipal UserDetails userDetails) {
//	        User user = domainUserService.getByName(userDetails.getUsername()).get();
////
////	        if (user != null) {
//	        model.addAttribute("user", user);
//
//	        return "forum/userProfile"; // Assuming you have this HTML template
////	        } else {
////	            return "redirect:/login"; // Redirect to login if the user is not found
////	        }
//	    }
	    
	    
//	    @Autowired
//	    private FavouriteAuthorRepository favouriteAuthorRepository;
//
//	    @Autowired
//	    private MutedAuthorRepository mutedAuthorRepository;

//	    // Add a favorite author for a user
//	    @PostMapping("/{userId}/add-favorite-author/{favAuthorId}")
//	    public User addFavoriteAuthor(@PathVariable Integer userId, @PathVariable Integer favAuthorId) {
//	        User user = userRepository.findById(userId).orElse(null);
//	        User favAuthor = userRepository.findById(favAuthorId).orElse(null);
//
//	        if (user != null && favAuthor != null) {
//	            FavAuthor favAuthorEntry = new FavAuthor();
//	            favAuthorEntry.setUser(user);
//	            favAuthorEntry.setFavUser(favAuthor);
//	            favouriteAuthorRepository.save(favAuthorEntry);
//	        }
//
//	        return user;
//	    }
//
//	    // Get all favorite authors of a user
//	    @GetMapping("/{userId}/favorite-authors")
//	    public List<User> getFavoriteAuthors(@PathVariable Integer userId) {
//	        List<FavAuthor> favAuthors = favouriteAuthorRepository.findAllByPostId(userId);
//	        return favAuthors.stream()
//	                .map(FavAuthor::getFavUser)
//	                .collect(Collectors.toList());
//	    }
//
//	    // Add a muted author for a user
//	    @PostMapping("/{userId}/add-muted-author/{mutedAuthorId}")
//	    public User addMutedAuthor(@PathVariable Integer userId, @PathVariable Integer mutedAuthorId) {
//	        User user = userRepository.findById(userId).orElse(null);
//	        User mutedAuthor = userRepository.findById(mutedAuthorId).orElse(null);
//
//	        if (user != null && mutedAuthor != null) {
//	            MutedAuthor mutedAuthorEntry = new MutedAuthor();
//	            mutedAuthorEntry.setUser(user);
//	            mutedAuthorEntry.setMutedUser(mutedAuthor);
//	            mutedAuthorRepository.save(mutedAuthorEntry);
//	        }
//
//	        return user;
//	    }
//
//	    // Get all muted authors of a user
//	    @GetMapping("/{userId}/muted-authors")
//	    public List<User> getMutedAuthors(@PathVariable Integer userId) {
//	    	 return mutedAuthors.stream()
//	                 .map(MutedAuthor::getMutedUser)
//	                 .collect(Collectors.toList());
//				}
//			}
//	    
//	
//
//	    @GetMapping("/{userId}/favorite-authors")
//	    public String getFavoriteAuthors(@PathVariable Integer userId, Model model) {
//	        List<FavoriteAuthor> favAuthors = favouriteAuthorRepository.findAllByPostId(userId);
//	        List<User> favoriteAuthors = favAuthors.stream()
//	                .map(FavoriteAuthor::getFavUser)
//	                .collect(Collectors.toList());
//
//	        // Add favorite authors to the model for rendering in the HTML template
//	        model.addAttribute("favoriteAuthors", favoriteAuthors);
//
//	        // Return the HTML template
//	        return "forum/userProfile";
//	    }
//
//	    // Get all muted authors of a user
//	    @GetMapping("/{userId}/muted-authors")
//	    public String getMutedAuthors(@PathVariable Integer userId, Model model) {
//	        List<MutedAuthor> mutedAuthors = mutedAuthorRepository.findAllByPostId(userId);
//	        List<User> mutedAuthorList = mutedAuthors.stream()
//	                .map(MutedAuthor::getMutedUser)
//	                .collect(Collectors.toList());
//
//	        // Add muted authors to the model for rendering in the HTML template
//	        model.addAttribute("mutedAuthors", mutedAuthorList);
//
//	        // Return the HTML template
//	        return "forum/userProfile";
//	    }
//	    @PostMapping("/{userId}/add-favorite-author/{favAuthorId}")
//	    public String addFavoriteAuthor(@PathVariable Integer userId, @PathVariable Integer favAuthorId) {
//	        Optional<User> userOptional = userRepository.findById(userId);
//	        Optional<User> favAuthorOptional = userRepository.findById(favAuthorId);
//
//	        if (userOptional.isPresent() && favAuthorOptional.isPresent()) {
//	            User user = userOptional.get();
//	            User favAuthor = favAuthorOptional.get();
//	            
//	            FavoriteAuthor favAuthorEntry = new FavoriteAuthor();
//	            favAuthorEntry.setUser(user);
//	            favAuthorEntry.setFavUser(favAuthor);
//	            favouriteAuthorRepository.save(favAuthorEntry);
//	        }
//
//	        return "redirect:/forum/userProfile"; // Redirect to the user profile page after adding a favorite author.
//	    }
//	    @PostMapping("/{userId}/add-muted-author/{mutedAuthorId}")
//	    public String addMutedAuthor(@PathVariable Integer userId, @PathVariable Integer mutedAuthorId) {
//	        Optional<User> userOptional = userRepository.findById(userId);
//	        Optional<User> mutedAuthorOptional = userRepository.findById(mutedAuthorId);
//
//	        if (userOptional.isPresent() && mutedAuthorOptional.isPresent()) {
//	            User user = userOptional.get();
//	            User mutedAuthor = mutedAuthorOptional.get();
//
//	            MutedAuthor mutedAuthorEntry = new MutedAuthor();
//	            mutedAuthorEntry.setUser(user);
//	            mutedAuthorEntry.setMutedUser(mutedAuthor);
//	            mutedAuthorRepository.save(mutedAuthorEntry);
//	        }
//
//	        return "redirect:/forum/userProfile"; // Redirect to the user profile page after adding a muted author.
//	    }
	    
	    @Autowired
	    private FavoriteAuthorRepository favoriteAuthorRepository;

	    @Autowired
	    private MutedAuthorRepository mutedAuthorRepository;
//
//	    
//	    @GetMapping("/userprofile")
//	    public String userProfile(Model model, @AuthenticationPrincipal UserDetails userDetails) {
//	        User user = userRepository.findByName(userDetails.getUsername()).orElse(null);
//
//	        if (user != null) {
//	            List<User> allAuthors = (List<User>) userRepository.findAll(); // Retrieve all authors from the database
//
//	            List<FavoriteAuthor> favoriteAuthors = favoriteAuthorRepository.findAllByUserId(user.getId());
//	            List<MutedAuthor> mutedAuthors = mutedAuthorRepository.findAllByUserId(user.getId());
//
//	            // Add data to the model
//	            model.addAttribute("user", user);
//	            model.addAttribute("allAuthors", allAuthors);
//	            model.addAttribute("favoriteAuthors", favoriteAuthors);
//	            model.addAttribute("mutedAuthors", mutedAuthors);
//
//	            return "forum/userProfile";
//	        } else {
//	            return "redirect:/login"; // Redirect to login if the user is not found
//	        }
//	    }
//
//	    // Handle marking a user as favorite
//	    @PostMapping("/markFavorite")
//	    public String markAsFavorite(@RequestParam("userId") int userId, @AuthenticationPrincipal UserDetails userDetails) {
//	        User user = userRepository.findByName(userDetails.getUsername()).orElse(null);
//
//	        if (user != null) {
//	            favoriteAuthorRepository.save(new FavoriteAuthor());
//	        }
//
//	        return "redirect:/user/profile";
//	    }
//
//	    // Handle marking a user as muted
//	    @PostMapping("/markMuted")
//	    public String markAsMuted(@RequestParam("userId") int userId, @AuthenticationPrincipal UserDetails userDetails) {
//	        User user = userRepository.findByName(userDetails.getUsername()).orElse(null);
//
//	        if (user != null) {
//	            mutedAuthorRepository.save(new MutedAuthor(user.getId(), userId));
//	        }
//
//	        return "redirect:/user/profile";
//	    }
//	}
	    
//	@GetMapping("/userprofile")
//	public String userProfile(Model model, @AuthenticationPrincipal UserDetails userDetails) {
//	    Optional<User> user = userRepository.findByName(userDetails.getUsername());
//        // Load the list of authors (You can implement this method)
//	        List<User> authors = loadAuthors();
//
//	        model.addAttribute("authors", authors);
//	        // Add other user profile details as needed
//
//	        return "forum/userProfile";
//	}
//	
//	private List<User> loadAuthors()  {
//	    // Retrieve the list of authors from your repository (e.g., UserRepository)
//	    List<User> authors = (List<User>) userRepository.findAll();
//
//	    // Remove the currently logged-in user from the list (assuming the user is also listed as an author)
//	    authors = authors.stream()
//	            .filter(author -> !author.getName().equals(SecurityContextHolder.getContext().getAuthentication().getName()))
//	            .collect(Collectors.toList());
//
//	    return authors;
//	}
//
//	@PostMapping("/user/markFavorite")
//	public String markAuthorAsFavorite(@RequestParam("authorId") int authorId, @AuthenticationPrincipal UserDetails userDetails) {
//	    Optional<User> user = userRepository.findByName(userDetails.getUsername());
//
//	    if (user.isPresent()) {
//	        User currentUser = user.get();
//	        Optional<User> author = userRepository.findById(authorId);
//
//	        if (author.isPresent()) {
//	            User favoriteAuthor = author.get();
//	            FavoriteAuthor favorite = new FavoriteAuthor();
//	            favorite.setUser(currentUser);
//	            favorite.setAuthor(favoriteAuthor);
//	            favoriteAuthorRepository.save(favorite);
//	        }
//	    }
//
//	    return "redirect:/forum/user/profile";
//	}
//
//	@PostMapping("/user/markMuted")
//	public String markAuthorAsMuted(@RequestParam("authorId") int authorId, @AuthenticationPrincipal UserDetails userDetails) {
//	    Optional<User> user = userRepository.findByName(userDetails.getUsername());
//
//	    if (user.isPresent()) {
//	        User currentUser = user.get();
//	        Optional<User> author = userRepository.findById(authorId);
//
//	        if (author.isPresent()) {
//	            User mutedAuthor = author.get();
//	            MutedAuthor muted = new MutedAuthor();
//	            muted.setUser(currentUser);
//	            muted.setAuthor(mutedAuthor);
//	            mutedAuthorRepository.save(muted);
//	        }
//	    }
//
//	    return "redirect:/forum/user/profile";
//	}
//}
	
	    @GetMapping("/userProfile")
		public String userProfile(Model model, @AuthenticationPrincipal UserDetails userDetails) {
		    Optional<User> user = userRepository.findByName(userDetails.getUsername());
	        // Load the list of authors (You can implement this method)
		        List<User> authors = loadAuthors();
		        List<User> favoriteAuthors = new ArrayList<>();
		        List<FavoriteAuthor> favorites = favoriteAuthorRepository.findAllByUserId(user.get().getId());
		        for(FavoriteAuthor f : favorites) {
		        	User newUser = userRepository.findById(f.getAuthor().getId()).get();
		        	favoriteAuthors.add(newUser);
		        }
		        model.addAttribute("authors", authors);
		        model.addAttribute("favoriteAuthors", favoriteAuthors);
		        // Add other user profile details as needed

		        return "forum/userProfile";
		}
		
		private List<User> loadAuthors()  {
		    // Retrieve the list of authors from your repository (e.g., UserRepository)
		    List<User> authors = (List<User>) userRepository.findAll();

		    // Remove the currently logged-in user from the list (assuming the user is also listed as an author)
		    authors = authors.stream()
		            .filter(author -> !author.getName().equals(SecurityContextHolder.getContext().getAuthentication().getName()))
		            .collect(Collectors.toList());

		    return authors;
		}
//
//		@PostMapping("/user/markFavorite")
//		public String markAuthorAsFavorite(@RequestParam("authorId") int authorId, @AuthenticationPrincipal UserDetails userDetails) {
//		    Optional<User> user = userRepository.findByName(userDetails.getUsername());
//
//		    if (user.isPresent()) {
//		        User currentUser = user.get();
//		        Optional<User> author = userRepository.findById(authorId);
//
//		        if (author.isPresent()) {
//		            User favoriteAuthor = author.get();
//		            FavoriteAuthor favorite = new FavoriteAuthor();
//		            favorite.setUser(currentUser);
//		            favorite.setAuthor(favoriteAuthor);
//		            favoriteAuthorRepository.save(favorite);
//		        }
//		    }
//
//		    return "redirect:/forum/userProfile";
//		}
//
//		@PostMapping("/user/markMuted")
//		public String markAuthorAsMuted(@RequestParam("authorId") int authorId, @AuthenticationPrincipal UserDetails userDetails) {
//		    Optional<User> user = userRepository.findByName(userDetails.getUsername());
//
//		    if (user.isPresent()) {
//		        User currentUser = user.get();
//		        Optional<User> author = userRepository.findById(authorId);
//
//		        if (author.isPresent()) {
//		            User mutedAuthor = author.get();
//		            MutedAuthor muted = new MutedAuthor();
//		            muted.setUser(currentUser);
//		            muted.setAuthor(mutedAuthor);
//		            mutedAuthorRepository.save(muted);
//		        }
//		    }
//
//		    return "redirect:/forum/userProfile";
//		}
//	}
//		
	    
	    @PostMapping("/user/markFavorite")
public String markAuthorAsFavorite(@RequestParam("authorId") int authorId, @AuthenticationPrincipal UserDetails userDetails) {
    Optional<User> user = userRepository.findByName(userDetails.getUsername());

    if (user.isPresent()) {
        User currentUser = user.get();
        Optional<User> author = userRepository.findById(authorId);

        if (author.isPresent()) {
            User favoriteAuthor = author.get();

            // Check if the author is already a favorite
            if (!isAuthorFavorite(currentUser, favoriteAuthor)) {
                FavoriteAuthor favorite = new FavoriteAuthor();
                favorite.setUser(currentUser);
                favorite.setAuthor(favoriteAuthor);
                favoriteAuthorRepository.save(favorite);
            }
        }
    }

    return "redirect:/forum/userProfile";
}

	    private boolean isAuthorFavorite(User currentUser, User author) {
	        List<FavoriteAuthor> favorites = favoriteAuthorRepository.findByUserAndAuthor(currentUser, author);
	        return !favorites.isEmpty();
	    }

		
	    @PostMapping("/user/markMuted")
	    public String markAuthorAsMuted(@RequestParam("authorId") int authorId, @AuthenticationPrincipal UserDetails userDetails) {
	        Optional<User> user = userRepository.findByName(userDetails.getUsername());

	        if (user.isPresent()) {
	            User currentUser = user.get();
	            Optional<User> author = userRepository.findById(authorId);

	            if (author.isPresent()) {
	                User mutedAuthor = author.get();

	                // Check if the author is already muted
	                if (!isAuthorMuted(currentUser, mutedAuthor)) {
	                    MutedAuthor muted = new MutedAuthor();
	                    muted.setUser(currentUser);
	                    muted.setAuthor(mutedAuthor);
	                    mutedAuthorRepository.save(muted);
	                }
	            }
	        }

	        return "redirect:/forum/userProfile";
	    }

	    private boolean isAuthorMuted(User currentUser, User author) {
	        List<MutedAuthor> mutedAuthors = mutedAuthorRepository.findByUserAndAuthor(currentUser, author);
	        return !mutedAuthors.isEmpty();
	    }
	    
	    @Transactional
	    @PostMapping("/user/removeFavorite")
	    public String removeFavoriteAuthor(@RequestParam("authorId") int authorId, @AuthenticationPrincipal UserDetails userDetails) {
	        Optional<User> user = userRepository.findByName(userDetails.getUsername());
	        System.out.println("going...");
	        
	        if (user.isPresent()) {
	            User currentUser = user.get();
	            Optional<User> author = userRepository.findById(authorId);

	            if (author.isPresent()) {
	                User favoriteAuthor = author.get();
	                System.out.println(author);
	                // Check if the author is a favorite
	                if (isAuthorFavorite(currentUser, favoriteAuthor)) {
	                    // Remove the favorite
	                	favoriteAuthorRepository.deleteByUserAndAuthor(currentUser, favoriteAuthor);
//	                    favoriteAuthorRepository.save(del);
	                    
	                }
	            }
	        }

	        return "redirect:/forum/userProfile";
	    }
}
	
	   