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

//others


