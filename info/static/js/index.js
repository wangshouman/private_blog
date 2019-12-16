var isDialog = false
$(window).scroll(function () {
    const windowH = $(window).height();
    const documentH = $(document).height();
    const scrollH = $(window).scrollTop();
    if (windowH+scrollH>=documentH) {
        console.log("2222")
    }
});
function btnCategory(index, that) {
    //获取当前的分类ID
    $(that).addClass("active");
    $(that).siblings().removeClass("active")
    console.log(index)
};

function btnDetail1() {
    const news_id = 2
    $.ajax({
        url: `/getArticle/${news_id}`,
        type: "GET",
        contentType: "application/json",
        success: function (resp) {
           console.log("uuu", resp.content);
           // $('#html-content').html(resp.content);
           // console.log("dddd");
           window.location.href="/detail"
        },
        fail: function (error) {
            console.log(error)
        }
    })
};

function btnLogin() {
    // 点击登陆按钮，弹出登录框
    const username = $("#username").val() || '';
    const password = $("#password").val() || '';
    console.log("3333")
    console.log($("#username").val())
    console.log($("#password").val())
    // 判断是否为空 或者校验 输入框的规则是否满足 TODO
    if (username == '' || password == '') {
        console.log("55555")
    }
    const params = {
        "username": username,
        "password": password
    }
    // 请求接口，完成登录的逻辑
    $.ajax({
        url: "/login",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(params),
        success: function (resp) {
            window.location.href="/"
        },
        fail: function (error) {
            console.log(error)
        }
    })
};
