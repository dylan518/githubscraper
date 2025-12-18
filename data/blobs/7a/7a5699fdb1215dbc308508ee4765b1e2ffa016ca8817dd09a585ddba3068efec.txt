package Application.CodeTier.DAL;

import Application.AppTier.Model.NhaCungCap;
import Database.MyConnect;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;

public class NhaCungCapDA {

    public ArrayList<NhaCungCap> getListNhaCungCap() {
        try {
            ArrayList<NhaCungCap> dsncc = new ArrayList<>();
            String sql = "SELECT * FROM nhacungcap";
            Statement stmt = MyConnect.conn.createStatement();
            ResultSet rs = stmt.executeQuery(sql);
            while (rs.next()) {
                NhaCungCap ncc = new NhaCungCap();
                ncc.setMaNCC(rs.getInt(1));
                ncc.setTenNCC(rs.getString(2));
                ncc.setDiaChi(rs.getString(3));
                ncc.setDienThoai(rs.getString(4));
                ncc.setCreatedAt(rs.getTimestamp(5));
                ncc.setUpdatedAt(rs.getTimestamp(6));
                dsncc.add(ncc);
            }
            return dsncc;
        } catch (SQLException ex) {
            return null;
        }
    }

    public NhaCungCap getNhaCungCap(int maNCC) {
        NhaCungCap ncc = null;
        try {
            String sql = "SELECT * FROM nhacungcap WHERE MaNCC=" + maNCC;
            Statement stmt = MyConnect.conn.createStatement();
            ResultSet rs = stmt.executeQuery(sql);
            while (rs.next()) {
                ncc = new NhaCungCap();
                ncc.setMaNCC(rs.getInt(1));
                ncc.setTenNCC(rs.getString(2));
                ncc.setDiaChi(rs.getString(3));
                ncc.setDienThoai(rs.getString(4));
                ncc.setCreatedAt(rs.getTimestamp(5));
                ncc.setUpdatedAt(rs.getTimestamp(6));
            }
        } catch (SQLException ex) {
            return null;
        }
        return ncc;
    }

    public boolean addNCC(NhaCungCap ncc) {
        boolean result = false;
        try {
            String sql = "INSERT INTO nhacungcap(MaNCC, TenNCC, DiaChi, DienThoai, CreatedAt, UpdatedAt) VALUES(?,?,?,?,?,?)";
            PreparedStatement prep = MyConnect.conn.prepareStatement(sql);
            prep.setInt(1, ncc.getMaNCC());
            prep.setString(2, ncc.getTenNCC());
            prep.setString(3, ncc.getDiaChi());
            prep.setString(4, ncc.getDienThoai());
            prep.setTimestamp(5, ncc.getCreatedAt());
            prep.setTimestamp(6, ncc.getUpdatedAt());
            result = prep.executeUpdate() > 0;
        } catch (SQLException ex) {
            String methodName = Thread.currentThread().getStackTrace()[1].getMethodName();
            System.out.println("Error occurred in method: " + methodName);
            System.out.println(ex);
            return false;
        }
        return result;
    }

    public boolean updateNCC(NhaCungCap ncc) {
        boolean result = false;
        try {
            String sql = "UPDATE nhacungcap SET TenNCC=?, DiaChi=?, DienThoai=?, UpdatedAt=? WHERE MaNCC=?";
            PreparedStatement prep = MyConnect.conn.prepareStatement(sql);
            prep.setString(1, ncc.getTenNCC());
            prep.setString(2, ncc.getDiaChi());
            prep.setString(3, ncc.getDienThoai());
            prep.setTimestamp(4, ncc.getUpdatedAt());
            prep.setInt(5, ncc.getMaNCC());
            result = prep.executeUpdate() > 0;
        } catch (SQLException ex) {
            ex.printStackTrace();
            return false;
        }
        return result;
    }

    public boolean deleteNCC(int maNCC) {
        boolean result = false;
        try {
            String sql = "DELETE FROM nhacungcap WHERE MaNCC=" + maNCC;
            Statement stmt = MyConnect.conn.createStatement();
            result = stmt.executeUpdate(sql) > 0;
        } catch (SQLException ex) {
            return false;
        }
        return result;
    }
}
