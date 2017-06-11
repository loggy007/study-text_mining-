//動態載入JS檔案
var jsFile = document.createElement("script");
jsFile.setAttribute("type","text/javascript");
jsFile.setAttribute("src", "static/app/ajax/crawler.js");
document.getElementsByTagName("head")[0].appendChild(jsFile);

//初始化 網頁準備好以後才執行
$("document").ready(function()	
{
   main();
});


//主程序
function main()
{


}

//UI事件處理
function submit()
{
	alert("go");
	var fid = $('#input_fid').val();
	var token = $('#input_token').val();
	var limit = $('#input_limit').val();
	crawler_facebook(fid,token,limit);
}