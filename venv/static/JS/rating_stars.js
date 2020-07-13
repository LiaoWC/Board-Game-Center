// 顯示評分
$(document).ready(function(){
    var rating = $("#rating").text();
    rating = parseFloat(rating)
    if(rating<=0)
    {$("#rating_stars").text("☆☆☆☆☆");}
    else if(rating<=2&&rating>0)
    {$("#rating_stars").text("★☆☆☆☆");}
    else if(rating>2&&rating<=4)
    {$("#rating_stars").text("★★☆☆☆");}
    else if(rating>4&&rating<=6)
    {$("#rating_stars").text("★★★☆☆");}
    else if(rating>6&&rating<=8)
    {$("#rating_stars").text("★★★★☆");}
    else if(rating>8)
    {$("#rating_stars").text("★★★★★");}
    else
    {alert("There's something error.")}
})

// 評分功能
var game_name="";
$(document).ready(function get_game_name(){
    game_name = $("div#info > h1").attr("name");
//    alert(game_name);
})

// 評分 (1~10)
function rate(num){
    alert("Thank you for your rating!")
    var ret_link = "/rate/" + game_name + "/" + String(num);
    window.open(ret_link,"_self");
}

window.onload = function(){
    $("#rate10").click(function(){rate(10);});
    $("#rate9").click(function(){rate(9);});
    $("#rate8").click(function(){rate(8);});
    $("#rate7").click(function(){rate(7);});
    $("#rate6").click(function(){rate(6);});
    $("#rate5").click(function(){rate(5);});
    $("#rate4").click(function(){rate(4);});
    $("#rate3").click(function(){rate(3);});
    $("#rate2").click(function(){rate(2);});
    $("#rate1").click(function(){rate(1);});
};


