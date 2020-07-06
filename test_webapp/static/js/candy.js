$(".candy").on("click", function (e) {
    // 多重クリック防止
    e.stopPropagation();
    // ID名を取得
    let file_name = $(this).attr("id")
    // APIをGET
    $.get("../get_candy/2", function (data, status) {
        // デバッグ用
        // APIからのレスポンス
        console.log("data:" + data)
        console.log("status" + status)
        // n枚の画像を差し替える
        for (let i = 0; i < data.length; i++) {
            $(".candy-" + String(i + 1)).attr("src", data[i])
        }
    })
})
$(".button1").on("click", function (e){

})

$(".button2").on("click", function (e){

})