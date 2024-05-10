use bakery_management; 
create table Employee
	(E_id		varchar(20), 
	 E_Firstname varchar(15), 
     E_Lastname varchar(15),
	 E_phoneno	varchar(15),
     E_salary   varchar(8),
     E_age      varchar(3),
     E_Type     varchar(30),
	 primary key (E_id)
	);
      create table login
	(EM_username		varchar(20), 
	 EM_password		varchar(15), 
	 E_id		    varchar(8),
	 primary key (EM_username,E_id)
	);
    create table supplier
	(SUPP_id	varchar(20), 
	 SUPP_firstname    varchar(15), 
     SUPP_lastname     varchar(15),
	 SUPP_phonenumber numeric(15),
	 primary key (SUPP_id)
	);
    SET SQL_SAFE_UPDATES = 0;
UPDATE supplier
SET type_='Supplier';
    ALTER TABLE supplier
	ADD type_ varchar(10);
 create table suplier_login
	(SUPP_username		varchar(20), 
	 SUPP_password		varchar(15), 
	 SUPP_id		    varchar(8),
	 primary key (SUPP_username,SUPP_id)
	);
    create table bakery
	(B_name		   varchar(15), 
     price       varchar(15),
     locationrack varchar(10),
     category          varchar(20),
     B_sellingprice   varchar(15),
	 primary key(B_name)
	);
    create table sales
	(SA_id		   varchar(20),
     SA_date       date,
	 primary key (SA_id)
	);
     create table make
	(E_id             varchar(20),
     SA_id		       varchar(20), 
	 primary key (SA_id),
     foreign key (E_id) references employee (E_id)
		on delete set null
	);
   create table customer
	(C_id		   varchar(20), 
	 C_name		   varchar(15),
     C_phonenumber          varchar(20),
     C_lastname       varchar(25),
	 primary key (C_id)
	);
    create table sold_to
	(SA_id		   varchar(20), 
     C_id          varchar(20),
	 primary key (SA_id),
     foreign key (C_id) references customer (C_id)
		on delete set null
     );
create table delivery
	(D_id		   varchar(20), 
	 D_address	   varchar(50), 
     postal_code   varchar(32),
     delivery_personscore varchar(10),
	 primary key (D_id)
	);
create table customer_request
	(CR_id              varchar(20),
     C_id		     varchar(20), 
	 CR_request	     varchar(15), 
     CR_date          date, 
	 primary key (CR_id)
	);
create table request
	(CR_id             varchar(20),
     C_id		     varchar(20),
     primary key(CR_id)
	);
create table wants_delivery
	(C_id		   varchar(20), 
	 D_id    	   varchar(15), 
	 primary key (D_id),
     foreign key (C_id) references customer (C_id)
		on delete set null
	);
   create table product_request
	(E_id		        varchar(20), 
	 product		varchar(15),
     SUPP_id		   varchar(20), 
	 primary key (E_id),
     foreign key (SUPP_id) references supplier (SUPP_id)
		on delete set null
	);
    
create table sales_items
	(SI_name              varchar(20),
     SA_id		       varchar(20), 
	 SI_quantity	   varchar(15), 
	 primary key (SA_id)
	);

create view employee_details as
    select E_id, E_Firstname, E_phoneno
    from Employee;
    
create view customer_delivery as 
select C_name, C_phonenumber, D_address 
from customer as c
inner join wants_delivery as w
inner join delivery as d
where c.C_id=w.C_id and w.D_id= d.D_id;

create view requests as 
select C_name, CR_request
from customer as c 
inner join customer_request as cr
where c.C_id=cr.C_id;

create view logins as 
select * from login union select * from suplier_login;
select * from logins;

create view details as
select SUPP_id,type_ from supplier union select E_id,  E_type from Employee ;

