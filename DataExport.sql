-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: database
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
-- Table structure for table `candidato`
--

DROP TABLE IF EXISTS `candidato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `candidato` (
  `idCandidato` int(11) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(45) NOT NULL,
  `Partido` varchar(45) NOT NULL,
  `Numero` int(11) NOT NULL,
  PRIMARY KEY (`idCandidato`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `candidato`
--

LOCK TABLES `candidato` WRITE;
/*!40000 ALTER TABLE `candidato` DISABLE KEYS */;
INSERT INTO `candidato` VALUES (1,'Bolsonaro','PSC',17),(2,'Lula','PT',13);
/*!40000 ALTER TABLE `candidato` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hashtag`
--

DROP TABLE IF EXISTS `hashtag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hashtag` (
  `idHashTag` int(11) NOT NULL AUTO_INCREMENT,
  `Texto` varchar(45) NOT NULL,
  PRIMARY KEY (`idHashTag`),
  UNIQUE KEY `Texto` (`Texto`)
) ENGINE=InnoDB AUTO_INCREMENT=3238 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hashtag`
--

LOCK TABLES `hashtag` WRITE;
/*!40000 ALTER TABLE `hashtag` DISABLE KEYS */;
/*!40000 ALTER TABLE `hashtag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lugar`
--

DROP TABLE IF EXISTS `lugar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lugar` (
  `idLugar` int(11) NOT NULL AUTO_INCREMENT,
  `Cidade` varchar(45) NOT NULL,
  `Estado` varchar(45) NOT NULL,
  `Pais` varchar(45) NOT NULL,
  PRIMARY KEY (`idLugar`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lugar`
--

LOCK TABLES `lugar` WRITE;
/*!40000 ALTER TABLE `lugar` DISABLE KEYS */;
/*!40000 ALTER TABLE `lugar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manager`
--

DROP TABLE IF EXISTS `manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manager` (
  `idMining` int(11) NOT NULL AUTO_INCREMENT,
  `hastag` varchar(45) NOT NULL,
  `idTweet` varchar(45) NOT NULL,
  `idCandidato` varchar(45) NOT NULL,
  `timeStamp` int(11) NOT NULL,
  PRIMARY KEY (`idMining`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manager`
--

LOCK TABLES `manager` WRITE;
/*!40000 ALTER TABLE `manager` DISABLE KEYS */;
/*!40000 ALTER TABLE `manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sentimento`
--

DROP TABLE IF EXISTS `sentimento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sentimento` (
  `idSentimento` int(11) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(45) NOT NULL,
  PRIMARY KEY (`idSentimento`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sentimento`
--

LOCK TABLES `sentimento` WRITE;
/*!40000 ALTER TABLE `sentimento` DISABLE KEYS */;
INSERT INTO `sentimento` VALUES (1,'Negativo'),(2,'Neutro'),(3,'Positivo');
/*!40000 ALTER TABLE `sentimento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tweet`
--

DROP TABLE IF EXISTS `tweet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tweet` (
  `idTweet` int(11) NOT NULL AUTO_INCREMENT,
  `Texto` varchar(400) NOT NULL,
  `Data` varchar(45) NOT NULL,
  `Replys` int(11) DEFAULT NULL,
  `Retweets` int(11) NOT NULL,
  `Likes` int(11) NOT NULL,
  `Usuario_idUsuario` int(11) NOT NULL,
  `Lugar_idLugar` int(11) DEFAULT NULL,
  `idTweetOrigem` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idTweet`),
  KEY `fk_Tweet_Usuario1_idx` (`Usuario_idUsuario`),
  KEY `fk_Tweet_Lugar1_idx` (`Lugar_idLugar`),
  CONSTRAINT `fk_Tweet_Lugar1` FOREIGN KEY (`Lugar_idLugar`) REFERENCES `lugar` (`idLugar`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Tweet_Usuario1` FOREIGN KEY (`Usuario_idUsuario`) REFERENCES `usuario` (`idUsuario`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=1660 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tweet`
--

LOCK TABLES `tweet` WRITE;
/*!40000 ALTER TABLE `tweet` DISABLE KEYS */;
/*!40000 ALTER TABLE `tweet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tweet_has_hashtag`
--

DROP TABLE IF EXISTS `tweet_has_hashtag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tweet_has_hashtag` (
  `tweet_idTweet` int(11) NOT NULL,
  `hashtag_idHashTag` int(11) NOT NULL,
  PRIMARY KEY (`tweet_idTweet`,`hashtag_idHashTag`),
  KEY `fk_tweet_has_hashtag_hashtag1_idx` (`hashtag_idHashTag`),
  KEY `fk_tweet_has_hashtag_tweet1_idx` (`tweet_idTweet`),
  CONSTRAINT `fk_tweet_has_hashtag_hashtag1` FOREIGN KEY (`hashtag_idHashTag`) REFERENCES `hashtag` (`idHashTag`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_tweet_has_hashtag_tweet1` FOREIGN KEY (`tweet_idTweet`) REFERENCES `tweet` (`idTweet`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tweet_has_hashtag`
--

LOCK TABLES `tweet_has_hashtag` WRITE;
/*!40000 ALTER TABLE `tweet_has_hashtag` DISABLE KEYS */;
/*!40000 ALTER TABLE `tweet_has_hashtag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tweetcandidato`
--

DROP TABLE IF EXISTS `tweetcandidato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tweetcandidato` (
  `Tweet_idTweet` int(11) NOT NULL,
  `Candidato_idCandidato` int(11) NOT NULL,
  `Sentimento_idSentimento` int(11) NOT NULL,
  PRIMARY KEY (`Tweet_idTweet`,`Candidato_idCandidato`),
  KEY `fk_TweetCandidato_Candidato1_idx` (`Candidato_idCandidato`),
  KEY `fk_TweetCandidato_Sentimento1_idx` (`Sentimento_idSentimento`),
  CONSTRAINT `fk_TweetCandidato_Candidato1` FOREIGN KEY (`Candidato_idCandidato`) REFERENCES `candidato` (`idCandidato`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_TweetCandidato_Sentimento1` FOREIGN KEY (`Sentimento_idSentimento`) REFERENCES `sentimento` (`idSentimento`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_TweetCandidato_Tweet1` FOREIGN KEY (`Tweet_idTweet`) REFERENCES `tweet` (`idTweet`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tweetcandidato`
--

LOCK TABLES `tweetcandidato` WRITE;
/*!40000 ALTER TABLE `tweetcandidato` DISABLE KEYS */;
/*!40000 ALTER TABLE `tweetcandidato` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuario` (
  `idUsuario` int(11) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(45) NOT NULL,
  `Followers` int(11) NOT NULL,
  `TotalTweets` int(11) NOT NULL,
  `Lugar_idLugar` int(11) DEFAULT NULL,
  PRIMARY KEY (`idUsuario`)
) ENGINE=InnoDB AUTO_INCREMENT=1723 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-26 23:17:52
