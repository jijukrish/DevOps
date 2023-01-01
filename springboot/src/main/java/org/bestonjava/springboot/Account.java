package org.bestonjava.springboot;

public class Account {
	String accountType;
	double balance;
	double fees;
	Account(String acType,double balance,double fee){
		this.accountType=acType;
		this.balance=balance;
		this.fees = fee;
	}
	
	public void addAmount(double amt){
		this.balance += amt;
	}
	public void withDrawAmount(double amt){
		this.balance -= amt;
	}

	public String getAccountType() {
		return accountType;
	}

	public double getBalance() {
		return balance;
	}

	public double getFees() {
		return fees;
	}
	
}
