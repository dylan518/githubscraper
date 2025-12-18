package principle.dependenceInversionPrinciple;

/**
 * @ClassName: AppTest
 * @Description:
 * @Author: Macay
 * @Date: 2022/7/24 2:45 下午
 */
public class AppTest {
    public static void main(String[] args) {
        Cpu amdCpu = new AMDCpu();
        Memory samSungMemory = new SamSungMemory();
        Computer computer = new Computer();
        computer.setCpu(amdCpu);
        computer.setMemory(samSungMemory);
        computer.run();
    }
}
