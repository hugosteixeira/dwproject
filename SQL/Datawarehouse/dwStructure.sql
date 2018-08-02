-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: dwbase
-- ------------------------------------------------------
-- Server version	5.5.5-10.2.14-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `dimcandidato`
--

DROP TABLE IF EXISTS `dimcandidato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dimcandidato` (
  `key` int(11) NOT NULL AUTO_INCREMENT,
  `IdCandidato` int(11) DEFAULT NULL,
  `Nome` varchar(60) DEFAULT NULL,
  `Partido` varchar(60) DEFAULT NULL,
  `Numero` int(11) DEFAULT NULL,
  `date_from` datetime DEFAULT NULL,
  `date_to` datetime DEFAULT NULL,
  `version` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`key`)
) ENGINE=InnoDB AUTO_INCREMENT=1655 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dimdata`
--

DROP TABLE IF EXISTS `dimdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dimdata` (
  `keyData` int(11) NOT NULL,
  `data_id` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `dia_ehdiautil` int(11) DEFAULT NULL,
  `dia_numeronasemana` int(11) DEFAULT NULL,
  `dia_numeronomes` int(11) DEFAULT NULL,
  `dia_numeronoano` int(11) DEFAULT NULL,
  `semana_id` int(11) DEFAULT NULL,
  `semana_nome` varchar(255) DEFAULT NULL,
  `semana_texto` varchar(255) DEFAULT NULL,
  `semana_numeronoano` int(11) DEFAULT NULL,
  `mes_id` int(11) DEFAULT NULL,
  `mes_nome` varchar(255) DEFAULT NULL,
  `mes_texto` varchar(255) DEFAULT NULL,
  `mes_numeronoano` varchar(255) DEFAULT NULL,
  `trimestre_id` int(11) DEFAULT NULL,
  `trimestre_nome` varchar(255) DEFAULT NULL,
  `trimestre_texto` varchar(255) DEFAULT NULL,
  `trimestre_numeronoano` int(11) DEFAULT NULL,
  `semestre_id` int(11) DEFAULT NULL,
  `semestre_nome` varchar(255) DEFAULT NULL,
  `semestre_texto` varchar(255) DEFAULT NULL,
  `semestre_numeronoano` int(11) DEFAULT NULL,
  `ano_id` int(11) DEFAULT NULL,
  `ano_nome` varchar(255) DEFAULT NULL,
  `ano_texto` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`keyData`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dimhashtag`
--

DROP TABLE IF EXISTS `dimhashtag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dimhashtag` (
  `key` int(11) NOT NULL AUTO_INCREMENT,
  `hashtag` varchar(255) DEFAULT NULL,
  `IdHashtag` int(11) DEFAULT NULL,
  `date_from` datetime DEFAULT NULL,
  `date_to` datetime DEFAULT NULL,
  `version` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`key`)
) ENGINE=InnoDB AUTO_INCREMENT=2787 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dimlocal`
--

DROP TABLE IF EXISTS `dimlocal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dimlocal` (
  `key` int(11) NOT NULL AUTO_INCREMENT,
  `Cidade` varchar(255) DEFAULT NULL,
  `Estado` varchar(255) DEFAULT NULL,
  `Pais` varchar(255) DEFAULT NULL,
  `Lat` varchar(80) DEFAULT NULL,
  `Lng` varchar(80) DEFAULT NULL,
  `IdLocal` int(11) NOT NULL,
  `date_from` datetime DEFAULT NULL,
  `date_to` datetime DEFAULT NULL,
  `version` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`key`)
) ENGINE=InnoDB AUTO_INCREMENT=586 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fatosentimento`
--

DROP TABLE IF EXISTS `fatosentimento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fatosentimento` (
  `dimdata_keyData` int(11) NOT NULL,
  `dimCandidato_key` int(11) NOT NULL,
  `dimHashtag_key` int(11) NOT NULL,
  `dimLocal_key` int(11) NOT NULL,
  `TotalPositivo` int(11) DEFAULT NULL,
  `TotalNegativo` int(11) DEFAULT NULL,
  `TotalNeutro` int(11) DEFAULT NULL,
  `PercentualPositivo` double DEFAULT NULL,
  `PercentualNegativo` double DEFAULT NULL,
  `PercentualNeutro` double DEFAULT NULL,
  `TotalSentimentos` double DEFAULT NULL,
  PRIMARY KEY (`dimdata_keyData`,`dimCandidato_key`,`dimHashtag_key`,`dimLocal_key`),
  KEY `fk_FatoSentimento_dimCandidato1_idx` (`dimCandidato_key`),
  KEY `fk_FatoSentimento_dimUsuario1_idx` (`dimHashtag_key`),
  KEY `fk_FatoSentimento_dimLocal1_idx` (`dimLocal_key`),
  CONSTRAINT `fk_FatoSentimento_dimCandidato1` FOREIGN KEY (`dimCandidato_key`) REFERENCES `dimcandidato` (`key`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_FatoSentimento_dimLocal1` FOREIGN KEY (`dimLocal_key`) REFERENCES `dimlocal` (`key`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_FatoSentimento_dimUsuario1` FOREIGN KEY (`dimHashtag_key`) REFERENCES `dimhashtag` (`key`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_FatoSentimento_dimdata` FOREIGN KEY (`dimdata_keyData`) REFERENCES `dimdata` (`keyData`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-02  4:47:44
