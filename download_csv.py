import requests
req=requests.get("https://raw.githubusercontent.com/mk-gurucharan/Regression/master/IceCreamData.csv")
url_content=req.content
csv_file=open("dataset.csv",'wb')
csv_file.write(url_content)
csv_file.close()