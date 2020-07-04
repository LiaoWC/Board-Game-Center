<!-- Display Notification -->
<
button type = "button"
id = "btnShowNotification" > 跑一個顯示通知範例 < /button> <
    script >

    var notification = null;

function ShowNotification(title, body) {
    notification = new Notification(title, {
        icon: '/icon/ms-icon-310x310.png',
        body: body,
        onclick: function() {
            parent.focus();
            window.focus(); //just in case, older browsers
            this.close();
        }
    })
}

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
}); <
/script>