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
public class Student {
    private String _studentId;
    private String _studentName;
    private String _address;
    
    public Student(String studentId, String studentName){
        _studentId = studentId;
        _studentName = studentName;
    }        
    public String getStudentName(){
            return _studentName;
    }        
    public void setStudentName(String sname){
            _studentName = sname;
    }
    
    public String getStudentId(){
        return _studentId;
    }
    public void setStudentId(String sId){
        _studentId = sId;
    }
    
    public String getAddress(){
        return _address;
    }
    public void setAddress(String address){
        _address = address;
    }
    
}
