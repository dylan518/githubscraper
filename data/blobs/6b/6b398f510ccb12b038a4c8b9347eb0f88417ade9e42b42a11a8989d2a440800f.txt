package com.lft.boot.starter;

import com.lft.imodel.aop.ControllerIntercept;
import com.lft.imodel.factory.ModelFactory;
import com.lft.imodel.model.ModelResolver;
import org.springframework.boot.autoconfigure.condition.ConditionalOnWebApplication;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Import;
import org.springframework.web.method.support.HandlerMethodArgumentResolver;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import java.util.List;

@Configuration
@Import(ControllerIntercept.class)
@ConditionalOnWebApplication
public class AutoConfiguration implements WebMvcConfigurer {
    private final ModelFactory factory;

    public AutoConfiguration() {
        this.factory = new ModelFactory();
    }

    @Override
    public void addArgumentResolvers(List<HandlerMethodArgumentResolver> resolvers) {
        resolvers.add(new ModelResolver(factory));
    }

    public ModelFactory modelFactory() {
        return factory;
    }
}
