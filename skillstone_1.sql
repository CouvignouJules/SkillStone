START
TRANSACTION;


INSERT INTO `auth_user` (`
id`,
`password
`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$100000$2j8WyRty5ThZ$DaUrAqxzOvAQCR1rLcfnqOPyBuxd9Xu5aWydcRLdAv8=', '2018-01-26 07:07:36.804742', 1, 'root', '', '', '', 1, 1, '2018-01-19 10:53:55.483275'),
(2, 'pbkdf2_sha256$100000$F5wkL2RRg7kA$0vhahw0+XMbFLM/kIzq+5DJsnaqwa5ibT8hIj+aBVAs=', '2018-01-19 10:58:38.596287', 0, 'toto', '', '', '', 0, 1, '2018-01-19 10:56:03.696634');

INSERT INTO `deck_card` (`
id`,
`name
`, `description`, `cost`, `attack`, `health`, `cardType_id`, `effect_id`, `img`) VALUES
(1, 'Boule de feu', 'Inflige 6 points de dégâts.', 4, 6, 0, 2, NULL, 'static/img/card/Boule_de_feu.png'),
(2, 'Cobra empereur', 'Toxicité', 3, 2, 3, 1, 3, 'static/img/card/Cobra_empereur.png'),
(3, 'Feu follet', 'Ne fait rien', 0, 1, 1, 1, NULL, 'static/img/card/Feu_follet.png'),
(4, 'Rampant des tourbières', 'Provocation', 5, 3, 6, 1, 2, 'static/img/card/Rampant_des_tourbières.png'),
(5, 'Tigre de Strangleronce', 'Camouflage', 5, 5, 5, 1, 1, 'static/img/card/Tigre_de_Strangleronce.png'),
(6, 'Consécration', 'Inflige 2 points de dégâts à tous les adversaires.', 4, 2, 0, 2, NULL, 'static/img/card/Consecration.png'),
(7, 'Crocilisque des rivières', 'Ne fait rien', 2, 2, 3, 1, NULL, 'static/img/card/Crocilisque_des_rivieres.png'),
(8, 'Diablotin des flammes', 'Cri de guerre : Inflige 3 points de dégâts à votre héros.', 1, 3, 2, 1, 4, 'static/img/card/Diablotin_des_flammes.png'),
(9, 'Défenseur d Argus', 'Cri de guerre : donne aux serviteurs adjacents +1 / +1 et Provocation.', 4, 2, 3, 1, 4, 'static/img/card/Defenseur_d_Argus.png'),
(10, 'Éclair', 'Inflige 3 points de dégâts', 1, 3, 0, 2, NULL, 'static/img/card/Eclair.png'),
(11, 'Exécution', 'Détruit un serviteur blessé.', 2, 0, 0, 2, NULL, 'static/img/card/Execution.png'),
(12, 'Gardien mogu shan', 'Provocation', 4, 1, 7, 1, 2, 'static/img/card/Gardien_mogushan.png'),
(13, 'Imposition des mains', 'Rend 8 points de vie. Vous piochez 3 cartes', 8, 0, 0, 2, NULL, 'static/img/card/Imposition_des_mains.png'),
(14, 'Intelligence des Arcanes', 'Vous piochez 2 cartes.', 3, 0, 0, 2, NULL, 'static/img/card/Intelligence_des_arcanes.png'),
(15, 'Massacreur du temple', 'Cri de guerre :  donne +3 PV à un serviteur allié.', 6, 6, 6, 1, 4, 'static/img/card/Massacreur_du_temple.png'),
(16, 'Prêtresse d Élune', 'Cri de guerre : rend 4 points de vie à votre héros.', 6, 5, 4, 1, 4, 'static/img/card/Pretresse_d_Elune.png'),
(17, 'Sanglier Brocheroc', 'Charge', 1, 1, 1, 1, 6, 'static/img/card/Sanglier_brocheroc.png'),
(18, 'Seigneur de l arène', 'Provocation', 6, 6, 5, 1, 2, 'static/img/card/Seigneur_de_l_arene.png'),
(19, 'Sylvanas Coursevent', 'Râle d agonie : prend le contrôle d un serviteur adverse aléatoire', 6, 5, 5, 1, 5, 'static/img/card/Waifu.png'),
(20, 'Yéti noroît', 'Ne fait rien', 4, 4, 5, 1, NULL, 'static/img/card/Yeti_noroit.png'),
(21, 'Abomination', '', 4, 6, 0, 2, NULL, 'static/img/card/Boule_de_feu.png'),
(22, 'Acclimatation', '', 3, 2, 3, 1, 3, 'static/img/card/Acclimatation.png'),
(23, 'Acolyte de la souffrance', '', 0, 1, 1, 1, NULL, 'static/img/card/Acolyte_de_la_souffrance.png'),
(24, 'Amasseur de butin', '', 5, 3, 6, 1, 2, 'static/img/card/Amasseur_de_butin.png'),
(25, 'Archère Elfe', '', 5, 5, 5, 1, 1, 'static/img/card/Archere_elfe.png'),
(26, 'Assassin de Ravenholdt', '', 4, 2, 0, 2, NULL, 'static/img/card/Assassin_de_ravenholdt.png'),
(27, 'Assassiner', '', 2, 2, 3, 1, NULL, 'static/img/card/Assassiner.png'),
(28, 'Bénédiction des rois', '', 1, 3, 2, 1, 4, 'static/img/card/Benediction_des_rois.png'),
(29, 'Cercle de soin', '', 4, 2, 3, 1, 4, 'static/img/card/Cercle_de_soin.png'),
(30, 'Champion de la main d argent', '', 1, 3, 0, 2, NULL, 'static/img/card/Champion_main_argent.png'),
(31, 'Chasseur de gros gibier', '', 2, 0, 0, 2, NULL, 'static/img/card/Chasseur_gros_gibier.png'),
(32, 'Chasseuse de Tranchebauge', '', 4, 1, 7, 1, 2, 'static/img/card/Chasseuse_de_Tranchebauge.png'),
(33, 'Chef de guerre loup de givre', '', 8, 0, 0, 2, NULL, 'static/img/card/Chef_guerre_loup_givre.png'),
(34, 'Le Chevalier noir', '', 3, 0, 0, 2, NULL, 'static/img/card/Chevalier_noir.png'),
(35, 'Chevaucheur de loup', '', 6, 6, 6, 1, 4, 'static/img/card/Chevaucheur_de_loup.png'),
(36, 'Chien du magma', '', 6, 5, 4, 1, 4, 'static/img/card/Chien_du_magma.png'),
(37, 'Clerc du Soleil brisé', '', 1, 1, 1, 1, 6, 'static/img/card/Clerc_du_Soleil_brise.png'),
(38, 'Commandant d Argent', '', 6, 6, 5, 1, 2, 'static/img/card/Commandant_argent.png'),
(39, 'Consécration', '', 6, 5, 5, 1, 5, 'static/img/card/Consecration.png'),
(40, 'Contrôle mental', '', 4, 4, 5, 1, NULL, 'static/img/card/Controle_mental.png'),
(41, 'Croisée écarlate', '', 4, 6, 0, 2, NULL, 'static/img/card/Croisee_ecarlate.png'),
(42, 'Diablotin de sang', '', 3, 2, 3, 1, 3, 'static/img/card/Diablotin_de_sang.png'),
(43, 'Dissimuler', '', 0, 1, 1, 1, NULL, 'static/img/card/Dissimuler.png'),
(44, 'Docteur vaudou', '', 5, 3, 6, 1, 2, 'static/img/card/Docteur_vaudou.png'),
(45, 'Drake azur', '', 5, 5, 5, 1, 1, 'static/img/card/Drake_azur.png'),
(46, 'Drake du crépuscule', '', 4, 2, 0, 2, NULL, 'static/img/card/Drake_du_crepuscule.png'),
(47, 'Écuyère d Argent', '', 2, 2, 3, 1, NULL, 'static/img/card/Ecuyere_d_Argent.png'),
(48, 'Égalité', '', 1, 3, 2, 1, 4, 'static/img/card/Egalite.png'),
(49, 'Élémentaire de feu', 'Cri de guerre : ', 4, 2, 3, 1, 4, 'static/img/card/Elementaire_de_feu.png'),
(50, 'Explosion pyrotechnique', 'Inflige 10 points de dégâts.', 10, 10, 0, 2, NULL, 'static/img/card/Explosion_pyrotechnique.png'),
(51, 'Feu intérieur', '', 2, 0, 0, 2, NULL, 'static/img/card/Feu_interieur.png'),
(52, 'Flammes infernales', '', 4, 1, 7, 1, 2, 'static/img/card/Flammes_infernales.png'),
(53, 'Flammes sacrées', '', 8, 0, 0, 2, NULL, 'static/img/card/Flammes_sacrees.png'),
(54, 'Force de la nature', '', 3, 0, 0, 2, NULL, 'static/img/card/Force_de_la_nature.png'),
(55, 'Garde de la Lune d argent', '', 6, 6, 6, 1, 4, 'static/img/card/Garde_de_Lune_argent.png'),
(56, 'Garde-paix de l Aldor', '', 6, 5, 4, 1, 4, 'static/img/card/Garde_paix_de_Aldor.png'),
(57, 'Gardien des rois', '', 1, 1, 1, 1, 6, 'static/img/card/Gardien_des_rois.png'),
(58, 'Gnôme lépreux', '', 6, 6, 5, 1, 2, 'static/img/card/Gnome_lepreux.png'),
(59, 'Golem de guerre', '', 6, 5, 5, 1, 5, 'static/img/card/Golem_de_guerre.png'),
(60, 'Grande crinière des savanes', '', 4, 4, 5, 1, NULL, 'static/img/card/Grande_criniere_des_savanes.png'),
(61, 'Heurtoir', '', 4, 6, 0, 2, NULL, 'static/img/card/Heurtoir.png'),
(62, 'Image miroir', '', 3, 2, 3, 1, 3, 'static/img/card/Image_miroir.png'),
(63, 'Infernal de l effroi', '', 0, 1, 1, 1, NULL, 'static/img/card/Infernal_de_effroi.png'),
(64, 'Infiltrateur worgen', '', 5, 3, 6, 1, 2, 'static/img/card/Infiltrateur_worgen.png'),
(65, 'Ingénieur novice', '', 5, 5, 5, 1, 1, 'static/img/card/Ingenieur_novice.png'),
(66, 'La bête', '', 4, 2, 0, 2, NULL, 'static/img/card/La_bete.png'),
(67, 'Lâcher les chiens', '', 2, 2, 3, 1, NULL, 'static/img/card/Lacher_les_chiens.png'),
(68, 'Lamenuit', '', 1, 3, 2, 1, 4, 'static/img/card/Lamenuit.png'),
(69, 'Leeroy Jenkins', '', 4, 2, 3, 1, 4, 'static/img/card/Leeroy_jenkins.png'),
(70, 'Loup alpha redoutable', '', 1, 3, 0, 2, NULL, 'static/img/card/Loup_alpha_redoutable.png'),
(71, 'Maître-bouclier de Sen jin', '', 2, 0, 0, 2, NULL, 'static/img/card/Maitre_bouclier_senjin.png'),
(72, 'Maître-lame blessé', '', 4, 1, 7, 1, 2, 'static/img/card/Maitre_lame_blesse.png'),
(73, 'Marche-soleil', '', 8, 0, 0, 2, NULL, 'static/img/card/Marche_soleil.png'),
(74, 'Mécano de petit dragon', '', 3, 0, 0, 2, NULL, 'static/img/card/Mecano_petit_dragon.png'),
(75, 'Métamorphose', '', 6, 6, 6, 1, 4, 'static/img/card/Metamorphose.png'),
(76, 'Missiliaire téméraire', '', 6, 5, 4, 1, 4, 'static/img/card/Missiliaire_temeraire.png'),
(77, 'Mot de l ombre : Mort', '', 1, 1, 1, 1, 6, 'static/img/card/Mort_ombre_mort.png'),
(78, 'Mot de pouvoir : Bouclier', '', 6, 6, 5, 1, 2, 'static/img/card/Mot_pouvoir_bouclier.png'),
(79, 'Nain sombrefer', '', 6, 5, 5, 1, 5, 'static/img/card/Nain_sombrefer.png'),
(80, 'Néant distordu', '', 4, 4, 5, 1, NULL, 'static/img/card/Neant_distordu.png'),
(81, 'Ogre rochepoing', '', 4, 6, 0, 2, NULL, 'static/img/card/Ogre_rochepoing.png'),
(82, 'Onyxia', '', 3, 2, 3, 1, 3, 'static/img/card/Onyxia.png'),
(83, 'Oracle froide-lumière', '', 0, 1, 1, 1, NULL, 'static/img/card/Oracle_froide_lumiere.png'),
(84, 'Panthère de la jungle', '', 5, 3, 6, 1, 2, 'static/img/card/Panthere_de_la_jungle.png'),
(85, 'Prêtresse de la Cabale', '', 5, 5, 5, 1, 1, 'static/img/card/Pretresse_de_la_Cabale.png'),
(86, 'Prophête du cercle terrestre', '', 4, 2, 0, 2, NULL, 'static/img/card/Prophete_du_cercle_terrestre.png'),
(87, 'Protecteur de l Aube', '', 2, 2, 3, 1, NULL, 'static/img/card/Protecteur_de_l_Aube.png'),
(88, 'Protecteur Écorcefer', '', 1, 3, 2, 1, 4, 'static/img/card/Protecteur_ecorcefer.png'),
(89, 'Protectrice solfurie', '', 4, 2, 3, 1, 4, 'static/img/card/Protectrice_solfurie.png'),
(90, 'Puissance accablante', '', 1, 3, 0, 2, NULL, 'static/img/card/Puissance_accablante.png'),
(91, 'Rage intérieure', '', 2, 0, 0, 2, NULL, 'static/img/card/Rage_interieure.png'),
(92, 'Roi Krush', '', 4, 1, 7, 1, 2, 'static/img/card/Roi_krush.png'),
(93, 'Sergent grossier', '', 8, 0, 0, 2, NULL, 'static/img/card/Sergent_grossier.png'),
(94, 'Siphonner l âme', '', 3, 0, 0, 2, NULL, 'static/img/card/Siphonner_ame.png'),
(95, 'Soldat d élite kor kron', '', 6, 6, 6, 1, 4, 'static/img/card/Soldat_elite_korkron.png'),
(96, 'Sous-chef cruel', 'Cri de guerre : ', 6, 5, 4, 1, 4, 'static/img/card/Sous_chef_cruel.png'),
(97, 'Sprint', '', 1, 1, 1, 1, 6, 'static/img/card/Sprint.png'),
(98, 'Tir meurtrier', '', 6, 6, 5, 1, 2, 'static/img/card/Tir_meurtrier.png'),
(99, 'Toucher guérisseur', '', 6, 5, 5, 1, 5, 'static/img/card/Toucher_guerisseur.png'),
(100, 'Voile de mort', '', 4, 4, 5, 1, NULL, 'static/img/card/Voile_de_mort.png'),

INSERT INTO `deck_cardtype` (`
id`,
`name
`) VALUES
(1, 'Minion'),
(2, 'Spell');

INSERT INTO `deck_deck` (`
id`,
`name
`) VALUES
(1, 'fist'),
(2, 'second');

INSERT INTO `deck_deck_cards` (`
id`,
`deck_id
`, `card_id`) VALUES
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

INSERT INTO `deck_effect` (`
id`,
`name
`) VALUES
(1, 'Camouflage'),
(2, 'Provocation'),
(3, 'Toxicité'),
(4, 'Cri de guerre'),
(5, "Râle d'agonie"),
(6, "Charge")

INSERT INTO `deck_player` (`
id`,
`user_id
`) VALUES
(1, 1),
(2, 2);

INSERT INTO `deck_player_cardcollection` (`
id`,
`player_id
`, `card_id`) VALUES
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