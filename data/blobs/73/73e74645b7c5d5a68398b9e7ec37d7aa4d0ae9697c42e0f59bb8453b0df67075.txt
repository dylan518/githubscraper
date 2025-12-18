package net.earthshine17.earthshine.worldgen;

import net.earthshine17.earthshine.ESMod;
import net.minecraft.core.Holder;
import net.minecraft.core.HolderGetter;
import net.minecraft.core.registries.Registries;
import net.minecraft.data.worldgen.BootstrapContext;
import net.minecraft.resources.ResourceKey;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.level.levelgen.VerticalAnchor;
import net.minecraft.world.level.levelgen.feature.ConfiguredFeature;
import net.minecraft.world.level.levelgen.placement.HeightRangePlacement;
import net.minecraft.world.level.levelgen.placement.PlacedFeature;
import net.minecraft.world.level.levelgen.placement.PlacementModifier;

import java.util.List;

public class ModPlacedFeatures {
    public static ResourceKey<PlacedFeature> RAINBOW_ORE = createKey("rainbow_ore");
    public static ResourceKey<PlacedFeature> ROSIUM_ORE = createKey("rosium_ore");
    public static ResourceKey<PlacedFeature> LUNARITE_ORE = createKey("lunarite_ore");
    public static ResourceKey<PlacedFeature> DREAMSTONE_ORE = createKey("dreamstone_ore");

    public static void bootstrap(BootstrapContext<PlacedFeature> context) {
        HolderGetter<ConfiguredFeature<?, ?>> configuredFeatures = context.lookup(Registries.CONFIGURED_FEATURE);

        Holder<ConfiguredFeature<?, ?>> holderRainbow =
                configuredFeatures.getOrThrow(ModConfiguredFeatures.OVERWORLD_RAINBOW_ORE);
        Holder<ConfiguredFeature<?, ?>> holderRosium =
                configuredFeatures.getOrThrow(ModConfiguredFeatures.OVERWORLD_ROSIUM_ORE);
        Holder<ConfiguredFeature<?, ?>> holderLunarite =
                configuredFeatures.getOrThrow(ModConfiguredFeatures.OVERWORLD_LUNARITE_ORE);
        Holder<ConfiguredFeature<?, ?>> holderDreamstone =
                configuredFeatures.getOrThrow(ModConfiguredFeatures.OVERWORLD_DREAMSTONE_ORE);

        register(context, RAINBOW_ORE, holderRainbow, ModOrePlacement.commonOrePlacements(12, HeightRangePlacement.uniform(VerticalAnchor.absolute(-64), VerticalAnchor.absolute(0))));
        register(context, ROSIUM_ORE, holderRosium, ModOrePlacement.commonOrePlacements(12, HeightRangePlacement.uniform(VerticalAnchor.absolute(0), VerticalAnchor.absolute(32))));
        register(context, LUNARITE_ORE, holderLunarite, ModOrePlacement.commonOrePlacements(12, HeightRangePlacement.uniform(VerticalAnchor.absolute(33), VerticalAnchor.absolute(64))));
        register(context, DREAMSTONE_ORE, holderDreamstone, ModOrePlacement.commonOrePlacements(12, HeightRangePlacement.uniform(VerticalAnchor.absolute(64), VerticalAnchor.absolute(128))));
    }


    private static ResourceKey<PlacedFeature> createKey(String name) {
        return ResourceKey.create(Registries.PLACED_FEATURE, ResourceLocation.fromNamespaceAndPath(ESMod.MOD_ID, name));
    }

    private static void register(BootstrapContext<PlacedFeature> context, ResourceKey<PlacedFeature> key, Holder<ConfiguredFeature<?, ?>> feature, List<PlacementModifier> placementModifiers) {
        context.register(key, new PlacedFeature(feature, placementModifiers));
    }
}