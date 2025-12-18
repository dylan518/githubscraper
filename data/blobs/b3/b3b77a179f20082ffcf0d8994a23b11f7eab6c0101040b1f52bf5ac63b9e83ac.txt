package invariant.evaluator.openai;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.theokanning.openai.service.OpenAiService;
import okhttp3.OkHttpClient;
import retrofit2.Retrofit;

public enum GPTModel implements LLM {

    GPT_3_5("gpt-3.5-turbo-1106"),
    GPT_4("gpt-4-turbo-2024-04-09"),
    GPT_4o("gpt-4o-2024-08-06"),
    GPT_4o_mini("gpt-4o-mini-2024-07-18"),
    GPT_o1_mini("o1-mini-2024-09-12");

    private final String identifier;

    GPTModel(String identifier) {
        this.identifier = identifier;
    }


    @Override
    public String getIdentifier() {
        return this.identifier;
    }

    @Override
    public String getName() {
        return name();
    }

    public String getSimpleName(){
        return switch (this){
            case GPT_3_5 -> "GPT-3.5";
            case GPT_4 -> "GPT-4";
            case GPT_4o -> "GPT-4o";
            case GPT_4o_mini -> "GPT-4o-mini";
            case GPT_o1_mini -> "GPT-o1-mini";
        };
    }

    @Override
    public String getApiKey() {
        return System.getenv("OPENAI_API_KEY");
    }

    @Override
    public Retrofit getRetroFit(OkHttpClient client, ObjectMapper mapper) {
        return OpenAiService.defaultRetrofit(client, mapper);
    }
}
