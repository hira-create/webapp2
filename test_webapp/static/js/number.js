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
        $(".button1").val(data);
        $(".button1").text(data);
        }
        
    )
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
        $(".button2").val(data);
        $(".button2").text(data);
        }
    )
    })