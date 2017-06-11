from flask import jsonify
import requests
import pandas as pd 
from dateutil.parser import parse
import os
class main:
	def __init__(self,savepath):
 		self.name = "facebook"
 		self.savepath = savepath

 	
	def crawler_csv(self,package):
		error = "true"

		fid = package["fid"]
		token = package["token"]
		limit = package["limit"]
		try:
			#在Facebook Graph API Exploer取得token
			token = token
			
			#在Facebook Graph API Exploer取得粉絲專頁的id與名稱，並將其包成字典dic
			fanpage = {fid:'蘋果新聞'} 

			#建立一個空的list
			information_list = []

			#使用for迴圈依序讀取粉絲頁的資訊，並使用format將id與token傳入{}裡
			url = 'https://graph.facebook.com/v2.9/232633627068/posts?fields=message,created_time,comments&limit='+str(limit)+'&access_token={}'.format(token)
			for ele in fanpage:
			    res = requests.get(url)

			#API最多一次呼叫100筆資料，因此使用while迴圈去翻頁取得所有的資料

			for information in res.json()['data']:
			    if 'message' in information:
			        information_list.append([fanpage[ele], information['message'], parse(information['created_time']).date()])

			#最後將list轉換成dataframe，並輸出成csv檔
			information_df = pd.DataFrame(information_list, columns=['粉絲專頁', '發文內容', '發文時間']) 
			information_df.to_csv(self.savepath+"\\temp\\data.csv", index=False)

			error = "false"
		except ValueError:
			error = "true"

		return jsonify(error=error)