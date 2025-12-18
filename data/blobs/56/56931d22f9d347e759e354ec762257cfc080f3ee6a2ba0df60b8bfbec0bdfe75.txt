import java.util.List;
import java.util.Locale;

class PigLatinTranslator {

    List<Character> vowels = List.of('a', 'e', 'i', 'o', 'u');
    List<Character> consonants = List.of('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z');


    public String translate(String word) {
        String wordLowerCase = word.toLowerCase(Locale.ROOT);
        StringBuilder sb = new StringBuilder(wordLowerCase);
        String[] palavras = null;

        if (wordLowerCase.indexOf(' ') > 0) {
            palavras = wordLowerCase.split(" ");
            StringBuilder resultado = new StringBuilder();
            for (String palavra : palavras) {
                resultado.append(translateSingleWord(palavra)).append(" ");
            }
            return resultado.toString().trim();
        }

        return translateSingleWord(wordLowerCase);
    }

    private String translateSingleWord(String wordLowerCase) {
        StringBuilder sb = new StringBuilder(wordLowerCase);

        if (vowels.contains(wordLowerCase.charAt(0)) || wordLowerCase.startsWith("xr") || wordLowerCase.startsWith("yt")) {
            sb.append("ay");
        } else if (wordLowerCase.startsWith("qu")) {
            String prefix = sb.substring(0, 2);
            sb.delete(0, 2);
            sb.append(prefix).append("ay");
        } else if (consonants.contains(wordLowerCase.charAt(0)) && wordLowerCase.startsWith("qu", 1)) {
            String prefix = sb.substring(0, 3);
            sb.delete(0, 3);
            sb.append(prefix).append("ay");
        } else if (consonants.contains(wordLowerCase.charAt(0))) {
            int prefixLength = 0;

            if (wordLowerCase.charAt(prefixLength) == 'y') {
                prefixLength = 1;
            }

            while (prefixLength < wordLowerCase.length() && consonants.contains(wordLowerCase.charAt(prefixLength))) {
                if (wordLowerCase.charAt(prefixLength) == 'y') {
                    break;
                }
                prefixLength++;
            }

            String prefix = sb.substring(0, prefixLength);
            sb.delete(0, prefixLength);
            sb.append(prefix).append("ay");
        }

        return sb.toString();
    }

}