select *from orders6;

start transaction;
	update orders6
    set status = "completed"
    where status = "pending";
    rollback;
commit;