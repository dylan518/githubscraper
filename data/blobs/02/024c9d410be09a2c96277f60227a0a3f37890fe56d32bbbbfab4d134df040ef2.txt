package com.example.Buoi_9.controller;

import com.example.Buoi_9.entity.CuaHang;


import com.example.Buoi_9.repository.CuaHangRepository;
import jakarta.servlet.*;
import jakarta.servlet.http.*;
import jakarta.servlet.annotation.*;

import java.io.IOException;
import java.util.List;

@WebServlet(name = "CuaHangServlet", value = {"/cua-hang/hien-thi","/cua-hang/add","/cua-hang/update","/cua-hang/delete","/cua-hang/detail"})
public class CuaHangServlet extends HttpServlet {
    private CuaHangRepository cuaHangRepository = new CuaHangRepository();
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String uri = request.getRequestURI();
        if (uri.contains("hien-thi")) {
            List<CuaHang> list = cuaHangRepository.getAll();
            request.setAttribute("list", list);
            request.getRequestDispatcher("/views/cuahang.jsp").forward(request, response);
        }else if (uri.contains("detail")) {
            String id = request.getParameter("id");
            CuaHang cuaHang = cuaHangRepository.getById(id);
            request.setAttribute("ch", cuaHang);
//            System.out.println(khachHang.getNgaySinh());
//            String ngaySinh = dateFormat.format(khachHang.getNgaySinh());
//            request.setAttribute("ngaySinh", ngaySinh);
            List<CuaHang> list = cuaHangRepository.getAll();
            request.setAttribute("list", list);
            request.getRequestDispatcher("/views/cuahang.jsp").forward(request, response);

        } else if (uri.contains("delete")) {
            String id = request.getParameter("id");
            this.cuaHangRepository.delete(id);
            response.sendRedirect("/cua-hang/hien-thi");
        }
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String uri = request.getRequestURI();
        if (uri.contains("add")) {
            String ma = request.getParameter("ma");
            String ten = request.getParameter("ten");
            String diaChi = request.getParameter("diaChi");
            String thanhPho = request.getParameter("thanhPho");
            String quocGia = request.getParameter("quocGia");
            CuaHang cuaHang = new CuaHang();
            cuaHang.setMa(ma);
            cuaHang.setTen(ten);
            cuaHang.setDiaChi(diaChi);
            cuaHang.setThanhPho(thanhPho);
            cuaHang.setQuocGia(quocGia);
            this.cuaHangRepository.add(cuaHang);
            response.sendRedirect("/cua-hang/hien-thi");
        } else if (uri.contains("update")) {
            String id = request.getParameter("id");
            String ma = request.getParameter("ma");
            String ten = request.getParameter("ten");
            String diaChi = request.getParameter("diaChi");
            String thanhPho = request.getParameter("thanhPho");
            String quocGia = request.getParameter("quocGia");
            CuaHang cuaHang = new CuaHang();
            cuaHang.setId(id);
            cuaHang.setMa(ma);
            cuaHang.setTen(ten);
            cuaHang.setDiaChi(diaChi);
            cuaHang.setThanhPho(thanhPho);
            cuaHang.setQuocGia(quocGia);
            this.cuaHangRepository.update(cuaHang);
            response.sendRedirect("/cua-hang/hien-thi");
        }
    }
}
