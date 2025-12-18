package main;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.OutputStream;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        // Tao danh sach diem
        ArrayList<Point2D> points2D = new ArrayList<>();
        points2D.add(new Point2D(1, 2));
        points2D.add(new Point2D(3, 4));
        points2D.add(new Point2D(5, 6));

        ArrayList<Point3D> points3D = new ArrayList<>();
        points3D.add(new Point3D(1, 2, 3));
        points3D.add(new Point3D(4, 5, 6));
        points3D.add(new Point3D(7, 8, 9));

        // Tinh tong khoang cach cac diem 2D
        double totalDistance2D = calculateTotalDistance2D(points2D);
        System.out.println("Tong khoang cach cac diem 2D: " + totalDistance2D);

        // Tinh tong khoang cach cac diem 3D
        double totalDistance3D = calculateTotalDistance3D(points3D);
        System.out.println("Tong khoang cach cac diem 3D: " + totalDistance3D);

     // Dua diem vao danh sach cac ddiem doi xung
        ArrayList<Point2D> newPoints2D = new ArrayList<>();
        for (Point2D point : points2D) {
            newPoints2D.add(point);
            newPoints2D.add(point.symmetry());
        }
        points2D = newPoints2D;

        ArrayList<Point3D> newPoints3D = new ArrayList<>();
        for (Point3D point : points3D) {
            newPoints3D.add(point);
            newPoints3D.add(point.symmetry());
        }
        points3D = newPoints3D;

        //Hien thi danh sach
        System.out.println("Danh sách điểm 2D và 3D sau khi thêm các điểm đối xứng:");
        for (Point2D point : points2D) {
            System.out.println(point);
        }
        for (Point3D point : points3D) {
            System.out.println(point);
        }
        
        //Doc cac point tu file vao trong 1 danh sach 
        ArrayList<Point2D> filePoints2D = new ArrayList<>();
        ReadFromFile(filePoints2D);
        
        System.out.println("Danh sanh cac diem 2D doc tu file la : ");
        for (Point2D point : filePoints2D) {
            System.out.println(point);
        }
        
        //tinh tong khoang cach ac points
        double totalDistance2DFile = calculateTotalDistance2D(filePoints2D);
        System.out.println("Tong khoang cach 2D tu file: " + totalDistance2DFile);
        
        // Ghi file ket qua
        WriteData(filePoints2D,totalDistance2DFile);
        
        //Ghi list 2D ra file voi object : 
        WriteDataObject( filePoints2D);
        
        //Doc du lieu tu file voi Object : 
        ArrayList<Point2D> fileObjectPoints2D = new ArrayList<>();
        try {
			ReadDataObject(fileObjectPoints2D);
		} catch (ClassNotFoundException | IOException e) {
			e.printStackTrace();
		}
        for (Point2D point : fileObjectPoints2D) {
            System.out.println(point);
        }
    }
    
    private static void WriteDataObject(ArrayList<Point2D> filePoints2D) throws IOException {
    	OutputStream os = null;
    	ObjectOutputStream oos = null;
    	try {
    		os = new FileOutputStream("E:\\theFourSemester\\JavaInCLass\\file\\obj_point.txt");
    		oos = new ObjectOutputStream(os);
    		for (Point2D point : filePoints2D) {
    			oos.writeObject(point);
    		}
    		System.out.println("END");
		} catch (IOException e) {
			e.printStackTrace();
		}finally {
			if(oos != null) {
				oos.close();
			}
			if(os != null) {
				os.close();
			}
		}
    }
    private static void ReadDataObject(ArrayList<Point2D> fileObjectPoints2D) throws IOException, ClassNotFoundException {
    	InputStream is = null;
    	ObjectInputStream ois = null;
    	try {
    		is = new FileInputStream("E:\\theFourSemester\\JavaInCLass\\file\\obj_point.txt");
    		ois = new ObjectInputStream(is);
    		Point2D temp = null;
    		while(true) {
    			Object oj = ois.readObject();
    			if(oj == null) {
    				break;
    			}else {
    				temp = (Point2D) oj;
    				fileObjectPoints2D.add(temp);
    			}
    		}
		} catch (IOException e) {
			e.printStackTrace();
		}finally {
			if(ois != null) {
				ois.close();
			}
			if(is != null) {
				is.close();
			}
		}
    }
    private static void WriteData(ArrayList<Point2D> filePoints2D, double totalDistance2DFile) {
    	//ghi file ket qua 
        FileWriter fw = null;
		BufferedWriter bw = null;
		try {
			fw = new FileWriter("E:\\theFourSemester\\JavaInCLass\\file\\point_bw.txt");
			bw = new BufferedWriter(fw);
			bw.write("NumberOfPoint: ");
			bw.write(Integer.toString(filePoints2D.size()));
			bw.newLine();
			bw.write("TotalDistance: ");	
			bw.write(Double.toString(totalDistance2DFile));
			System.out.println("success");
		} catch (IOException e) {
			e.printStackTrace();
		}finally {
			try {
	            if (bw != null) {
	                bw.close();
	            }
	            if (fw != null) {
	                fw.close();
	            }
	        } catch (IOException e) {
	            e.printStackTrace();
	        }
		}
		
	}

	private static void ReadFromFile(ArrayList<Point2D> filePoints2D) throws IOException {
    	FileReader fr = null;
		BufferedReader br = null;
		try {
			fr = new FileReader("E:\\theFourSemester\\JavaInCLass\\file\\point_br.txt");
			br = new BufferedReader(fr);
			String line; 
			while(true) {
				line = br.readLine();
				if(line == null) {
					System.out.println("FAIL");
					break;
				}else {
					String points[] = line.split("-");
					for(String point : points) {
						String xy[] = point.substring(1, point.length() - 1).split(";");
						int x = Integer.parseInt(xy[0]);
						int y = Integer.parseInt(xy[1]);
						filePoints2D.add(new Point2D(x,y));
						System.out.println("SUCCESS");
					}
				}
			}
			
		} catch (IOException e) {
			e.printStackTrace();
		}finally {
			if(fr == null) {
				fr.close();
			}
			if(br == null) {
				br.close();
			}
		}
		
	}

	private static double calculateTotalDistance2D(ArrayList<Point2D> points) {
        double totalDistance = 0;
        for (int i = 0; i < points.size() - 1; i++) {
            totalDistance += points.get(i).distance(points.get(i + 1));
        }
        return totalDistance;
    }
    
    private static double calculateTotalDistance3D(ArrayList<Point3D> points) {
        double totalDistance = 0;
        for (int i = 0; i < points.size() - 1; i++) {
            totalDistance += points.get(i).distance(points.get(i + 1));
        }
        return totalDistance;
    }
}