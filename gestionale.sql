-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Creato il: Feb 23, 2023 alle 12:32
-- Versione del server: 10.1.13-MariaDB
-- Versione PHP: 5.6.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gestionale`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `accompagnatori`
--

CREATE TABLE `accompagnatori` (
  `Cognome` text NOT NULL,
  `Nome` text NOT NULL,
  `CFaccompagnatori` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struttura della tabella `accompagnatoripartecipanti`
--

CREATE TABLE `accompagnatoripartecipanti` (
  `CFaccompagnatori` varchar(30) NOT NULL,
  `codAttività` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struttura della tabella `alunnipartecipanti`
--

CREATE TABLE `alunnipartecipanti` (
  `CFalunni` varchar(40) NOT NULL,
  `codAttività` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struttura della tabella `alunno`
--

CREATE TABLE `alunno` (
  `CFalunni` varchar(40) NOT NULL,
  `Nome` text NOT NULL,
  `Cognome` text NOT NULL,
  `Classe` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struttura della tabella `attività`
--

CREATE TABLE `attività` (
  `Nome` text NOT NULL,
  `codAttività` varchar(40) NOT NULL,
  `Approvata` text NOT NULL,
  `DataInzio` date NOT NULL,
  `Indirizzo` varchar(30) NOT NULL,
  `DataFine` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
