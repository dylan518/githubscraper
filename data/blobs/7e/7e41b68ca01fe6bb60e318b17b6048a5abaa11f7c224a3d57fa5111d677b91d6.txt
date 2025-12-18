package HomeWork_Exception.EX_2;

public class CalculateLessTwenty extends CalculateLessTen{
    @Override
    public void squaring(int num) throws CalculateMoreTwentyException{
        if (num>=20){
            throw new CalculateMoreTwentyException("Введенное число должно быть меньше 20");
        }
        int result = num*num;
        System.out.println(result);
    }
}
