$(".button1").on("click", function (e){
    // 多重クリック防止
    e.stopPropagation();
    // ID名を取得
    let button_value = $(this).val()
    // APIをGET
    $.get("../get_number/"+button_value, function (data, status) {
        // デバッグ用
        // APIからのレスポンス
        console.log("data:" + data)
        console.log("status" + status)
        //加算
        for (let i = 0; i < data.length; i++){
            $(".button1").prop("value", data[i]);
        }

    })
    })

$(".button2").on("click", function (e){
    // 多重クリック防止
    e.stopPropagation();
    // ID名を取得
    let button_value = $(this).val()
    // APIをGET
    $.get("../get_number/"+button_value, function (data, status) {
        // デバッグ用
        // APIからのレスポンス
        console.log("data:" + data)
        console.log("status" + status)
        //加算
        for (let i = 0; i < data.length; i++){
            $(".button2").prop("value", data[i]);
        }
    })
    })