SELECT schema_name FROM information_schema.schemata WHERE schema_name != 'information_schema' AND schema_name != 'performance_schema' AND schema_name != 'cascade-7-12-2-prod' AND schema_name != 'cascade-7-12-2-test';
