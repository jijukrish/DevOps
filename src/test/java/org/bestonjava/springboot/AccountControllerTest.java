package org.bestonjava.springboot;

import junit.framework.TestCase;

public class AccountControllerTest extends TestCase{
	//Setup
	@Override
	protected void setUp() throws Exception {
		// TODO Auto-generated method stub
		
	}
	//Test for deposit amount
	public void testDepositAmountInAccount(){
		Account acc1 = new Account("Savings",1000,30);
		AccountController.deposit(acc1, 300);
		//Test fails if the amount if balance is not equal to the test account
		assertEquals(1300, acc1.getBalance());
	}
	//Test for deposit amount
		public void testWitdraAmountInAccount(){
			Account acc1 = new Account("Savings",5000,30);
			AccountController.withDraw(acc1, 300);
			//Test fails if the amount if balance is not equal to the test account
			assertEquals(4700.00, acc1.getBalance());
		}
}
