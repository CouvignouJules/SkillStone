START TRANSACTION;


INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$100000$2j8WyRty5ThZ$DaUrAqxzOvAQCR1rLcfnqOPyBuxd9Xu5aWydcRLdAv8=', '2018-01-26 07:07:36.804742', 1, 'root', '', '', '', 1, 1, '2018-01-19 10:53:55.483275'),
(2, 'pbkdf2_sha256$100000$F5wkL2RRg7kA$0vhahw0+XMbFLM/kIzq+5DJsnaqwa5ibT8hIj+aBVAs=', '2018-01-19 10:58:38.596287', 0, 'toto', '', '', '', 0, 1, '2018-01-19 10:56:03.696634');

INSERT INTO `deck_card` (`id`, `name`, `description`, `cost`, `attack`, `health`, `cardType_id`, `effect_id`, `img`) VALUES
(1, 'Boule de feu', 'Inflige 6 points de dégâts.', 6, 6, 0, 2, NULL, 'static/img/card/deck.jpg'),
(2, 'Cobra empereur', 'Toxicité', 3, 2, 3, 1, 3, 'static/img/card/Cobra_empereur.jpg'),
(3, 'Feu follet', 'Ne fait rien', 0, 1, 1, 1, NULL, 'static/img/card/deck.jpg'),
(4, 'Rampant des tourbières', 'Provocation', 5, 3, 6, 1, 2, 'static/img/card/Rampant_des_tourbières.jpg'),
(5, 'Tigre de Strangleronce', 'Camouflage', 5, 5, 5, 1, 1, 'static/img/card/Tigre_de_Strangleronce.jpg'),
(6, 'Boule de feu', 'Inflige 6 points de dégâts.', 6, 6, 0, 2, NULL, 'static/img/card/deck.jpg'),
(7, 'Cobra empereur', 'Toxicité', 3, 2, 3, 1, 3, 'static/img/card/Cobra_empereur.jpg'),
(8, 'Feu follet', 'Ne fait rien', 0, 1, 1, 1, NULL, 'static/img/card/deck.jpg'),
(9, 'Rampant des tourbières', 'Provocation', 5, 3, 6, 1, 2, 'static/img/card/Rampant_des_tourbières.jpg'),
(10, 'Tigre de Strangleronce', 'Camouflage', 5, 5, 5, 1, 1, 'static/img/card/Tigre_de_Strangleronce.jpg'),
(11, 'Boule de feu', 'Inflige 6 points de dégâts.', 6, 6, 0, 2, NULL, 'static/img/card/deck.jpg'),
(12, 'Cobra empereur', 'Toxicité', 3, 2, 3, 1, 3, 'static/img/card/Cobra_empereur.jpg'),
(13, 'Feu follet', 'Ne fait rien', 0, 1, 1, 1, NULL, 'static/img/card/deck.jpg'),
(14, 'Rampant des tourbières', 'Provocation', 5, 3, 6, 1, 2, 'static/img/card/Rampant_des_tourbières.jpg'),
(15, 'Tigre de Strangleronce', 'Camouflage', 5, 5, 5, 1, 1, 'static/img/card/Tigre_de_Strangleronce.jpg'),
(16, 'Boule de feu', 'Inflige 6 points de dégâts.', 6, 6, 0, 2, NULL, 'static/img/card/deck.jpg'),
(17, 'Cobra empereur', 'Toxicité', 3, 2, 3, 1, 3, 'static/img/card/Cobra_empereur.jpg'),
(18, 'Feu follet', 'Ne fait rien', 0, 1, 1, 1, NULL, 'static/img/card/deck.jpg'),
(19, 'Rampant des tourbières', 'Provocation', 5, 3, 6, 1, 2, 'static/img/card/Rampant_des_tourbières.jpg'),
(20, 'Tigre de Strangleronce', 'Camouflage', 5, 5, 5, 1, 1, 'static/img/card/Tigre_de_Strangleronce.jpg');

INSERT INTO `deck_cardtype` (`id`, `name`) VALUES
(1, 'Minion'),
(2, 'Spell');

INSERT INTO `deck_deck` (`id`, `name`) VALUES
(1, 'fist'),
(2, 'second');

INSERT INTO `deck_deck_cards` (`id`, `deck_id`, `card_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4),
(5, 1, 5),
(6, 2, 1),
(7, 2, 2),
(8, 2, 4),

(9, 1, 10),
(10, 1, 11),
(11, 1, 12),
(12, 1, 13),
(13, 1, 14),
(14, 1, 15),
(15, 1, 16),
(16, 1, 17),
(17, 1, 18),
(18, 1, 19),
(19, 1, 20),
(20, 1, 7),
(21, 1, 8),
(22, 1, 9);

INSERT INTO `deck_effect` (`id`, `name`) VALUES
(1, 'Camouflage'),
(2, 'Provocation'),
(3, 'Toxicité');

INSERT INTO `deck_player` (`id`, `user_id`) VALUES
(1, 1),
(2, 2);

INSERT INTO `deck_player_cardcollection` (`id`, `player_id`, `card_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4),
(5, 1, 5),

(6, 1, 6),
(7, 1, 7),
(8, 1, 8),
(9, 1, 9),
(10, 1, 10),
(11, 1, 11),
(12, 1, 12),
(13, 1, 13),
(14, 1, 14),
(15, 1, 15),
(16, 1, 16),
(17, 1, 17),
(18, 1, 18),
(19, 1, 19),
(20, 1, 20);

COMMIT;