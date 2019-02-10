CREATE TABLE `accounts` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `age` int(3) NOT NULL,
  `city` varchar(255) NOT NULL,
  `hash` varchar(45) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`, `name`),
  UNIQUE `hash` (`hash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
