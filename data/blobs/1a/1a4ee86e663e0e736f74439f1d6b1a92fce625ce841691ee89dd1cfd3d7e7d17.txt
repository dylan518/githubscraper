package services;

import enums.StudyProfile;
import exceptions.SheetNotFoundException;
import moduls.Student;
import moduls.University;
import org.apache.poi.ss.formula.functions.Log;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

public class XSSFFileReader {

    private static final Logger logger = Logger.getLogger(XSSFFileReader.class.getName());

    private XSSFFileReader() {
    }

    public static List<Student> getStudentsFromFile(String sheetName, String path) {
        logger.info("Starting method getStudentsFromFile");
        Sheet sheet = XSSFFileReader.getSheetFromXSSF(sheetName, path);
        return getStudents(sheet);
    }

    private static Sheet getSheetFromXSSF(String sheetName, String path) {
        logger.info("Creating sheet");
        if (sheetName == null || path == null) {
            logger.warning("sheetName or path contains null");
            throw new NullPointerException("sheetName or path contains null");
        }
        try (XSSFWorkbook workbook = new XSSFWorkbook(new FileInputStream(path))) {
            logger.info("Reading xls file");
            Sheet sheet = workbook.getSheet(sheetName);
            if (sheet == null) {
                logger.warning("Sheet == null");
                throw new SheetNotFoundException("Sheet not found");
            }
            return sheet;
        } catch (IOException | SheetNotFoundException exception) {
            logger.severe(exception.getMessage());
        }
        logger.log(Level.WARNING, "Method getSheetFromXSSF didnt return a sheet", new SheetNotFoundException("Sheet not found"));
        throw new SheetNotFoundException("Sheet not found");
    }

    private static List<Student> getStudents(Sheet sheet) {
        List<Student> students = new ArrayList<>();
        skipFirstRow(sheet);
        for (Row row : sheet) {
            List<String> oneRow = getCells(row);
            students.add(getStudent(oneRow));
        }
        return students;
    }

    private static void skipFirstRow(Sheet sheet) {
        if (sheet == null) {
            throw new SheetNotFoundException("Sheet not found");
        }
        sheet.removeRow(sheet.getRow(0));
    }

    private static List<String> getCells(Row row) {
        List<String> cells = new ArrayList<>();
        for (Cell cell : row)
            cells.add(String.valueOf(cell));
        return cells;
    }

    private static Student getStudent(List<String> studentData) {
        return new Student(studentData.get(1), studentData.get(0),
                Integer.parseInt(studentData.get(2).substring(0, 1)), Float.parseFloat(studentData.get(3)));
    }

    public static List<University> getUniversitiesFromFile(String sheetName, String path) {
        Sheet sheet = getSheetFromXSSF(sheetName, path);
        return getUniversities(sheet);
    }

    private static List<University> getUniversities(Sheet sheet) {
        List<University> universities = new ArrayList<>();
        skipFirstRow(sheet);
        for (Row row : sheet) {
            List<String> oneRow = getCells(row);
            universities.add(getUniversity(oneRow));
        }
        return universities;
    }

    private static University getUniversity(List<String> universityData) {
        return new University(universityData.get(0), universityData.get(1), universityData.get(2),
                Integer.parseInt(universityData.get(3).substring(0, 4)),
                StudyProfile.valueOf(universityData.get(4)));
    }
}