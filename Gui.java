

import javax.swing.JOptionPane;

public class Gui {

    public static void main(String[] args) {

        String name = JOptionPane.showInputDialog("Enter Your name");
        JOptionPane.showMessageDialog(null,"Hi "+ name);

        int age = Integer.parseInt(JOptionPane.showInputDialog("How old are you ?"));
        JOptionPane.showMessageDialog(null, "You are "+age+ " years old!");

        Double Height = Double.parseDouble(JOptionPane.showInputDialog("How tall are you in cm ?"));
        
        JOptionPane.showMessageDialog(null, "You are "+ Height/2.5 + " inches tall.");
  

    }

    
}
