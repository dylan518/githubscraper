
package halallabirintus;

import java.awt.HeadlessException;
import javax.swing.ImageIcon;
import javax.swing.JOptionPane;

public class HalalLabirintus extends javax.swing.JFrame {

    public HalalLabirintus() {
        initComponents();
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jtp_alap = new javax.swing.JTabbedPane();
        jp_kezdo = new javax.swing.JPanel();
        pnl_halallabirintus = new javax.swing.JPanel();
        btn_kilepes = new javax.swing.JButton();
        lbl_cim = new javax.swing.JLabel();
        lbl_kep = new javax.swing.JLabel();
        pnl_tortenet = new javax.swing.JPanel();
        btn_sugo = new javax.swing.JButton();
        lbl_tortenet = new javax.swing.JLabel();
        scr_leiras = new javax.swing.JScrollPane();
        txtp_leiras = new javax.swing.JTextPane();
        jButton6 = new javax.swing.JButton();
        jp_kaland = new javax.swing.JPanel();
        pnl_stat = new javax.swing.JPanel();
        lbl_stat = new javax.swing.JLabel();
        lbl_ugyesseg = new javax.swing.JLabel();
        lbl_ugyessegpont = new javax.swing.JLabel();
        btn_ugyesseg = new javax.swing.JButton();
        lbl_eletero = new javax.swing.JLabel();
        lbl_eleteropont = new javax.swing.JLabel();
        btn_eletero = new javax.swing.JButton();
        lbl_szerencse = new javax.swing.JLabel();
        lbl_szerencsepont = new javax.swing.JLabel();
        btn_szerencse = new javax.swing.JButton();
        pnl_karakter = new javax.swing.JPanel();
        lbl_nev = new javax.swing.JLabel();
        txt_nev = new javax.swing.JTextField();
        lbl_karakterkep = new javax.swing.JLabel();
        btn_vissza = new javax.swing.JButton();
        btn_elore = new javax.swing.JButton();
        chk_karakter = new javax.swing.JCheckBox();
        pnl_hatizsak = new javax.swing.JPanel();
        lbl_hatizsak = new javax.swing.JLabel();
        scr_hatizsak = new javax.swing.JScrollPane();
        txt_hatizsak = new javax.swing.JTextPane();
        btn_kaland = new javax.swing.JButton();
        jp_sztori = new javax.swing.JPanel();
        pnl_sztorihatter = new javax.swing.JPanel();
        lbl_sztorikep = new javax.swing.JLabel();
        pnl_sztori = new javax.swing.JPanel();
        jLabel1 = new javax.swing.JLabel();
        jScrollPane1 = new javax.swing.JScrollPane();
        txt_tortenet = new javax.swing.JTextPane();
        btn_valasztas_jobb = new javax.swing.JButton();
        btn_valasztas_bal = new javax.swing.JButton();
        menu = new javax.swing.JMenuBar();
        m_fajl = new javax.swing.JMenu();
        m_mentes = new javax.swing.JMenuItem();
        menu_ujrakezdes = new javax.swing.JMenuItem();
        jSeparator1 = new javax.swing.JPopupMenu.Separator();
        m_kilepes = new javax.swing.JMenuItem();
        m_beallitasok = new javax.swing.JMenu();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Halállabirintus");
        addWindowListener(new java.awt.event.WindowAdapter() {
            public void windowClosing(java.awt.event.WindowEvent evt) {
                formWindowClosing(evt);
            }
        });

        jtp_alap.setForeground(new java.awt.Color(255, 255, 255));
        jtp_alap.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jtp_alapMouseClicked(evt);
            }
        });

        jp_kezdo.setBackground(new java.awt.Color(255, 255, 255));

        pnl_halallabirintus.setBackground(new java.awt.Color(171, 125, 95));
        pnl_halallabirintus.setBorder(javax.swing.BorderFactory.createLineBorder(null));

        btn_kilepes.setText("Kilépés");
        btn_kilepes.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btn_kilepesActionPerformed(evt);
            }
        });

        lbl_cim.setFont(new java.awt.Font("Edwardian Script ITC", 1, 36)); // NOI18N
        lbl_cim.setForeground(new java.awt.Color(255, 255, 255));
        lbl_cim.setText("Halál Labirintus");

        lbl_kep.setIcon(new javax.swing.ImageIcon(getClass().getResource("/halallabirintus/menű 1.png"))); // NOI18N

        javax.swing.GroupLayout pnl_halallabirintusLayout = new javax.swing.GroupLayout(pnl_halallabirintus);
        pnl_halallabirintus.setLayout(pnl_halallabirintusLayout);
        pnl_halallabirintusLayout.setHorizontalGroup(
            pnl_halallabirintusLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pnl_halallabirintusLayout.createSequentialGroup()
                .addContainerGap()
                .addGroup(pnl_halallabirintusLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(lbl_kep)
                    .addGroup(pnl_halallabirintusLayout.createSequentialGroup()
                        .addGap(22, 22, 22)
                        .addComponent(lbl_cim, javax.swing.GroupLayout.PREFERRED_SIZE, 216, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addComponent(btn_kilepes))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        pnl_halallabirintusLayout.setVerticalGroup(
            pnl_halallabirintusLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pnl_halallabirintusLayout.createSequentialGroup()
                .addContainerGap()
                .addComponent(lbl_cim)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(lbl_kep)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(btn_kilepes)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        pnl_tortenet.setBackground(new java.awt.Color(171, 125, 95));
        pnl_tortenet.setBorder(javax.swing.BorderFactory.createLineBorder(null));

        btn_sugo.setText("Súgó");
        btn_sugo.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btn_sugoActionPerformed(evt);
            }
        });

        lbl_tortenet.setFont(new java.awt.Font("Edwardian Script ITC", 1, 36)); // NOI18N
        lbl_tortenet.setForeground(new java.awt.Color(255, 255, 255));
        lbl_tortenet.setText("Történet:");

        txtp_leiras.setEditable(false);
        txtp_leiras.setBackground(new java.awt.Color(255, 255, 255));
        txtp_leiras.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        txtp_leiras.setText("Egy versenyre nevezel, aminek a lényege, hogy át kell kelni a halállabirintuson. A labirintusban tárgyakat találhatsz és szörnyekkel kell harcoljál.");
        txtp_leiras.setPreferredSize(new java.awt.Dimension(256, 320));
        scr_leiras.setViewportView(txtp_leiras);

        jButton6.setText("Készítsd el a karaktered!");
        jButton6.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton6ActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout pnl_tortenetLayout = new javax.swing.GroupLayout(pnl_tortenet);
        pnl_tortenet.setLayout(pnl_tortenetLayout);
        pnl_tortenetLayout.setHorizontalGroup(
            pnl_tortenetLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pnl_tortenetLayout.createSequentialGroup()
                .addContainerGap()
                .addGroup(pnl_tortenetLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(pnl_tortenetLayout.createSequentialGroup()
                        .addGap(60, 60, 60)
                        .addComponent(lbl_tortenet, javax.swing.GroupLayout.PREFERRED_SIZE, 116, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(70, 76, Short.MAX_VALUE))
                    .addGroup(pnl_tortenetLayout.createSequentialGroup()
                        .addGroup(pnl_tortenetLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(pnl_tortenetLayout.createSequentialGroup()
                                .addComponent(jButton6)
                                .addGap(18, 18, 18)
                                .addComponent(btn_sugo))
                            .addComponent(scr_leiras, javax.swing.GroupLayout.PREFERRED_SIZE, 246, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(0, 0, Short.MAX_VALUE))))
        );
        pnl_tortenetLayout.setVerticalGroup(
            pnl_tortenetLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pnl_tortenetLayout.createSequentialGroup()
                .addContainerGap()
                .addComponent(lbl_tortenet)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(scr_leiras, javax.swing.GroupLayout.PREFERRED_SIZE, 320, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(pnl_tortenetLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(btn_sugo)
                    .addComponent(jButton6))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        javax.swing.GroupLayout jp_kezdoLayout = new javax.swing.GroupLayout(jp_kezdo);
        jp_kezdo.setLayout(jp_kezdoLayout);
        jp_kezdoLayout.setHorizontalGroup(
            jp_kezdoLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jp_kezdoLayout.createSequentialGroup()
                .addContainerGap()
                .addComponent(pnl_halallabirintus, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 91, Short.MAX_VALUE)
                .addComponent(pnl_tortenet, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap())
        );
        jp_kezdoLayout.setVerticalGroup(
            jp_kezdoLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jp_kezdoLayout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jp_kezdoLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                    .addComponent(pnl_halallabirintus, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(pnl_tortenet, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        jtp_alap.addTab("Kezdőlap", jp_kezdo);

        jp_kaland.setBackground(new java.awt.Color(255, 255, 255));

        pnl_stat.setBackground(new java.awt.Color(171, 125, 95));
        pnl_stat.setBorder(javax.swing.BorderFactory.createLineBorder(null));

        lbl_stat.setFont(new java.awt.Font("Edwardian Script ITC", 1, 24)); // NOI18N
        lbl_stat.setForeground(new java.awt.Color(255, 255, 255));
        lbl_stat.setText("Statisztika");

        lbl_ugyesseg.setForeground(new java.awt.Color(255, 255, 255));
        lbl_ugyesseg.setText("Ügyesség:");

        lbl_ugyessegpont.setForeground(new java.awt.Color(255, 255, 255));
        lbl_ugyessegpont.setText("0");

        btn_ugyesseg.setText("Sorsolás");
        btn_ugyesseg.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btn_ugyessegActionPerformed(evt);
            }
        });

        lbl_eletero.setForeground(new java.awt.Color(255, 255, 255));
        lbl_eletero.setText("Életerő:");

        lbl_eleteropont.setForeground(new java.awt.Color(255, 255, 255));
        lbl_eleteropont.setText("0");

        btn_eletero.setText("Sorsolás");
        btn_eletero.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btn_eleteroActionPerformed(evt);
            }
        });

        lbl_szerencse.setForeground(new java.awt.Color(255, 255, 255));
        lbl_szerencse.setText("Szerencse:");

        lbl_szerencsepont.setForeground(new java.awt.Color(255, 255, 255));
        lbl_szerencsepont.setText("0");

        btn_szerencse.setText("Sorsolás");
        btn_szerencse.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btn_szerencseActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout pnl_statLayout = new javax.swing.GroupLayout(pnl_stat);
        pnl_stat.setLayout(pnl_statLayout);
        pnl_statLayout.setHorizontalGroup(
            pnl_statLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pnl_statLayout.createSequentialGroup()
                .addContainerGap()
                .addGroup(pnl_statLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                    .addGroup(javax.swing.GroupLayout.Alignment.LEADING, pnl_statLayout.createSequentialGroup()
                        .addComponent(lbl_eletero)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(lbl_eleteropont, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                    .addGroup(javax.swing.GroupLayout.Alignment.LEADING, pnl_statLayout.createSequentialGroup()
                        .addComponent(lbl_szerencse)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(lbl_szerencsepont, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                    .addGroup(javax.swing.GroupLayout.Alignment.LEADING, pnl_statLayout.createSequentialGroup()
                        .addComponent(lbl_ugyesseg)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(lbl_ugyessegpont, javax.swing.GroupLayout.PREFERRED_SIZE, 80, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 35, Short.MAX_VALUE)
                .addGroup(pnl_statLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(btn_ugyesseg)
                    .addComponent(btn_eletero)
                    .addComponent(btn_szerencse, javax.swing.GroupLayout.Alignment.TRAILING))
                .addContainerGap())
            .addGroup(pnl_statLayout.createSequentialGroup()
                .addGap(74, 74, 74)
                .addComponent(lbl_stat, javax.swing.GroupLayout.PREFERRED_SIZE, 88, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        pnl_statLayout.setVerticalGroup(
            pnl_statLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, pnl_statLayout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(lbl_stat)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(pnl_statLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(lbl_ugyesseg)
                    .addComponent(lbl_ugyessegpont)
                    .addComponent(btn_ugyesseg))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(pnl_statLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(lbl_eletero)
                    .addComponent(lbl_eleteropont)
                    .addComponent(btn_eletero))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(pnl_statLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(lbl_szerencse)
                    .addComponent(lbl_szerencsepont)
                    .addComponent(btn_szerencse))
                .addContainerGap())
        );

        pnl_karakter.setBackground(new java.awt.Color(171, 125, 95));
        pnl_karakter.setBorder(javax.swing.BorderFactory.createLineBorder(null));

        lbl_nev.setFont(new java.awt.Font("Edwardian Script ITC", 1, 24)); // NOI18N
        lbl_nev.setForeground(new java.awt.Color(255, 255, 255));
        lbl_nev.setText("Név");

        txt_nev.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                txt_nevActionPerformed(evt);
            }
        });

        lbl_karakterkep.setBackground(new java.awt.Color(255, 255, 255));
        lbl_karakterkep.setIcon(new javax.swing.ImageIcon(getClass().getResource("/halallabirintus/character1.jpg"))); // NOI18N

        btn_vissza.setText("<");
        btn_vissza.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btn_visszaActionPerformed(evt);
            }
        });

        btn_elore.setText(">");
        btn_elore.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btn_eloreActionPerformed(evt);
            }
        });

        chk_karakter.setText("Ez legyen a karaktered?");
        chk_karakter.setEnabled(false);
        chk_karakter.addItemListener(new java.awt.event.ItemListener() {
            public void itemStateChanged(java.awt.event.ItemEvent evt) {
                chk_karakterItemStateChanged(evt);
            }
        });

        javax.swing.GroupLayout pnl_karakterLayout = new javax.swing.GroupLayout(pnl_karakter);
        pnl_karakter.setLayout(pnl_karakterLayout);
        pnl_karakterLayout.setHorizontalGroup(
            pnl_karakterLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, pnl_karakterLayout.createSequentialGroup()
                .addContainerGap()
                .addGroup(pnl_karakterLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addComponent(lbl_karakterkep, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addGroup(javax.swing.GroupLayout.Alignment.LEADING, pnl_karakterLayout.createSequentialGroup()
                        .addComponent(btn_vissza)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(chk_karakter, javax.swing.GroupLayout.PREFERRED_SIZE, 152, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(27, 27, 27)
                        .addComponent(btn_elore))
                    .addComponent(txt_nev))
                .addContainerGap())
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, pnl_karakterLayout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(lbl_nev, javax.swing.GroupLayout.PREFERRED_SIZE, 51, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(126, 126, 126))
        );
        pnl_karakterLayout.setVerticalGroup(
            pnl_karakterLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pnl_karakterLayout.createSequentialGroup()
                .addContainerGap()
                .addComponent(lbl_nev)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(txt_nev, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addComponent(lbl_karakterkep, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(pnl_karakterLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(btn_vissza)
                    .addComponent(btn_elore)
                    .addComponent(chk_karakter))
                .addContainerGap())
        );

        pnl_hatizsak.setBackground(new java.awt.Color(171, 125, 95));
        pnl_hatizsak.setBorder(javax.swing.BorderFactory.createLineBorder(null));

        lbl_hatizsak.setFont(new java.awt.Font("Edwardian Script ITC", 1, 24)); // NOI18N
        lbl_hatizsak.setForeground(new java.awt.Color(255, 255, 255));
        lbl_hatizsak.setText("Hátizsák:");

        txt_hatizsak.setEditable(false);
        txt_hatizsak.setBackground(new java.awt.Color(255, 255, 255));
        txt_hatizsak.setText("Arany: \nÜzenetek:");
        scr_hatizsak.setViewportView(txt_hatizsak);

        btn_kaland.setText("Kezdődhet a kaland...");
        btn_kaland.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btn_kalandActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout pnl_hatizsakLayout = new javax.swing.GroupLayout(pnl_hatizsak);
        pnl_hatizsak.setLayout(pnl_hatizsakLayout);
        pnl_hatizsakLayout.setHorizontalGroup(
            pnl_hatizsakLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pnl_hatizsakLayout.createSequentialGroup()
                .addGap(93, 93, 93)
                .addComponent(lbl_hatizsak)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
            .addComponent(scr_hatizsak, javax.swing.GroupLayout.Alignment.TRAILING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, pnl_hatizsakLayout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(btn_kaland)
                .addContainerGap())
        );
        pnl_hatizsakLayout.setVerticalGroup(
            pnl_hatizsakLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pnl_hatizsakLayout.createSequentialGroup()
                .addContainerGap()
                .addComponent(lbl_hatizsak)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(scr_hatizsak)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(btn_kaland)
                .addContainerGap())
        );

        javax.swing.GroupLayout jp_kalandLayout = new javax.swing.GroupLayout(jp_kaland);
        jp_kaland.setLayout(jp_kalandLayout);
        jp_kalandLayout.setHorizontalGroup(
            jp_kalandLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jp_kalandLayout.createSequentialGroup()
                .addContainerGap()
                .addComponent(pnl_karakter, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 46, Short.MAX_VALUE)
                .addGroup(jp_kalandLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                    .addComponent(pnl_hatizsak, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(pnl_stat, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                .addContainerGap())
        );
        jp_kalandLayout.setVerticalGroup(
            jp_kalandLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jp_kalandLayout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jp_kalandLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jp_kalandLayout.createSequentialGroup()
                        .addComponent(pnl_stat, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(pnl_hatizsak, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                    .addComponent(pnl_karakter, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                .addContainerGap())
        );

        jtp_alap.addTab("Kalandlap", jp_kaland);

        jp_sztori.setBackground(new java.awt.Color(255, 255, 255));

        pnl_sztorihatter.setBackground(new java.awt.Color(171, 125, 95));
        pnl_sztorihatter.setBorder(javax.swing.BorderFactory.createLineBorder(null));

        lbl_sztorikep.setIcon(new javax.swing.ImageIcon(getClass().getResource("/halallabirintus/1. oldal.png"))); // NOI18N

        pnl_sztori.setBackground(new java.awt.Color(154, 110, 81));
        pnl_sztori.setBorder(javax.swing.BorderFactory.createLineBorder(null));

        jLabel1.setFont(new java.awt.Font("Edwardian Script ITC", 1, 36)); // NOI18N
        jLabel1.setForeground(new java.awt.Color(255, 255, 255));
        jLabel1.setText("Történet");

        txt_tortenet.setEditable(false);
        txt_tortenet.setBackground(new java.awt.Color(255, 255, 255));
        txt_tortenet.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        txt_tortenet.setText("Miután öt percet haladtál lassan az alagútban, egy kőasztalhoz érsz, amely a bal oldali fal mellett áll. Hat doboz van rajta, egyikükre a te neved festették. ");
        jScrollPane1.setViewportView(txt_tortenet);

        javax.swing.GroupLayout pnl_sztoriLayout = new javax.swing.GroupLayout(pnl_sztori);
        pnl_sztori.setLayout(pnl_sztoriLayout);
        pnl_sztoriLayout.setHorizontalGroup(
            pnl_sztoriLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pnl_sztoriLayout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 0, Short.MAX_VALUE)
                .addContainerGap())
            .addGroup(pnl_sztoriLayout.createSequentialGroup()
                .addGap(117, 117, 117)
                .addComponent(jLabel1, javax.swing.GroupLayout.PREFERRED_SIZE, 104, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(119, Short.MAX_VALUE))
        );
        pnl_sztoriLayout.setVerticalGroup(
            pnl_sztoriLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pnl_sztoriLayout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jLabel1)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jScrollPane1)
                .addContainerGap())
        );

        javax.swing.GroupLayout pnl_sztorihatterLayout = new javax.swing.GroupLayout(pnl_sztorihatter);
        pnl_sztorihatter.setLayout(pnl_sztorihatterLayout);
        pnl_sztorihatterLayout.setHorizontalGroup(
            pnl_sztorihatterLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pnl_sztorihatterLayout.createSequentialGroup()
                .addContainerGap()
                .addComponent(lbl_sztorikep)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 10, Short.MAX_VALUE)
                .addComponent(pnl_sztori, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap())
        );
        pnl_sztorihatterLayout.setVerticalGroup(
            pnl_sztorihatterLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pnl_sztorihatterLayout.createSequentialGroup()
                .addContainerGap()
                .addGroup(pnl_sztorihatterLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(pnl_sztorihatterLayout.createSequentialGroup()
                        .addGap(9, 9, 9)
                        .addComponent(lbl_sztorikep)
                        .addContainerGap(19, Short.MAX_VALUE))
                    .addGroup(pnl_sztorihatterLayout.createSequentialGroup()
                        .addComponent(pnl_sztori, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addContainerGap())))
        );

        btn_valasztas_jobb.setText("Inkább Északnak indulok tovább");
        btn_valasztas_jobb.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btn_valasztas_jobbActionPerformed(evt);
            }
        });

        btn_valasztas_bal.setText("Kinyitom a dobozt");
        btn_valasztas_bal.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btn_valasztas_balActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout jp_sztoriLayout = new javax.swing.GroupLayout(jp_sztori);
        jp_sztori.setLayout(jp_sztoriLayout);
        jp_sztoriLayout.setHorizontalGroup(
            jp_sztoriLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jp_sztoriLayout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jp_sztoriLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(pnl_sztorihatter, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addGroup(jp_sztoriLayout.createSequentialGroup()
                        .addComponent(btn_valasztas_bal, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(btn_valasztas_jobb, javax.swing.GroupLayout.PREFERRED_SIZE, 305, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addContainerGap())
        );
        jp_sztoriLayout.setVerticalGroup(
            jp_sztoriLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jp_sztoriLayout.createSequentialGroup()
                .addContainerGap()
                .addComponent(pnl_sztorihatter, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addGroup(jp_sztoriLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(btn_valasztas_bal, javax.swing.GroupLayout.DEFAULT_SIZE, 71, Short.MAX_VALUE)
                    .addComponent(btn_valasztas_jobb, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                .addContainerGap())
        );

        jtp_alap.addTab("Sztori", jp_sztori);

        m_fajl.setText("Fájl");

        m_mentes.setText("Mentés");
        m_fajl.add(m_mentes);

        menu_ujrakezdes.setText("Újrakezdés");
        menu_ujrakezdes.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                menu_ujrakezdesActionPerformed(evt);
            }
        });
        m_fajl.add(menu_ujrakezdes);
        m_fajl.add(jSeparator1);

        m_kilepes.setText("Kilépés");
        m_kilepes.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                m_kilepesActionPerformed(evt);
            }
        });
        m_fajl.add(m_kilepes);

        menu.add(m_fajl);

        m_beallitasok.setText("Beállítások");
        m_beallitasok.setEnabled(false);
        menu.add(m_beallitasok);

        setJMenuBar(menu);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jtp_alap, javax.swing.GroupLayout.Alignment.TRAILING)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jtp_alap, javax.swing.GroupLayout.Alignment.TRAILING)
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    int statszamolas;
    String pontok;
    int gombnyomasjobb = 0;
    int gombnyomasbal = 0;
    int karaktervaltas = 0;
    String elso = "Miután öt percet haladtál lassan az alagútban, egy kőasztalhoz érsz, amely a bal oldali fal mellett áll. Hat doboz van rajta, egyikükre a te neved festették.";
    String otvenhatos = "Látod, hogy az akadály egy széles, barna, sziklaszerű tárgy. Megérinted, és meglepve tapasztalod, hogy lágy, szivacsszerű.";
    String hatvanhatos = "Néhány perc gyaloglás után egy elágazáshoz érsz az alagútban. Egy, a falra festett fehér nyíl nyugatfelé mutat. A földön nedves lábnyomok jelzik, merre haladtak az előtted járók. Nehéz biztosan megmondani, de úgy tűnik, hogy három közülük a nyíl irányába halad, míg egyikük úgy döntött, hogy keletnek megy.";
    String szharminchet = "Ahogy végigmész az alagúton, csodálkozva látod, hogy egy jókora vasharang csüng alá a boltozatról.";
    String ksztizenot = "Kardod könnyedén áthatol a spóragolyó vékonykülső burkán. Sűrű barna spórafelhő csap ki a golyóból, és körülvesz. Némelyik spóra a bőrödhöz tapad, és rettenetes viszketést okoz. Nagy daganatok nőnek az arcodon és karodon, és a bőröd mintha égne.";
    String kszhetven = "A doboz teteje könnyedén nyílik. Benne két aranypénzt találsz, és egy üzenetet, amely egy kis pergamenen neked szól. Előbb zsebre vágod az aranyakat, aztán elolvasod az üzenetet. (Hátizsák) Megjegyzed a tanácsot, apródarabokra téped a pergament, és tovább mész észak felé.";
    String kszkilencvenharom = "A három pár nedves lábnyomot követve az alagútnyugati elágazásában hamarosan egy újabb el-ágazáshoz érsz.";
    String hszhetvenharom = "Fölmászol a lágy sziklára, attól tartasz, hogy bár-melyik pillanatban elnyelhet. Nehéz átvergődni rajta, mert puha anyagában alig tudod a lábadat emelni, de végül átvergődsz rajta.";
    String hsznyolcvanhet = "Hallod, hogy elölről súlyos lépések közelednek. Egy széles, állatbőrökbe öltözött, kőbaltás, primitívlény lép elő. Ahogy meglát, morog, a földre köp, majd a kőbaltát felemelve közeledik, és mindennek kinéz, csak barátságosnak nem.";
    

    private void btn_kilepesActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btn_kilepesActionPerformed
        kilepes();
    }//GEN-LAST:event_btn_kilepesActionPerformed

    private void m_kilepesActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_m_kilepesActionPerformed
        kilepes();
    }//GEN-LAST:event_m_kilepesActionPerformed

    private void jtp_alapMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_jtp_alapMouseClicked
        boolean chk = chk_karakter.isSelected();
        if(jtp_alap.getSelectedIndex() == 2 && !chk){
            jtp_alap.setSelectedIndex(1);
            JOptionPane.showMessageDialog(rootPane, "Nem véglegesítetted a karaktered.");
        }
    }//GEN-LAST:event_jtp_alapMouseClicked

    private void chk_karakterItemStateChanged(java.awt.event.ItemEvent evt) {//GEN-FIRST:event_chk_karakterItemStateChanged
        String nev = txt_nev.getText();
        if(chk_karakter.isSelected()){
            txt_nev.setEnabled(false);
            btn_vissza.setEnabled(false);
            btn_elore.setEnabled(false);
        }
        else{
            txt_nev.setEnabled(true);
            btn_vissza.setEnabled(true);
            btn_elore.setEnabled(true);
        }
    }//GEN-LAST:event_chk_karakterItemStateChanged

    private void formWindowClosing(java.awt.event.WindowEvent evt) {//GEN-FIRST:event_formWindowClosing
        kilepes();
    }//GEN-LAST:event_formWindowClosing

    private void txt_nevActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_txt_nevActionPerformed
        String nev = txt_nev.getText();
        if(nev != ""){
            chk_karakter.setEnabled(true);
        }
        else if(nev == ""){
            chk_karakter.setEnabled(false);
        }
    }//GEN-LAST:event_txt_nevActionPerformed

    private void btn_sugoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btn_sugoActionPerformed
        String sugo = String.format("A játék egy régen népszerű lapozgatós könyv számítógépes verziója.\nA játék során különböző választási lehetőségeid lesznek.\nVálassz ügyesen és jó kalandot!");
        JOptionPane.showMessageDialog(pnl_tortenet, sugo, "Súgó",JOptionPane.INFORMATION_MESSAGE);
    }//GEN-LAST:event_btn_sugoActionPerformed

    private void jButton6ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton6ActionPerformed
        jtp_alap.setSelectedIndex(1);
    }//GEN-LAST:event_jButton6ActionPerformed

    private void btn_kalandActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btn_kalandActionPerformed
        if(chk_karakter.isSelected() && lbl_ugyessegpont.getText() != "0" && lbl_eleteropont.getText() != "0" && lbl_szerencsepont.getText() != "0"){
            jtp_alap.setSelectedIndex(2);
        }
        
    }//GEN-LAST:event_btn_kalandActionPerformed

    private void btn_ugyessegActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btn_ugyessegActionPerformed
        statszamolas = 6;
        statszamitas();
        lbl_ugyessegpont.setText(pontok);
        btn_ugyesseg.setEnabled(false);
    }//GEN-LAST:event_btn_ugyessegActionPerformed


    private void btn_eleteroActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btn_eleteroActionPerformed
        statszamolas = 12;
        statszamitas();
        lbl_eleteropont.setText(pontok);
        btn_eletero.setEnabled(false);
    }//GEN-LAST:event_btn_eleteroActionPerformed

    private void btn_szerencseActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btn_szerencseActionPerformed
        statszamolas = 6;
        statszamitas();
        lbl_szerencsepont.setText(pontok);
        btn_szerencse.setEnabled(false);
    }//GEN-LAST:event_btn_szerencseActionPerformed

    private void btn_visszaActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btn_visszaActionPerformed
    if(karaktervaltas == 0){
        lbl_karakterkep.setIcon(new ImageIcon("src/halallabirintus/character2.png"));
        karaktervaltas += 1;
    }
    else{
        lbl_karakterkep.setIcon(new ImageIcon("src/halallabirintus/character1.jpg"));
        karaktervaltas = 0;
    }
    }//GEN-LAST:event_btn_visszaActionPerformed
    
    private void btn_eloreActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btn_eloreActionPerformed
    if(karaktervaltas == 0){
        lbl_karakterkep.setIcon(new ImageIcon("src/halallabirintus/character2.png"));
        karaktervaltas += 1;
    }
    else{
        lbl_karakterkep.setIcon(new ImageIcon("src/halallabirintus/character1.jpg"));
        karaktervaltas = 0;
    }
    }//GEN-LAST:event_btn_eloreActionPerformed

    private void btn_valasztas_jobbActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btn_valasztas_jobbActionPerformed
    if(gombnyomasjobb == 0 && gombnyomasbal == 0){
        gombnyomasjobb += 1;
        txt_tortenet.setText(hatvanhatos);
        btn_valasztas_bal.setEnabled(true);
        btn_valasztas_jobb.setText("Keletnek megyek tovább");
        btn_valasztas_bal.setText("Nyugatnak megyek tovább");
        lbl_sztorikep.setIcon(new ImageIcon("src/halallabirintus/66. oldal.png"));
    }
    else if(gombnyomasjobb == 1 && gombnyomasbal == 0) {
        gombnyomasjobb += 1;
        txt_tortenet.setText(otvenhatos);
        btn_valasztas_jobb.setText("Ketté vágom!");
        btn_valasztas_bal.setText("Átmászok rajta...");
        lbl_sztorikep.setIcon(new ImageIcon("src/halallabirintus/56. oldal.png"));
    }
    else if(gombnyomasbal == 0 && gombnyomasjobb == 2){
        txt_tortenet.setText(ksztizenot);
        gombnyomasjobb += 1;
        btn_valasztas_jobb.setText("Vége a játéknak!");
        btn_valasztas_bal.setText("");
        btn_valasztas_jobb.setEnabled(false);
        btn_valasztas_bal.setEnabled(false);
        lbl_sztorikep.setIcon(new ImageIcon("src/halallabirintus/215. oldal .png"));
        eleterovaltozas();
    }
    else{
        txt_tortenet.setText(hsznyolcvanhet);
        btn_valasztas_jobb.setText("Vége a játéknak!");
        btn_valasztas_bal.setText("");
        btn_valasztas_jobb.setEnabled(false);
        btn_valasztas_bal.setEnabled(false);
        lbl_sztorikep.setIcon(new ImageIcon("src/halallabirintus/387. oldal.png"));
    }
    }//GEN-LAST:event_btn_valasztas_jobbActionPerformed

    private void btn_valasztas_balActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btn_valasztas_balActionPerformed
    if(gombnyomasbal == 0 && gombnyomasjobb == 0){
        txt_tortenet.setText(kszhetven);
        btn_valasztas_bal.setEnabled(false);
        btn_valasztas_jobb.setText("Haladok tovább északnak");
        btn_valasztas_bal.setText("");
        lbl_sztorikep.setIcon(new ImageIcon("src/halallabirintus/270. oldal 2.png"));
        txt_hatizsak.setText(String.format("Arany: 2\nÜzenetek: :\n„Jól tetted. Legalább volt annyi eszed,\nhogy megállj és elfogadd az ajándékot.\nMost azt tanácsolom neked,\nhogy keress és használj különféle tárgyakat,\nha sikerrel akarsz áthaladni Halállabirintusomon.”\n- Szukumvit"));
    }
    else if(gombnyomasjobb == 1 && gombnyomasbal == 0){
        txt_tortenet.setText(kszkilencvenharom);
        gombnyomasbal += 1;
        btn_valasztas_jobb.setText("Inkább észak felé megyek a harmadik lábnyom után.");
        btn_valasztas_bal.setText("Megyek nyugat felé a lábnyomokat követve");
        lbl_sztorikep.setIcon(new ImageIcon("src/halallabirintus/293. oldal.png"));
    }
    else if(gombnyomasbal == 1 && gombnyomasjobb == 1){
        txt_tortenet.setText(hszhetvenharom);
        gombnyomasbal += 1;
        btn_valasztas_jobb.setText("Vége a játéknak!");
        btn_valasztas_bal.setText("");
        btn_valasztas_jobb.setEnabled(false);
        btn_valasztas_bal.setEnabled(false);
        lbl_sztorikep.setIcon(new ImageIcon("src/halallabirintus/373. oldal.png"));
    }
    else{
        txt_tortenet.setText(szharminchet);
        btn_valasztas_jobb.setText("Vége a játéknak!");
        btn_valasztas_bal.setText("");
        btn_valasztas_jobb.setEnabled(false);
        btn_valasztas_bal.setEnabled(false);
        lbl_sztorikep.setIcon(new ImageIcon("src/halallabirintus/215. oldal 2.png"));
    }
    }//GEN-LAST:event_btn_valasztas_balActionPerformed

    private void menu_ujrakezdesActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_menu_ujrakezdesActionPerformed
    gombnyomasbal = 0;
    gombnyomasjobb = 0;
    txt_tortenet.setText(elso);
    btn_valasztas_jobb.setText("Inkább Északnak indulok tovább");
    btn_valasztas_bal.setText("Kinyitom a dobozt");
    lbl_sztorikep.setIcon(new ImageIcon("src/halallabirintus/1. oldal.png"));
    btn_valasztas_jobb.setEnabled(true);
    btn_valasztas_bal.setEnabled(true);
    
    }//GEN-LAST:event_menu_ujrakezdesActionPerformed
    public static void main(String args[]) {
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new HalalLabirintus().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btn_eletero;
    private javax.swing.JButton btn_elore;
    private javax.swing.JButton btn_kaland;
    private javax.swing.JButton btn_kilepes;
    private javax.swing.JButton btn_sugo;
    private javax.swing.JButton btn_szerencse;
    private javax.swing.JButton btn_ugyesseg;
    private javax.swing.JButton btn_valasztas_bal;
    private javax.swing.JButton btn_valasztas_jobb;
    private javax.swing.JButton btn_vissza;
    private javax.swing.JCheckBox chk_karakter;
    private javax.swing.JButton jButton6;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JPopupMenu.Separator jSeparator1;
    private javax.swing.JPanel jp_kaland;
    private javax.swing.JPanel jp_kezdo;
    private javax.swing.JPanel jp_sztori;
    private javax.swing.JTabbedPane jtp_alap;
    private javax.swing.JLabel lbl_cim;
    private javax.swing.JLabel lbl_eletero;
    private javax.swing.JLabel lbl_eleteropont;
    private javax.swing.JLabel lbl_hatizsak;
    private javax.swing.JLabel lbl_karakterkep;
    private javax.swing.JLabel lbl_kep;
    private javax.swing.JLabel lbl_nev;
    private javax.swing.JLabel lbl_stat;
    private javax.swing.JLabel lbl_szerencse;
    private javax.swing.JLabel lbl_szerencsepont;
    private javax.swing.JLabel lbl_sztorikep;
    private javax.swing.JLabel lbl_tortenet;
    private javax.swing.JLabel lbl_ugyesseg;
    private javax.swing.JLabel lbl_ugyessegpont;
    private javax.swing.JMenu m_beallitasok;
    private javax.swing.JMenu m_fajl;
    private javax.swing.JMenuItem m_kilepes;
    private javax.swing.JMenuItem m_mentes;
    private javax.swing.JMenuBar menu;
    private javax.swing.JMenuItem menu_ujrakezdes;
    private javax.swing.JPanel pnl_halallabirintus;
    private javax.swing.JPanel pnl_hatizsak;
    private javax.swing.JPanel pnl_karakter;
    private javax.swing.JPanel pnl_stat;
    private javax.swing.JPanel pnl_sztori;
    private javax.swing.JPanel pnl_sztorihatter;
    private javax.swing.JPanel pnl_tortenet;
    private javax.swing.JScrollPane scr_hatizsak;
    private javax.swing.JScrollPane scr_leiras;
    private javax.swing.JTextPane txt_hatizsak;
    private javax.swing.JTextField txt_nev;
    private javax.swing.JTextPane txt_tortenet;
    private javax.swing.JTextPane txtp_leiras;
    // End of variables declaration//GEN-END:variables
        
    private void eleterovaltozas(){
    int jelenlegi = Integer.parseInt(lbl_eleteropont.getText());
    jelenlegi = jelenlegi-2;
    lbl_eleteropont.setText(jelenlegi + "");
    }
    private void statszamitas() {
        int sors = (int)(Math.random() * 7);
        int pont = sors+statszamolas;
        pontok = pont + "";
    }
    private void kilepes() throws HeadlessException {
        String u = "Biztos kilépsz?";
        String c = "Kilépés?";
        int ot = JOptionPane.OK_CANCEL_OPTION;
        int mt = JOptionPane.INFORMATION_MESSAGE;
        int gomb = JOptionPane.showConfirmDialog(null, u, c, ot, mt);
        if(gomb == JOptionPane.OK_OPTION){
            System.exit(0);
        }
    }
}
