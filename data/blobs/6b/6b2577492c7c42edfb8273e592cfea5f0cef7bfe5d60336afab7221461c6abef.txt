package view.images;


import javax.swing.JLabel;
import com.formdev.flatlaf.extras.FlatSVGIcon;

public class SVGImage extends JLabel {
    private FlatSVGIcon svgIcon;
    public void setSvgImage(String image, int width, int height) {
        svgIcon = new FlatSVGIcon(image, width, height);
        setIcon(svgIcon);
    }
}
