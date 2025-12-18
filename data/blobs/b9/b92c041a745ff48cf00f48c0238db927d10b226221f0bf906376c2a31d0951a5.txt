package defpackage;

/* compiled from: PG */
/* loaded from: classes3.dex */
public final /* synthetic */ class snu implements agne {
    private final /* synthetic */ int a;

    @Override // defpackage.agne
    public final void a(int i, agnw agnwVar) {
        switch (this.a) {
            case 0:
                Integer valueOf = Integer.valueOf(i);
                String[] strArr = snz.a;
                valueOf.getClass();
                if (i != 58240) {
                    return;
                }
                snz.b(agnwVar);
                return;
            case 1:
                Integer valueOf2 = Integer.valueOf(i);
                String[] strArr2 = snp.a;
                valueOf2.getClass();
                if (i != 57000) {
                    return;
                }
                snp.b(agnwVar);
                return;
            case 2:
                Integer valueOf3 = Integer.valueOf(i);
                String[] strArr3 = sof.a;
                valueOf3.getClass();
                if (i != 51010) {
                    return;
                }
                sof.a(agnwVar);
                return;
            case 3:
                Integer valueOf4 = Integer.valueOf(i);
                String[] strArr4 = sor.a;
                valueOf4.getClass();
                switch (i) {
                    case 15020:
                        sor.b(agnwVar, 15020);
                        return;
                    case 18020:
                        agnwVar.z("ALTER TABLE desktop ADD COLUMN browser_type INT DEFAULT(0);");
                        return;
                    case 20020:
                        agnwVar.z("ALTER TABLE desktop ADD COLUMN needs_unpairing INT DEFAULT(0);");
                        return;
                    case 21030:
                        agnwVar.z("ALTER TABLE desktop ADD COLUMN encryption_key BLOB;");
                        agnwVar.z("ALTER TABLE desktop ADD COLUMN hmac_key BLOB;");
                        return;
                    case 22040:
                        agnwVar.z("ALTER TABLE desktop ADD COLUMN operating_system TEXT DEFAULT('') NOT NULL;");
                        agnwVar.z("ALTER TABLE desktop ADD COLUMN operating_system_version TEXT DEFAULT('') NOT NULL;");
                        return;
                    case 41010:
                        agnwVar.z("ALTER TABLE desktop ADD COLUMN backend_type INT;");
                        return;
                    case 58010:
                        agnwVar.z("ALTER TABLE desktop ADD COLUMN is_active INT DEFAULT(0);");
                        agnwVar.z("ALTER TABLE desktop ADD COLUMN request_id TEXT DEFAULT('');");
                        agnwVar.z("ALTER TABLE desktop ADD COLUMN is_persistent INT DEFAULT(0);");
                        agnwVar.z("ALTER TABLE desktop ADD COLUMN desktop_type INT DEFAULT(0);");
                        return;
                    case 58960:
                        agnwVar.z("ALTER TABLE desktop ADD COLUMN pairing_type INT DEFAULT(0);");
                        return;
                    case 59290:
                        agnwVar.z("ALTER TABLE desktop ADD COLUMN destination_registration_id BLOB;");
                        return;
                    case 59560:
                        agnwVar.z("ALTER TABLE desktop ADD COLUMN gaia_email TEXT;");
                        return;
                    case 59870:
                        agnwVar.z("ALTER TABLE desktop ADD COLUMN creation_time INT DEFAULT(0);");
                        return;
                    default:
                        return;
                }
            case 4:
                Integer valueOf5 = Integer.valueOf(i);
                String[] strArr5 = soz.a;
                valueOf5.getClass();
                if (i != 10015) {
                    return;
                }
                soz.b(agnwVar);
                return;
            case 5:
                Integer valueOf6 = Integer.valueOf(i);
                String[] strArr6 = spj.a;
                valueOf6.getClass();
                switch (i) {
                    case 59150:
                        spj.c(agnwVar, 59150);
                        return;
                    case 59170:
                        agnwVar.z("ALTER TABLE drafts ADD COLUMN subject TEXT;");
                        agnwVar.z("ALTER TABLE drafts ADD COLUMN is_urgent INT DEFAULT(0) NOT NULL;");
                        return;
                    case 59420:
                        agnwVar.z("ALTER TABLE drafts ADD COLUMN attachments BLOB;");
                        return;
                    case 59540:
                        agnwVar.z("ALTER TABLE drafts ADD COLUMN replied_to_message_id TEXT;");
                        return;
                    case 59720:
                        agnwVar.z("ALTER TABLE drafts ADD COLUMN is_encrypted INT DEFAULT(0) NOT NULL;");
                        return;
                    default:
                        return;
                }
            case 6:
                Integer valueOf7 = Integer.valueOf(i);
                String[] strArr7 = spv.a;
                valueOf7.getClass();
                switch (i) {
                    case 35050:
                        spv.c(agnwVar, 35050);
                        return;
                    case 35060:
                        agnwVar.z("ALTER TABLE etouffee_rcs_metadata ADD COLUMN attachment_uri TEXT;");
                        return;
                    case 37020:
                        agnwVar.z("ALTER TABLE etouffee_rcs_metadata ADD COLUMN custom_delivery_receipt_mime_type TEXT;");
                        agnwVar.z("ALTER TABLE etouffee_rcs_metadata ADD COLUMN custom_delivery_receipt_content BLOB;");
                        return;
                    case 48010:
                        agnwVar.z("ALTER TABLE etouffee_rcs_metadata ADD COLUMN file_uploaded_xml_from_content_server BLOB;");
                        agnwVar.z("ALTER TABLE etouffee_rcs_metadata ADD COLUMN file_uploaded_fallback_uri TEXT;");
                        agnwVar.z("ALTER TABLE etouffee_rcs_metadata ADD COLUMN file_uploaded_expiry INT;");
                        return;
                    case 56020:
                        agnwVar.z("ALTER TABLE etouffee_rcs_metadata ADD COLUMN plaintext_attachment_name TEXT;");
                        agnwVar.z("ALTER TABLE etouffee_rcs_metadata ADD COLUMN plaintext_attachment_content_type TEXT;");
                        agnwVar.z("ALTER TABLE etouffee_rcs_metadata ADD COLUMN plaintext_thumbnail_content_type TEXT;");
                        return;
                    default:
                        return;
                }
            case 7:
                Integer valueOf8 = Integer.valueOf(i);
                String[] strArr8 = sqd.a;
                valueOf8.getClass();
                if (i != 33010) {
                    return;
                }
                sqd.a(agnwVar);
                return;
            case 8:
                Integer valueOf9 = Integer.valueOf(i);
                String[] strArr9 = sqp.a;
                valueOf9.getClass();
                if (i != 39010) {
                    if (i != 39030) {
                        if (i != 46030) {
                            return;
                        }
                        agnwVar.z("ALTER TABLE flagged_messages ADD COLUMN flagged_message_notified INT DEFAULT(0);");
                        return;
                    }
                    agnwVar.z("ALTER TABLE flagged_messages ADD COLUMN flagged_message_timestamp INT;");
                    return;
                }
                sqp.b(agnwVar, 39010);
                return;
            case 9:
                Integer valueOf10 = Integer.valueOf(i);
                String[] strArr10 = sqv.a;
                valueOf10.getClass();
                if (i != 60140) {
                    return;
                }
                agnc.F(agnwVar, "gemini_conversation_id_mappings", sqv.c("TEMP___gemini_conversation_id_mappings"), sqv.a, sqv.b(60140));
                return;
            case 10:
                Integer valueOf11 = Integer.valueOf(i);
                String[] strArr11 = sqv.a;
                valueOf11.getClass();
                if (i != 60010) {
                    if (i != 60090) {
                        return;
                    }
                    agnwVar.z("DROP INDEX IF EXISTS index_gemini_conversation_id_mappings_gemini_conversation_id");
                    agnwVar.z("CREATE UNIQUE INDEX index_gemini_conversation_id_mappings_gemini_conversation_id ON gemini_conversation_id_mappings(gemini_conversation_id);");
                    return;
                }
                sqv.a(agnwVar, 60010);
                return;
            case 11:
                Integer valueOf12 = Integer.valueOf(i);
                String[] strArr12 = src.a;
                valueOf12.getClass();
                if (i != 60000) {
                    return;
                }
                src.a(agnwVar);
                return;
            case 12:
                Integer valueOf13 = Integer.valueOf(i);
                String[] strArr13 = srm.a;
                valueOf13.getClass();
                switch (i) {
                    case 24000:
                        srm.b(agnwVar, 24000);
                        return;
                    case 32000:
                        agnwVar.z("ALTER TABLE generic_worker_queue ADD COLUMN flags INTEGER DEFAULT(0);");
                        return;
                    case 34000:
                        agnwVar.z("ALTER TABLE generic_worker_queue ADD COLUMN next_execute_timestamp INTEGER DEFAULT(0);");
                        return;
                    case 39020:
                        agnwVar.z("ALTER TABLE generic_worker_queue ADD COLUMN account_id INTEGER DEFAULT(-1);");
                        return;
                    case 58340:
                        agnwVar.z("DROP INDEX IF EXISTS index_generic_worker_queue_next_execute_timestamp");
                        agnwVar.z("CREATE INDEX index_generic_worker_queue_next_execute_timestamp ON generic_worker_queue(next_execute_timestamp);");
                        agnwVar.z("DROP INDEX IF EXISTS index_multi_column_index");
                        agnwVar.z("CREATE INDEX index_multi_column_index ON generic_worker_queue(in_flight, retry_count, item_id, item_table_type, next_execute_timestamp);");
                        return;
                    case 59700:
                        agnwVar.z("ALTER TABLE generic_worker_queue ADD COLUMN trigger_name TEXT;");
                        return;
                    case 59970:
                        agnwVar.z("ALTER TABLE generic_worker_queue ADD COLUMN enqueued_timestamp INTEGER DEFAULT(0);");
                        return;
                    default:
                        return;
                }
            case 13:
                Integer valueOf14 = Integer.valueOf(i);
                int[] iArr = srn.a;
                valueOf14.getClass();
                if (i != 59680) {
                    return;
                }
                agnc.E(agnwVar, "group_conversation_participants_audit_log");
                return;
            case 14:
                Integer valueOf15 = Integer.valueOf(i);
                int[] iArr2 = srn.a;
                valueOf15.getClass();
                if (i != 59610) {
                    return;
                }
                srn.a(agnwVar, 59610);
                return;
            case 15:
                Integer valueOf16 = Integer.valueOf(i);
                int[] iArr3 = sro.a;
                valueOf16.getClass();
                if (i != 59690) {
                    return;
                }
                agnc.E(agnwVar, "group_conversation_participants");
                return;
            case 16:
                Integer valueOf17 = Integer.valueOf(i);
                int[] iArr4 = sro.a;
                valueOf17.getClass();
                if (i != 59590) {
                    return;
                }
                sro.a(agnwVar, 59590);
                return;
            case 17:
                Integer valueOf18 = Integer.valueOf(i);
                String[] strArr14 = srz.a;
                valueOf18.getClass();
                switch (i) {
                    case 58660:
                        srz.c(agnwVar, 58660);
                        return;
                    case 58700:
                        agnwVar.z("ALTER TABLE lighter_conversations_table ADD COLUMN read INTEGER DEFAULT(1);");
                        return;
                    case 58760:
                        agnwVar.z("DROP INDEX IF EXISTS index_lighter_conversation_read_0");
                        agnwVar.z("CREATE INDEX index_lighter_conversation_read_0 ON lighter_conversations_table(read) WHERE read == 0;");
                        return;
                    case 58810:
                        agnwVar.z("ALTER TABLE lighter_conversations_table ADD COLUMN is_last_message_outgoing INTEGER;");
                        return;
                    case 58930:
                        agnwVar.z("DROP INDEX IF EXISTS index_lighter_conversations_table_conversation_id");
                        agnwVar.z("CREATE INDEX index_lighter_conversations_table_conversation_id ON lighter_conversations_table(conversation_id);");
                        return;
                    case 59030:
                        agnwVar.z("ALTER TABLE lighter_conversations_table ADD COLUMN conversation_status INTEGER;");
                        return;
                    case 59040:
                        agnwVar.z("ALTER TABLE lighter_conversations_table ADD COLUMN last_action_timestamp INT DEFAULT(0);");
                        return;
                    case 59100:
                        agnwVar.z("ALTER TABLE lighter_conversations_table ADD COLUMN sync_timestamp_ms INT DEFAULT(0);");
                        return;
                    default:
                        return;
                }
            case 18:
                Integer valueOf19 = Integer.valueOf(i);
                String[] strArr15 = srz.a;
                valueOf19.getClass();
                if (i != 59110) {
                    return;
                }
                agnc.F(agnwVar, "lighter_conversations_table", srz.b(59110, "TEMP___lighter_conversations_table"), srz.a, srz.d(59110));
                return;
            case 19:
                Integer valueOf20 = Integer.valueOf(i);
                String[] strArr16 = ssh.a;
                valueOf20.getClass();
                if (i != 26010) {
                    return;
                }
                ssh.a(agnwVar);
                return;
            default:
                Integer valueOf21 = Integer.valueOf(i);
                String[] strArr17 = sss.a;
                valueOf21.getClass();
                if (i != 21010) {
                    if (i != 22020) {
                        return;
                    }
                    agnwVar.z("ALTER TABLE link_preview ADD COLUMN link_preview_failed INTEGER DEFAULT(0);");
                    return;
                }
                agnwVar.z("ALTER TABLE link_preview ADD COLUMN link_preview_prevented INTEGER DEFAULT(0);");
                return;
        }
    }
}
