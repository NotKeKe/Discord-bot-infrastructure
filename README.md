## Discord bot的基礎架構
### core.classes (./core/classes.py)
- 在__init__中包含基礎的cog宣告
    - 在其他程式中可使用from core.classes import Cog_Extension
### main.py
- 簡易開啟discord bot
### config.json
- "TOKEN":
    - 在此處放上你discord bot的token
- "online_text":
    - 自定義你bot上線時的訊息 (如: 正在遊玩 online_text)

