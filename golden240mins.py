import pandas as pd
import datetime
import requests
import time
import webbrowser
import numpy as np
import telegram

a = 1

while True:
    def goldencross(symbol):
        url = "https://api.upbit.com/v1/candles/minutes/240"
        
        querystring = {"market":symbol,"count":"100"}
        
        response = requests.request("GET", url, params=querystring)
        
        data = response.json()
        
        df = pd.DataFrame(data)
        
        df=df['trade_price'].iloc[::-1]
        
    
        global a
        if a==1:



    
            a=2    
        
    
        ma20 = df.rolling(window=20).mean()
        ma60 = df.rolling(window=60).mean()
        
        test1=ma20.iloc[-2]-ma60.iloc[-2]
        test2=ma20.iloc[-1]-ma60.iloc[-1]
        
        call='해당없음'
        
        if test1>0 and test2<0:
           call='데드크로스' 
            
        if test1<0 and test2>0:
           call='골든크로스'     
        
        print(symbol)
        print('이동평균선 20: ', round(ma20.iloc[-1],2))
        print('이동평균선 60: ', round(ma60.iloc[-1],2))
        print('골든크로스/데드크로스: ',call)
        print('')
        
        if call=='골든크로스' or call=='데드크로스':       
        
            text=symbol+'/'+'이동평균선 20: '+ str(round(ma20.iloc[-1],2))+'/'+'이동평균선 60: '+ str(round(ma60.iloc[-1],2))+'/'+'골든크로스/데드크로스: '+call
            chat_id='텔레그램 챗아이디'
            bot = telegram.Bot(token='2005969126:AAFPxDYQ5UClw9rauesbANXCtJTmuvxHZY0')
            bot.sendMessage(chat_id=1576502417, text=text)              
            time.sleep(0)
    


goldencross("KRW-BTC") ###원하는 코인종목을 밑에 추가해주면 추가가된다 #기본적으로 비트,도지,이클,이더,리플
goldencross("KRW-ETH") #이더리움
goldencross("KRW-QKC") #쿼크체인
goldencross("KRW-SC") #시아코인
goldencross("KRW-IQ") #에브리피디아
goldencross("KRW-RFR") #리퍼리움
goldencross("KRW-AHT") #아하토큰
goldencross("KRW-MVL") #엠블
goldencross("KRW-TT") #썬더토큰
goldencross("KRW-MFT") #메인프레임
goldencross("KRW-CRE") #캐리프로토콜
goldencross("KRW-MBL") #무비블록
goldencross("KRW-BTT") #비트토렌트
goldencross("KRW-XEC") #이캐시
goldencross("KRW-BCH") #비트코인캐시
goldencross("KRW-AAVE") #에이브
goldencross("KRW-LTC") #라이트코인
goldencross("KRW-SOL") #솔라나
goldencross("KRW-BSV") #비트코인SV
goldencross("KRW-AXS") #엑시인피니티
goldencross("KRW-BTG") #비트코인골드
goldencross("KRW-ETC") #이더리움클래식
goldencross("KRW-STRK") #스트라이크
goldencross("KRW-NEO") #네오
goldencross("KRW-DOT") #폴카닷
goldencross("KRW-LINK") #체인링크
goldencross("KRW-ATOM") #코스모스
goldencross("KRW-WAVES") #웨이브
goldencross("KRW-REP") #어거
goldencross("KRW-QTUM") #퀀텀
goldencross("KRW-FLOW") #플로우
goldencross("KRW-OMG") #오미세고
goldencross("KRW-GAS") #가스
goldencross("KRW-TON") #톤
goldencross("KRW-THETA") #쎄타
goldencross("KRW-SBD") #스팀달러
goldencross("KRW-SRM") #세럼
goldencross("KRW-XTZ") #테조스
goldencross("KRW-KAVA") #카바
goldencross("KRW-EOS") #이오스
goldencross("KRW-CBK") #코박
goldencross("KRW-1INCH") #1인치네트워크
goldencross("KRW-AQT") #알파쿼크
goldencross("KRW-LSK") #리스트
goldencross("KRW-MANA") #디센트럴랜드
goldencross("KRW-MTL") #메탈
goldencross("KRW-DAWN") #던프로토콜
goldencross("KRW-ENJ") #엔진
goldencross("KRW-SAND") #샌드박스
goldencross("KRW-SXP") #스와이프
goldencross("KRW-STX") #스택스
goldencross("KRW-ICX") #아이콘
goldencross("KRW-STRAX") #스트라티스
goldencross("KRW-ADA") #에이다
goldencross("KRW-KNC") #카이버네트워크
goldencross("KRW-ARK") #아크
goldencross("KRW-STORJ") #스토리지
goldencross("KRW-MATIC") #폴리곤
goldencross("KRW-PLA") #플레이댑
goldencross("KRW-PUNDIX") #펀디엑스
goldencross("KRW-ZRX") #제로엑스
goldencross("KRW-IOTA") #아이오타
goldencross("KRW-BAT") #베이직어텐션토큰
goldencross("KRW-XRP") #리플
goldencross("KRW-ONG") #온톨로지가스
goldencross("KRW-MLK") #밀크
goldencross("KRW-ONT") #온톨로지
goldencross("KRW-NU") #누사이퍼
goldencross("KRW-HIVE") #하이브
goldencross("KRW-HUNT") #헌트
goldencross("KRW-POLY") #폴리메스
goldencross("KRW-STEEM") #스팀
goldencross("KRW-WAXP") #왁스
goldencross("KRW-ELF") #엘프
goldencross("KRW-CHZ") #칠리즈
goldencross("KRW-GLM") #골렘
goldencross("KRW-HBAR") #헤데라
goldencross("KRW-CVC") #시빅
goldencross("KRW-XLM") #스텔라루멘
goldencross("KRW-POWR") #파워렛져
goldencross("KRW-BORA") #보라
goldencross("KRW-TFUEL") #쎄타퓨엘
goldencross("KRW-CRO") #크립토닷컴체인
goldencross("KRW-ARDR") #아더
goldencross("KRW-AERGO") #아르고
goldencross("KRW-DOGE") #도지코인
goldencross("KRW-HUM") #휴먼스케이프
goldencross("KRW-UPP") #센티넬프로토콜
goldencross("KRW-XEM") #넴
goldencross("KRW-MOC") #모스코인
goldencross("KRW-FCT2") #피르마체인
goldencross("KRW-VET") #비체인
goldencross("KRW-DKA") #디카르고
goldencross("KRW-ANKR") #앵커
goldencross("KRW-ORBS") #오브스
goldencross("KRW-STPT") #에스티피
goldencross("KRW-META") #메타디움
goldencross("KRW-TRX") #트론
goldencross("KRW-LOOM") #룸네트워크
goldencross("KRW-ZIL") #질리카
goldencross("KRW-SNT") #스테이터스네트워크
goldencross("KRW-JST") #저스트
goldencross("KRW-MED") #메디블록
goldencross("KRW-SSX") #썸씽



