DROP TABLE users;
CREATE TABLE users
(
    `id`             INT             NOT NULL    AUTO_INCREMENT COMMENT 'pk',
    `name`           VARCHAR(100)    NOT NULL    COMMENT 'username',
    PRIMARY KEY (id)
);
INSERT INTO users (id, name) VALUES (1, 'user1');