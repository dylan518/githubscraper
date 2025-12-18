package org.cours.tp1.service;

import org.springframework.stereotype.Service;
import org.cours.tp1.modele.Module;

import java.util.ArrayList;
import java.util.List;

@Service
public class ModuleService {

    private List<Module> modules;

    public ModuleService() {
        this.modules = new ArrayList<>();


        this.modules.add(new Module(10, "La plateforme Java Standard Edition", "Description de la plateforme Java SE"));
        this.modules.add(new Module(12, "La plateforme Java Enterprise Edition", "Description de la plateforme Java EE"));
    }

    public List<Module> getModules() {
        return modules;
    }

    public Module getModule(Integer id) {
        for (Module module : modules) {
            if (id.equals(module.getId())) {
                return module;
            }
        }
        return null;
    }

    public void ajouterModule(Module module) {
        modules.add(module);
    }

    public void modifierModule(Integer id, Module module) {
        for (int i=0; i<modules.size(); i++) {
            Module m = modules.get(i);
            if (id.equals(m.getId())) {
                modules.set(i, module);
                return;
            }
        }
    }

    public void supprimerModule(Integer id) {
        modules.removeIf(m -> id.equals(m.getId()));
    }
}