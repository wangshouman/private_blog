// $(function () {
//         $.ajax({
//         url: "/category",
//         type: "GET",
//         contentType: "application/json",
//         success: function (resp) {
//             console.log(resp)
//         },
//         fail: function (error) {
//             console.log(error)
//         }
//     })
// })

function btnCategory(index, that) {
    //获取当前的分类ID
    $(that).parent('div').addClass("active");
    $(that).parent('div').siblings().removeClass("active")
    console.log(index)
}