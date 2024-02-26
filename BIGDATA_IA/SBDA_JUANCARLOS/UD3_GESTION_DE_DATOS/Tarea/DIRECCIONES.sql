-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: db
-- Tiempo de generación: 10-08-2022 a las 18:29:04
-- Versión del servidor: 8.0.29
-- Versión de PHP: 8.0.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `mibbdd`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `DIRECCIONES`
--

CREATE TABLE `DIRECCIONES` (
  `ID` int NOT NULL,
  `ID_pedido` int DEFAULT NULL,
  `dir_entrega` varchar(50) COLLATE utf8_bin DEFAULT NULL,
  `tipo_entrega` varchar(25) CHARACTER SET utf8mb3 COLLATE utf8_bin DEFAULT NULL,
  `email` varchar(50) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;

--
-- Volcado de datos para la tabla `DIRECCIONES`
--

INSERT INTO `DIRECCIONES` (`ID`, `ID_pedido`, `dir_entrega`, `tipo_entrega`, `email`) VALUES
(7, 56904, 'Gran vía 24 1C, Madrid', 'Correos', 'twana_ellwood@yahoo.com'),
(8, 84698, 'Rúa Rosalía de castro 28 4B, Vigo', 'Domicilio', 'emery_aitken@mail.com'),
(9, 14325, 'Avenida de Europa 2, Vigo', 'Correos', 'thomasina_stone@hotmail.com'),
(10, 68893, 'c/Orense 25 2C, Madrid', 'Domicilio', 'justin_higgins@gmail.com'),
(11, 72994, 'c/agua 25 3D, Sevilla', 'Punto de recogida', 'liliana_wilde@outlook.com'),
(12, 82407, 'c/San Lorenzo 12, Málaga', 'Domicilio', 'bo_finnegan@hotmail.com'),
(13, 74285, 'Avinguda de Manuel Azaña 4, Barcelona', 'Domicilio', 'mayme_driscoll@yandex.com'),
(14, 5364, 'Avenida de Casablanca 45, Madrid', 'Correos', 'jenifer_reid@zohomail.com'),
(15, 80407, 'Calle de Canarias 1 2B, Madrid', 'Punto de recogida', 'julie_macgregor@gmail.com'),
(16, 18447, 'c/Esla 34, León', 'Domicilio', 'yvonne_povey@mail.com'),
(17, 76092, 'Cami Assagador del Morro 12, Valencia', 'Domicilio', 'magdalene_mcrae@yandex.com'),
(18, 60659, 'C/Burriana 12 3C, Oviedo', 'Domicilio', 'minta_hodge@yandex.com'),
(19, 44964, 'c/González del Villar 12, A Coruña', 'Domicilio', 'samara_bright@yandex.com'),
(20, 87871, 'Rúa Lepanto 4 3A, Vigo', 'Domicilio', 'coy_rice@gmail.com'),
(21, 86276, 'Rúa Amado Carballo 10 1A, Ourense', 'Domicilio', 'cleotilde_hargreaves@aol.com'),
(22, 98183, 'Avenida de Cataluña 22, Zaragoza', 'Punto de recogida', 'brendan_weir@yandex.com'),
(23, 71938, 'Avenida de los Pilares 30, Cáceres', 'Correos', 'danelle_sanderson@yahoo.com'),
(24, 96811, 'c/Blanco Coris 23 1C, Málaga', 'Domicilio', NULL),
(25, 12573, 'Bajada antequeruela 5, Toledo', 'Domicilio', 'claretha_mcgill@yandex.com'),
(26, 31349, 'c/Daoíz y Velarde 5 2A, León', 'Punto de recogida', 'len_hartley@yahoo.com'),
(27, 18447, 'c/Esla 34, León', 'Domicilio', 'yvonne_povey@mail.com'),
(28, 23052, 'Rúa Rosalía de castro 28 4B, Vigo', 'Domicilio', 'tona_hobbs@yahoo.com'),
(29, 28324, 'Gran vía 24 1C, Madrid', 'Domicilio', 'tanner_russell@protonmail.com'),
(30, 78031, 'Avenida da Concordia 12, A Coruña', 'Domicilio', 'sid_wilks@protonmail.com'),
(31, 38805, 'c/Nuevas Profesiones 5 5D, Sevilla', 'Domicilio', 'sarai_kendall@gmail.com'),
(32, 55280, 'Avinguda de Manuel Azaña 4, Barcelona', 'Domicilio', 'tenisha_ward@yahoo.com'),
(33, 78844, 'c/González Besada 12 3A, Oviedo', 'Domicilio', 'margit_appleton@aol.com'),
(34, 28966, 'c/San Lorenzo 12, Málaga', 'Domicilio', 'carl_levy@hotmail.com'),
(35, 44903, 'Rúa Petanca 5, Ourense', 'Domicilio', 'alvaro_greig@yandex.com'),
(36, 34175, 'Carrer de Santaló 3 1B, Barcelona', 'Punto de recogida', 'roger_raymond@outlook.com'),
(37, 77345, 'Avenida de Casablanca 45, Madrid', 'Domicilio', 'samantha_haines@zohomail.com'),
(38, 3800, 'Calle de Canarias 1 2B, Madrid', 'Correos', 'dee_phillips@protonmail.com'),
(39, 71084, 'c/del Lirio 3 1A, Ciudad Real', 'Domicilio', 'alfredia_peterson@hotmail.com'),
(40, 22315, 'Avenida de Carlos 2 1A, Toledo', 'Domicilio', 'bao_allan@zohomail.com'),
(41, 33380, 'Calle de Santa Inés 5, Madrid', 'Domicilio', 'eura_mcintyre@zohomail.com'),
(42, 22397, 'Cami Assagador del Morro 12, Valencia', 'Domicilio', 'antone_george@protonmail.com'),
(43, 68207, 'Avenida Ruta de la Plata 5 1A, Cáceres', 'Domicilio', 'grace_cohen@protonmail.com'),
(44, 29986, 'Rúa Rosalía de castro 28 4B, Vigo', 'Domicilio', 'jeanine_barnard@mail.com'),
(45, 17669, 'c/González del Villar 12, A Coruña', 'Domicilio', 'norah_clayton@protonmail.com'),
(46, 58904, 'c/La nave, Zaragoza', 'Correos', 'gayle_khan@mail.com'),
(47, 37331, 'Gran vía 24 1C, Madrid', 'Domicilio', 'peter_arnold@yandex.com'),
(48, 6777, 'Carrer de Manuel de Falla 24, Barcelona', 'Domicilio', 'sunny_mullins@yahoo.com'),
(49, 10018, 'Rúa Lepanto 4 3A, Vigo', 'Domicilio', 'clelia_sanchez@gmail.com'),
(50, 31627, 'Rúa Amado Carballo 10 1A, Ourense', 'Punto de recogida', 'arielle_duffy@aol.com'),
(51, 46547, 'Rúa do Picouto 12 2A, Ourense', 'Punto de recogida', 'viki_charles@gmail.com'),
(52, 95073, 'Avenida de Cataluña 22, Zaragoza', 'Domicilio', 'dinorah_sadler@yahoo.com'),
(53, 40579, 'Avenida de Francia 34, Valencia', 'Punto de recogida', 'archie_o brien@aol.com'),
(54, 28239, 'Avenida de los Pilares 30, Cáceres', 'Domicilio', 'sebastian_curry@hotmail.com'),
(55, 5220, 'c/Blanco Coris 23 1C, Málaga', 'Correos', 'virginia_cooke@yahoo.com'),
(56, 27943, 'Bajada antequeruela 5, Toledo', 'Correos', 'shaquana_miles@mail.com'),
(57, 28497, 'c/Esla 34, León', 'Domicilio', 'evia_redman@yahoo.com'),
(58, 51480, 'Avenida da Concordia 12, A Coruña', 'Domicilio', 'beverley_brookes@aol.com'),
(59, 72208, 'Calle del Lucero 12 6A, Madrid', 'Domicilio', NULL),
(60, 56277, 'C/Burriana 12 3C, Oviedo', 'Punto de recogida', 'noella_drew@protonmail.com'),
(61, 71233, 'c/del Lirio 3 1A, Ciudad Real', 'Punto de recogida', 'adella_steadman@outlook.com'),
(62, 26364, 'Calle de Eugenia de Montijo 3, Madrid', 'Domicilio', 'beth_horner@aol.com'),
(63, 11542, 'c/Padre Barranco 5 1A, Valencia', 'Domicilio', 'jacalyn_mccarthy@protonmail.com'),
(64, 68207, 'Avenida Ruta de la Plata 5 1A, Cáceres', 'Domicilio', 'grace_cohen@protonmail.com'),
(65, 30066, 'Calle Ugalde 10 4C, Bilbao', 'Domicilio', 'cris_watt@hotmail.com'),
(66, 18447, 'c/Esla 34, León', 'Domicilio', 'yvonne_povey@mail.com');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `DIRECCIONES`
--
ALTER TABLE `DIRECCIONES`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `DIRECCIONES`
--
ALTER TABLE `DIRECCIONES`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
