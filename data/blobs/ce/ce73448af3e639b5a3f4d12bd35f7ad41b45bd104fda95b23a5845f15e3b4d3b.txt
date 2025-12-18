package Controller.Commands;

import CollectionObjects.Product;
import Controller.Command;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import static CollectionObjects.Collectionss.stringCollection;
import static java.lang.Integer.parseInt;

/**
 * Класс RemLow реализует команду удаления из коллекции всех элементов, ключи которых меньше заданного.
 */
public class RemLow implements Command {

    /**
     * Возвращает описание команды.
     *
     * @return строка с описанием команды.
     */
    @Override
    public String getDescription() {
        return getName() + " удалить из коллекции все элементы, меньшие, чем заданный";
    }

    /**
     * Возвращает имя команды.
     *
     * @return строка с именем команды.
     */
    @Override
    public String getName() {
        return "remove_lower";
    }

    /**
     * Выполняет команду удаления из коллекции всех элементов, ключи которых меньше заданного.
     *
     * @param arg аргумент команды, представляющий ключ, с которым сравниваются элементы.
     */
    @Override
    public void execute(String arg) {
        try {
            // Преобразование аргумента в целое число (ключ для сравнения)
            Integer id2 = parseInt(arg);

            // Список для хранения ключей элементов, которые нужно удалить
            List<Integer> IdToRemove = new ArrayList<>();

            // Поиск элементов, ключи которых меньше заданного
            for (Map.Entry<Integer, Product> entry : stringCollection.entrySet()) {
                Integer id = entry.getKey();
                if (id.compareTo(id2) < 0) {
                    IdToRemove.add(id);
                }
            }

            // Удаление найденных элементов
            for (Integer id : IdToRemove) {
                stringCollection.remove(id);
            }

            System.out.println("Удалено " + IdToRemove.size() + " элементов, ключи которых меньше " + id2 + ".");
        } catch (NumberFormatException e) {
            System.err.println("Ошибка: Неверный формат ключа. Ключ должен быть целым числом.");
        }
    }
}