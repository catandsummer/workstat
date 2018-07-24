function login() {
    var data = $("#form1").serialize();
    $.ajax({
        type: "POST",
        url: "/auth/login",
        data: data,
        success: function (msg) {
window.location.href = '/';
        },
        error:function (msg) {
            alert("用户名密码错误");
        }
    });
    return false;
}
