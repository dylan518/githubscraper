  
package io.github.shatterdest.ShatterSMPPlugin;

import io.github.shatterdest.ShatterSMPPlugin.commands.MagmaStaffCommand;
import io.github.shatterdest.ShatterSMPPlugin.events.MagmaStaffUse;
import org.bukkit.configuration.file.FileConfiguration;
import org.bukkit.event.Listener;
import org.bukkit.plugin.java.JavaPlugin;

public class Main extends JavaPlugin implements Listener {
    FileConfiguration config = getConfig();
    JavaPlugin plugin;
    @Override
    public void onEnable() {
    	getLogger().info("Shatterdest's Plugin has been Enabled!");
		this.getCommand("MagmaStaff").setExecutor(new MagmaStaffCommand());
        config.addDefault("Welcome msg", true);
        config.options().copyDefaults(true);
        saveConfig();
        getServer().getPluginManager().registerEvents(new MagmaStaffUse(), this);
        plugin = this;
    }
    @Override
    public void onDisable() {
    	getLogger().info("Shatterdest's Plugin has been Disabled!");
    }

}