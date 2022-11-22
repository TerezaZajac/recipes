
select * from ingredient;
select * from recipe;
select * from recipe_ingredient;
select * from unit;

select * from recipe r left join recipe_ingredient ri on r.id = ri.recipe_id left join ingredient i on i.id = ri.ingredient_id left join unit u on u.id = i.unit_id;

select concat(r.name, ' ', i.name, ' ', ri.amount, ' ', u.name) from recipe r left join recipe_ingredient ri on r.id = ri.recipe_id left join ingredient i on i.id = ri.ingredient_id left join unit u on u.id = i.unit_id;



insert into recipe_ingredient values(4, 1, 4, 0.5)



