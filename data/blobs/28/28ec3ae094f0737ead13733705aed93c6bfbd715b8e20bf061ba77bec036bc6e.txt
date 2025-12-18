package com.jukomu.exercise2;

import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;
import javafx.geometry.Insets;
import javafx.scene.Node;
import javafx.scene.control.*;
import javafx.scene.input.KeyCode;
import javafx.scene.layout.VBox;
import javafx.scene.text.Font;

import java.util.concurrent.atomic.AtomicBoolean;

/**
 * @Description:
 * @Author：Jukomu
 * @Package：com.jukomu.exercise2
 * @Project：Exercise2
 * @name：Right
 * @Date：2023/12/8 10:35
 * @Filename：Right
 */
public class Right extends VBox {
    private final String _1 = "This should be a unique identifier for the purposes of filing. If more than one person is working on the project or more than one analysis technique is being used, this identifier could contain letters and numbers. For example, if Chris Smith and Jan Koo are both doing an analysis, the identifier might be CS1 or JK75. If both a heuristic evaluation and a think-aloud usability study were used, the identifiers might be HE6 or TA89. Follow the unique identifier with the word 'Problem,' if the report pertains to a usability problem of the interface, or the words 'Good Feature,' if it describes an aspect of the interface you feel should be preserved in any redesign.";
    private final String _2 = "This description will be used as the 'name' of this UAR when you talk about its relation to other UARs. Make the name as short as possible (about three to five words) but still descriptive and distinguishable from other aspects of the system. If this UAR is about a problem (as opposed to a good feature), make sure you have a name that describes the problem, rather than a solution.";
    private final String _3 = "This is the objective supporting material that justifies your identifying the aspect as worthy of report. This section needs to contain enough information for a reader of this UAR to understand what triggered the report. For an HE report, for instance, this could be an image of a cluttered screen and the heuristic about aesthetics and minimalist design. In a think-aloud study this is usually what was on the screen (a screen shot or description), what the user did (keystrokes, mouse movements), what the system did in response to any user actions, and what the user said. You need to include enough pertinent information about the identification of an aspect for the reader to understand what the analyst was thinking when the aspect was identified (for HE) or what the user was trying to do when the aspect either hindered or facilitated his or her progress.";
    private final String _4 = "This is your interpretation of the evidence. That is, for a think-aloud usability test, why you think what happened happened, or, for an HE, why you think the aspect was designed the way it was. You need to provide enough content in this explanation for the reader to understand the problem-even if they do not know the system or domain as well as you do.";
    private final String _5 = "This is your reasoning about how important it is to either fix this problem or preserve this good feature. This includes how frequently the users will experience this aspect, whether they are likely to learn how it works, whether it will affect new users, casual users, experienced users, etc.";
    private final String _6 = "If this aspect is a problem (as opposed to a good feature to be preserved in the next version of the software), this is the place to propose a solution. It is not necessary to have a solution as soon as you identify a problem-you might find after analyzing the whole interface that many problems are related and can all be fixed by making a single broad change instead of making several small changes. However, if you do propose a possible solution, report any potential design trade-offs that you see";
    private final String _7 = "It is often the case that UARs are related to each other. This is where you record which UARs this one is related to and a statement about how it is related. Make sure that all the related UARs point to each other. It is a common mistake to enter the pointer into a newly created UAR, but neglect to go back to the previous ones that it relates to and update their UARs.";

    String[] list = {_1, _2, _3, _4, _5, _6, _7};
    String currentDescription = "";
    StringProperty descriptionString = new SimpleStringProperty();
    String foundDescription1 = "";
    StringProperty foundString1 = new SimpleStringProperty();
    String foundDescription2 = "";
    StringProperty foundString2 = new SimpleStringProperty();
    TextArea area = new TextArea();
    Label label3 = new Label("");
    Label label4 = new Label("");

