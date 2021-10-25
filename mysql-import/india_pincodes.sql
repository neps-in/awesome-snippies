-- phpMyAdmin SQL Dump
-- version 4.3.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Sep 18, 2020 at 11:23 PM
-- Server version: 5.6.22
-- PHP Version: 5.6.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `pfs_py`
--

-- --------------------------------------------------------

--
-- Table structure for table `india_pincodes`
--

CREATE TABLE IF NOT EXISTS `india_pincodes` (
`id` int(11) NOT NULL,
  `office_name` varchar(200) NOT NULL,
  `pincode` varchar(16) NOT NULL,
  `office_type` varchar(100) NOT NULL,
  `delivery_status` varchar(100) NOT NULL,
  `division_name` varchar(255) NOT NULL,
  `region_name` varchar(200) NOT NULL,
  `circle_name` varchar(200) NOT NULL,
  `taluk` varchar(200) NOT NULL,
  `district_name` varchar(200) NOT NULL,
  `state_name` varchar(200) NOT NULL,
  `telephone` varchar(16) NOT NULL,
  `related_suboffice` varchar(200) NOT NULL,
  `related_headoffice` varchar(200) NOT NULL,
  `longitude` varchar(50) NOT NULL,
  `latitude` varchar(50) NOT NULL,
  `date_created` datetime NOT NULL,
  `last_updated` datetime NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=MyISAM AUTO_INCREMENT=154798 DEFAULT CHARSET=latin1 COMMENT='Contains PINCODE of India';

--
-- Indexes for dumped tables
--

--
-- Indexes for table `india_pincodes`
--
ALTER TABLE `india_pincodes`
 ADD PRIMARY KEY (`id`) COMMENT 'Primary key';

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `india_pincodes`
--
ALTER TABLE `india_pincodes`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=154798;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
