-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 16, 2022 at 09:39 PM
-- Server version: 8.0.31-0ubuntu0.22.04.1
-- PHP Version: 8.1.2-1ubuntu2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Archives`
--

-- --------------------------------------------------------

--
-- Table structure for table `Données`
--

CREATE TABLE `Données` (
  `nom` text,
  `prenom` text,
  `age` int DEFAULT NULL,
  `pays` text,
  `commune` text,
  `departement` text,
  `mois` text,
  `metier` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Données`
--

INSERT INTO `Données` (`nom`, `prenom`, `age`, `pays`, `commune`, `departement`, `mois`, `metier`) VALUES
('Leduc', 'Paul-François', 22, 'Loire inférieure', ' Achery', 'Inconnu', 'Agriculteur', 'janvier'),
('Delahaye', 'Thibault', 25, 'Loire inférieure', 'Donchery', 'Inconnu', 'Agriculteur', 'fevrier'),
('Aimé-Gilles', 'Weiss', 32, 'Loire inférieure', 'Glennes', 'Inconnu', 'Ouvrier', 'mars'),
('Honoré-Frédéric', 'Toussaint', 37, 'Loire inférieure', 'Donchery', 'Inconnu', 'Artisan', 'janvier'),
('Patrick', 'Barthelemy', 18, 'Loire inférieure', 'Achery', 'Inconnu', 'Artisan', 'mars'),
('René', 'Le Ruiz', 29, 'Loire inférieure', 'Cerseuil', 'Inconnu', 'Commerçant', 'mai'),
('Théodore', 'Pelletier', 41, 'Loire inférieure', 'Cerseuil', 'Inconnu', 'Ouvrier', 'mai'),
('Xavier', 'Gosselin', 19, 'Afrique du Nord', 'Inconnu', 'Inconnu', 'Commerçant', 'juin'),
('Matthieu', 'Fleury', 23, 'Afrique du Nord', 'Inconnu', 'Inconnu', 'Agriculteur', 'juin'),
('Pierre', 'Navarro', 30, 'Afrique du Nord', 'Inconnu', 'Inconnu', 'Commerçant', 'juin'),
('Roger', 'Masse', 20, 'Afrique du Nord', 'Inconnu', 'Inconnu', 'Ouvrier', 'juillet'),
('Maurice', 'Maillot', 40, 'Afrique du Nord', 'Inconnu', 'Inconnu', 'Artisan', 'aout'),
('Rémy-Thibaut', 'Julien', 24, 'Autres pays', 'Inconnu', 'Inconnu', 'Agriculteur', 'aout'),
('Maurice', 'Munoz', 45, 'Autres pays', 'Inconnu', 'Inconnu', 'Agriculteur', 'octobre'),
('Emmanuel-Julien', 'Garnier', 21, 'Autres pays', 'Inconnu', 'Inconnu', 'Ouvrier', 'janvier'),
('Étienne', 'Masse', 27, 'Autres pays', 'Inconnu', 'Inconnu', 'Ouvrier', 'octobre'),
('Xavier', 'Carre', 31, 'Autres pays', 'Inconnu', 'Inconnu', 'Ouvrier', 'novembre'),
('Adrien', 'Humbert', 28, 'Autres pays', 'Inconnu', 'Inconnu', 'Artisan', 'decembre'),
('Denis', 'Moreau', 18, 'Autres pays', 'Inconnu', 'Inconnu', 'Commerçant', 'decembre'),
('Aimé', 'Goncalves', 26, 'Autres pays', 'Inconnu', 'Inconnu', 'Commerçant', 'decembre');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
