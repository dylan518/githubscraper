import java.util.ArrayList;
import java.util.Scanner;

public class Runner {
    public static void main(String[] args) {
        ArrayList<PhysicalDrive> drives = new ArrayList<PhysicalDrive>();
        ArrayList<PhysicalVolume> pvs = new ArrayList<PhysicalVolume>();
        ArrayList<VolumeGroup> vgs = new ArrayList<VolumeGroup>();
        ArrayList<LogicalVolume> lvs = new ArrayList<LogicalVolume>();

        Scanner s = new Scanner(System.in);
        System.out.println("Welcome to the LVM System!");
        boolean exit = true;
        while (exit) {

            System.out.println("cmd#: ");
            String input = s.nextLine();
            if (input.contains("install-drive")) {
                System.out.println("Enter the name of the drive.");
                String name = s.nextLine();
                System.out.println("Enter the storage of the drive.");
                int storage = s.nextInt();
                PhysicalDrive drive1 = new PhysicalDrive(name, storage);
                drives.add(drive1);
                System.out.println("Drive " + name + " installed");
            } else if (input.contains("list-drives")) {
                for (PhysicalDrive drive : drives) {
                    System.out.println(drive.toString());
                }
            } else if (input.contains("pvcreate")) {
                System.out.println("Enter the name of the drive.");
                String drive = s.nextLine();
                System.out.println("Enter the name of the PhysicalVolume.");
                String name = s.nextLine();
                PhysicalDrive drive2 = null;
                for (PhysicalDrive pd : drives) {
                    if (pd.getName().equals(name)) {
                        drive2 = pd;
                    }
                }
                PhysicalVolume pv = new PhysicalVolume(name, drive2);
                pvs.add(pv);
                System.out.println(name + " installed");
            } else if (input.contains("pvlist")) {
                for (PhysicalVolume pV : pvs) {
                    System.out.println(pV.toString());
                }
            } else if (input.contains("vgcreate")) {
                System.out.println("Enter the name of the Physical Volume.");
                String drive = s.nextLine();
                System.out.println("Enter the name of the Volume Group.");
                String name = s.nextLine();
                PhysicalVolume v = null;
                for (PhysicalVolume pv : pvs) {
                    if (pv.getName().equals(name)) {
                        v = pv;
                    }
                }
                VolumeGroup vg = new VolumeGroup(name, pvs);
                vgs.add(vg);
                System.out.println(name + " installed");
            } else if (input.contains("vglist")) {
                for (VolumeGroup vG : vgs) {
                    System.out.println(vG.toString());
                }
            } else if (input.contains("lvcreate")) {
                System.out.println("Enter the size.");
                int size = s.nextInt();
                System.out.println("Enter the name of the Logical Volume.");
                String name = s.nextLine();
                System.out.println("Enter the name of the Volume Group.");
                String vg = s.nextLine();
                VolumeGroup v = null;
                for (VolumeGroup vg1 : vgs) {
                    if (vg1.getName().equals(name)) {
                        v = vg1;
                    }
                }
                LogicalVolume lv = new LogicalVolume(name, size, v);
                lvs.add(lv);
                System.out.println(name + " installed");
            } else if (input.contains("lvlist")) {
                for (LogicalVolume lv : lvs) {
                    System.out.println(lv.toString());
                }
            }
        }
    }
}