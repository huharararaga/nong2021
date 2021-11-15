from os import utime
import telegram

bot = telegram.Bot(token='2132644122:AAGbQj6CIa3K9InU1CdlHjvv8xYrkOe8leU')    ####자기 TELEGRAM API와 ID를 입력해준다 / 봇 토큰
chat_id = 1576502417 ## 숫자만 입력 / 내 챗id

##https://api.telegram.org/bot2132644122:AAGbQj6CIa3K9InU1CdlHjvv8xYrkOe8leU/getme          -> 봇 챗id 확인
##https://api.telegram.org/bot2005969126:AAFPxDYQ5UClw9rauesbANXCtJTmuvxHZY0/getupdates     -> 내 챗id 확인

import requests
import pandas as pd
import time
import webbrowser
import numpy as np

a = 1

if any:
    
    def rsiindex(symbol):
        url = "https://api.upbit.com/v1/candles/minutes/240" #### minutes 뒤에 원하는 분 설정을 넣으면 된다 기본적으로 3분으로 설정
    
        querystring = {"market":symbol,"count":"500"}
    
        response = requests.request("GET", url, params=querystring)
    
        data = response.json()
    
        df = pd.DataFrame(data)
    
        df=df.reindex(index=df.index[::-1]).reset_index()
    
        df['close']=df["trade_price"]
        
        global a
    
        if a==1:
 
         
            a=2   

    
    
        def rsi(ohlc: pd.DataFrame, period: int = 14):
            ohlc["close"] = ohlc["close"]
            delta = ohlc["close"].diff()
    
            up, down = delta.copy(), delta.copy()
            up[up < 0] = 0
            down[down > 0] = 0
    
            _gain = up.ewm(com=(period - 1), min_periods=period).mean()
            _loss = down.abs().ewm(com=(period - 1), min_periods=period).mean()
    
            RS = _gain / _loss
            return pd.Series(100 - (100 / (1 + RS)), name="RSI")
    
        rsi = rsi(df, 14).iloc[-1]
        print(symbol)
        print('upbit 240 minute RSI:', rsi)
        print('')
        if rsi<30:     ######## rsi 지수가 30미만이면 텔레그램봇을통해 메시지 전송 ,원하는 숫자로 수정가능
            bot.sendMessage(chat_id=chat_id, text=f"{symbol}:rsi:{round(rsi,3)}  /240분봉 ") 
        time.sleep(0)
      



 
    rsiindex("KRW-BTC")   ###원하는 코인종목을 밑에 추가해주면 추가가된다 #기본적으로 비트,도지,이클,이더,리플
    rsiindex("KRW-ETH") #이더리움
    rsiindex("KRW-QKC") #쿼크체인
    rsiindex("KRW-SC") #시아코인
    rsiindex("KRW-IQ") #에브리피디아
    rsiindex("KRW-RFR") #리퍼리움
    rsiindex("KRW-AHT") #아하토큰
    rsiindex("KRW-MVL") #엠블
    rsiindex("KRW-TT") #썬더토큰
    rsiindex("KRW-MFT") #메인프레임
    rsiindex("KRW-CRE") #캐리프로토콜
    rsiindex("KRW-MBL") #무비블록
    rsiindex("KRW-BTT") #비트토렌트
    rsiindex("KRW-XEC") #이캐시
    rsiindex("KRW-BCH") #비트코인캐시
    rsiindex("KRW-AAVE") #에이브
    rsiindex("KRW-LTC") #라이트코인
    rsiindex("KRW-SOL") #솔라나
    rsiindex("KRW-BSV") #비트코인SV
    rsiindex("KRW-AXS") #엑시인피니티
    rsiindex("KRW-BTG") #비트코인골드
    rsiindex("KRW-ETC") #이더리움클래식
    rsiindex("KRW-STRK") #스트라이크
    rsiindex("KRW-NEO") #네오
    rsiindex("KRW-DOT") #폴카닷
    rsiindex("KRW-LINK") #체인링크
    rsiindex("KRW-ATOM") #코스모스
    rsiindex("KRW-WAVES") #웨이브
    rsiindex("KRW-REP") #어거
    rsiindex("KRW-QTUM") #퀀텀
    rsiindex("KRW-FLOW") #플로우
    rsiindex("KRW-OMG") #오미세고
    rsiindex("KRW-GAS") #가스
    rsiindex("KRW-TON") #톤
    rsiindex("KRW-THETA") #쎄타
    rsiindex("KRW-SBD") #스팀달러
    rsiindex("KRW-SRM") #세럼
    rsiindex("KRW-XTZ") #테조스
    rsiindex("KRW-KAVA") #카바
    rsiindex("KRW-EOS") #이오스
    rsiindex("KRW-CBK") #코박
    rsiindex("KRW-1INCH") #1인치네트워크
    rsiindex("KRW-AQT") #알파쿼크
    rsiindex("KRW-LSK") #리스트
    rsiindex("KRW-MANA") #디센트럴랜드
    rsiindex("KRW-MTL") #메탈
    rsiindex("KRW-DAWN") #던프로토콜
    rsiindex("KRW-ENJ") #엔진
    rsiindex("KRW-SAND") #샌드박스
    rsiindex("KRW-SXP") #스와이프
    rsiindex("KRW-STX") #스택스
    rsiindex("KRW-ICX") #아이콘
    rsiindex("KRW-STRAX") #스트라티스
    rsiindex("KRW-ADA") #에이다
    rsiindex("KRW-KNC") #카이버네트워크
    rsiindex("KRW-ARK") #아크
    rsiindex("KRW-STORJ") #스토리지
    rsiindex("KRW-MATIC") #폴리곤
    rsiindex("KRW-PLA") #플레이댑
    rsiindex("KRW-PUNDIX") #펀디엑스
    rsiindex("KRW-ZRX") #제로엑스
    rsiindex("KRW-IOTA") #아이오타
    rsiindex("KRW-BAT") #베이직어텐션토큰
    rsiindex("KRW-XRP") #리플
    rsiindex("KRW-ONG") #온톨로지가스
    rsiindex("KRW-MLK") #밀크
    rsiindex("KRW-ONT") #온톨로지
    rsiindex("KRW-NU") #누사이퍼
    rsiindex("KRW-HIVE") #하이브
    rsiindex("KRW-HUNT") #헌트
    rsiindex("KRW-POLY") #폴리메스
    rsiindex("KRW-STEEM") #스팀
    rsiindex("KRW-WAXP") #왁스
    rsiindex("KRW-ELF") #엘프
    rsiindex("KRW-CHZ") #칠리즈
    rsiindex("KRW-GLM") #골렘
    rsiindex("KRW-HBAR") #헤데라
    rsiindex("KRW-CVC") #시빅
    rsiindex("KRW-XLM") #스텔라루멘
    rsiindex("KRW-POWR") #파워렛져
    rsiindex("KRW-BORA") #보라
    rsiindex("KRW-TFUEL") #쎄타퓨엘
    rsiindex("KRW-CRO") #크립토닷컴체인
    rsiindex("KRW-ARDR") #아더
    rsiindex("KRW-AERGO") #아르고
    rsiindex("KRW-DOGE") #도지코인
    rsiindex("KRW-HUM") #휴먼스케이프
    rsiindex("KRW-UPP") #센티넬프로토콜
    rsiindex("KRW-XEM") #넴
    rsiindex("KRW-MOC") #모스코인
    rsiindex("KRW-FCT2") #피르마체인
    rsiindex("KRW-VET") #비체인
    rsiindex("KRW-DKA") #디카르고
    rsiindex("KRW-ANKR") #앵커
    rsiindex("KRW-ORBS") #오브스
    rsiindex("KRW-STPT") #에스티피
    rsiindex("KRW-META") #메타디움
    rsiindex("KRW-TRX") #트론
    rsiindex("KRW-LOOM") #룸네트워크
    rsiindex("KRW-ZIL") #질리카
    rsiindex("KRW-SNT") #스테이터스네트워크
    rsiindex("KRW-JST") #저스트
    rsiindex("KRW-MED") #메디블록
    rsiindex("KRW-SSX") #썸씽
