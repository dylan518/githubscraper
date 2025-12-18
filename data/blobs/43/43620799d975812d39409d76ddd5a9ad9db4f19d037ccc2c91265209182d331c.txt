package dev.tracking.lossandbenefit.service;

import dev.tracking.lossandbenefit.dto.TransactionDto;
import dev.tracking.lossandbenefit.dto.UserDetailsDto;
import dev.tracking.lossandbenefit.dto.UserRegistrationDto;
import dev.tracking.lossandbenefit.entity.TransactionEntity;
import dev.tracking.lossandbenefit.entity.User;
import dev.tracking.lossandbenefit.repository.TransactionRepository;
import dev.tracking.lossandbenefit.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;


@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;
    @Autowired
    private PasswordEncoder passwordEncoder;
    @Autowired
    private TransactionRepository transactionRepository;

    public UserDetailsDto registerUser(UserRegistrationDto userDto) {
        // Check if username or email already exists
        if (userRepository.findByUsername(userDto.getUsername()).isPresent() ||
                userRepository.findByEmail(userDto.getEmail()).isPresent()) {
            throw new IllegalArgumentException("Username or email already exists");
        }

        // Map DTO to Entity
        User user = new User();
        user.setUsername(userDto.getUsername());
        user.setPassword(passwordEncoder.encode(userDto.getPassword()));
        user.setEmail(userDto.getEmail());
        user.setFirstName(userDto.getFirstName());
        user.setLastName(userDto.getLastName());

        // Save user to the repository
        user = userRepository.save(user);

        // Map Entity back to DTO
        return convertToDetailsDto(user);
    }

    public UserDetailsDto getUserByUsername(String username) {
        Optional<User> userOpt = userRepository.findByUsername(username);
        if (userOpt.isPresent()) {
            return convertToDetailsDto(userOpt.get());
        }
        return null;
    }

    public UserDetailsDto getUserWithTransactionsByUsername(String username) {
        Optional<User> userOpt = userRepository.findByUsername(username);
        if (userOpt.isPresent()) {
            User user = userOpt.get();
            List<TransactionEntity> transactions = transactionRepository.findByUserId(user.getId());
            return convertToDetailsWithTransactionsDto(user, transactions);
        }
        return null;
    }

    public boolean updatePassword(String username, String oldPassword, String newPassword) {
        Optional<User> userOpt = userRepository.findByUsername(username);
        if (userOpt.isPresent()) {
            User user = userOpt.get();
            if (passwordEncoder.matches(oldPassword, user.getPassword())) {
                user.setPassword(passwordEncoder.encode(newPassword));
                userRepository.save(user);
                return true;
            }
        }
        return false;
    }

    private UserDetailsDto convertToDetailsDto(User user) {
        UserDetailsDto userDto = new UserDetailsDto();
        userDto.setId(user.getId());
        userDto.setUsername(user.getUsername());
        userDto.setEmail(user.getEmail());
        userDto.setFirstName(user.getFirstName());
        userDto.setLastName(user.getLastName());
        return userDto;
    }

    private UserDetailsDto convertToDetailsWithTransactionsDto(User user, List<TransactionEntity> transactions) {
        UserDetailsDto userDto = new UserDetailsDto();
        userDto.setId(user.getId());
        userDto.setUsername(user.getUsername());
        userDto.setEmail(user.getEmail());
        userDto.setFirstName(user.getFirstName());
        userDto.setLastName(user.getLastName());
        userDto.setTransactions(transactions.stream().map(this::convertToTransactionDto).collect(Collectors.toList()));
        return userDto;
    }

    private TransactionDto convertToTransactionDto(TransactionEntity transaction) {
        TransactionDto transactionDto = new TransactionDto();
        transactionDto.setId(transaction.getId());
        transactionDto.setUserId(transaction.getUser().getId());
        transactionDto.setCategory(transaction.getCategory());
        transactionDto.setAmount(transaction.getAmount());
        transactionDto.setDate(transaction.getDate());
        transactionDto.setBenefit(transaction.isBenefit());
        return transactionDto;
    }
}