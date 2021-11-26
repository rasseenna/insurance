-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 26, 2021 at 11:35 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `insurance_package`
--

-- --------------------------------------------------------

--
-- Table structure for table `comment`
--

CREATE TABLE `comment` (
  `id` int(11) NOT NULL,
  `name` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `comment`
--

INSERT INTO `comment` (`id`, `name`) VALUES
(7, 'Motor Insurance Comment'),
(9, 'Home Insurance Comment');

-- --------------------------------------------------------

--
-- Table structure for table `home`
--

CREATE TABLE `home` (
  `home_id` int(11) NOT NULL,
  `username` varchar(55) NOT NULL,
  `policy_name` varchar(55) NOT NULL,
  `address` varchar(255) NOT NULL,
  `built_date` varchar(55) NOT NULL,
  `home_type` varchar(55) NOT NULL,
  `home_age` varchar(55) NOT NULL,
  `membership_type` varchar(55) NOT NULL,
  `premium_selected` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `home`
--

INSERT INTO `home` (`home_id`, `username`, `policy_name`, `address`, `built_date`, `home_type`, `home_age`, `membership_type`, `premium_selected`) VALUES
(19, 'John', 'Fire Insurance', 'Tc 45/477, kerala, India', '22-06-1995', 'Single Floor', '30', 'Family', 'Gold'),
(21, 'David', 'Theft Insurance', 'Test Address', '2021-11-05', 'Double Floor', '10', 'Individual', 'Bronze'),
(23, 'Raseena', 'Earthquake Insurance', 'Test Address', '2021-11-28', 'Double Floor', '32', 'Family', 'Silver');

-- --------------------------------------------------------

--
-- Table structure for table `member`
--

CREATE TABLE `member` (
  `member_id` int(11) NOT NULL,
  `username` varchar(55) NOT NULL,
  `email` varchar(55) NOT NULL,
  `password` varchar(55) NOT NULL,
  `phone` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `member`
--

INSERT INTO `member` (`member_id`, `username`, `email`, `password`, `phone`) VALUES
(15, 'John', 'john@gmail.com', '12345', '9447492847'),
(16, 'David', 'david@gmail.com', '12345', '7894561023'),
(18, 'Raseena', 'rasina786@gmail.com', '12345', '8907585456');

-- --------------------------------------------------------

--
-- Table structure for table `motor`
--

CREATE TABLE `motor` (
  `motor_id` int(11) NOT NULL,
  `username` varchar(55) NOT NULL,
  `policy_name` varchar(55) NOT NULL,
  `manufacturer` varchar(55) NOT NULL,
  `model` varchar(55) NOT NULL,
  `colour` varchar(55) NOT NULL,
  `registration_year` varchar(55) NOT NULL,
  `registration_number` varchar(55) NOT NULL,
  `premium_selected` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `motor`
--

INSERT INTO `motor` (`motor_id`, `username`, `policy_name`, `manufacturer`, `model`, `colour`, `registration_year`, `registration_number`, `premium_selected`) VALUES
(12, 'Raseena', 'Two Wheeler (Comprehensive)', 'Hyundai', 'Swift', 'Red', '2010', 'KL012DE33', 'Silver');

-- --------------------------------------------------------

--
-- Table structure for table `policy`
--

CREATE TABLE `policy` (
  `policy_id` int(11) NOT NULL,
  `policy_type` varchar(55) NOT NULL,
  `policy_name` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `policy`
--

INSERT INTO `policy` (`policy_id`, `policy_type`, `policy_name`) VALUES
(6, 'Motor', 'Private Cars (Comprehensive)'),
(7, 'Motor', 'Two Wheeler (Comprehensive)'),
(8, 'Motor', 'Commercial Vehicles (Comprehensive)'),
(9, 'Motor', 'Private Cars (Third party)'),
(10, 'Motor', 'Two Wheelers (Third Party)'),
(11, 'Motor', 'Commercial Vehicles (Third Party)'),
(12, 'Motor', 'Private Cars (Fire)'),
(13, 'Motor', 'Two Wheelers (Fire)'),
(14, 'Motor', 'Commercial Vehicles (Fire)'),
(15, 'Motor', 'Private Cars (Theft)'),
(16, 'Motor', 'Two Wheelers (Theft)'),
(17, 'Motor', 'Commercial Vehicles (Theft)'),
(18, 'Home', 'Theft Insurance'),
(19, 'Home', 'Fire Insurance'),
(20, 'Home', 'Flood Insurance'),
(21, 'Home', 'Earthquake Insurance'),
(22, 'Home', 'Storm Insurance'),
(23, 'Home', 'Fallen Tree Insurance'),
(24, 'Home', 'Residence Insurance');

-- --------------------------------------------------------

--
-- Table structure for table `premium`
--

CREATE TABLE `premium` (
  `premium_id` int(11) NOT NULL,
  `name` varchar(55) NOT NULL,
  `price` varchar(55) NOT NULL,
  `discount` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `premium`
--

INSERT INTO `premium` (`premium_id`, `name`, `price`, `discount`) VALUES
(3, 'Gold', '750', '7'),
(4, 'Silver', '600', '5'),
(5, 'Bronze', '450', '1');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `auth_key` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `password_hash` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `password_reset_token` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `status` smallint(6) NOT NULL DEFAULT 10,
  `created_at` int(11) NOT NULL,
  `updated_at` int(11) NOT NULL,
  `verification_token` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `auth_key`, `password_hash`, `password_reset_token`, `email`, `status`, `created_at`, `updated_at`, `verification_token`) VALUES
(1, 'Smart_Insurance_Admin', 'rT3M6VH0Pdc99mp_2h7q15ClmTZTNB4P', '$2y$13$eVMLi5gPYs2CjGO96SvEGu./0m0cQ4lmRBOHA6SIwU7LqNQ/cOYa6', NULL, 'admin-insurance@yopmail.com', 10, 1636010311, 1636010311, 'lk5cw67yTg4MHSud4N8POYp-GJXswelg_1636010311');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comment`
--
ALTER TABLE `comment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `home`
--
ALTER TABLE `home`
  ADD PRIMARY KEY (`home_id`);

--
-- Indexes for table `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`member_id`);

--
-- Indexes for table `motor`
--
ALTER TABLE `motor`
  ADD PRIMARY KEY (`motor_id`);

--
-- Indexes for table `policy`
--
ALTER TABLE `policy`
  ADD PRIMARY KEY (`policy_id`);

--
-- Indexes for table `premium`
--
ALTER TABLE `premium`
  ADD PRIMARY KEY (`premium_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `password_reset_token` (`password_reset_token`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `comment`
--
ALTER TABLE `comment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `home`
--
ALTER TABLE `home`
  MODIFY `home_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `member`
--
ALTER TABLE `member`
  MODIFY `member_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `motor`
--
ALTER TABLE `motor`
  MODIFY `motor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `policy`
--
ALTER TABLE `policy`
  MODIFY `policy_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `premium`
--
ALTER TABLE `premium`
  MODIFY `premium_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
