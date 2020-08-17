CREATE DATABASE ChallengeYourself IF NOT EXISTS;

USE ChallengeYourself;

CREATE TABLE TB_Profile IF NOT EXISTS(
    profile_id  int(12) NOT NULL AUTO_INCREMENT,
    profile_name    varchar(100),
    nickname    varchar(25),
    email   varchar(100),
    pass    varchar(25),
    active  char(1),
    profile_description varchar(200),
    birth   date,
    profile_image   varchar(200),
    cell    varchar(25),
    adress  varchar(200),
    lang    varchar(20),
    pontuation int(200),
    PRIMARY KEY ('profile_id')
);

CREATE TABLE TB_Challenge IF NOT EXISTS(
    challenge_id int(12) NOT NULL AUTO_INCREMENT,
    title   varchar(100),
    answer  varchar(25),
    media_1 varchar(200),
    media_2 varchar(200),
    media_3 varchar(200),
    media_4 varchar(200),
    text_1  varchar(200),
    text_2  varchar(200),
    dificult    char(1),
    lang    varchar(20),
    active  char(1),
    profile_id  int(12) NOT NULL,
    PRIMARY KEY ('challenge_id')
);

ALTER TABLE TB_Challenge ADD FOREIGN KEY(profile_id) REFERENCES TB_Profile(profile_id);