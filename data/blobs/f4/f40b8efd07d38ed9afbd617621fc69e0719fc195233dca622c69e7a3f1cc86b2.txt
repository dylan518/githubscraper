package net.spongy.catmod.item;

import net.fabricmc.fabric.api.item.v1.FabricItemSettings;
import net.fabricmc.fabric.api.itemgroup.v1.ItemGroupEvents;
import net.minecraft.item.Item;
import net.minecraft.item.ItemGroup;
import net.minecraft.item.ItemGroups;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.util.Identifier;
import net.spongy.catmod.CatMod;

public class ModItems {
    public static final Item CITRINE = registerItem("citrine",
            new Item(new FabricItemSettings()));
    public static final Item RAW_CITRINE = registerItem("raw_citrine",
            new Item(new FabricItemSettings()));
    private static Item registerItem(String name, Item item) {
        return Registry.register(Registries.ITEM, new Identifier(CatMod.MOD_ID,name), item);
    }


    public static void addItemstoItemGroup() {
        addtoItemGroup(ItemGroups.INGREDIENTS, CITRINE);
        addtoItemGroup(ItemGroups.INGREDIENTS, RAW_CITRINE);

        addtoItemGroup(ModItemGroup.CITRINE, CITRINE);
        addtoItemGroup(ModItemGroup.CITRINE, RAW_CITRINE);
    }
    private static void addtoItemGroup(ItemGroup group, Item item) {
        ItemGroupEvents.modifyEntriesEvent(group).register(entries -> entries.add(item));
    }
    public static void registerModItems() {
        CatMod.LOGGER.info("Registering Mod Items for " + CatMod.MOD_ID);
        addItemstoItemGroup();
    }

}
