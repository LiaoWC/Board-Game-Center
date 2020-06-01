//range

minplayer=2 maxplayer=5 
min_playtime=30 max_playtime=60
board_category="Card Game"

//15 specific category(can change variable)
select info.name, info.board_category, info.min_player, info.max_player,
info.min_playtime, info.max_playtime, case when user_rating.rating is NULL then info.rating 
else ((info.rating*info.rating_player)+(user_rating.rating*user_rating.rating_players))/(info.rating_player+user_rating.rating_players)end as "rating",
case when user_rating.rating is NULL then info.rating_player else info.rating_player+user_rating.rating_players end as "#rating"
from info left join user_rating on info.id=user_rating.id
where (max_player<=5 & max_player>=2)|(min_player<=5 & min_player>=2)|(max_player>=5 & min_player<=2)
and (max_playtime<=60 & max_playtime>=30)|(min_playtime<=60 & min_playtime>=30)|(max_playtime>=60 & min_playtime<=30)
and board_category like "%Card Game%"
and info.rating<=10
order by case when user_rating.rating is NULL then info.rating 
else ((info.rating*info.rating_player)+(user_rating.rating*user_rating.rating_players))/(info.rating_player+user_rating.rating_players)end desc,
case when user_rating.rating is NULL then info.rating_player
else info.rating_player+user_rating.rating_players end desc
limit 15; 

//others
select info.name, info.board_category, info.min_player, info.max_player,
info.min_playtime, info.max_playtime, case when user_rating.rating is NULL then info.rating 
else ((info.rating*info.rating_player)+(user_rating.rating*user_rating.rating_players))/(info.rating_player+user_rating.rating_players)end as "rating",
case when user_rating.rating is NULL then info.rating_player else info.rating_player+user_rating.rating_players end as "#rating"
from info left join user_rating on info.id=user_rating.id
where (max_player<=5 & max_player>=2)|(min_player<=5 & min_player>=2)|(max_player>=5 & min_player<=2)
and (max_playtime<=60 & max_playtime>=30)|(min_playtime<=60 & min_playtime>=30)|(max_playtime>=60 & min_playtime<=30)
and info.rating<=10
and board_category not like "%Card Game%"
and board_category not like '%Wargame%'
and board_category not like "%Children's Game%"
and board_category not like '%Dice%'
and board_category not like '%Fantasy%'
and board_category not like '%Abstract Strategy%'
and board_category not like '%Miniatures%'
and board_category not like '%Educational%'
and board_category not like '%Party Game%'
and board_category not like '%Science Fiction%'
and board_category not like '%Fighting%'
and board_category not like '%Trivia%'
and board_category not like '%Economic%'
and board_category not like '%Movies / TV / Radio theme%'
and board_category not like '%Print & Play%'
order by case when user_rating.rating is NULL then info.rating 
else ((info.rating*info.rating_player)+(user_rating.rating*user_rating.rating_players))/(info.rating_player+user_rating.rating_players)end desc,
case when user_rating.rating is NULL then info.rating_player
else info.rating_player+user_rating.rating_players end desc
limit 15; 

//all
select info.name, info.board_category, info.min_player, info.max_player,
info.min_playtime, info.max_playtime, case when user_rating.rating is NULL then info.rating 
else ((info.rating*info.rating_player)+(user_rating.rating*user_rating.rating_players))/(info.rating_player+user_rating.rating_players)end as "rating",
case when user_rating.rating is NULL then info.rating_player else info.rating_player+user_rating.rating_players end as "#rating"
from info left join user_rating on info.id=user_rating.id
where (max_player<=5 & max_player>=2)|(min_player<=5 & min_player>=2)|(max_player>=5 & min_player<=2)
and (max_playtime<=60 & max_playtime>=30)|(min_playtime<=60 & min_playtime>=30)|(max_playtime>=60 & min_playtime<=30)
and info.rating<=10
order by case when user_rating.rating is NULL then info.rating 
else ((info.rating*info.rating_player)+(user_rating.rating*user_rating.rating_players))/(info.rating_player+user_rating.rating_players)end desc,
case when user_rating.rating is NULL then info.rating_player
else info.rating_player+user_rating.rating_players end desc
limit 15;