    public Right() {
        Label label1 = new Label("UAR component description:");
        Label label2 = new Label("Found at: ");
        area.setPrefSize(350,240);
        area.setMaxSize(350,240);
        area.setStyle("-fx-border-color: rgba(0,0,0,0.5);-fx-font-size: 11;-fx-focus-color: rgba(0,0,0,0.24); -fx-faint-focus-color: transparent;");
        // 禁用自动换行
        area.setWrapText(true);
        // 文本框绑定currentDescription
        area.textProperty().bind(descriptionString);
        // label3绑定foundDescription1
        label3.textProperty().bind(foundString1);
        // label4绑定foundDescription2
        label4.textProperty().bind(foundString2);
        // 创建一个ScrollPane，并将TextArea添加到其中
        ScrollPane scrollPane = new ScrollPane(area);
        scrollPane.setFitToWidth(true);
        scrollPane.setFitToHeight(true);
        scrollPane.setMaxSize(360,240);
        // 设置ScrollPane的滚动条策略，始终显示垂直滚动条
        scrollPane.setVbarPolicy(ScrollPane.ScrollBarPolicy.ALWAYS);
        Insets insets = new Insets(0, 0, 0, 19);
        this.getChildren().addAll(label1,scrollPane,label2,label3,label4);
        this.setPadding(insets);
        this.setSpacing(15);
        /* 设置组件字体 */
        Font font = new Font(11);
        for (Node node : this.getChildren()) {
            if (node instanceof Label) {
                ((Label) node).setFont(font);
            }
        }
        label1.setStyle("-fx-font-weight: bold;-fx-font-size: 12px");
        label1.setPadding(new Insets(9,0,0,0));
    }

    public String getCurrentDescription() {
        return currentDescription;
    }

    public void setCurrentDescription(String currentDescription) {
        this.currentDescription = currentDescription;
        descriptionString.set(this.currentDescription);
    }
    public void setCurrentDescription(int number) {
        this.currentDescription = list[number-1];
        descriptionString.set(this.currentDescription);
    }

    public String getFoundDescription1() {
        return foundDescription1;
    }

    public void setFoundDescription1(String foundDescription1) {
        this.foundDescription1 = foundDescription1;
        foundString1.set(this.foundDescription1);
    }

    public String getFoundDescription2() {
        return foundDescription2;
    }

    public void setFoundDescription2(String foundDescription2) {
        this.foundDescription2 = foundDescription2;
        foundString2.set(this.foundDescription2);
    }

    public boolean searchString(String searchString) {
        AtomicBoolean is = new AtomicBoolean(true);

        System.out.println("Search: " + searchString);
        // 查找字符串出现的次数
        int occurrences = countOccurrences(this.currentDescription, searchString);

        // 查找第一次出现的位置
        int firstIndex = 1+this.currentDescription.indexOf(searchString);

        // 查找最后一次出现的位置
        int lastIndex = 1+this.currentDescription.lastIndexOf(searchString);

        setFoundDescription1("Occurrence 1: Position: " + firstIndex);
        setFoundDescription2("Occurrence " + occurrences + ": Position: " + lastIndex);
        System.out.println("Found: " + searchString+ ": first at " + firstIndex + ", last at " + lastIndex);

        // 创建一个Alert（弹窗）
        Alert alert = new Alert(Alert.AlertType.CONFIRMATION);
        alert.setTitle("Search String");
        alert.setHeaderText(null);
        alert.setGraphic(null);
        alert.setContentText("The number of occurrences of 'a' is: "+ occurrences + "\n"+ "\n" +"Search same text?");
        alert.getDialogPane().setPrefSize(260, 150);

        // 设置"Yes"按钮
        ButtonType buttonTypeYes = new ButtonType("是(Y)");
        // 设置"No"按钮
        ButtonType buttonTypeNo = new ButtonType("否(N)");

        alert.getButtonTypes().setAll(buttonTypeYes, buttonTypeNo);

        // 添加键盘按键监听器
        alert.getDialogPane().getScene().setOnKeyPressed(event -> {
            if (event.getCode() == KeyCode.Y) {
                System.out.println("用户按下了 Y 键");
                // 在这里执行"Yes"按钮的相应操作
                is.set(true);
                alert.setResult(buttonTypeYes);
            } else if (event.getCode() == KeyCode.N) {
                System.out.println("用户按下了 N 键");
                // 在这里执行"No"按钮的相应操作
                is.set(false);
                alert.setResult(buttonTypeNo);
            }
        });

        // 显示弹窗并等待用户操作
        alert.showAndWait().ifPresent(buttonType -> {
            if (buttonType == buttonTypeYes) {
                System.out.println("用户点击了 Yes 按钮");
                // 在这里执行"Yes"按钮的相应操作
                is.set(true);
            } else if (buttonType == buttonTypeNo) {
                System.out.println("用户点击了 No 按钮");
                // 在这里执行"No"按钮的相应操作
                is.set(false);
            }
        });
        return is.get();
    }

    public void clearFoundString() {
        setFoundDescription1("");
        setFoundDescription2("");
    }
    public void clearDisplay() {
        setCurrentDescription("");
    }

    private int countOccurrences(String mainString, String strToFind) {
        int count = 0;
        int index = 0;
        mainString = mainString.toLowerCase();
        strToFind = strToFind.toLowerCase();

        while ((index = mainString.indexOf(strToFind, index)) != -1) {
            count++;
            index += strToFind.length();
        }
        return count;
    }
}
