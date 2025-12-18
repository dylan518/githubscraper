package initBrowser;

import com.microsoft.playwright.*;

import java.util.Arrays;

public class InitAplication {
    Playwright playwright;
    Browser browser;
    BrowserContext context;
    public static Page page;

    public void Browser(String url) {
        playwright = Playwright.create();
        browser = playwright.chromium().launch(new BrowserType.LaunchOptions().setHeadless(true));
        context = browser.newContext(new Browser.NewContextOptions().setViewportSize(1920, 1080));
        page = context.newPage();
        page.navigate(url, new Page.NavigateOptions().setTimeout(60000));
        System.out.println(page.title());
    }

    public void quit() {
        if (context != null) {
            context.close();
        }
        if (browser != null) {
            browser.close();
        }
        if (playwright != null) {
            playwright.close();
        }
    }
}
