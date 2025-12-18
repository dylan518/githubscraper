package com.mycompany.java.project.pages;
import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.sql.SQLException;
import java.util.ArrayList;
import com.mycompany.java.project.classes.User;
import com.mycompany.java.project.classes.Book;
import com.mycompany.java.project.classes.customs.exceptions.JBookException;
import com.mycompany.java.project.interfaces.PageHandling;
import com.mycompany.java.project.interfaces.ImageConstants;
import com.mycompany.java.project.interfaces.InstanceProvider;
import com.mycompany.java.project.db.controllers.UserController;
import com.mycompany.java.project.db.controllers.BookController;
import com.mycompany.java.project.db.Authorization;

public class Home extends javax.swing.JFrame implements PageHandling, InstanceProvider<Home> {
    public Home(User user, ArrayList<Book> books) {
        
        this.user = user;
        this.books = books;
        //
        this.updateBookData();

        initComponents();
        this.setLocationRelativeTo(null);

        this.panels[0] = this.jPanel4;
        this.panels[1] = this.jPanel3;
        this.panels[2] = this.jPanel5;
        this.panels[3] = this.jPanel6;
        this.panels[4] = this.jPanel7;
        this.panels[5] = this.jPanel8;

        this.showUserInfo();
        this.showBooks();
        this.setPage();
        this.display();
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        userAvatar = new javax.swing.JPanel();
        addButton = new javax.swing.JButton();
        editButton = new javax.swing.JButton();
        deleteButton = new javax.swing.JButton();
        saleButton = new javax.swing.JButton();
        salesHistoryButton = new javax.swing.JButton();
        userSettingButton = new javax.swing.JButton();
        logoutButton = new javax.swing.JButton();
        username = new javax.swing.JLabel();
        email = new javax.swing.JLabel();
        filler1 = new javax.swing.Box.Filler(new java.awt.Dimension(0, 0), new java.awt.Dimension(0, 0), new java.awt.Dimension(32767, 0));
        jPanel3 = new javax.swing.JPanel();
        jLabel3 = new javax.swing.JLabel();
        jPanel4 = new javax.swing.JPanel();
        jPanel5 = new javax.swing.JPanel();
        jPanel6 = new javax.swing.JPanel();
        jPanel7 = new javax.swing.JPanel();
        jPanel8 = new javax.swing.JPanel();
        prevButton = new javax.swing.JButton();
        pageCount = new javax.swing.JLabel();
        nextButton = new javax.swing.JButton();
        lastButton = new javax.swing.JButton();
        firstButton = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Home page");
        setResizable(false);
        setSize(new java.awt.Dimension(1920, 1080));

        jPanel1.setBackground(new java.awt.Color(27, 26, 26));
        jPanel1.setPreferredSize(new java.awt.Dimension(300, 100));

        userAvatar.setToolTipText("");
        userAvatar.setDoubleBuffered(false);

        javax.swing.GroupLayout userAvatarLayout = new javax.swing.GroupLayout(userAvatar);
        userAvatar.setLayout(userAvatarLayout);
        userAvatarLayout.setHorizontalGroup(
            userAvatarLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 118, Short.MAX_VALUE)
        );
        userAvatarLayout.setVerticalGroup(
            userAvatarLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 106, Short.MAX_VALUE)
        );

        addButton.setBackground(new java.awt.Color(0, 0, 0));
        addButton.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        addButton.setForeground(new java.awt.Color(255, 255, 255));
        addButton.setText("Add");
        addButton.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        addButton.setPreferredSize(new java.awt.Dimension(200, 200));
        addButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                addButtonActionPerformed(evt);
            }
        });

        editButton.setBackground(new java.awt.Color(0, 0, 0));
        editButton.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        editButton.setForeground(new java.awt.Color(255, 255, 255));
        editButton.setText("Edit");
        editButton.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        editButton.setPreferredSize(new java.awt.Dimension(200, 200));
        editButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                editButtonActionPerformed(evt);
            }
        });

        deleteButton.setBackground(new java.awt.Color(0, 0, 0));
        deleteButton.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        deleteButton.setForeground(new java.awt.Color(255, 255, 255));
        deleteButton.setText("Delete");
        deleteButton.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        deleteButton.setPreferredSize(new java.awt.Dimension(200, 200));
        deleteButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                deleteButtonActionPerformed(evt);
            }
        });

        saleButton.setBackground(new java.awt.Color(0, 0, 0));
        saleButton.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        saleButton.setForeground(new java.awt.Color(255, 255, 255));
        saleButton.setText("Sale");
        saleButton.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        saleButton.setPreferredSize(new java.awt.Dimension(200, 200));
        saleButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                saleButtonActionPerformed(evt);
            }
        });

        salesHistoryButton.setBackground(new java.awt.Color(0, 0, 0));
        salesHistoryButton.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        salesHistoryButton.setForeground(new java.awt.Color(255, 255, 255));
        salesHistoryButton.setText("Sales history");
        salesHistoryButton.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        salesHistoryButton.setPreferredSize(new java.awt.Dimension(200, 200));
        salesHistoryButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                salesHistoryButtonActionPerformed(evt);
            }
        });

        userSettingButton.setBackground(new java.awt.Color(0, 0, 0));
        userSettingButton.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        userSettingButton.setForeground(new java.awt.Color(255, 255, 255));
        userSettingButton.setText("User settings");
        userSettingButton.setToolTipText("");
        userSettingButton.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        userSettingButton.setPreferredSize(new java.awt.Dimension(200, 200));
        userSettingButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                userSettingButtonActionPerformed(evt);
            }
        });

        logoutButton.setBackground(new java.awt.Color(255, 0, 0));
        logoutButton.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        logoutButton.setForeground(new java.awt.Color(255, 255, 255));
        logoutButton.setText("Logout");
        logoutButton.setBorder(null);
        logoutButton.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        logoutButton.setPreferredSize(new java.awt.Dimension(200, 200));
        logoutButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                logoutButtonActionPerformed(evt);
            }
        });

        username.setFont(new java.awt.Font("Leelawadee UI", 0, 14)); // NOI18N
        username.setForeground(new java.awt.Color(255, 255, 255));
        username.setText("Username:");

        email.setFont(new java.awt.Font("Leelawadee UI", 0, 14)); // NOI18N
        email.setForeground(new java.awt.Color(255, 255, 255));
        email.setText("Email:");

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGap(41, 41, 41)
                        .addComponent(userAvatar, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGap(22, 22, 22)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addComponent(saleButton, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.PREFERRED_SIZE, 152, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                .addComponent(userSettingButton, javax.swing.GroupLayout.DEFAULT_SIZE, 152, Short.MAX_VALUE)
                                .addComponent(salesHistoryButton, javax.swing.GroupLayout.PREFERRED_SIZE, 0, Short.MAX_VALUE)
                                .addComponent(deleteButton, javax.swing.GroupLayout.PREFERRED_SIZE, 0, Short.MAX_VALUE)
                                .addComponent(editButton, javax.swing.GroupLayout.PREFERRED_SIZE, 0, Short.MAX_VALUE)
                                .addComponent(addButton, javax.swing.GroupLayout.PREFERRED_SIZE, 0, Short.MAX_VALUE)
                                .addComponent(logoutButton, javax.swing.GroupLayout.DEFAULT_SIZE, 152, Short.MAX_VALUE)
                                .addComponent(username, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                .addComponent(email, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))))
                .addGap(54, 54, 54))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGap(36, 36, 36)
                .addComponent(userAvatar, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addComponent(username)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(email)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(addButton, javax.swing.GroupLayout.PREFERRED_SIZE, 33, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(editButton, javax.swing.GroupLayout.PREFERRED_SIZE, 33, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(deleteButton, javax.swing.GroupLayout.PREFERRED_SIZE, 34, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(saleButton, javax.swing.GroupLayout.PREFERRED_SIZE, 36, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(salesHistoryButton, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(userSettingButton, javax.swing.GroupLayout.PREFERRED_SIZE, 36, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(logoutButton, javax.swing.GroupLayout.PREFERRED_SIZE, 34, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(38, Short.MAX_VALUE))
        );

        jPanel3.setBackground(new java.awt.Color(217, 217, 217));
        jPanel3.setBorder(new javax.swing.border.LineBorder(new java.awt.Color(0, 0, 0), 3, true));
        jPanel3.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        jPanel3.setPreferredSize(new java.awt.Dimension(218, 130));

        javax.swing.GroupLayout jPanel3Layout = new javax.swing.GroupLayout(jPanel3);
        jPanel3.setLayout(jPanel3Layout);
        jPanel3Layout.setHorizontalGroup(
            jPanel3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 140, Short.MAX_VALUE)
        );
        jPanel3Layout.setVerticalGroup(
            jPanel3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 196, Short.MAX_VALUE)
        );

        jLabel3.setFont(new java.awt.Font("Leelawadee", 0, 36)); // NOI18N
        jLabel3.setText("JBook Store");

        jPanel4.setBackground(new java.awt.Color(217, 217, 217));
        jPanel4.setBorder(new javax.swing.border.LineBorder(new java.awt.Color(0, 0, 0), 3, true));
        jPanel4.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        jPanel4.setPreferredSize(new java.awt.Dimension(218, 130));

        javax.swing.GroupLayout jPanel4Layout = new javax.swing.GroupLayout(jPanel4);
        jPanel4.setLayout(jPanel4Layout);
        jPanel4Layout.setHorizontalGroup(
            jPanel4Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 140, Short.MAX_VALUE)
        );
        jPanel4Layout.setVerticalGroup(
            jPanel4Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 196, Short.MAX_VALUE)
        );

        jPanel5.setBackground(new java.awt.Color(217, 217, 217));
        jPanel5.setBorder(new javax.swing.border.LineBorder(new java.awt.Color(0, 0, 0), 3, true));
        jPanel5.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        jPanel5.setPreferredSize(new java.awt.Dimension(218, 130));

        javax.swing.GroupLayout jPanel5Layout = new javax.swing.GroupLayout(jPanel5);
        jPanel5.setLayout(jPanel5Layout);
        jPanel5Layout.setHorizontalGroup(
            jPanel5Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 140, Short.MAX_VALUE)
        );
        jPanel5Layout.setVerticalGroup(
            jPanel5Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 196, Short.MAX_VALUE)
        );

        jPanel6.setBackground(new java.awt.Color(217, 217, 217));
        jPanel6.setBorder(new javax.swing.border.LineBorder(new java.awt.Color(0, 0, 0), 3, true));
        jPanel6.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        jPanel6.setPreferredSize(new java.awt.Dimension(218, 130));

        javax.swing.GroupLayout jPanel6Layout = new javax.swing.GroupLayout(jPanel6);
        jPanel6.setLayout(jPanel6Layout);
        jPanel6Layout.setHorizontalGroup(
            jPanel6Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 140, Short.MAX_VALUE)
        );
        jPanel6Layout.setVerticalGroup(
            jPanel6Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 196, Short.MAX_VALUE)
        );

        jPanel7.setBackground(new java.awt.Color(217, 217, 217));
        jPanel7.setBorder(new javax.swing.border.LineBorder(new java.awt.Color(0, 0, 0), 3, true));
        jPanel7.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        jPanel7.setPreferredSize(new java.awt.Dimension(218, 130));

        javax.swing.GroupLayout jPanel7Layout = new javax.swing.GroupLayout(jPanel7);
        jPanel7.setLayout(jPanel7Layout);
        jPanel7Layout.setHorizontalGroup(
            jPanel7Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 140, Short.MAX_VALUE)
        );
        jPanel7Layout.setVerticalGroup(
            jPanel7Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 196, Short.MAX_VALUE)
        );

        jPanel8.setBackground(new java.awt.Color(217, 217, 217));
        jPanel8.setBorder(new javax.swing.border.LineBorder(new java.awt.Color(0, 0, 0), 3, true));
        jPanel8.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        jPanel8.setPreferredSize(new java.awt.Dimension(218, 130));

        javax.swing.GroupLayout jPanel8Layout = new javax.swing.GroupLayout(jPanel8);
        jPanel8.setLayout(jPanel8Layout);
        jPanel8Layout.setHorizontalGroup(
            jPanel8Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 140, Short.MAX_VALUE)
        );
        jPanel8Layout.setVerticalGroup(
            jPanel8Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 196, Short.MAX_VALUE)
        );

        prevButton.setBackground(new java.awt.Color(0, 0, 0));
        prevButton.setFont(new java.awt.Font("Leelawadee UI", 0, 18)); // NOI18N
        prevButton.setForeground(new java.awt.Color(255, 255, 255));
        prevButton.setText("Prev page");
        prevButton.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        prevButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                prevButtonActionPerformed(evt);
            }
        });

        pageCount.setFont(new java.awt.Font("Leelawadee UI", 0, 18)); // NOI18N
        pageCount.setText("1/-");

        nextButton.setBackground(new java.awt.Color(0, 0, 0));
        nextButton.setFont(new java.awt.Font("Leelawadee UI", 0, 18)); // NOI18N
        nextButton.setForeground(new java.awt.Color(255, 255, 255));
        nextButton.setText("Next page");
        nextButton.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        nextButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                nextButtonActionPerformed(evt);
            }
        });

        lastButton.setBackground(new java.awt.Color(0, 0, 0));
        lastButton.setFont(new java.awt.Font("Leelawadee UI", 0, 18)); // NOI18N
        lastButton.setForeground(new java.awt.Color(255, 255, 255));
        lastButton.setText("Last page");
        lastButton.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        lastButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                lastButtonActionPerformed(evt);
            }
        });

        firstButton.setBackground(new java.awt.Color(0, 0, 0));
        firstButton.setFont(new java.awt.Font("Leelawadee UI", 0, 18)); // NOI18N
        firstButton.setForeground(new java.awt.Color(255, 255, 255));
        firstButton.setText("First page");
        firstButton.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        firstButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                firstButtonActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, 200, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(jLabel3)
                        .addGap(217, 217, 217))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                        .addGap(66, 66, 66)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                                    .addGroup(layout.createSequentialGroup()
                                        .addComponent(jPanel7, javax.swing.GroupLayout.PREFERRED_SIZE, 146, javax.swing.GroupLayout.PREFERRED_SIZE)
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                        .addComponent(jPanel6, javax.swing.GroupLayout.PREFERRED_SIZE, 146, javax.swing.GroupLayout.PREFERRED_SIZE))
                                    .addGroup(layout.createSequentialGroup()
                                        .addComponent(jPanel4, javax.swing.GroupLayout.PREFERRED_SIZE, 146, javax.swing.GroupLayout.PREFERRED_SIZE)
                                        .addGap(44, 44, 44)
                                        .addComponent(jPanel3, javax.swing.GroupLayout.PREFERRED_SIZE, 146, javax.swing.GroupLayout.PREFERRED_SIZE)))
                                .addGap(42, 42, 42)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jPanel5, javax.swing.GroupLayout.PREFERRED_SIZE, 146, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jPanel8, javax.swing.GroupLayout.PREFERRED_SIZE, 146, javax.swing.GroupLayout.PREFERRED_SIZE)))
                            .addGroup(layout.createSequentialGroup()
                                .addComponent(firstButton)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                                    .addComponent(filler1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addGroup(layout.createSequentialGroup()
                                        .addComponent(prevButton)
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                        .addComponent(pageCount)
                                        .addGap(18, 18, 18)
                                        .addComponent(nextButton)
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                        .addComponent(lastButton)))))
                        .addGap(35, 53, Short.MAX_VALUE))))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, 572, Short.MAX_VALUE)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addGroup(layout.createSequentialGroup()
                        .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(prevButton)
                            .addComponent(pageCount)
                            .addComponent(nextButton)
                            .addComponent(lastButton)
                            .addComponent(firstButton)))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(14, 14, 14)
                        .addComponent(jLabel3)
                        .addGap(18, 18, 18)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jPanel3, javax.swing.GroupLayout.PREFERRED_SIZE, 202, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(jPanel4, javax.swing.GroupLayout.PREFERRED_SIZE, 202, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(jPanel5, javax.swing.GroupLayout.PREFERRED_SIZE, 202, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(18, 18, 18)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jPanel7, javax.swing.GroupLayout.PREFERRED_SIZE, 202, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(jPanel6, javax.swing.GroupLayout.PREFERRED_SIZE, 202, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(jPanel8, javax.swing.GroupLayout.PREFERRED_SIZE, 202, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(filler1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addGap(17, 17, 17))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void userSettingButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_userSettingButtonActionPerformed
        Usersetting usersetting = new Usersetting(this.user.getInstance(), () -> {
            try {
                UserController userController = new UserController();
                if(Authorization.isLoggedIn){
                    this.user = userController.getUser("SELECT * FROM users WHERE user_id = " + Authorization.authorizedUserId);
                    this.showUserInfo();
                } else {
                    Authorization.accessDenied(this.getInstance());
                    this.user = null;
                    Login login = new Login();
                }
            } catch(SQLException | JBookException e){
                JOptionPane.showMessageDialog(this.getInstance(), e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
                e.printStackTrace();
            }
        });
    }//GEN-LAST:event_userSettingButtonActionPerformed

    private void logoutButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_logoutButtonActionPerformed
        Authorization.accessDenied(this.getInstance());
        this.user = null;
        Login login = new Login();
    }//GEN-LAST:event_logoutButtonActionPerformed

    private void addButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_addButtonActionPerformed
        if(Authorization.isLoggedIn){
            AddBook addBook = new AddBook(() -> {
                this.fetchBooks();
                this.updateBookData();
                this.showBooks();
                this.setPage();
            });
        } else {
            Authorization.accessDenied(this.getInstance());
            this.user = null;
            Login login = new Login();
        }
    }//GEN-LAST:event_addButtonActionPerformed

    private void deleteButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_deleteButtonActionPerformed
        if(Authorization.isLoggedIn){
            DeleteBook deleteBook = new DeleteBook(() -> {
                this.fetchBooks();
                this.updateBookData();
                this.showBooks();
                this.setPage();
            });
        } else {
            Authorization.accessDenied(this.getInstance());
            this.user = null;
            Login login = new Login();
        }
    }//GEN-LAST:event_deleteButtonActionPerformed

    private void saleButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_saleButtonActionPerformed
        if(Authorization.isLoggedIn){
            Sale sale = new Sale(this.books, () -> {
                this.fetchBooks();
                this.updateBookData();
                this.showBooks();
                this.setPage();
            });
        } else {
            Authorization.accessDenied(this.getInstance());
            this.user = null;
            Login login = new Login();
        }
    }//GEN-LAST:event_saleButtonActionPerformed

    private void editButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_editButtonActionPerformed
        if(Authorization.isLoggedIn){
            EditBook editBook = new EditBook(this.books, () -> {
                this.fetchBooks();
                this.updateBookData();
                this.showBooks();
            });
        } else {
            Authorization.accessDenied(this.getInstance());
            this.user = null;
            Login login = new Login();
        }
    }//GEN-LAST:event_editButtonActionPerformed

    private void salesHistoryButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_salesHistoryButtonActionPerformed
        if(Authorization.isLoggedIn){
            SalesHistory salesHistory = new SalesHistory();
        } else {
            Authorization.accessDenied(this.getInstance());
            this.user = null;
            Login login = new Login();
        }
    }//GEN-LAST:event_salesHistoryButtonActionPerformed

    private void prevButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_prevButtonActionPerformed
        if(this.getCurrentIndex() >= 0 && this.getCurrentIndex() <= this.getLastIndex() && (this.getCurrentIndex() - 1) >= 0) {
            this.setCurrentIndex(this.getCurrentIndex() - 1);
            this.showBooks();
            this.setPage();
        }
    }//GEN-LAST:event_prevButtonActionPerformed

    private void nextButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_nextButtonActionPerformed
        if(this.getCurrentIndex() >= 0 && this.getCurrentIndex() <= this.getLastIndex() && (this.getCurrentIndex() + 1) <= this.getLastIndex()){
            this.setCurrentIndex(this.getCurrentIndex() + 1);
            this.showBooks();
            this.setPage();
        }
    }//GEN-LAST:event_nextButtonActionPerformed

    private void lastButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_lastButtonActionPerformed
        if(this.getCurrentIndex() == (this.bookSets.size() - 1)){
            return;
        }

        this.setCurrentIndex(this.bookSets.size() - 1);
        this.showBooks();
        this.setPage();
    }//GEN-LAST:event_lastButtonActionPerformed

    private void firstButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_firstButtonActionPerformed
        if(this.getCurrentIndex() == 0){
            return;
        }

        this.setCurrentIndex(0);
        this.showBooks();
        this.setPage();
    }//GEN-LAST:event_firstButtonActionPerformed

    private void fetchBooks(){
        try {
            BookController bookController = new BookController();
            this.books = bookController.getBooks("SELECT * FROM books");
        } catch(SQLException | JBookException e){
            e.printStackTrace();
        }
    }

    private void updateBookData(){
        //2d Array เก็บข้อมูลประเภทหนังสือ
        this.bookSets = new ArrayList<ArrayList<Book>>();
        //1d Array เก็บข้อมูลประเภทหนังสือ
        ArrayList<Book> set = new ArrayList<Book>();
        //loop 2d Array  
        for(int i = 0; i < this.books.size(); i++){
            //add ข้อมูลหนังสือลงArray
            set.add(this.books.get(i));
            if((i + 1) % 6 == 0){
                //add Arrayของข้อมูลหนังสือลงArray
                this.bookSets.add(set);
                //สร้าง Arrayของข้อมูลหนังสือ
                set = new ArrayList<Book>();
            }
        }
        
        if(set.size() != 0){
            this.bookSets.add(set);
        }
        //ตั้งค่าindexสุดท้าย
        this.setLastIndex(this.bookSets.size() - 1);
    }

    private void showUserInfo(){
        ImageConstants.addImage(this.user.getAvatar(), this.userAvatar, ImageConstants.DEFAULT_USER_AVATAR);
        this.username.setText("Username: " + this.user.getUsername());
        this.email.setText("Email: " + this.user.getEmail());
    }

    private void showBooks(){
        for(int i = 0; i < this.panels.length; i++){
            if(this.panels[i].getComponentCount() > 0){
                this.panels[i].removeAll();
            }

            if(this.panels[i].getMouseListeners().length > 0){
                for(MouseListener ml : this.panels[i].getMouseListeners()){
                    this.panels[i].removeMouseListener(ml);
                }
            }
        }

        int bookCount = 0;
        try {
            bookCount = this.bookSets.get(this.getCurrentIndex()).size() == 0 ?
                    this.bookSets.get(this.getCurrentIndex() - 1).size() :
                    this.bookSets.get(this.getCurrentIndex()).size();
        } catch(IndexOutOfBoundsException e){
            this.setCurrentIndex(this.getCurrentIndex() - 1);
            bookCount = this.bookSets.get(this.getCurrentIndex()).size();
        }

        for(int j = 0; j < bookCount; j++){
            ImageConstants.addImage(this.bookSets.get(this.getCurrentIndex()).get(j).getImageUrl(), this.panels[j], ImageConstants.DEFAULT_IMAGE_NOT_AVALIBLE);
            this.panels[j].add(new JLabel(this.bookSets.get(this.getCurrentIndex()).get(j).getBookName(), SwingConstants.CENTER), BorderLayout.SOUTH);

            int k = j;
            this.panels[j].addMouseListener(new MouseAdapter() {
                @Override
                public void mouseClicked(MouseEvent e) {
                    Preview.showPreview(k, bookSets.get(currentIndex).get(k), bookSets.get(currentIndex), () -> {
                        fetchBooks();
                        updateBookData();
                        showBooks();
                        setPage();
                    });
                }
            });
        }

        for(int v = 0; v < this.panels.length; v++){
            if(this.panels[v].getComponentCount() > 0){
                continue;
            }

            for(MouseListener ml : this.panels[v].getMouseListeners()){
                this.panels[v].removeMouseListener(ml);
            }

            ImageConstants.addImage(ImageConstants.DEFAULT_NO_IMAGE, this.panels[v], ImageConstants.DEFAULT_NO_IMAGE);
            this.panels[v].addMouseListener(new MouseAdapter() {
                @Override
                public void mouseClicked(MouseEvent e) {
                    addButtonActionPerformed(null);
                }
            });
        }
    }

    private int getCurrentIndex(){
        return this.currentIndex;
    }

    private Home setCurrentIndex(int currentIndex){
        if(currentIndex >= 0){
            this.currentIndex = currentIndex;
        }

        return this.getInstance();
    }

    private int getLastIndex(){
        return this.lastIndex;
    }

    private Home setLastIndex(int lastIndex){
        if(lastIndex >= 0){
            this.lastIndex = lastIndex;
        }

        return this.getInstance();
    }

    private Home setPage(){
        this.pageCount.setText((this.getCurrentIndex() + 1) + "/" + (this.getLastIndex() + 1));
        return this.getInstance();
    }

    @Override
    public void display(){
        this.setVisible(true);
    }

    @Override
    public void destroy(){
        this.dispose();
    }

    @Override
    public Home getInstance(){
        return this;
    }

    //run main ของหน้า Home
    public static void main(String []args){
        try {
            //set login เป็น จริง
            Authorization.isLoggedIn = true;
            //เตรียมโหลด database ข้อมูลหนังสือ
            UserController userController = new UserController();
            //เตรียมโหลด database ข้อมูลUser
            BookController bookController = new BookController();
            //โหลด ข้อมูลUser จาก User
            User user = userController.getUser("SELECT * FROM users WHERE username = 'root'");
            //set UserId จาก ข้อมูลUser
            Authorization.authorizedUserId = user.getUserId();
            //โหลดเก็บArray ของข้อมูลหนังสือ เพื่อใช้เเสดงผล
            ArrayList<Book> books = bookController.getBooks("SELECT * FROM books");
            //refresh หน้า Home
            Home home = new Home(user, books);

        } catch(JBookException | SQLException e){
            e.printStackTrace();
            //login ใหม่
            Login login = new Login();
        }
    }

    private User user = null;
    private ArrayList<Book> books = null;
    private JPanel []panels = new JPanel[6];
    private int currentIndex = 0;
    private ArrayList<ArrayList<Book>> bookSets = new ArrayList<ArrayList<Book>>();
    private final int LIMITED = 6;
    private int lastIndex;
    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton addButton;
    private javax.swing.JButton deleteButton;
    private javax.swing.JButton editButton;
    private javax.swing.JLabel email;
    private javax.swing.Box.Filler filler1;
    private javax.swing.JButton firstButton;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPanel jPanel3;
    private javax.swing.JPanel jPanel4;
    private javax.swing.JPanel jPanel5;
    private javax.swing.JPanel jPanel6;
    private javax.swing.JPanel jPanel7;
    private javax.swing.JPanel jPanel8;
    private javax.swing.JButton lastButton;
    private javax.swing.JButton logoutButton;
    private javax.swing.JButton nextButton;
    private javax.swing.JLabel pageCount;
    private javax.swing.JButton prevButton;
    private javax.swing.JButton saleButton;
    private javax.swing.JButton salesHistoryButton;
    private javax.swing.JPanel userAvatar;
    private javax.swing.JButton userSettingButton;
    private javax.swing.JLabel username;
    // End of variables declaration//GEN-END:variables
}