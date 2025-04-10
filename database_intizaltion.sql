INSERT INTO class(name, hp_mod, description)
    VALUES ('Warrior', 90,'temp');
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Swipe', 'A quick swing of ones weapons in a large arching circle', NULL, 1, 1);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Second Wind', 'No amount of pain can stop a true Warrior', NULL, 1, 4);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Taunt', 'Spew the violest of insult forceing enemies to attack you', NULL, 1, 7);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Skull Bash', 'A quick blow to the head tend to discomboulate ones enemie', NULL, 1, 10);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Blade Whirlwind', 'When facing multiple enmies try spinning realy quickly
    and hope you hit something', NULL, 1, 13);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Unstopable Force', 'once you get going nothing can stay in your way, ust do not try turning', NULL, 1, 16);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Unmoveable Object', 'Getting hit by a building can not even phase you', NULL, 1, 20);

INSERT INTO class(name, hp_mod, description)
    VALUES ('Priest', 60,'temp');
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Heal', 'Use holy energy to resotre the health of others', NULL, 2, 1);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Smite', 'Holy hammer to the face', NULL, 2, 4);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Prayer', 'Request aid from the divine', NULL, 2, 7);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Holy Fire', 'Heal the faithfull burn the heretic', NULL, 2, 10);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Sanctuary', 'Bless some land and stop the unholy from enetering', NULL, 2, 13);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Holy Light', 'Your gods light will burn away all the heritics', NULL, 2, 16);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Divine Intervention', 'Your god realy does not want you or your friends to die', NULL, 2, 20);

INSERT INTO class(name, hp_mod, description)
    VALUES ('Mage', 50,'temp');
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Magic Missle', 'Five scattered shots', NULL, 3, 1);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Magic Arrow', 'Single focus shot', NULL, 3, 4);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Illusion', 'create small to medium ilusionary object or disguise other objects', NULL, 3, 7);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Fireball', 'Throw a meduim balls of fire that explodes', NULL, 3, 10);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Combustion', 'Make anything burn to the ground', NULL, 3, 13);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Lightning bolt', 'For when fire does not work', NULL, 3, 16);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Death Ray', 'just incase you really dont like someone', NULL, 3, 20);

INSERT INTO class(name, hp_mod, description)
    VALUES ('Ranger', 70,'temp');
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Triple Shot', 'three arrows for the price of one', NULL, 4, 1);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Speak with Animals', 'you undersand all the freindly and not so freindly animals', NULL, 4, 4);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Entangling Strike', 'k', NULL, 4, 7);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Animal Companion', 'every hunter needs a friend', NULL, 4, 10);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Snipe', 'no matter the range you can hit it', NULL, 4, 13);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Explosive Shot', 'straping a bomb to an arrow is definitly a good idea', NULL, 4, 16);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Rain of Arrows', 'for trying to hit everyone in a large area', NULL, 4, 20);


INSERT INTO class(name, hp_mod, description)
    VALUES ('Rouge', 50,'temp');
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Backstab', 'a knife from behind is alway more painful', NULL, 5, 1);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Sneaky Git', 'makes you extra sneaky', NULL, 5, 4);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Pick Pocket', 'steal form anyone with ease', NULL, 5, 7);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Deadly Poison', 'poison weapons so enemies die slowly', NULL, 5, 10);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Caltrops', 'People can''t attack if they cant stand up', NULL, 5, 13);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('One Thousand Years of Death', 'The user tightly clasps
    their hands together and extends their middle and index fingers,
    using the full weight of their body, the user thrusts these four
    fingers between the target''s buttocks', NULL, 5, 16);
INSERT INTO ability(name, description, race_req, class_req, level)
    VALUES('Execute', 'kill those who are already injured', NULL, 5, 20);

INSERT INTO race(name, grt_mod, prw_mod, grc_mod, wit_mod, sav_mod)
    values ('Orc',3,3,3,3,3)

insert into country(name)
    values ('depresso land');

insert into  location(name, country)
    values ('happy land',1)