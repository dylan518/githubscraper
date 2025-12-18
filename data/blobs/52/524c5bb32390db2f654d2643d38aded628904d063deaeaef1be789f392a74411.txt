package m_proxy;

/**
 * Proxy 는 대리인이라는 뜻으로
 * 어떤 작업의 실행을 대리인을 통해 실행하도록 하는 패턴입니다.
 */
public class Main {
  public static void main(String[] args) {
    System.out.println("======== ScreenDisplay =======");
    Display screenDisplay = new ScreenDisplay();

    screenDisplay.print("SW 설계를 위한 디자인패턴은");
    screenDisplay.print("이해하기 난해한 부분도 있지만, ");
    screenDisplay.print("이해하고 개발에 적용을 하면");
    screenDisplay.print("큰 규모의 SW 개발에 큰 도움이 됩니다.");
    screenDisplay.print("또한 유지보수와 기능확장에도 매우 도움이 됩니다.");

    System.out.println("======== BufferDisplay =======");
    Display bufferDisplay = new BufferDisplay(3);

    bufferDisplay.print("SW 설계를 위한 디자인패턴은");
    bufferDisplay.print("이해하기 난해한 부분도 있지만, ");
    bufferDisplay.print("이해하고 개발에 적용을 하면");
    bufferDisplay.print("큰 규모의 SW 개발에 큰 도움이 됩니다.");
    bufferDisplay.print("또한 유지보수와 기능확장에도 매우 도움이 됩니다.");

    /** 버퍼의 내용을 버퍼의 크기와 상관없이 출력. */
    ((BufferDisplay)bufferDisplay).flush();
  }
}
