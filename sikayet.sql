-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1:3306
-- Üretim Zamanı: 27 Ağu 2020, 16:33:34
-- Sunucu sürümü: 10.4.10-MariaDB
-- PHP Sürümü: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `sikayet`
--

DELIMITER $$
--
-- Yordamlar
--
DROP PROCEDURE IF EXISTS `sirketadinagöre`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sirketadinagöre` (IN `sirketadi` VARCHAR(50))  NO SQL
SELECT calisan.mail,sirket.ad FROM calisan,calisan_sirket,sirket WHERE calisan.calisan_id=calisan_sirket.calisan_id AND calisan_sirket.sirket_id=sirket.sirket_id AND sirket.ad=sirketadi$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `calisan`
--

DROP TABLE IF EXISTS `calisan`;
CREATE TABLE IF NOT EXISTS `calisan` (
  `calisan_id` int(50) NOT NULL,
  `ad` varchar(50) COLLATE utf8_turkish_ci NOT NULL,
  `soyad` varchar(50) COLLATE utf8_turkish_ci NOT NULL,
  `mail` varchar(200) COLLATE utf8_turkish_ci NOT NULL,
  PRIMARY KEY (`calisan_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `calisan`
--

INSERT INTO `calisan` (`calisan_id`, `ad`, `soyad`, `mail`) VALUES
(1, 'Selin', 'Yilmaz', 'seliny872@gmail.com'),
(2, 'Pelin', 'Aslan', '17hilalyldz@gmail.com'),
(3, 'Mehmet', 'Mutlu', 'gamzes.kaya@gmail.com');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `calisan_sirket`
--

DROP TABLE IF EXISTS `calisan_sirket`;
CREATE TABLE IF NOT EXISTS `calisan_sirket` (
  `calisan_id` int(50) NOT NULL,
  `sirket_id` int(50) NOT NULL,
  KEY `calisan_id` (`calisan_id`),
  KEY `sirket_id` (`sirket_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `calisan_sirket`
--

INSERT INTO `calisan_sirket` (`calisan_id`, `sirket_id`) VALUES
(1, 1),
(2, 2),
(3, 3);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `sirket`
--

DROP TABLE IF EXISTS `sirket`;
CREATE TABLE IF NOT EXISTS `sirket` (
  `sirket_id` int(50) NOT NULL,
  `ad` varchar(200) COLLATE utf8_turkish_ci NOT NULL,
  PRIMARY KEY (`sirket_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `sirket`
--

INSERT INTO `sirket` (`sirket_id`, `ad`) VALUES
(1, 'Dalin'),
(2, 'Flormar'),
(3, 'Danone');

--
-- Dökümü yapılmış tablolar için kısıtlamalar
--

--
-- Tablo kısıtlamaları `calisan_sirket`
--
ALTER TABLE `calisan_sirket`
  ADD CONSTRAINT `calisan_sirket_ibfk_1` FOREIGN KEY (`calisan_id`) REFERENCES `calisan` (`calisan_id`),
  ADD CONSTRAINT `calisan_sirket_ibfk_2` FOREIGN KEY (`sirket_id`) REFERENCES `sirket` (`sirket_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
