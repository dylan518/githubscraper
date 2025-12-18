package com.aurionpro.exceptions;

public class MinimumBalanceException extends RuntimeException {
	private double balance;

	public MinimumBalanceException(double balance) {
		this.balance = balance;

	}

	public String getMessage() {
		return "Balance goes minimum balance limi  balance is " + balance;
	}
}
