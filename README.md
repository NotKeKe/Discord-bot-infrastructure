## Discord bot的基礎架構
### core.classes (./core/classes.py)
- 在__init__中包含基礎的cog宣告
    - 在其他程式中可使用from core.classes import Cog_Extension去繼承classes中預設好的東西
### main.py
- 簡易開啟discord bot
### .env
- TOKEN:
    - 在此處放上你discord bot的token
- ONLINE_TEXT:
    - 自定義你bot上線時的訊息 (如: 正在遊玩 ONLINE_TEXT)
### 提示.py
- 裡面有些會用到的東西!
### cmds 資料夾
- 裡面我放了hello.py，預設好兩個指令: hello, ping

