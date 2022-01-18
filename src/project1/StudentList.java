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
public class StudentList {
    public static void main (String[] args){
    
        Student[] studentList = new Student[4];
        studentList[0] = new Student("s1", "Amr Abdelwahed");
        studentList[1] = new Student("s2", "Jacob Hou");
        studentList[2] = new Student("s3", "A7a 7amra");
        
        for(int i =0; i<studentList.length; i++){
            System.out.print(studentList[i].getStudentId());
            System.out.print("   ");
            System.out.println(studentList[i].getStudentName());
        }
    }
}
