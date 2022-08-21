-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  Dim 21 août 2022 à 00:44
-- Version du serveur :  10.4.10-MariaDB
-- Version de PHP :  7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `gbstore`
--

-- --------------------------------------------------------

--
-- Structure de la table `livres`
--

DROP TABLE IF EXISTS `livres`;
CREATE TABLE IF NOT EXISTS `livres` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nomlivre` varchar(100) NOT NULL,
  `categorie` varchar(100) NOT NULL,
  `auteur` varchar(100) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `prix` int(11) NOT NULL,
  `stock` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `livres`
--

INSERT INTO `livres` (`id`, `nomlivre`, `categorie`, `auteur`, `description`, `prix`, `stock`) VALUES
(1, 'La belle histoire de Leuk-le-Lièvre', 'Conte', 'Abdoulaye Sadji,Léopold Sédar Senghor', 'Composée de plusieurs récits initiatiques et de contes populaires, La belle histoire de Leuk-le-Lièvre révèle l’intention profonde de ses auteurs, tous deux enseignants et militants de la Négritude : nous faire découvrir la puissante originalité des cultures et traditions africaines.', 4000, 100),
(2, 'Un chant écarlate ', 'Roman', 'Mariama Bâ', '\"Un chant écarlate\" est l\'histoire d’amour impossible entre deux étudiants idéalistes, une Française et un Sénégalais, dans le Dakar des années 1980, où l’apprentissage de l’autre, au-delà des frontières, des cultures et des traditions, s’avère difficile.', 3000, 100),
(3, 'Le ventre de l\'Atlantique ', 'Roman', 'Fatou Diome', 'Salie vit en France. Son frère, Madické, rêve de l\'y rejoindre et compte sur elle. Mais comment lui expliquer la face cachée de l\'immigration, lui qui voit la France comme une terre promise où réussissent les footballeurs sénégalais, où vont se réfugier ceux qui, comme Sankèle, fuient leur destin tragique?', 5000, 20),
(4, 'Le ventre de l\'Atlantique ', 'Roman', 'Fatou Diome', 'Salie vit en France. Son frère, Madické, rêve de l\'y rejoindre et compte sur elle. Mais comment lui expliquer la face cachée de l\'immigration, lui qui voit la France comme une terre promise où réussissent les footballeurs sénégalais, où vont se réfugier ceux qui, comme Sankèle, fuient leur destin tragique?', 5000, 20),
(5, 'Celles qui attendent ', 'Roman', 'Fatou Diome', 'Arame et Bougna, mères de Lamine et Issa, clandestins partis pour l’Europe, ne comptaient plus leurs printemps ; chacune était la sentinelle vouée et dévouée à la sauvegarde des siens, le pilier qui tenait la demeure sur les galeries creusées par l’absence. ', 5000, 10),
(6, 'Oeuvre poétique ', 'Poésie', 'Léopold Sédar Senghor', 'Ce volume comprend l\'œuvre poétique intégrale de Léopold Sedar Senghor : successivement Chants d\'ombre, Hosties noires, Ethiopiques, Nocturnes, Lettres d\'hivernage, Elégies majeures, Poèmes perdus (jusqu\'alors inédits), ainsi que les Dialogues sur la poésie francophone et un ensemble de poèmes divers.', 4000, 12),
(7, 'Maïmouna ', 'Roman', 'Abdoulaye Sadji', 'Maïmouna est une enfant de l\'Afrique paysanne, séduite puis finalement meurtrie par la grande ville. Jolie, innocente, rêveuse, Dakar en fera une victime. Elle reviendra panser ses blessures au pays, auprès de sa vieille mère, mieux armée pour consentir aux vertus des gens simples.', 3000, 10),
(8, ' L\'Aventure ambiguë ', 'Roman', 'Cheikh Hamidou Kane', 'De manière significative \"L\'aventure ambiguë\", histoire d\'un itinéraire spirituel, porte en sous-titre \"récit\". Ce qui frappe en effet le lecteur de ce livre, c\'est le classicisme dû autant à la retenue du ton qu\'à la portée universelle de la réflexion philosophique. ', 4000, 10),
(9, ' Impossible de grandir ', 'Roman', 'Fatou Diome', 'Salie est invitée à dîner chez des amis. Une invitation apparemment anodine mais qui la plonge dans la plus grande angoisse. Pourquoi est-ce si « impossible » pour elle d\'aller chez les autres, de répondre aux questions sur sa vie, sur ses parents ?', 4500, 20),
(10, ' Les contes d\'Amadou-Koumba ', 'Conte', 'Birago Diop', '\r\nS\'il avait le ventre derrière lui, ce ventre le mettrait dans un trou. S\'il n\'est que de vous nourrir, une seule femme suffit. Rendre un salut n\'a jamais écorché la bouche. Demandez©vous à l\'aveugle de vous affirmer si le coton est blanc ou si le corbeau est bien noir ?', 3000, 50);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
