package org.bestonjava.springboot;

public class AccountController {
	public static double deposit(Account act,double depositAmt){
		act.addAmount(depositAmt);
		double newBalance = act.getBalance();
		return newBalance;
	}
	public static double withDraw(Account act, double withDrawAmt){
		act.withDrawAmount(withDrawAmt);
		double newBalance = act.getBalance();
		return newBalance;
	}
}
