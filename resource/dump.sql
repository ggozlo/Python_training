BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'Yang','ggozlo@naver.com','010-4400-5041','ggozlo.com','2021-02-21 22:08:24');
INSERT INTO "users" VALUES(2,'Park','park@naver.com','010-4400-5041','park.com','2021-02-21 22:08:24');
INSERT INTO "users" VALUES(3,'LEE','LEE@naver.com','010-1111-1111','LEE.com','2021-02-21 22:08:24');
INSERT INTO "users" VALUES(4,'cho','cho@naver.com','101-1111-111','cho.com','2021-02-21 22:08:24');
INSERT INTO "users" VALUES(5,'jin','jin@naver.com','999-9999-9999','jin.net','2021-02-21 22:08:24');
COMMIT;
