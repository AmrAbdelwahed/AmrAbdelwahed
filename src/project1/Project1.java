/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package project1;

/**
 *
 * @author User
 */
public class Project1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

        char[] myWord = new char[7];
        myWord[0] = 's';
        myWord[1] = 't';
        myWord[2] = 'u';
        myWord[3] = 'd';
        myWord[4] = 'e';
        myWord[5] = 'n';
        myWord[6] = 't';
        
        for(int i=0; i<myWord.length; i++){
            System.out.print(myWord[i]);
        }
        
        System.out.println("");
        System.out.println("reverse order");
        
        for (int i =myWord.length-1; i >-1; i--){
            System.out.print(myWord[i]);
        
        }
    }
    
}
