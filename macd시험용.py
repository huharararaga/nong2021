import requests
import pandas as pd
import time
import webbrowser
import numpy as np
import telegram

a = 1

if  any:
    def goldencrossMACD(symbol):
        url = "https://api.upbit.com/v1/candles/minutes/240"

        querystring = {"market":symbol,"count":"100"}
    
        response = requests.request("GET", url, params=querystring)
    
        data = response.json()
    
        df = pd.DataFrame(data)
    
        df=df.iloc[::-1]
    
        df=df['trade_price']

        global a
        if a==1:
 
            a=2

        exp1 = df.ewm(span=20, adjust=False).mean()
        exp2 = df.ewm(span=60, adjust=False).mean()
        macd = exp1-exp2
        exp3 = macd.ewm(span=12, adjust=False).mean()
    
        test1=exp3[0]-macd[0]
        test2=exp3[1]-macd[1]
    
        call='매매 필요없음'
    
        if test1<0 and test2>0:
            call='MACD 데드크로스'
       
        if test1>0 and test2<0:
            call='MACD 골든크로스'
       
        print(symbol)
        print('MACD: ',macd[0])
        print('Signal: ',exp3[0])
        print('골든크로스/데드크로스: ',call)
        print('')

        if call=='MACD 골든크로스' or call=='MACD 데드크로스':       
        
            text=symbol+ '\n' +call
            bot = telegram.Bot(token='5037154944:AAHup32NJPsahGYdpDJOnpsZVsK4wOtjtfo')
            bot.sendMessage(chat_id=1576502417, text=text)              
            time.sleep(1)


