// if (!('Notification' in window)) {
//     console.log('This browser does not support notification');
// }
//
// if (Notification.permission === 'default' || Notification.permission === 'undefined') {
//     Notification.requestPermission(function(permission) {
//         // permission 可為「granted」（同意）、「denied」（拒絕）和「default」（未授權）
//         // 在這裡可針對使用者的授權做處理
//     });
// }
//
// var notifyConfig = {
//     body: '\\ ^o^ /', // 設定內容
//     icon: '/images/favicon.ico', // 設定 icon
// };
//
// if (Notification.permission === 'default' || Notification.permission === 'undefined') {
//     Notification.requestPermission(function(permission) {
//         if (permission === 'granted') {
//             // 使用者同意授權
//             var notification = new Notification('Hi there!', notifyConfig); // 建立通知
//         }
//     });
// }
// var notify = new Notification("Hi there!", {
//     body: '\\ ^o^ /',
//     icon: '/images/favicon.ico',
//     tag: 'newArrival' // 設定標籤
// });
//
// var notify = new Notification("Hi there!", {
//     body: '\\ ^o^ /',
//     icon: '/images/favicon.ico'
// });
//
// notify.onclick = function(e) { // 綁定點擊事件
//     e.preventDefault(); // prevent the browser from focusing the Notification's tab
//     window.open('http://sample.com./'); // 打開特定網頁
// }
//
//
var notification = null;

function ShowNotification(title, body) {
    notification = new Notification(title, {
//        icon: '/icon/ms-icon-310x310.png',
        icon: 'warning.png',
        body: body,
        onclick: function() {
            parent.focus();
            window.focus(); //just in case, older browsers
            this.close();
        }
    })
}

$(document).ready(function() {
    $('#btnGetNotification').click(function() {

        if (Notification && Notification.permission === 'default') {
            Notification.requestPermission(function(permission) {
                if (!('permission' in Notification)) {
                    Notification.permission = permission;
                }
            });
        } else if (Notification.permission === 'granted') {
            alert('已經有取得權限了!');
        } else {
            alert('請檢查是否你的瀏覽器支援');
        }
    });



    $('#btnShowNotification').click(function() {
        if (Notification && Notification.permission === 'default') {
            Notification.requestPermission(function(permission) {
                if (!('permission' in Notification)) {
                    Notification.permission = permission;
                }
            });
        } else if (Notification.permission === 'granted') {
            ShowNotification("測試標題", "測試內文");
            //三秒後自動關閉
            setTimeout(notification.close.bind(notification), 3000);
        } else {
            alert('請檢查是否你的瀏覽器支援');
        }
    });
//    setTimeout(ShowNotification("aaa","bbb"),10000);

});










$(function() {
    // 這裡我有改過
    csmapi.set_endpoint('http://2.iottalk.tw:9999');
    var profile = {
        'dm_name': 'Bulb',
        'idf_list': [],
        'odf_list': [Luminance, Color_O],
    }

    var r = 0;
    var g = 255;
    var b = 0;
    var lum = 100;
    var pic_vis = 1;
    var if_bling = 0;
    var if_open_Warn = 0;

    function draw() {
        if (pic_vis > 0) {
            var rr = Math.floor((r * lum) / 100);
            var gg = Math.floor((g * lum) / 100);
            var bb = Math.floor((b * lum) / 100);
        } else {
            rr = gg = bb = 0;
        }
        $('.bulb-top, .bulb-middle-1, .bulb-middle-2, .bulb-middle-3, .bulb-bottom, .night').css({ 'background': 'rgb(' + rr + ', ' + gg + ', ' + bb + ')' });
    }

    // function Warn() {
    //     /* var imgid = document.getElementById("imgid");*/
    //     if (if_bling > 0) {
    //         if (pic_vis == 1) {
    //             console.log("Warn => if_bling>0 => picvis ==1");
    //             r = 255;
    //             g = 0;
    //             b = 0;
    //             lum = 100;
    //             draw();
    //             pic_vis = 0;
    //         } else {
    //             console.log("Warn => if_bling>0  => picvis ==1");
    //             pic_vis = 1;
    //             draw();
    //         }
    //     } else {
    //         console.log("Warn => if_bling<=0");
    //         pic_vis = 1;
    //         if_bling = 0;
    //         return;
    //     }
    //     setTimeout(Warn, 1000);
    // }
    // Warn();



    function Luminance(data) {
        aaa = data[0]
        if (aaa < 10) {
            if_bling = 1;
            r= 255;
            g = b = 0;
            console.log(aaa);
            draw();
            $("#warn").text("警告！");
            $("#warn").css("size:30px; color:red; background-color:white;")
            ShowNotification("能見度低，請小心","⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️️\n請小心慢行");
        } else {
            r = 0;
            g = 255;
            b = 0;
            if_bling = 0;
            pic_vis = 1;
            $("#warn").text("");
            console.log(aaa);
            draw();
        }
    }

    function Color_O(data) {
        r = data[0];
        g = data[1];
        b = data[2];
        draw();
    }

    function ida_init() {
        // $('font')[0].innerText = profile.d_name;
        $('font')[0].innerText = "Visualbility Warning Device";
        draw();
    }

    var ida = {
        'ida_init': ida_init,
    };

    dai(profile, ida);
});