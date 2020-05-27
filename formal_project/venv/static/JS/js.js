/* 時間 */
/* 來源：sololearn */
function printTime() {
    var d = new Date();
    var hours = d.getHours();
    var mins = d.getMinutes();
    var secs = d.getSeconds();
    document.getElementById("show_time").innerHTML = ("It's " + hours + ":" + mins + ":" + secs + " now.");
}
setInterval(printTime, 1000);