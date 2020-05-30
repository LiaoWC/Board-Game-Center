- 不同種類遊戲的出版數量對上時間的折線圖

//query example for category="Card Game"
select '1951~1955' as year_published, sum(number) as quantity from (select count(*) as number from info where board_category like '%Card Game%' group by year_published having year_published>=1951 and year_published<=1955) as a union
select '1956~1960' as year_published, sum(number) as quantity from (select count(*) as number from info where board_category like '%Card Game%' group by year_published having year_published>=1956 and year_published<=1960) as a union
select '1961~1965' as year_published, sum(number) as quantity from (select count(*) as number from info where board_category like '%Card Game%' group by year_published having year_published>=1961 and year_published<=1965) as a union
select '1966~1970' as year_published, sum(number) as quantity from (select count(*) as number from info where board_category like '%Card Game%' group by year_published having year_published>=1966 and year_published<=1970) as a union
select '1971~1975' as year_published, sum(number) as quantity from (select count(*) as number from info where board_category like '%Card Game%' group by year_published having year_published>=1971 and year_published<=1975) as a union
select '1976~1980' as year_published, sum(number) as quantity from (select count(*) as number from info where board_category like '%Card Game%' group by year_published having year_published>=1976 and year_published<=1980) as a union
select '1981~1985' as year_published, sum(number) as quantity from (select count(*) as number from info where board_category like '%Card Game%' group by year_published having year_published>=1981 and year_published<=1985) as a union
select '1986~1990' as year_published, sum(number) as quantity from (select count(*) as number from info where board_category like '%Card Game%' group by year_published having year_published>=1986 and year_published<=1990) as a union
select '1991~1995' as year_published, sum(number) as quantity from (select count(*) as number from info where board_category like '%Card Game%' group by year_published having year_published>=1991 and year_published<=1995) as a union
select '1996~2000' as year_published, sum(number) as quantity from (select count(*) as number from info where board_category like '%Card Game%' group by year_published having year_published>=1996 and year_published<=2000) as a union
select '2001~2005' as year_published, sum(number) as quantity from (select count(*) as number from info where board_category like '%Card Game%' group by year_published having year_published>=2001 and year_published<=2005) as a union
select '2006~2010' as year_published, sum(number) as quantity from (select count(*) as number from info where board_category like '%Card Game%' group by year_published having year_published>=2006 and year_published<=2010) as a union
select '2011~2015' as year_published, sum(number) as quantity from (select count(*) as number from info where board_category like '%Card Game%' group by year_published having year_published>=2011 and year_published<=2015) as a union
select '2016~2020' as year_published, sum(number) as quantity from (select count(*) as number from info where board_category like '%Card Game%' group by year_published having year_published>=2016 and year_published<=2020) as a;

//Card Game
year_published  quantity  
--------------  ----------
1951~1955       67        
1956~1960       66        
1961~1965       104       
1966~1970       117       
1971~1975       132       
1976~1980       175       
1981~1985       324       
1986~1990       420       
1991~1995       614       
1996~2000       1124      
2001~2005       2320      
2006~2010       3704      
2011~2015       6876      
2016~2020       2604

//Wargame
year_published  quantity  
--------------  ----------
1951~1955       4         
1956~1960       9         
1961~1965       32        
1966~1970       78        
1971~1975       375       
1976~1980       756       
1981~1985       795       
1986~1990       718       
1991~1995       908       
1996~2000       1014      
2001~2005       1635      
2006~2010       2352      
2011~2015       2758      
2016~2020       1000 

//Children's Game
year_published  quantity  
--------------  ----------
1951~1955       106       
1956~1960       182       
1961~1965       182       
1966~1970       207       
1971~1975       246       
1976~1980       322       
1981~1985       408       
1986~1990       569       
1991~1995       650       
1996~2000       865       
2001~2005       1352      
2006~2010       1908      
2011~2015       1913      
2016~2020       396

//Dice
year_published  quantity  
--------------  ----------
1951~1955       52        
1956~1960       65        
1961~1965       58        
1966~1970       85        
1971~1975       166       
1976~1980       174       
1981~1985       232       
1986~1990       343       
1991~1995       389       
1996~2000       501       
2001~2005       757       
2006~2010       1276      
2011~2015       2071      
2016~2020       802

