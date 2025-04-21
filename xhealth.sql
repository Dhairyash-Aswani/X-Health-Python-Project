-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 21, 2025 at 07:30 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `xhealth`
--

-- --------------------------------------------------------

--
-- Table structure for table `health_library`
--

CREATE TABLE `health_library` (
  `id` int(11) NOT NULL,
  `username` varchar(30) DEFAULT NULL,
  `medical_history` varchar(30) NOT NULL,
  `current_diseases` varchar(30) NOT NULL,
  `surgeries_done` varchar(30) NOT NULL,
  `medications` varchar(30) NOT NULL,
  `allergies` varchar(30) NOT NULL,
  `family_medical_history` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `health_library`
--

INSERT INTO `health_library` (`id`, `username`, `medical_history`, `current_diseases`, `surgeries_done`, `medications`, `allergies`, `family_medical_history`) VALUES
(1, 'sian', 'common flu', 'viral fever', 'zero', 'homeopathy', 'none', 'none');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `name` varchar(30) NOT NULL,
  `age` int(11) NOT NULL,
  `gender` varchar(11) NOT NULL,
  `address` varchar(100) NOT NULL,
  `email` varchar(30) NOT NULL,
  `mobile` int(10) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`name`, `age`, `gender`, `address`, `email`, `mobile`, `username`, `password`) VALUES
('BIHARI', 69, 'TRANS', 'BIHAR ', 'yash1509@gmail.com', 1234567890, 'bihari_chor', '12345678'),
('Dhairyash Aswani', 18, 'Male', '17th Road, Ram krishna Mission Marg, Santacruz(West), Mumbai, India', 'aswanidhairyash@gmail.com', 1234567890, 'dhairyash_aswani', 'pass@123'),
('sian', 16, 'male', 'sion east', 'sian.mehta@gmail.com', 2147483647, 'sian', 'abcdefg123'),
('Test one', 18, 'Male', 'irla, ram ganesh gadkari marg, Ville Parle(West), Mumbai, India', 'test1@gmail.com', 1234567891, 'test1', 'test@123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `health_library`
--
ALTER TABLE `health_library`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_username` (`username`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `health_library`
--
ALTER TABLE `health_library`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `health_library`
--
ALTER TABLE `health_library`
  ADD CONSTRAINT `fk_username` FOREIGN KEY (`username`) REFERENCES `login` (`username`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
