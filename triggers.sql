

CREATE OR REPLACE FUNCTION process_person_audit_insert() RETURNS trigger as $$

begin
		
		insert into person_personaudit
			(person_id, type, cpf_new, last_update)
		values(
			new.id, 1, new.cpf, current_timestamp
		);
		return new;
end;
$$ language plpgsql

CREATE OR REPLACE FUNCTION process_person_audit_update() RETURNS trigger as $$

begin
		if(new.cpf != old.cpf) then
			insert into person_personaudit
				(person_id, type, cpf_new, cpf_old,last_update)
			values
				(
					new.id, 1, new.cpf, old.cpf, current_timestamp
				);
			return new;
		end if;
end;
$$ language plpgsql

create trigger per_audit_insert
AFTER INSERT ON person_person
    for each row EXECUTE PROCEDURE process_person_audit_insert();

create trigger per_audit_update
AFTER update ON person_person
    FOR EACH ROW EXECUTE PROCEDURE process_person_audit_update();

	