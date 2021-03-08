# packages-execute-for-python

### bottle
=簡易網頁框架
Bottle 透過 @route("/action") 定義不同網址的回應行為，@route("/action/<varName>") 可從路由取參數。讀檔及刪檔時不使用檔名，而是採取雜湊碼比對，存取範圍嚴格限制在指定目錄內，可降低資安風險。取得檔案清單後轉成 Dictionary，以檔名雜湊碼為 Key，使用白名單方式限定只能下載項目，避免有人在路徑參數動手腳幹壞事。對映到檔案後，再使用 Bottle 提供的 static_file 傳回檔案內容。
這個對映裝飾器有可選的關鍵字method預設是method=’GET’. 還有可能是POST,PUT,DELETE,HEAD或者監聽其他的HTTP請求方法

[bottle參考](https://codertw.com/程式語言/372274/)