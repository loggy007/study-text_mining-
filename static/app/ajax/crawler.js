function crawler_facebook(id,token,limit)
{
	$.ajax({

        url: "/api/facebook", //網址
        data: {id:id,token:token,limit:limit}, //資料
        type: "POST", //接收方式
        dataType: 'json', //傳送類型

        success: function (msg) { //成功時 msg接收回傳資料
        	if(msg.error =="false")
            	alert("save ok");
            else
            	alert("save fail");
        },
        error: function (xhr, ajaxOptions, thrownError) { //失敗時
            alert("ee" + ajaxOptions);
        }
    });
    
}