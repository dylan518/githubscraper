package org.example;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class UniqString {
    private boolean iFlag;
    //TODO: классы оберты боксинг анбоксин

    private boolean uFlag;
    private int sNum;
    private boolean cFlag;

    private String inputFile;
    private String outputFile;

    public int getsNum() {
        return sNum;
    }

    public void setsNum(int sNum) {
        this.sNum = sNum;
    }

    public UniqString(boolean iFlag, boolean uFlag, int sNum, boolean cFlag, String inputFile, String outputFile) {
        this.iFlag = iFlag;
        this.uFlag = uFlag;
        this.sNum = sNum;
        this.cFlag = cFlag;
        this.inputFile = inputFile;
        this.outputFile = outputFile;
        System.out.println(this.outputFile);
    }

    public boolean isiFlag() {
        return iFlag;
    }

    public void setiFlag(boolean iFlag) {
        this.iFlag = iFlag;
    }

    public boolean isuFlag() {
        return uFlag;
    }

    public void setuFlag(boolean uFlag) {
        this.uFlag = uFlag;
    }

    public boolean iscFlag() {
        return cFlag;
    }

    public void setcFlag(boolean cFlag) {
        this.cFlag = cFlag;
    }

    public String getInputFile() {
        return inputFile;
    }

    public void setInputFile(String inputFile) {
        this.inputFile = inputFile;
    }

    public String getOutputFile() {
        return outputFile;
    }

    public void setOutputFile(String outputFile) {
        this.outputFile = outputFile;
    }

    public List<String> lines;
    List<String> result;


    public List<String> transform() throws IOException {
        lines = Files.readAllLines(Paths.get(inputFile));
        result = new ArrayList<String>();
        doTransform();
        if (outputFile != null) {
            Path outfile = Paths.get(outputFile);
            Files.write(outfile, result, StandardCharsets.UTF_8);
        }else {
            System.out.println(result);
        }
        return result;
    }

    private void doTransform() {

        int counterStreak = 1;
        for (int i = 1; i < lines.size(); i++) {
            boolean isStrEq;
            if(iFlag && sNum != 0){
                isStrEq = lines.get(i).substring(sNum).equalsIgnoreCase(lines.get(i - 1).substring(sNum));
            }else if(iFlag){
             isStrEq = lines.get(i).equalsIgnoreCase(lines.get(i - 1));
            } else if (sNum != 0){
                isStrEq = lines.get(i).substring(sNum).equals(lines.get(i - 1).substring(sNum));
            }else {
             isStrEq = lines.get(i).equals(lines.get(i - 1));
            }

            if (isStrEq) {
                counterStreak++;
                if (i == lines.size() - 1) {

                    if (uFlag && counterStreak == 1) {
                        result.add(lines.get(i));
                    } else if (cFlag) {
                        if (counterStreak > 1) {
                            result.add(counterStreak + lines.get(i));
                        } else {
                            result.add(lines.get(i));
                        }
                    } else {
                        result.add(lines.get(i));
                    }


                }
            } else {
                if (uFlag && counterStreak == 1) {
                    result.add( lines.get(i-1));
                } else if (cFlag) {
                    if (counterStreak > 1) {
                        result.add(counterStreak + lines.get(i-1));
                    } else {
                        result.add(lines.get(i-1));
                    }
                } else {
                    result.add(lines.get(i-1));
                }
                counterStreak = 1;
                if (i == lines.size() - 1) {
                    if (uFlag && counterStreak == 1) {
                        result.add( lines.get(i));
                    } else if (cFlag) {
                        if (counterStreak > 1) {
                            result.add(counterStreak + lines.get(i));
                        } else {
                            result.add(lines.get(i));
                        }
                    } else {
                        result.add(lines.get(i));
                    }
                }

            }
        }
    }


// aa aa bb ac ac
}


//     boolean eq;
//                                                                        Uniqttt flagFromUniq = new Uniqttt();
//
//        boolean uFlagEq;
//        int counter = 1;
//        if (flagFromUniq.sflag()) {
//            for (int i = 0; i < lines.size(); i++) {
//                lines.set(i, lines.get(i).substring(n));
//            }
//        }
//        for (int i = 1; i < lines.size(); i++) {
//            // -i flag beginning
//            if (flagFromUniq.iflag()) {
//                eq = lines.get(i).equalsIgnoreCase(lines.get(i - 1));
//                if (eq) {
//                    counter++;
//                } else {
//                    counter = 1;
//                }
//                if (i != lines.size() - 1) {
//                    uFlagEq = !lines.get(i).equalsIgnoreCase(lines.get(i - 1)) && !lines.get(i).equalsIgnoreCase(lines.get(i + 1));
//                } else {
//                    uFlagEq = !lines.get(i).equalsIgnoreCase(lines.get(i - 1));
//                }
//                //abc aa abc abc
//            } else {
//                eq = lines.get(i).equals(lines.get(i - 1));
//                if (eq) {
//                    counter++;
//                } else {
//                    counter = 1;
//                }
//                if (flagFromUniq.cflag()) {
//                    if (i == 1 && !eq) {
//                        result.add(lines.get(i - 1));
//                    }
//                }
//
// abc abc aaa aaa
//
//                if (i != lines.size() - 1) {
//                    uFlagEq = !lines.get(i).equals(lines.get(i - 1)) && !lines.get(i).equals(lines.get(i + 1));
//                } else {
//                    uFlagEq = !lines.get(i).equals(lines.get(i - 1));
//                }
//            }
//            // -i flag ending
//            // -u flag beginning
//            if (flagFromUniq.uflag()) {
//                if (i == 1 && !eq) {
//                    result.add(lines.get(i - 1));
//                }
//                if (uFlagEq) {
//                    result.add(lines.get(i));
//                }
//            }
//            // -u flag ending
//            else {
//                // -c flag beginning
//                if (flagFromUniq.cflag()) {
//                    if (i != lines.size() - 1) {
//                        System.out.println(result);
//                        System.out.println(i);
//                        if (flagFromUniq.iflag()) {
//                            if (!lines.get(i + 1).equalsIgnoreCase(lines.get(i)) && counter != 1) {
//                                result.add(counter + " " + lines.get(i));
//                            } else {
//                                if (!lines.get(i + 1).equalsIgnoreCase(lines.get(i))) {
//                                    result.add(lines.get(i));
//                                }
//                            }
//                        } else {
//                            if (!lines.get(i + 1).equals(lines.get(i)) && counter != 1) {
//                                result.add(counter + " " + lines.get(i));
//                            } else {
//                                if (!lines.get(i + 1).equals(lines.get(i))) {
//                                    result.add(lines.get(i));
//                                }
//                            }
//                        }
//
//                    } else {
//                        if (eq) {
//                            result.add(counter + " " + lines.get(i));
//                        } else {
//                            result.add(lines.get(i));
//                        }
//                    }
//                } else {
//                    if (!eq) {
//                        result.add(lines.get(i - 1));
//                    }
//                    if (eq && i == lines.size() - 1) {
//                        result.add(lines.get(i));
//                    }
//                }
//
//
//            }
//
//        }
//        Files.write(outfile, result, StandardCharsets.UTF_8);
//        return outfileread();