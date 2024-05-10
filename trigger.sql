

CREATE TABLE employees_audit (
    EA_id INT AUTO_INCREMENT PRIMARY KEY,
    lastname VARCHAR(50) NOT NULL,
    changedat DATETIME DEFAULT NULL,
    action VARCHAR(50) DEFAULT NULL
);
CREATE TRIGGER before_employee_update 
    BEFORE UPDATE ON employee
    FOR EACH ROW 
 INSERT INTO employees_audit
 SET action = 'update',
     EA_id = OLD.E_id,
     lastname = OLD.E_lastname,
     changedat = NOW();
     
SHOW TRIGGERS;
select * from employee;
UPDATE employee 
SET 
    E_lastname = 'Phan'
WHERE
    E_id = 90622;
    
SELECT * FROM employees_audit;

SET SQL_SAFE_UPDATES = 0;

