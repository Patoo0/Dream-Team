-- phpMyAdmin SQL Dump
-- version 4.2.7.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Feb 09, 2023 alle 12:31
-- Versione del server: 5.6.20
-- PHP Version: 5.5.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `gestionale`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `accompagnatori`
--

CREATE TABLE IF NOT EXISTS `accompagnatori` (
  `codAttività` varchar(20) NOT NULL,
  `CodFiscale` varchar(30) NOT NULL,
  `Nome` text NOT NULL,
  `Cognome` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struttura della tabella `alunno`
--

CREATE TABLE IF NOT EXISTS `alunno` (
  `cognome` text NOT NULL,
  `Nome` text NOT NULL,
  `CodFiscale` varchar(30) NOT NULL,
  `classe` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struttura della tabella `attivita`
--

CREATE TABLE IF NOT EXISTS `attivita` (
  `codAttività` varchar(20) NOT NULL,
  `Data` date NOT NULL,
  `Approvata` text NOT NULL,
  `NomeAttivita` text NOT NULL,
  `CodFiscalePartecipanti` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
