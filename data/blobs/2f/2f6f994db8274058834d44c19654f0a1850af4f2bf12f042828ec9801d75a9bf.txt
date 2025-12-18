package ru.serggh.garry_bot.service.impl;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;
import org.xml.sax.InputSource;
import ru.serggh.garry_bot.client.CbrClient;
import ru.serggh.garry_bot.exception.ServiceException;
import ru.serggh.garry_bot.service.ExchangeRatesService;
import org.w3c.dom.Document;

import javax.xml.xpath.*;
import java.io.StringReader;
import java.util.Optional;

@Service
public class ExchangeRatesServiceImpl implements ExchangeRatesService {

    private static final String USD_XPATH = "/ValCurs//Valute[@ID='R01235']/Value";
    private static final String EUR_XPATH = "/ValCurs//Valute[@ID='R01239']/Value";

    @Autowired
    private CbrClient client;

    @Cacheable(value = "usd", unless = "#result == null or #result.isEmpty()")
    @Override
    public String getUSDExchangeRate() throws ServiceException {
        Optional<String> xmlOptional = client.getCurrencyRatesXML();
        String xml = xmlOptional.orElseThrow(
                () -> new ServiceException("Не удалось получить XML")
        );
        return extractCurrencyValueFromXML(xml, USD_XPATH);
    }

    @Cacheable(value = "eur", unless = "#result == null or #result.isEmpty()")
    @Override
    public String getEURExchangeRate() throws ServiceException {

        Optional<String> xmlOptional = client.getCurrencyRatesXML();
        String xml;
        xml = xmlOptional.orElseThrow(
                () -> new ServiceException("Не удалось получить XML")
        );
        return extractCurrencyValueFromXML(xml, EUR_XPATH);
    }


    private static String extractCurrencyValueFromXML(String xml, String xpathExpression)
            throws ServiceException {
        InputSource source = new InputSource(new StringReader(xml));
        try {
            XPath xPath = XPathFactory.newInstance().newXPath();
            Document document = (Document) xPath.evaluate("/", source, XPathConstants.NODE);

            return xPath.evaluate(xpathExpression, document);
        } catch (XPathExpressionException e) {
            throw new ServiceException("Не удалось распарсить XML", e);
        }
    }
}