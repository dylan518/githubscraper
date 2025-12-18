package com.liferay.portlet;

import com.liferay.constants.*;
import com.liferay.frontend.js.loader.modules.extender.npm.*;
import com.liferay.portal.kernel.portlet.bridges.mvc.*;
import org.osgi.service.component.annotations.*;

import javax.portlet.*;
import java.io.*;

/**
 * @author root318
 */
@Component(
	immediate = true,
	property = {
		"com.liferay.portlet.display-category=category.sample",
		"com.liferay.portlet.header-portlet-css=/css/index.css",
		"com.liferay.portlet.instanceable=true",
		"javax.portlet.init-param.template-path=/",
		"javax.portlet.init-param.view-template=/view.jsp",
		"javax.portlet.name=" + NewReactPortletKeys.NewReact,
		"javax.portlet.resource-bundle=content.Language",
		"javax.portlet.security-role-ref=power-user,user"
	},
	service = Portlet.class
)
public class NewReactPortlet extends MVCPortlet {

	@Override
	public void doView(
			RenderRequest renderRequest, RenderResponse renderResponse)
		throws IOException, PortletException {
		renderRequest.setAttribute(
			"mainRequire",
			_npmResolver.resolveModuleName("new-react") + " as main");

		super.doView(renderRequest, renderResponse);
	}

	@Reference
	private NPMResolver _npmResolver;

}