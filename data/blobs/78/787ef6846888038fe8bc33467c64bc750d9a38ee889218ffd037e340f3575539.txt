package makersharks.example.user.Management.utilities;
import lombok.experimental.UtilityClass;
import org.modelmapper.Conditions;
import org.modelmapper.ModelMapper;
import java.rmi.ServerException;


@UtilityClass
public class ObjectMapperUtil {
    public static String ERROR_OCCURRED = "Error: {}";
    private static final ModelMapper mapper = new ModelMapper();

    static {
        mapper.getConfiguration().setPropertyCondition(Conditions.isNotNull());
    }

    public static <S, D> D map(S source, Class<D> destinationClass) throws ServerException {
        try {
            return mapper.map(source, destinationClass);
        }catch (Exception e){
            throw new ServerException(String.format(ERROR_OCCURRED,e.getMessage()));
        }
    }
}