//Fantasy
year_published  quantity  
--------------  ----------
1951~1955       4         
1956~1960       7         
1961~1965       6         
1966~1970       8         
1971~1975       33        
1976~1980       121       
1981~1985       174       
1986~1990       212       
1991~1995       267       
1996~2000       336       
2001~2005       874       
2006~2010       1365      
2011~2015       2948      
2016~2020       1321

//Abstract Strategy
year_published  quantity  
--------------  ----------
1951~1955       26        
1956~1960       33        
1961~1965       64        
1966~1970       158       
1971~1975       294       
1976~1980       300       
1981~1985       379       
1986~1990       356       
1991~1995       357       
1996~2000       448       
2001~2005       927       
2006~2010       1161      
2011~2015       1541      
2016~2020       385

//Miniatures
year_published  quantity  
--------------  ----------
1951~1955       1         
1956~1960       0          
1961~1965       19        
1966~1970       26        
1971~1975       78        
1976~1980       162       
1981~1985       105       
1986~1990       208       
1991~1995       280       
1996~2000       417       
2001~2005       781       
2006~2010       1162      
2011~2015       2193      
2016~2020       939

//Educational 
year_published  quantity  
--------------  ----------
1951~1955       63        
1956~1960       68        
1961~1965       69        
1966~1970       121       
1971~1975       149       
1976~1980       160       
1981~1985       208       
1986~1990       330       
1991~1995       333       
1996~2000       479       
2001~2005       800       
2006~2010       1178      
2011~2015       959       
2016~2020       234

//Party Game 
year_published  quantity  
--------------  ----------
1951~1955       41        
1956~1960       25        
1961~1965       24        
1966~1970       55        
1971~1975       50        
1976~1980       36        
1981~1985       131       
1986~1990       334       
1991~1995       386       
1996~2000       378       
2001~2005       798       
2006~2010       1151      
2011~2015       1780      
2016~2020       695 

//Science Fiction 
year_published  quantity  
--------------  ----------
1951~1955       13        
1956~1960       5         
1961~1965       18        
1966~1970       22        
1971~1975       42        
1976~1980       211       
1981~1985       307       
1986~1990       284       
1991~1995       290       
1996~2000       380       
2001~2005       664       
2006~2010       820       
2011~2015       2094      
2016~2020       848

//Fighting 
year_published  quantity  
--------------  ----------
1951~1955       2         
1956~1960       4         
1961~1965       9         
1966~1970       12        
1971~1975       35        
1976~1980       80        
1981~1985       101       
1986~1990       167       
1991~1995       213       
1996~2000       300       
2001~2005       813       
2006~2010       1182      
2011~2015       1954      
2016~2020       762

//Trivia 
year_published  quantity  
--------------  ----------
1951~1955       39        
1956~1960       28        
1961~1965       35        
1966~1970       42        
1971~1975       44        
1976~1980       55        
1981~1985       287       
1986~1990       433       
1991~1995       441       
1996~2000       468       
2001~2005       819       
2006~2010       1295      
2011~2015       712       
2016~2020       80 

//Economic 
year_published  quantity  
--------------  ----------
1951~1955       18        
1956~1960       28        
1961~1965       49        
1966~1970       56        
1971~1975       116       
1976~1980       177       
1981~1985       252       
1986~1990       296       
1991~1995       233       
1996~2000       406       
2001~2005       679       
2006~2010       1033      
2011~2015       1137      
2016~2020       336

//Movies / TV / Radio theme
year_published  quantity  
--------------  ----------
1951~1955       58        
1956~1960       135       
1961~1965       225       
1966~1970       130       
1971~1975       134       
1976~1980       196       
1981~1985       294       
1986~1990       289       
1991~1995       326       
1996~2000       356       
2001~2005       767       
2006~2010       875       
2011~2015       969       
2016~2020       323 

//Print & Play 
year_published  quantity  
--------------  ----------
1951~1955       0          
1956~1960       0          
1961~1965       1         
1966~1970       3         
1971~1975       3         
1976~1980       5         
1981~1985       12        
1986~1990       14        
1991~1995       31        
1996~2000       128       
2001~2005       787       
2006~2010       1430      
2011~2015       1753      
2016~2020       414

