package com.shopping.admin.user;

import static org.assertj.core.api.Assertions.assertThat;

import java.util.List;
import java.util.Optional;

import javax.persistence.EntityManager;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.jdbc.AutoConfigureTestDatabase;
import org.springframework.boot.test.autoconfigure.jdbc.AutoConfigureTestDatabase.Replace;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.test.annotation.Rollback;

import com.shopping.admin.user.repository.UserRepository;
import com.shopping.common.entity.Role;
import com.shopping.common.entity.User;

@DataJpaTest
@AutoConfigureTestDatabase(replace = Replace.NONE)
@Rollback(false)
public class UserRespositoryTesting {

	@Autowired
	UserRepository userRepo;

	@Autowired
	EntityManager entityManager;

	@Test
	public void testCreateUser() {
		Role role = entityManager.find(Role.class, 1);
		User user = new User("name4@hello.txt", "test2022", "nam", "test",false);
		user.addRole(role);
		user = userRepo.save(user);
		assertThat(user.getId()).isGreaterThan(0);
	}

	@Test
	public void testTwoRoleForSingleUser() {
		Role role2 = entityManager.find(Role.class, 1);
		Role role = entityManager.find(Role.class, 3);
		Role role1 = entityManager.find(Role.class, 5);
		User user = new User("hello5@hello.txt", "dog12022", "test", "testing",true);
		user.addRole(role);
		user.addRole(role1);
		user.addRole(role2);
		user = userRepo.save(user);
		assertThat(user.getId()).isGreaterThan(0);
	}

	@Test
	public void fetchAllUser() {
		List<User> allUsers = (List<User>) userRepo.findAll();
		allUsers.stream().forEach(singleUser -> {
			System.out.println(singleUser);
		});
		assertThat(allUsers.size()).isGreaterThan(0);
	}

	@Test
	public void testGetUserById() {
		User user = userRepo.findById(1).get();
		assertThat(user).isNotNull();
	}

	@Test
	public void testUpdateUserDetails()
	{
		User user=userRepo.findById(1).get();
		user.setEnabled(true);
		userRepo.save(user);
		//assertThat
	}
	
	@Test
	public void testUpdateUserRoles()
	{
		User user=userRepo.findById(10).get();
		Role role= entityManager.find(Role.class,1);
		user.getRoles().remove(role);
		userRepo.save(user);
	}
	
	@Test
	public void testDeleteUser()
	{
		//User user=userRepo.findById(10).get();
		userRepo.deleteById(10);
	}
	
	@Test
	public void Test()
	{
		String testEmail="hello@hello.txt";
		Optional<User> user=userRepo.findByEmail(testEmail);
		assertThat(user.get()).isNotNull();
	}
}
