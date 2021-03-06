from os import utime
import telegram

bot = telegram.Bot(token='2005969126:AAFPxDYQ5UClw9rauesbANXCtJTmuvxHZY0')    ####자기 TELEGRAM API와 ID를 입력해준다 / 봇 토큰
chat_id = 1576502417 ## 숫자만 입력 / 내 챗id

##https://api.telegram.org/bot2005969126:AAFPxDYQ5UClw9rauesbANXCtJTmuvxHZY0/getme          -> 봇 챗id 확인
##https://api.telegram.org/bot2005969126:AAFPxDYQ5UClw9rauesbANXCtJTmuvxHZY0/getupdates     -> 내 챗id 확인

import requests
import pandas as pd
import time
import webbrowser
import numpy as np

a = 1


while True:
    
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
            bot.sendMessage(chat_id=chat_id, text=f"{symbol}:rsi:{round(rsi,3)}") 
        time.sleep(1)
      

    def stockrsi(symbol):
        url = "https://api.upbit.com/v1/candles/minutes/240"
        
        querystring = {"market":symbol,"count":"500"}
        
        response = requests.request("GET", url, params=querystring)
        
        data = response.json()
        
        df = pd.DataFrame(data)
        
        series=df['trade_price'].iloc[::-1]
        
        df = pd.Series(df['trade_price'].values)
    
        period=14
        smoothK=3
        smoothD=3
         
        delta = series.diff().dropna()
        ups = delta * 0
        downs = ups.copy()
        ups[delta > 0] = delta[delta > 0]
        downs[delta < 0] = -delta[delta < 0]
        ups[ups.index[period-1]] = np.mean( ups[:period] )
        ups = ups.drop(ups.index[:(period-1)])
        downs[downs.index[period-1]] = np.mean( downs[:period] )
        downs = downs.drop(downs.index[:(period-1)])
        rs = ups.ewm(com=period-1,min_periods=0,adjust=False,ignore_na=False).mean() / \
             downs.ewm(com=period-1,min_periods=0,adjust=False,ignore_na=False).mean() 
        rsi = 100 - 100 / (1 + rs)
    
        stochrsi  = (rsi - rsi.rolling(period).min()) / (rsi.rolling(period).max() - rsi.rolling(period).min())
        stochrsi_K = stochrsi.rolling(smoothK).mean()
        stochrsi_D = stochrsi_K.rolling(smoothD).mean()
        
        print(symbol)    
       
        print('')
        time.sleep(1)

 
    rsiindex("KRW-BTC")   ###원하는 코인종목을 밑에 추가해주면 추가가된다 #기본적으로 비트,도지,이클,이더,리플
    stockrsi("KRW-BTC")
    rsiindex("KRW-ETH") #이더리움
    stockrsi("KRW-ETH")
    rsiindex("KRW-QKC") #쿼크체인
    stockrsi("KRW-QKC")
    rsiindex("KRW-SC") #시아코인
    stockrsi("KRW-SC")
    rsiindex("KRW-IQ") #에브리피디아
    stockrsi("KRW-IQ")
    rsiindex("KRW-RFR") #리퍼리움
    stockrsi("KRW-RFR")
    rsiindex("KRW-AHT") #아하토큰
    stockrsi("KRW-AHT")
    rsiindex("KRW-MVL") #엠블
    stockrsi("KRW-MVL")
    rsiindex("KRW-TT") #썬더토큰
    stockrsi("KRW-TT")
    rsiindex("KRW-MFT") #메인프레임
    stockrsi("KRW-MFT")
    rsiindex("KRW-CRE") #캐리프로토콜
    stockrsi("KRW-CRE")
    rsiindex("KRW-MBL") #무비블록
    stockrsi("KRW-MBL")
    rsiindex("KRW-BTT") #비트토렌트
    stockrsi("KRW-BTT")
    rsiindex("KRW-XEC") #이캐시
    stockrsi("KRW-XEC")
    rsiindex("KRW-BCH") #비트코인캐시
    stockrsi("KRW-BCH")
    rsiindex("KRW-AAVE") #에이브
    stockrsi("KRW-AAVE")
    rsiindex("KRW-LTC") #라이트코인
    stockrsi("KRW-LTC")
    rsiindex("KRW-SOL") #솔라나
    stockrsi("KRW-SOL")
    rsiindex("KRW-BSV") #비트코인SV
    stockrsi("KRW-BSV")
    rsiindex("KRW-AXS") #엑시인피니티
    stockrsi("KRW-AXS")
    rsiindex("KRW-BTG") #비트코인골드
    stockrsi("KRW-BTG")
    rsiindex("KRW-ETC") #이더리움클래식
    stockrsi("KRW-ETC")
    rsiindex("KRW-STRK") #스트라이크
    stockrsi("KRW-STRK")
    rsiindex("KRW-NEO") #네오
    stockrsi("KRW-NEO")
    rsiindex("KRW-DOT") #폴카닷
    stockrsi("KRW-DOT")
    rsiindex("KRW-LINK") #체인링크
    stockrsi("KRW-LINK")
    rsiindex("KRW-ATOM") #코스모스
    stockrsi("KRW-ATOM")
    rsiindex("KRW-WAVES") #웨이브
    stockrsi("KRW-WAVES")
    rsiindex("KRW-REP") #어거
    stockrsi("KRW-REP")
    rsiindex("KRW-QTUM") #퀀텀
    stockrsi("KRW-QTUM")
    rsiindex("KRW-FLOW") #플로우
    stockrsi("KRW-FLOW")
    rsiindex("KRW-OMG") #오미세고
    stockrsi("KRW-OMG")
    rsiindex("KRW-GAS") #가스
    stockrsi("KRW-GAS")
    rsiindex("KRW-TON") #톤
    stockrsi("KRW-TON")
    rsiindex("KRW-THETA") #쎄타
    stockrsi("KRW-THETA")
    rsiindex("KRW-SBD") #스팀달러
    stockrsi("KRW-SBD")
    rsiindex("KRW-SRM") #세럼
    stockrsi("KRW-SRM")
    rsiindex("KRW-XTZ") #테조스
    stockrsi("KRW-XTZ")
    rsiindex("KRW-KAVA") #카바
    stockrsi("KRW-KAVA")
    rsiindex("KRW-EOS") #이오스
    stockrsi("KRW-EOS")
    rsiindex("KRW-CBK") #코박
    stockrsi("KRW-CBK")
    rsiindex("KRW-1INCH") #1인치네트워크
    stockrsi("KRW-1INCH")
    rsiindex("KRW-AQT") #알파쿼크
    stockrsi("KRW-AQT")
    rsiindex("KRW-LSK") #리스트
    stockrsi("KRW-LSK")
    rsiindex("KRW-MANA") #디센트럴랜드
    stockrsi("KRW-MANA")
    rsiindex("KRW-MTL") #메탈
    stockrsi("KRW-MTL")
    rsiindex("KRW-DAWN") #던프로토콜
    stockrsi("KRW-DAWN")
    rsiindex("KRW-ENJ") #엔진
    stockrsi("KRW-ENJ")
    rsiindex("KRW-SAND") #샌드박스
    stockrsi("KRW-SAND")
    rsiindex("KRW-SXP") #스와이프
    stockrsi("KRW-SXP")
    rsiindex("KRW-STX") #스택스
    stockrsi("KRW-STX")
    rsiindex("KRW-ICX") #아이콘
    stockrsi("KRW-ICX")
    rsiindex("KRW-STRAX") #스트라티스
    stockrsi("KRW-STRAX")
    rsiindex("KRW-ADA") #에이다
    stockrsi("KRW-ADA")
    rsiindex("KRW-KNC") #카이버네트워크
    stockrsi("KRW-KNC")
    rsiindex("KRW-ARK") #아크
    stockrsi("KRW-ARK")
    rsiindex("KRW-STORJ") #스토리지
    stockrsi("KRW-STORJ")
    rsiindex("KRW-MATIC") #폴리곤
    stockrsi("KRW-MATIC")
    rsiindex("KRW-PLA") #플레이댑
    stockrsi("KRW-PLA")
    rsiindex("KRW-PUNDIX") #펀디엑스
    stockrsi("KRW-PUNDIX")
    rsiindex("KRW-ZRX") #제로엑스
    stockrsi("KRW-ZRX")
    rsiindex("KRW-IOTA") #아이오타
    stockrsi("KRW-IOTA")
    rsiindex("KRW-BAT") #베이직어텐션토큰
    stockrsi("KRW-BAT")
    rsiindex("KRW-XRP") #리플
    stockrsi("KRW-XRP")
    rsiindex("KRW-ONG") #온톨로지가스
    stockrsi("KRW-ONG")
    rsiindex("KRW-MLK") #밀크
    stockrsi("KRW-MLK")
    rsiindex("KRW-ONT") #온톨로지
    stockrsi("KRW-ONT")
    rsiindex("KRW-NU") #누사이퍼
    stockrsi("KRW-NU")
    rsiindex("KRW-HIVE") #하이브
    stockrsi("KRW-HIVE")
    rsiindex("KRW-HUNT") #헌트
    stockrsi("KRW-HUNT")
    rsiindex("KRW-POLY") #폴리메스
    stockrsi("KRW-POLY")
    rsiindex("KRW-STEEM") #스팀
    stockrsi("KRW-STEEM")
    rsiindex("KRW-WAXP") #왁스
    stockrsi("KRW-WAXP")
    rsiindex("KRW-ELF") #엘프
    stockrsi("KRW-ELF")
    rsiindex("KRW-CHZ") #칠리즈
    stockrsi("KRW-CHZ")
    rsiindex("KRW-GLM") #골렘
    stockrsi("KRW-GLM")
    rsiindex("KRW-HBAR") #헤데라
    stockrsi("KRW-HBAR")
    rsiindex("KRW-CVC") #시빅
    stockrsi("KRW-CVC")
    rsiindex("KRW-XLM") #스텔라루멘
    stockrsi("KRW-XLM")
    rsiindex("KRW-POWR") #파워렛져
    stockrsi("KRW-POWR")
    rsiindex("KRW-BORA") #보라
    stockrsi("KRW-BORA")
    rsiindex("KRW-TFUEL") #쎄타퓨엘
    stockrsi("KRW-TFUEL")
    rsiindex("KRW-CRO") #크립토닷컴체인
    stockrsi("KRW-CRO")
    rsiindex("KRW-ARDR") #아더
    stockrsi("KRW-ARDR")
    rsiindex("KRW-AERGO") #아르고
    stockrsi("KRW-AERGO")
    rsiindex("KRW-DOGE") #도지코인
    stockrsi("KRW-DOGE")
    rsiindex("KRW-HUM") #휴먼스케이프
    stockrsi("KRW-HUM")
    rsiindex("KRW-UPP") #센티넬프로토콜
    stockrsi("KRW-UPP")
    rsiindex("KRW-XEM") #넴
    stockrsi("KRW-XEM")
    rsiindex("KRW-MOC") #모스코인
    stockrsi("KRW-MOC")
    rsiindex("KRW-FCT2") #피르마체인
    stockrsi("KRW-FCT2")
    rsiindex("KRW-VET") #비체인
    stockrsi("KRW-VET")
    rsiindex("KRW-DKA") #디카르고
    stockrsi("KRW-DKA")
    rsiindex("KRW-ANKR") #앵커
    stockrsi("KRW-ANKR")
    rsiindex("KRW-ORBS") #오브스
    stockrsi("KRW-ORBS")
    rsiindex("KRW-STPT") #에스티피
    stockrsi("KRW-STPT")
    rsiindex("KRW-META") #메타디움
    stockrsi("KRW-META")
    rsiindex("KRW-TRX") #트론
    stockrsi("KRW-TRX")
    stockrsi("KRW-LOOM") #룸네트워크
    rsiindex("KRW-LOOM")
    stockrsi("KRW-ZIL")  #질리카
    rsiindex("KRW-ZIL")
    stockrsi("KRW-SNT") #스테이터스네트워크
    rsiindex("KRW-SNT")
    stockrsi("KRW-JST") #저스트
    rsiindex("KRW-JST")
    stockrsi("KRW-MED") #메디블록
    rsiindex("KRW-MED")
    stockrsi("KRW-SSX") #썸씽
    rsiindex("KRW-SSX")
