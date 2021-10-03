alter table player_bios
	add column height_inches integer;
	
update player_bios
	set height_inches = 12*split_part(height,'-',1)::integer + split_part(height,'-',2)::integer
	from new_table;
	
alter table player_bios
	drop column height;
	
alter table player_bios
	rename column height_inches to height;
	

select firstname, lastname, height from player_bios order by id limit 5;