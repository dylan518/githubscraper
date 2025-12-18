package academy.learnprogramming;

import java.util.ArrayList;

public class Bank {

    private String bankName;
    private ArrayList<Branch> branches;

    public Bank(String bankName) {
        this.bankName = bankName;
        branches = new ArrayList<>();
        System.out.println("Bank with name " + bankName + " created");
    }

    public void addBranch(String name) {
        if (!branchExists(name)) {
            branches.add(new Branch(name));
        } else {
            System.out.println("Branch with name " + name + " already exists");
        }
    }

    public void addCustomerToBranch(String customerName, String branchName, double initialTransaction) {
        Branch branch = findBranch(branchName);
        if (null != branch) {
            branch.addCustomer(customerName, initialTransaction);
        } else {
            System.out.println("Branch with name " + branchName + " does not exist");
        }
    }

    public void addTranascationToCusomerAtBranch(double transaction, String customerName, String branchName) {
        Branch branch = findBranch(branchName);
        if (null != branch) {
            branch.addTransaction(customerName, transaction);
        } else {
            System.out.println("Branch with name " + branchName + " does not exist");
        }
    }

    public void printCustomerListForBranch(String branchName, boolean withTransactions) {
        Branch branch = findBranch(branchName);
        if (null != branch) {
            branch.printCustomerList(withTransactions);
        } else {
            System.out.println("Branch with name " + branchName + " does not exist");
        }
    }

    public void printBranchList() {
        System.out.println("Branch list for brank " + this.bankName);
        for (Branch branch : branches) {
            System.out.println(branch.getName());
        }
    }

    private boolean branchExists(String name) {
        if (findBranch(name) == null) {
            return false;
        } else {
            return true;
        }
    }

    private Branch findBranch(String name) {
        for (Branch branch : branches) {
            if (branch.getName().equals(name)) {
                return branch;
            }
        }

        return null;
    }
}
