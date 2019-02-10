DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `spApp_GetAccount`()
BEGIN 
select name, age, city from tstech.accounts  
	limit 50; 
END$$
DELIMITER ;