package com.sonali.springboot.movieapp.controller;

import java.util.List;
import java.util.Optional;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.sonali.springboot.movieapp.models.Movie;
import com.sonali.springboot.movieapp.repository.MovieRepo;



@RestController
@RequestMapping("/movie_api")
public class MovieController {
	
	Logger logger = LoggerFactory.getLogger(MovieController.class);
	
	@Autowired
	MovieRepo movieRepo;

	//API for Saving a movie into db ==> CREATE/SAVE
	
	@PostMapping("/create")
	public Movie saveMovie(@RequestBody Movie movie) {
		logger.info("=== Create method started ===");
		Movie savedMovie = movieRepo.save(movie); ///hibernate is creating query BTS
		//now we will persist data into database
		return savedMovie;

	}
	
	
	
	//API to read all Movie data
	
	@GetMapping("/find_all")
	public List<Movie> getAllMovies() {
		logger.info("==== Going to get all movie records ====");
		List<Movie> movies = movieRepo.findAll();
		logger.info("No of records fetched :: {}",movies.size());
		return movies;
	}
	
	
	//API to get a particular movie based on its ID
	@GetMapping("/findMovieById/{movieId}")
	public Movie getMovieById(@PathVariable("movieId") Integer id) {
		logger.info("going to fetch movie by it's id "+id);
		Optional<Movie> optional = movieRepo.findById(id);
		if(optional.isPresent()) {
			return optional.get();
		}
		else {
			throw new RuntimeException("No records found for this id "+ id);
		}
	}
	
	@DeleteMapping("/deleteMovieById/{movieId}")
	public String deleteMovieById(@PathVariable("movieId")Integer id) {
		logger.info("going to delete movie by id "+id);
		movieRepo.deleteById(id);
		return "movie deleted successfully!";
		
	}
	@PutMapping("/updateMovieById/{movieId}")
	public Movie updateMovie(@PathVariable("movieId") Integer id,@RequestBody Movie updatedMovie) {
		logger.info("going to update movie by id "+id);
		Optional<Movie> optional = movieRepo.findById(id);
		if(optional.isPresent()) {
			Movie existingMovie = optional.get();
			existingMovie.setMovieName(updatedMovie.getMovieName());
			existingMovie.setPrice(updatedMovie.getPrice());
			existingMovie.setReleaseDate(updatedMovie.getReleaseDate());
			Movie updatedData = movieRepo.save(existingMovie);
			return updatedData;
		}
		else {
			throw new RuntimeException("record doesn't exist");
		}
	}
	
	
	
	
	
	
	
	
	
	
	
	
}
