package models;


import java.util.Objects;

public class Login {
    private String tenDangNhap;
    private String matKhau;

    public Login() {
        tenDangNhap = "admin";
        matKhau = "123456";
    }

    public Login(String tenDangNhap, String matKhau) {
        this.tenDangNhap = tenDangNhap;
        this.matKhau = matKhau;
    }

    public String getTenDangNhap() {
        return tenDangNhap;
    }

    public void setTenDangNhap(String tenDangNhap) {
        this.tenDangNhap = tenDangNhap;
    }

    public String getMatKhau() {
        return matKhau;
    }

    public void setMatKhau(String matKhau) {
        this.matKhau = matKhau;
    }

    @Override
    public int hashCode() {
        int hash = 7;
        hash = 97 * hash + Objects.hashCode(this.tenDangNhap);
        hash = 97 * hash + Objects.hashCode(this.matKhau);
        return hash;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final Login other = (Login) obj;
        if (!Objects.equals(this.tenDangNhap, other.tenDangNhap)) {
            return false;
        }
        return Objects.equals(this.matKhau, other.matKhau);
    }
    
}
