//document.getElementById("rating_stars").addEventListener("click",function({
//
//
//
//
//
//}))

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