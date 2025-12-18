package ru.itmo.stella.typechecker.expr;

import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import ru.itmo.stella.typechecker.exception.StellaException;
import ru.itmo.stella.typechecker.exception.record.StellaMissingRecordFieldsException;
import ru.itmo.stella.typechecker.exception.record.StellaUnexpectedRecordException;
import ru.itmo.stella.typechecker.exception.record.StellaUnexpectedRecordFieldsException;
import ru.itmo.stella.typechecker.type.StellaRecordType;
import ru.itmo.stella.typechecker.type.StellaType;
import ru.itmo.stella.typechecker.type.StellaType.Tag;

public class RecordExpr extends StellaExpression {
	private Map<String, StellaExpression> recordFields;
	
	public RecordExpr(Map<String, StellaExpression> recordFields) {
		this.recordFields = Collections.unmodifiableMap(recordFields);
	}
	
	public Map<String, StellaExpression> getRecordFields() {
		return recordFields;
	}
	
	public StellaExpression getField(String fieldName) {
		return recordFields.get(fieldName);
	}
	
	@Override
	public void checkType(ExpressionContext context, StellaType expected) throws StellaException {
		StellaRecordType actualRecordType = inferType(context);
		
		if (expected.getTypeTag() != Tag.RECORD)
			throw new StellaUnexpectedRecordException(expected, this);
		
		StellaRecordType expectedRecordType = (StellaRecordType) expected;
		
		List<String> problemFields = findMissingFields(actualRecordType, expectedRecordType);
		
		if (!problemFields.isEmpty())
			throw new StellaUnexpectedRecordFieldsException(problemFields, expectedRecordType, this);
		
		problemFields = findMissingFields(expectedRecordType, actualRecordType);
		
		if (!problemFields.isEmpty())
			throw new StellaMissingRecordFieldsException(problemFields, expectedRecordType, this);
		
		for (String fieldName: expectedRecordType.getFields()) {
			StellaType expectedFieldType = expectedRecordType.getFieldType(fieldName);
			
			getField(fieldName).checkType(context, expectedFieldType);
		}
		
		checkTypesEquality(expected, actualRecordType);
	}

	@Override
	public StellaRecordType inferType(ExpressionContext context) throws StellaException {
		Map<String, StellaType> fieldsTypes = new LinkedHashMap<>(recordFields.size());
		
		for (Map.Entry<String, StellaExpression> entry: recordFields.entrySet()) {
			StellaType recordType = entry.getValue().inferType(context);
			fieldsTypes.put(entry.getKey(), recordType);
		}
		
		return new StellaRecordType(fieldsTypes);
	}

	@Override
	public String toString() {
		return String.format("{%s}",
					String.join(
						", ",
						recordFields
							.entrySet()
							.stream()
							.map(entry -> String.format("%s = %s", entry.getKey(), entry.getValue()))
							.toList()
					)
				);
	}

	private static List<String> findMissingFields(StellaRecordType from, StellaRecordType where) {
		return from
			.getFields()
			.stream()
			.filter(field -> !where.hasField(field))
			.toList();
	}
}
