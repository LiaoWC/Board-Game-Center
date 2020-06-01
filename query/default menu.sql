//default menu

select *
from info
where rating<=10
order by rating desc, rating_player desc
limit 20;

// 20200531-0254

select name, max_player, min_player, max_playtime, min_playtime
from info
where rating<=10
order by rating desc, rating_player desc
limit 5;
