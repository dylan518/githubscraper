package ch6.remoteController;

public class RemoteController {
    public static void main(String[] args) {
        RemoteControlWithUndo remote = new RemoteControlWithUndo();
        Light light = new Light("Living Room");
        Light light2 = new Light("Kitchen");
        LightOnCommand livingRoomLightOn = new LightOnCommand(light);
        LightOnCommand kitchenLightOn = new LightOnCommand(light2);

        LightOffCommand livingRoomLightOff = new LightOffCommand(light);
        LightOffCommand kitchenLightOff = new LightOffCommand(light2);

        Stereo stereo = new Stereo();

        StereoOnWithCDCommand stereoOn = new StereoOnWithCDCommand(stereo);
        StereoOffCommand stereoOff = new StereoOffCommand(stereo);

        // Lambda 표현식으로 변경
        // 추상 메소드가 하나일 때만 사용 가능하므로 Command에 메소드 추가로 람다표현식 사용 불가
        remote.setCommand(0, livingRoomLightOn, livingRoomLightOff);
        remote.setCommand(1, kitchenLightOn, kitchenLightOff);
        remote.setCommand(2, stereoOn, stereoOff);

        System.out.println(remote);

        remote.onButtonWasPushed(0);
        remote.offButtonWasPushed(0);
        System.out.println(remote);

        // 다시 Living Room의 불이 켜진다.
        remote.undoButtonWasPushed();
        System.out.println(remote);

        remote.onButtonWasPushed(2);
        // 라디오가 꺼진다.
        remote.undoButtonWasPushed();
        System.out.println(remote);
        // 라디오는 꺼져있으나 현재 저장된 undo는 라디오 버튼을 켠 상태이므로
        // 다시 off가 된다.
        // 즉, undo할 때 명령어를 변경을 시켜주지 않는다.
        remote.undoButtonWasPushed();
    }
}
