//range

//15 specific category(can change variable)
minplayer=2 maxplayer=5 
min_playtime=30 max_playtime=60
board_category="Card Game"

select *
from info
where (max_player<=5 & max_player>=2)|(min_player<=5 & min_player>=2)|(max_player>=5 & min_player<=2)
and (max_playtime<=60 & max_playtime>=30)|(min_playtime<=60 & min_playtime>=30)|(max_playtime>=60 & min_playtime<=30)
and board_category like "%Card Game%";

//others(14918 rows)
select *
from info
where (max_player<=5 & max_player>=2)|(min_player<=5 & min_player>=2)|(max_player>=5 & min_player<=2)
and (max_playtime<=60 & max_playtime>=30)|(min_playtime<=60 & min_playtime>=30)|(max_playtime>=60 & min_playtime<=30)
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
and board_category not like '%Print & Play%';

//all
select *
from info
where (max_player<=5 & max_player>=2)|(min_player<=5 & min_player>=2)|(max_player>=5 & min_player<=2)
and (max_playtime<=60 & max_playtime>=30)|(min_playtime<=60 & min_playtime>=30)|(max_playtime>=60 & min_playtime<=30);


// 20200531
上面的加上這一行
order by rating desc, rating_player desc
