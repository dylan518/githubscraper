package krazyminer001.bettersniffer.mixin;

import krazyminer001.bettersniffer.entities.ModEntities;
import krazyminer001.bettersniffer.entities.custom.BetterSnifferEntity;
import net.minecraft.entity.Entity;
import net.minecraft.entity.ItemEntity;
import net.minecraft.entity.LivingEntity;
import net.minecraft.entity.SpawnReason;
import net.minecraft.entity.damage.DamageSource;
import net.minecraft.entity.passive.SnifferEntity;
import net.minecraft.server.world.ServerWorld;
import net.minecraft.util.math.BlockPos;
import net.minecraft.world.World;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.Unique;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

import java.util.Objects;
import java.util.UUID;

@Mixin(SnifferEntity.class)
public abstract class SnifferEntityMixin {

    @Inject(method = "tick()V", at = @At("HEAD"))
    private void replaceSniffer(CallbackInfo ci) {
        World world = ((EntityAccessor) this).getWorld();
        BlockPos pos = ((EntityAccessor) this).getPos();
        UUID uuid = ((EntityAccessor) this).getUUID();
        if (world instanceof ServerWorld serverWorld) {
            Entity entity = serverWorld.getEntity(uuid);
            if (entity instanceof SnifferEntity snifferEntity && !(entity instanceof BetterSnifferEntity)) {
                world.spawnEntity(ModEntities.BETTER_SNIFFER.spawn(serverWorld, pos, SpawnReason.CONVERSION));
                snifferEntity.remove(Entity.RemovalReason.DISCARDED);
            }
        }
    }
}