goldencrossMACD("KRW-BTC") ###원하는 코인종목을 밑에 추가해주면 추가가된다 #기본적으로 비트,도지,이클,이더,리플goldencrossMACD("KRW-ETH") #이더리움goldencrossMACD("KRW-QKC") #쿼크체인
goldencrossMACD("KRW-SC") #시아코인
goldencrossMACD("KRW-IQ") #에브리피디아
goldencrossMACD("KRW-RFR") #리퍼리움
goldencrossMACD("KRW-AHT") #아하토큰
goldencrossMACD("KRW-MVL") #엠블
goldencrossMACD("KRW-TT") #썬더토큰
goldencrossMACD("KRW-MFT") #메인프레임
goldencrossMACD("KRW-CRE") #캐리프로토콜
goldencrossMACD("KRW-MBL") #무비블록
goldencrossMACD("KRW-BTT") #비트토렌트
goldencrossMACD("KRW-XEC") #이캐시
goldencrossMACD("KRW-BCH") #비트코인캐시
goldencrossMACD("KRW-AAVE") #에이브
goldencrossMACD("KRW-LTC") #라이트코인
goldencrossMACD("KRW-SOL") #솔라나
goldencrossMACD("KRW-BSV") #비트코인SV
goldencrossMACD("KRW-AXS") #엑시인피니티
goldencrossMACD("KRW-BTG") #비트코인골드
goldencrossMACD("KRW-ETC") #이더리움클래식
goldencrossMACD("KRW-STRK") #스트라이크
goldencrossMACD("KRW-NEO") #네오
goldencrossMACD("KRW-DOT") #폴카닷
goldencrossMACD("KRW-LINK") #체인링크
goldencrossMACD("KRW-ATOM") #코스모스
goldencrossMACD("KRW-WAVES") #웨이브
goldencrossMACD("KRW-REP") #어거
goldencrossMACD("KRW-QTUM") #퀀텀
goldencrossMACD("KRW-FLOW") #플로우
goldencrossMACD("KRW-OMG") #오미세고
goldencrossMACD("KRW-GAS") #가스
goldencrossMACD("KRW-TON") #톤
goldencrossMACD("KRW-THETA") #쎄타
goldencrossMACD("KRW-SBD") #스팀달러
goldencrossMACD("KRW-SRM") #세럼
goldencrossMACD("KRW-XTZ") #테조스
goldencrossMACD("KRW-KAVA") #카바
goldencrossMACD("KRW-EOS") #이오스
goldencrossMACD("KRW-CBK") #코박
goldencrossMACD("KRW-1INCH") #1인치네트워크
goldencrossMACD("KRW-AQT") #알파쿼크
goldencrossMACD("KRW-LSK") #리스트
goldencrossMACD("KRW-MANA") #디센트럴랜드
goldencrossMACD("KRW-MTL") #메탈
goldencrossMACD("KRW-DAWN") #던프로토콜
goldencrossMACD("KRW-ENJ") #엔진
goldencrossMACD("KRW-SAND") #샌드박스
goldencrossMACD("KRW-SXP") #스와이프
goldencrossMACD("KRW-STX") #스택스
goldencrossMACD("KRW-ICX") #아이콘
goldencrossMACD("KRW-STRAX") #스트라티스
goldencrossMACD("KRW-ADA") #에이다
goldencrossMACD("KRW-KNC") #카이버네트워크
goldencrossMACD("KRW-ARK") #아크
goldencrossMACD("KRW-STORJ") #스토리지
goldencrossMACD("KRW-MATIC") #폴리곤
goldencrossMACD("KRW-PLA") #플레이댑
goldencrossMACD("KRW-PUNDIX") #펀디엑스
goldencrossMACD("KRW-ZRX") #제로엑스
goldencrossMACD("KRW-IOTA") #아이오타
goldencrossMACD("KRW-BAT") #베이직어텐션토큰
goldencrossMACD("KRW-XRP") #리플
goldencrossMACD("KRW-ONG") #온톨로지가스
goldencrossMACD("KRW-MLK") #밀크
goldencrossMACD("KRW-ONT") #온톨로지
goldencrossMACD("KRW-NU") #누사이퍼
goldencrossMACD("KRW-HIVE") #하이브
goldencrossMACD("KRW-HUNT") #헌트
goldencrossMACD("KRW-POLY") #폴리메스
goldencrossMACD("KRW-STEEM") #스팀
goldencrossMACD("KRW-WAXP") #왁스
goldencrossMACD("KRW-ELF") #엘프
goldencrossMACD("KRW-CHZ") #칠리즈
goldencrossMACD("KRW-GLM") #골렘
goldencrossMACD("KRW-HBAR") #헤데라
goldencrossMACD("KRW-CVC") #시빅
goldencrossMACD("KRW-XLM") #스텔라루멘
goldencrossMACD("KRW-POWR") #파워렛져
goldencrossMACD("KRW-BORA") #보라
goldencrossMACD("KRW-TFUEL") #쎄타퓨엘
goldencrossMACD("KRW-CRO") #크립토닷컴체인
goldencrossMACD("KRW-ARDR") #아더
goldencrossMACD("KRW-AERGO") #아르고
goldencrossMACD("KRW-DOGE") #도지코인
goldencrossMACD("KRW-HUM") #휴먼스케이프
goldencrossMACD("KRW-UPP") #센티넬프로토콜
goldencrossMACD("KRW-XEM") #넴
goldencrossMACD("KRW-MOC") #모스코인
goldencrossMACD("KRW-FCT2") #피르마체인
goldencrossMACD("KRW-VET") #비체인
goldencrossMACD("KRW-DKA") #디카르고
goldencrossMACD("KRW-ANKR") #앵커
goldencrossMACD("KRW-ORBS") #오브스
goldencrossMACD("KRW-STPT") #에스티피
goldencrossMACD("KRW-META") #메타디움
goldencrossMACD("KRW-TRX") #트론
goldencrossMACD("KRW-LOOM") #룸네트워크
goldencrossMACD("KRW-ZIL") #질리카
goldencrossMACD("KRW-SNT") #스테이터스네트워크
goldencrossMACD("KRW-JST") #저스트
goldencrossMACD("KRW-MED") #메디블록
goldencrossMACD("KRW-SSX") #썸씽
