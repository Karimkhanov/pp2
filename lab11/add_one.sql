CREATE OR REPLACE PROCEDURE add_one(contact_name VARCHAR(20), contact_number VARCHAR(20))
	AS $$
	DECLARE
		is_exist BOOLEAN;
	BEGIN
		SELECT EXISTS(SELECT PhoneBook.number FROM PhoneBook WHERE contact_name = PhoneBook.name) INTO is_exist;
		
		IF is_exist THEN 
			UPDATE PhoneBook SET number = contact_number WHERE PhoneBook.name = contact_name;
		ELSE
			INSERT INTO PhoneBook (name, number) VALUES (contact_name, contact_number);
		END IF;
		
	END; $$
	LANGUAGE 'plpgsql'
