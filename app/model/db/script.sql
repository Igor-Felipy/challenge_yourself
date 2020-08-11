CREATE DATABASE ChallengeYourself IF NOT EXISTS;

USE ChallengeYourself;

CREATE TABLE TB_Challenge IF NOT EXISTS(
    challenge_id
    title
    answer
    media_1
    media_2
    media_3
    media_4
    text_1
    text_2
    dificult
    lang
    active
);

CREATE TABLE TB_Profile IF NOT EXISTS(
    profile_id
    profile_name
    nickname
    email
    pass 
    active
    profile_description
    birth
    profile_image
    cell
    adress
    lang
);