// source: https://codertw.com/%E5%89%8D%E7%AB%AF%E9%96%8B%E7%99%BC/285514/


var pageSize = 15; //每頁顯示的記錄條數
var curPage = 0; //當前頁
var lastPage; //最後頁
var direct = 0; //方向
var len; //總行數
var page; //總頁數
var begin;
var end;


$(document).ready(function display() {
    len = $("#myTable tr").length; // 求這個表的總行數
    len = len - 1; //剔除第一行介紹
    page = len % pageSize == 0 ? len / pageSize : Math.floor(len / pageSize) + 1; //根據記錄條數，計算頁數
    // alert("page===" page);
    curPage = 1; // 設定當前為第一頁
    displayPage(1); //顯示第一頁

    document.getElementById("btn0").innerHTML = "Current page: " + curPage + " / " + page + " "; // 顯示當前多少頁
    document.getElementById("ssss").innerHTML = "Totally " + len + " rows."; // 顯示資料量
    document.getElementById("pageSize").value = pageSize;



    $("#btn1").click(function firstPage() { // 首頁
        curPage = 1;
        direct = 0;
        displayPage();
    });
    $("#btn2").click(function frontPage() { // 上一頁
        direct = -1;
        displayPage();
    });
    $("#btn3").click(function nextPage() { // 下一頁
        direct = 1;
        displayPage();
    });
    $("#btn4").click(function lastPage() { // 尾頁
        curPage = page;
        direct = 0;
        displayPage();
    });
    $("#btn5").click(function changePage() { // 轉頁
        curPage = document.getElementById("changePage").value * 1;
        if (!/^[1-9]\d*$/.test(curPage)) {
            alert("Please type positive integer.");
            return;
        }
        if (curPage > page) {
            alert("The page number is out of range.");
            return;
        }
        direct = 0;
        displayPage();
    });


    $("#pageSizeSet").click(function setPageSize() { // 設定每頁顯示多少條記錄
        pageSize = document.getElementById("pageSize").value; //每頁顯示的記錄條數
        if (!/^[1-9]\d*$/.test(pageSize)) {
            alert("Please type positive integer.");
            return;
        }
        len = $("#mytable tr").length;
        len = len - 1;
        page = len % pageSize == 0 ? len / pageSize : Math.floor(len / pageSize) + 1; //根據記錄條數，計算頁數
        curPage = 1; //當前頁
        direct = 0; //方向
        firstPage();
    });
});

function displayPage() {
    if (curPage <= 1 && direct == -1) {
        direct = 0;
        alert("Already on the first page.");
        return;
    } else if (curPage >= page && direct == 1) {
        direct = 0;
        alert("Already on the last page.");
        return;
    }

    lastPage = curPage;

    // 修復當len=1時，curPage計算得0的bug
    if (len > pageSize) {
        curPage = ((curPage + direct + len) % len);
    } else {
        curPage = 1;
    }


    document.getElementById("btn0").innerHTML = "Current page:" + curPage + "/ " + page + " 每頁"; // 顯示當前多少頁

    begin = (curPage - 1) * pageSize + 1; // 起始記錄號
    end = begin + 1 * pageSize;
    end = end - 1; // 末尾記錄號


    if (end > len) end = len;
    $("#mytable tr").hide(); // 首先，設定這行為隱藏
    $("#mytable tr").each(function(i) { // 然後，通過條件判斷決定本行是否恢復顯示
        if ((i >= begin && i <= end) || i == 0) //顯示begin<=x<=end的記錄
            $(this).show();
    });

};