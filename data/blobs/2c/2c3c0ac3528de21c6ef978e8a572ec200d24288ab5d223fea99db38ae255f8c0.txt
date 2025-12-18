/**
 * %% Copyright (C) 2021 DataScience 9 LLC %% Licensed under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance with the License. You may obtain a
 * copy of the License at
 *
 * <p>http://www.apache.org/licenses/LICENSE-2.0
 *
 * <p>Unless required by applicable law or agreed to in writing, software distributed under the
 * License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing permissions and
 * limitations under the License. #L%
 *
 * <p>This code is 100% AUTO generated. Please do not modify it DIRECTLY If you need new features or
 * function or changes please update the templates then submit the template through our web
 * interface.
 */
package com.drupal.test.dao;

import java.nio.charset.Charset;
import java.util.Arrays;
import java.io.IOException;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import java.io.IOException;
import java.nio.charset.Charset;
import java.util.Arrays;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;
import org.junit.After;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import com.drupal.test.entity.LafOlCommentFieldData;
import com.drupal.test.entity.LafOlCommentFieldDataId;
import com.drupal.test.utils.FileUtils;
import com.drupal.test.utils.ByteArrayToBase64TypeAdapter;

public class LafOlCommentFieldDataDaoTestIt {
  static final String inputFile = "LafOlCommentFieldData.json";
  static LafOlCommentFieldDataDao dao;
  static Gson gson =
      new GsonBuilder()
          .registerTypeHierarchyAdapter(byte[].class, new ByteArrayToBase64TypeAdapter())
          .setDateFormat("yyyy-MM-dd HH:mm:ss.S")
          .create();
  private LafOlCommentFieldData[] records;

  /** Run when the class is loaded. */
  @BeforeClass
  public static void beforeClass() {
    EntityManagerFactory factory = Persistence.createEntityManagerFactory("testpersistence");
    JpaDao jpa = new StandaloneJpaDao(factory.createEntityManager());
    dao = new DefaultLafOlCommentFieldDataDao(jpa);
  }

  /** Run before the test. */
  @Before
  public void before() {
    try {
      String json = FileUtils.readFileFromResource2String(inputFile, Charset.defaultCharset());
      records = gson.fromJson(json, LafOlCommentFieldData[].class);
      json = null;
      Arrays.stream(records).skip(1).forEach(o -> dao.create(o));
    } catch (IOException ex) {
      ex.printStackTrace();
    }
  }

  @After
  public void after() {
    records = null;
  }

  @Test
  public void testSelect() {
    final LafOlCommentFieldDataId id =
        new LafOlCommentFieldDataId(this.records[1].getLangcode(), this.records[1].getCid());
    LafOlCommentFieldData testResult = dao.find(id);
    assertNotNull("expect result", testResult);
    org.junit.Assert.assertEquals(
        "expect equals commentType ",
        this.records[1].getCommentType(),
        testResult.getCommentType());
    org.junit.Assert.assertTrue(
        "expect equals status ", this.records[1].getStatus() == testResult.getStatus());
    org.junit.Assert.assertTrue(
        "expect equals uid ", this.records[1].getUid() == testResult.getUid());
    org.junit.Assert.assertTrue(
        "expect equals pid ", this.records[1].getPid() == testResult.getPid());
    org.junit.Assert.assertTrue(
        "expect equals entityId ", this.records[1].getEntityId() == testResult.getEntityId());
    org.junit.Assert.assertEquals(
        "expect equals subject ", this.records[1].getSubject(), testResult.getSubject());
    org.junit.Assert.assertEquals(
        "expect equals name ", this.records[1].getName(), testResult.getName());
    org.junit.Assert.assertEquals(
        "expect equals mail ", this.records[1].getMail(), testResult.getMail());
    org.junit.Assert.assertEquals(
        "expect equals homepage ", this.records[1].getHomepage(), testResult.getHomepage());
    org.junit.Assert.assertEquals(
        "expect equals hostname ", this.records[1].getHostname(), testResult.getHostname());
    org.junit.Assert.assertTrue(
        "expect equals created ", this.records[1].getCreated() == testResult.getCreated());
    org.junit.Assert.assertTrue(
        "expect equals changed ", this.records[1].getChanged() == testResult.getChanged());
    org.junit.Assert.assertEquals(
        "expect equals thread ", this.records[1].getThread(), testResult.getThread());
    org.junit.Assert.assertEquals(
        "expect equals entityType ", this.records[1].getEntityType(), testResult.getEntityType());
    org.junit.Assert.assertEquals(
        "expect equals fieldName ", this.records[1].getFieldName(), testResult.getFieldName());
    org.junit.Assert.assertTrue(
        "expect equals defaultLangcode ",
        this.records[1].getDefaultLangcode() == testResult.getDefaultLangcode());
  }
}
