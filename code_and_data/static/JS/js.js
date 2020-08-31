/* 時間 */
/* 來源：sololearn */
//function printTime() {
//    var d = new Date();
//    var hours = d.getHours();
//    var mins = d.getMinutes();
//    var secs = d.getSeconds();
//    document.getElementById("show_time").innerHTML = ("It's " + hours + ":" + mins + ":" + secs + " now.");
//}
//setInterval(printTime, 1000);

//document.getElementById("cursor_effect").style.cursor = "pointer";
$(".td_row").css("cursor: pointer");
//
//function round_two_digit(n){
//    return Math.round(n*100)/100;
//}
//
//$(document).ready(function(){
//    $("#rating_round_row") = round_two_digit($("#rating_round_row").text().toString());
//})
$(document.getElementById("menu_btn").addEventListener('click', function(e) {
    $(this).toggleClass('active');
    $('#menu_ul').toggleClass('active');
    $("#searchNameFrame_inNav").toggleClass("active");
}));

//var vv = document.getElementById("menu_btn");
//if(vv){
//    vv.addEventListener('click', function(e) {
//     $(this).toggleClass('active');
//     $('#menu_ul').toggleClass('active');
// })}

// $('#menu_ul li').click(function() {
//     $(this).parent().find('li').each(function() {
//         if ($(this).hasClass('current-active')) {
//             $(this).toggleClass('current-active');
//         }
//     })
//     $(this).toggleClass('current-active');
//})