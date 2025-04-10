-- Do THIS FIRST
CREATE DATABASE RealmQuest;

--Switch over to schema for RealmQuest DB
--Then Run This

CREATE TABLE IF NOT EXISTS race(
    id SERIAL PRIMARY KEY,
    name VARCHAR(63) NOT NULL,
    grt_mod INTEGER NULL,
    prw_mod INTEGER NULL,
    grc_mod INTEGER NULL,
    wit_mod INTEGER NULL,
    sav_mod INTEGER NULL
);
CREATE TABLE IF NOT EXISTS class(
    id SERIAL PRIMARY KEY,
    name VARCHAR(63) NOT NULL,
    hp_mod INTEGER NOT NULL,
    description Text NOT NULL
);
CREATE TABLE IF NOT EXISTS country(
    id SERIAL PRIMARY KEY,
    name VARCHAR(63) NOT NULL
);
CREATE TABLE IF NOT EXISTS location(
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    country INTEGER NOT NULL,
    FOREIGN KEY(country) REFERENCES country(id)
);
CREATE TABLE IF NOT EXISTS event(
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    description TEXT NOT NULL,
    event_location BIGINT NOT NULL,
    FOREIGN KEY(event_location) REFERENCES location(id)
);
CREATE TABLE IF NOT EXISTS ability(
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(63) NOT NULL,
    description TEXT NOT NULL,
    race_req INTEGER NULL,
    class_req INTEGER NULL,
    level INTEGER NOT NULL,
    FOREIGN KEY(race_req) REFERENCES race(id),
    FOREIGN KEY(class_req) REFERENCES class(id)
);
CREATE TABLE IF NOT EXISTS item(
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    weight DOUBLE PRECISION NOT NULL,
    equipable BOOLEAN NOT NULL,
    damage INTEGER NULL,
    armor INTEGER NULL
);
CREATE TABLE IF NOT EXISTS account(
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(255) UNIQUE NOT NULL,
    password  VARCHAR(255) NOT NULL,
    creation_date DATE NOT NULL DEFAULT CURRENT_DATE
);
CREATE TABLE IF NOT EXISTS character(
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    account_id UUID NOT NULL,
    name VARCHAR(63) NOT NULL,
    race INTEGER NOT NULL,
    char_class INTEGER NOT NULL,
    experience BIGINT NOT NULL,
    creation_date DATE NOT NULL DEFAULT CURRENT_DATE,
    location BIGINT NOT NULL,
    armor BIGINT NULL,
    weapon BIGINT NULL,
    belt BIGINT NULL,
    grit INTEGER NOT NULL,
    prowess INTEGER NOT NULL,
    grace INTEGER NOT NULL,
    wit INTEGER NOT NULL,
    savvy INTEGER NOT NULL,
    cur_hp INTEGER NOT NULL,
    age INTEGER NOT NULL,
    religion VARCHAR(63) NULL,
    personality TEXT NULL,
    alignment INTEGER NOT NULL,
    description TEXT NULL,
    backstory TEXT NULL,
    image VARCHAR NULL,
    FOREIGN KEY(account_id) REFERENCES account(id),
    FOREIGN KEY(location) REFERENCES location(id),
    FOREIGN KEY(armor) REFERENCES item(id),
    FOREIGN KEY(race) REFERENCES race(id),
    FOREIGN KEY(char_class) REFERENCES class(id),
    FOREIGN KEY(weapon) REFERENCES item(id),
    FOREIGN KEY(belt) REFERENCES item(id)
);
CREATE TABLE IF NOT EXISTS chat_leungsaikok(
    id BIGSERIAL PRIMARY KEY,
    account_id UUID NOT NULL,
    char_id UUID NOT NULL,
    time_stamp TIMESTAMP NOT NULL DEFAULT NOW(),
    message TEXT NOT NULL,
    char_name VARCHAR(63) NOT NULL,
    profile_image VARCHAR NULL,
    FOREIGN KEY(account_id) REFERENCES account(id),
    FOREIGN KEY(char_id) REFERENCES character(id)
);
CREATE TABLE IF NOT EXISTS chat_linshanho(
    id BIGSERIAL PRIMARY KEY,
    account_id UUID NOT NULL,
    char_id UUID NOT NULL,
    time_stamp TIMESTAMP NOT NULL DEFAULT NOW(),
    message TEXT NOT NULL,
    char_name VARCHAR(63) NOT NULL,
    profile_image VARCHAR NULL,
    FOREIGN KEY(account_id) REFERENCES account(id),
    FOREIGN KEY(char_id) REFERENCES character(id)
);
CREATE TABLE IF NOT EXISTS chat_peton(
    id BIGSERIAL PRIMARY KEY,
    account_id UUID NOT NULL,
    char_id UUID NOT NULL,
    time_stamp TIMESTAMP NOT NULL DEFAULT NOW(),
    message TEXT NOT NULL,
    char_name VARCHAR(63) NOT NULL,
    profile_image VARCHAR NULL,
    FOREIGN KEY(account_id) REFERENCES account(id),
    FOREIGN KEY(char_id) REFERENCES character(id)
);
CREATE TABLE IF NOT EXISTS chat_boton(
    id BIGSERIAL PRIMARY KEY,
    account_id UUID NOT NULL,
    char_id UUID NOT NULL,
    time_stamp TIMESTAMP NOT NULL DEFAULT NOW(),
    message TEXT NOT NULL,
    char_name VARCHAR(63) NOT NULL,
    profile_image VARCHAR NULL,
    FOREIGN KEY(account_id) REFERENCES account(id),
    FOREIGN KEY(char_id) REFERENCES character(id)
);
CREATE TABLE IF NOT EXISTS chat_trere(
    id BIGSERIAL PRIMARY KEY,
    account_id UUID NOT NULL,
    char_id UUID NOT NULL,
    time_stamp TIMESTAMP NOT NULL DEFAULT NOW(),
    message TEXT NOT NULL,
    char_name VARCHAR(63) NOT NULL,
    profile_image VARCHAR NULL,
    FOREIGN KEY(account_id) REFERENCES account(id),
    FOREIGN KEY(char_id) REFERENCES character(id)
);
CREATE TABLE IF NOT EXISTS chat_towbury(
    id BIGSERIAL PRIMARY KEY,
    account_id UUID NOT NULL,
    char_id UUID NOT NULL,
    time_stamp TIMESTAMP NOT NULL DEFAULT NOW(),
    message TEXT NOT NULL,
    char_name VARCHAR(63) NOT NULL,
    profile_image VARCHAR NULL,
    FOREIGN KEY(account_id) REFERENCES account(id),
    FOREIGN KEY(char_id) REFERENCES character(id)
);
CREATE TABLE IF NOT EXISTS chat_sobury(
    id BIGSERIAL PRIMARY KEY,
    account_id UUID NOT NULL,
    char_id UUID NOT NULL,
    time_stamp TIMESTAMP NOT NULL DEFAULT NOW(),
    message TEXT NOT NULL,
    char_name VARCHAR(63) NOT NULL,
    profile_image VARCHAR NULL,
    FOREIGN KEY(account_id) REFERENCES account(id),
    FOREIGN KEY(char_id) REFERENCES character(id)
);
CREATE TABLE IF NOT EXISTS chat_torkneth(
    id BIGSERIAL PRIMARY KEY,
    account_id UUID NOT NULL,
    char_id UUID NOT NULL,
    time_stamp TIMESTAMP NOT NULL DEFAULT NOW(),
    message TEXT NOT NULL,
    char_name VARCHAR(63) NOT NULL,
    profile_image VARCHAR NULL,
    FOREIGN KEY(account_id) REFERENCES account(id),
    FOREIGN KEY(char_id) REFERENCES character(id)
);
CREATE TABLE IF NOT EXISTS chat_alneridge(
    id BIGSERIAL PRIMARY KEY,
    account_id UUID NOT NULL,
    char_id UUID NOT NULL,
    time_stamp TIMESTAMP NOT NULL DEFAULT NOW(),
    message TEXT NOT NULL,
    char_name VARCHAR(63) NOT NULL,
    profile_image VARCHAR NULL,
    FOREIGN KEY(account_id) REFERENCES account(id),
    FOREIGN KEY(char_id) REFERENCES character(id)
);
CREATE TABLE IF NOT EXISTS chat_tarmouth(
    id BIGSERIAL PRIMARY KEY,
    account_id UUID NOT NULL,
    char_id UUID NOT NULL,
    time_stamp TIMESTAMP NOT NULL DEFAULT NOW(),
    message TEXT NOT NULL,
    char_name VARCHAR(63) NOT NULL,
    profile_image VARCHAR NULL,
    FOREIGN KEY(account_id) REFERENCES account(id),
    FOREIGN KEY(char_id) REFERENCES character(id)
);
CREATE TABLE IF NOT EXISTS chat_wigan(
    id BIGSERIAL PRIMARY KEY,
    account_id UUID NOT NULL,
    char_id UUID NOT NULL,
    time_stamp TIMESTAMP NOT NULL DEFAULT NOW(),
    message TEXT NOT NULL,
    char_name VARCHAR(63) NOT NULL,
    profile_image VARCHAR NULL,
    FOREIGN KEY(account_id) REFERENCES account(id),
    FOREIGN KEY(char_id) REFERENCES character(id)
);
CREATE TABLE IF NOT EXISTS chat_dhodh(
    id BIGSERIAL PRIMARY KEY,
    account_id UUID NOT NULL,
    char_id UUID NOT NULL,
    time_stamp TIMESTAMP NOT NULL DEFAULT NOW(),
    message TEXT NOT NULL,
    char_name VARCHAR(63) NOT NULL,
    profile_image VARCHAR NULL,
    FOREIGN KEY(account_id) REFERENCES account(id),
    FOREIGN KEY(char_id) REFERENCES character(id)
);
CREATE TABLE IF NOT EXISTS chat_ghoregag(
    id BIGSERIAL PRIMARY KEY,
    account_id UUID NOT NULL,
    char_id UUID NOT NULL,
    time_stamp TIMESTAMP NOT NULL DEFAULT NOW(),
    message TEXT NOT NULL,
    char_name VARCHAR(63) NOT NULL,
    profile_image VARCHAR NULL,
    FOREIGN KEY(account_id) REFERENCES account(id),
    FOREIGN KEY(char_id) REFERENCES character(id)
);
CREATE TABLE IF NOT EXISTS chat_dhezzol(
    id BIGSERIAL PRIMARY KEY,
    account_id UUID NOT NULL,
    char_id UUID NOT NULL,
    time_stamp TIMESTAMP NOT NULL DEFAULT NOW(),
    message TEXT NOT NULL,
    char_name VARCHAR(63) NOT NULL,
    profile_image VARCHAR NULL,
    FOREIGN KEY(account_id) REFERENCES account(id),
    FOREIGN KEY(char_id) REFERENCES character(id)
);
CREATE TABLE IF NOT EXISTS chat_gugh(
    id BIGSERIAL PRIMARY KEY,
    account_id UUID NOT NULL,
    char_id UUID NOT NULL,
    time_stamp TIMESTAMP NOT NULL DEFAULT NOW(),
    message TEXT NOT NULL,
    char_name VARCHAR(63) NOT NULL,
    profile_image VARCHAR NULL,
    FOREIGN KEY(account_id) REFERENCES account(id),
    FOREIGN KEY(char_id) REFERENCES character(id)
);
CREATE TABLE IF NOT EXISTS chat_cudadh(
    id BIGSERIAL PRIMARY KEY,
    account_id UUID NOT NULL,
    char_id UUID NOT NULL,
    time_stamp TIMESTAMP NOT NULL DEFAULT NOW(),
    message TEXT NOT NULL,
    char_name VARCHAR(63) NOT NULL,
    profile_image VARCHAR NULL,
    FOREIGN KEY(account_id) REFERENCES account(id),
    FOREIGN KEY(char_id) REFERENCES character(id)
);
CREATE TABLE IF NOT EXISTS chat_arkorzaz(
    id BIGSERIAL PRIMARY KEY,
    account_id UUID NOT NULL,
    char_id UUID NOT NULL,
    time_stamp TIMESTAMP NOT NULL DEFAULT NOW(),
    message TEXT NOT NULL,
    char_name VARCHAR(63) NOT NULL,
    profile_image VARCHAR NULL,
    FOREIGN KEY(account_id) REFERENCES account(id),
    FOREIGN KEY(char_id) REFERENCES character(id)
);
CREATE TABLE IF NOT EXISTS char_abli(
    char_id UUID NOT NULL,
    abli_id BIGINT NOT NULL,
    PRIMARY KEY (char_id, abli_id),
    FOREIGN KEY(abli_id) REFERENCES ability(id),
    FOREIGN KEY(char_id) REFERENCES character(id)
);
CREATE TABLE IF NOT EXISTS char_inv(
    char_id UUID NOT NULL,
    item_id BIGINT NOT NULL,
    quantity INT NOT NULL, 
    PRIMARY KEY (char_id, item_id),
    FOREIGN KEY(item_id) REFERENCES item(id),
    FOREIGN KEY(char_id) REFERENCES character(id)
);