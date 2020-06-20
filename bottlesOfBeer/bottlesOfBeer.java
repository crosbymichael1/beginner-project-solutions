package com.beginner_project_solutions;

public class Main {

    public static void main(String[] args) {
        short bottles = 99;

        while(bottles > 1){
            if(bottles > 1) {
                System.out.println(bottles + " bottles of beer on the wall " + bottles + " bottles of beer");
                System.out.println("Take one down pass it around " + (bottles - 1) + " bottles of beer on the wall");
            }
            else{
                System.out.println(bottles + " bottles of beer on the wall " + bottles + " bottles of beer");
                System.out.println("Take one down pass it around " + (bottles - 1) + " bottle of beer on the wall");
            }
            bottles--;
        }
    }
}
