package dev.chrismharris.creative_cooking.block;

import dev.chrismharris.creative_cooking.CreativeCookingMod;
import dev.chrismharris.creative_cooking.register.BlockRegister;
import dev.chrismharris.creative_cooking.register.ItemRegister;
import net.minecraft.core.BlockPos;
import net.minecraft.core.Direction;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.sounds.SoundSource;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.context.BlockPlaceContext;
import net.minecraft.world.level.BlockGetter;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.HorizontalDirectionalBlock;
import net.minecraft.world.level.block.SoundType;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.block.state.StateDefinition;
import net.minecraft.world.level.block.state.properties.DirectionProperty;
import net.minecraft.world.level.material.FluidState;
import net.minecraft.world.level.material.Material;
import net.minecraft.world.level.material.MaterialColor;
import net.minecraft.world.phys.BlockHitResult;
import net.minecraft.world.phys.shapes.CollisionContext;
import net.minecraft.world.phys.shapes.VoxelShape;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

public class CookedBreadPan extends Block {
    public static final DirectionProperty FACING = HorizontalDirectionalBlock.FACING;

    public static final VoxelShape HITBOX_NORTH_SOUTH = Block.box(3, 0, 0, 13, 6, 16);
    public static final VoxelShape HITBOX_WEST_EAST = Block.box(0, 0, 3, 16, 6, 13);

    @SuppressWarnings("deprecation")
    @Override
    public @NotNull VoxelShape getShape(BlockState state, @NotNull BlockGetter getter, @NotNull BlockPos pos, @NotNull CollisionContext context) {
        if (state.getValue(FACING).equals(Direction.NORTH) ||
                state.getValue(FACING).equals(Direction.SOUTH)) {
            return HITBOX_NORTH_SOUTH;
        } else {
            return HITBOX_WEST_EAST;
        }
    }

    public static final BlockBehaviour.Properties PROPERTIES = BlockBehaviour.Properties
            .of(Material.METAL, MaterialColor.COLOR_GRAY)
            .strength(2f)
            .sound(SoundType.METAL)
            .dynamicShape();

    public static final Item.Properties ITEM_PROPERTIES = new Item.Properties()
            .tab(CreativeCookingMod.CC_TAB);

    public CookedBreadPan() {
        super(BreadPan.PROPERTIES);

        this.registerDefaultState(this.defaultBlockState().setValue(FACING, Direction.NORTH));
    }

    @Nullable
    @Override
    public BlockState getStateForPlacement(BlockPlaceContext context) {
        return this.defaultBlockState().setValue(FACING, context.getHorizontalDirection().getOpposite());
    }

    @Override
    protected void createBlockStateDefinition(StateDefinition.Builder<Block, BlockState> builder) {
        builder
                .add(FACING);
    }

    @SuppressWarnings("deprecation")
    @Override
    public @NotNull InteractionResult use(@NotNull BlockState state, @NotNull Level level, @NotNull BlockPos pos,
                                          @NotNull Player player, @NotNull InteractionHand hand, @NotNull BlockHitResult hit) {
        popResource(level, pos, new ItemStack(BlockRegister.BREAD_LOAF.get().asItem(), 1));
        level.playSound(null, pos, SoundEvents.ITEM_FRAME_REMOVE_ITEM, SoundSource.BLOCKS, 1.0F, 0.8F + level.random.nextFloat() * 0.4F);
        level.setBlock(pos, BlockRegister.BREAD_PAN.get().defaultBlockState().
                        setValue(BreadPan.DIRTY, true)
                        .setValue(BreadPan.FACING, state.getValue(CookedBreadPan.FACING)),
                1);
        player.getItemInHand(hand).use(level, player, hand);
        return InteractionResult.sidedSuccess(level.isClientSide);
    }

    @Override
    public boolean onDestroyedByPlayer(BlockState state, Level level, BlockPos pos, Player player, boolean willHarvest, FluidState fluid) {
        popResource(level, pos, new ItemStack(ItemRegister.BREAD_PAN_DIRTY.get(), 1));
        popResource(level, pos, new ItemStack(BlockRegister.BREAD_LOAF.get().asItem(), 1));
        return super.onDestroyedByPlayer(state, level, pos, player, willHarvest, fluid);
    }
}
