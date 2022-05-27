CREATE DATABASE IF NOT EXISTS notes_app;
USE notes_app;

CREATE TABLE users(
    id          int(25) auto_increment not null,
    name        varchar(100),
    surname     varchar(255),
    email       varchar(255) not null,
    password    varchar(255) not null,
    creation        date not null,
    CONSTRAINT pk_users PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDB;

CREATE TABLE notes(
    id          int(25) auto_increment not null,
    user_id     int(25) not null,
    title       varchar(255) not null,
    description MEDIUMTEXT,
    creation        date not null,
    CONSTRAINT pk_notes PRIMARY KEY(id),
    CONSTRAINT fk_user_note FOREIGN KEY(user_id) REFERENCES users(id)

)ENGINE=InnoDB;