DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `spApp_AddAccount`(IN `pname` TEXT CHARSET utf8,
IN `page` INT, IN `pcity` TEXT CHARSET utf8)
BEGIN

insert into tstech.accounts (name, age, city, hash) values(pname, page, pcity, md5(name))
	on duplicate key update age=`page`, city=`pcity`;

END$$
DELIMITER ;