package gbstore;

import com.mysql.jdbc.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import javax.swing.JOptionPane;

/**
 *
 * @author MSGB
 */
public class JavaConnect {
    Connection con;
        public Connection createConnection(){
            try{
                Class.forName("com.mysql.jdbc.Driver");
                con = (Connection)DriverManager.getConnection("jdbc:mysql://localhost:3306/gbstore","root","");
                System.out.println("Vous etes connecté a mysql de wampserver");
                
            }  catch (ClassNotFoundException e){e.printStackTrace();
            JOptionPane.showMessageDialog(null, "La connection à Wamp Server ne marche pas!");}
               catch (SQLException sqe){sqe.printStackTrace();
            JOptionPane.showMessageDialog(null, "La connection à Wamp Server ne marche pas!");}
            
            return con;
        }
            public static PreparedStatement getPreparedStatement(String sql) throws ClassNotFoundException, SQLException{
        PreparedStatement ps =  null;
        
        Class.forName("com.mysql.jdbc.Driver");
        java.sql.Connection con = (java.sql.Connection)DriverManager.getConnection("jdbc:mysql://localhost:3306/gbstore","root","");
        System.out.println("Vous etes connecté a mysql de wampserver");
        ps = con.prepareStatement(sql);
        
        return ps;
    }
                public static void main(String[] args) {
        JavaConnect jcs = new JavaConnect();
        jcs.createConnection();
    }
}
