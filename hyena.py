import streamlit as st
import numpy as np
import pandas as pd
from enum import Enum

st.title("ハイエナボーダーメモ")
machine = st.selectbox(
    '機種を選択',
    ('機種を選択','L北斗の拳', '沖ドキGOLD', '絆2天膳', '吉宗ライジング', 'ヴァルヴレイヴ', 'からくりサーカス', '甲鉄城のカバネリ', '戦国乙女4', 'L大工の源さん', 'モンキーターンV')
)

st.session_state['machine'] = machine

def home():
    st.markdown("""
    ## 注意事項
    ＊このサイトの狙い目は全て20円等価交換105%ボーダーです。 \n
    ＊閉店減算は考慮されていません。 \n
    ＊作者が収集したデータを基に、独自に算出した狙い目です。参考にする際は自己責任で。
    """)

def hokuto():
    st.header("スマスロ北斗の拳")
    reset = st.radio("リセット状態", options=("朝一以外", "朝一", "朝二"), horizontal=True)
    if reset == "朝一以外":
        before = st.radio("前回あたりの一撃獲得枚数", options=("799枚以下", "800枚〜1299枚", "1300枚以上"), horizontal=True)
        if before == "799枚以下":
            samai = st.slider("直近1600G差枚", -1500, 1500, 0, 1)
            neraime = int(samai*0.1158+490)
            st.subheader(f"狙い目は {neraime}G")

        elif before == "800枚〜1299枚":
            st.write("＊直近の差枚がマイナスでも、前回ATで一撃大量獲得した場合は辛くなります \n \n")
            st.subheader("狙い目は 600G")
        
        elif before == "1300枚以上":
            st.write("＊直近の差枚がマイナスでも、前回ATで一撃大量獲得した場合は辛くなります \n \n")
            st.subheader("狙い目は 650G")

    elif reset == "朝一":
        st.write("＊リセット時は天井が800G+前兆に短縮 \n \n")
        st.subheader("狙い目は 80G")

    elif reset == "朝二":
        st.write("＊朝二はデータ上甘めになっています。 \n \n")
        samai = st.slider("前回差枚", -750, 1000, 0, 1)
        neraime = int(samai*0.2312+400)
        st.subheader(f"狙い目は{neraime}G")
    st.write("\n")
    st.write("\n")

    st.markdown("""
    注意事項 \n
    ＊狙い目は内部状態不問で立てています。落ちている台は地獄の可能性が高くなるので、表記されたG数より少し深めから打ちましょう。 \n
    ＊逆に、通常以上の可能性が上がる台（マミヤ同行・ジャギステ・北斗カウンター点灯など）は少し浅めに狙えます。 \n
    ＊スイカを溢さないように！溢す人は深めから狙いましょう。
    """)

def okidoki_gold():
    st.header("沖ドキGOLD")
    st.markdown("""この台は有利区間が切れるタイミングがよくわかりません。
                このページでは、一撃1000枚以上後 or 有利2000G後のボナ後に切れるものとした狙い目を記します。
                狙い目表にある有利区間G数とは、前回のボーナス終了時点での有利区間G消化数のこと（ボーナス中含む、疑似遊戯は除く）です。
                32G以内の連荘が含まれる履歴の場合はマタギ狙いの狙い目を参考にしてください。""")
    st.write(" ")

    select = st.radio("状況を選択", options=("朝一以外","朝一","マタギ狙い"), index=0, horizontal=True)

    
    if select == "朝一以外":
        thru = st.slider("スルー回数",0,5,0,1)
        if thru == 0:
            st.write("狙い目:")
            st.subheader("700G～（天井狙い）")
            st.subheader("100～130G（ゾーン狙い）")
            st.subheader("390～402G（ゾーン狙い）")

        elif thru == 1:
            st.write("有利区間G数：狙い目")
            st.subheader("不問：580G")
            st.subheader("1090G：500G")
            st.subheader("1200G：400G")
            st.subheader("1310G：300G")
            st.subheader("1260G：250G")

        elif thru == 2:
            st.write("有利区間G数：狙い目")
            st.subheader("不問：550G")
            st.subheader("750G：500G")
            st.subheader("860G：400G")
            st.subheader("970G：300G")
            st.subheader("1080G：200G")
            st.subheader("1090G：100G")
            st.subheader("1280G：32G")

        elif thru == 3:
            st.write("有利区間G数：狙い目")
            st.subheader("不問：300G")
            st.subheader("950G：200G")
            st.subheader("1060G：100G")
            st.subheader("1150G：32G")

        elif thru == 4:
            st.write("有利区間G数：狙い目")
            st.subheader("不問：200G")
            st.subheader("990G：100G")
            st.subheader("1080G：32G")

        elif thru == 5:
            st.subheader("天国or有利切れまで全ツ！")



    elif select == "朝一":
        thru = st.slider("スルー回数",0,5,0,1)
        if thru == 0:
            st.write("狙い目:")
            st.subheader("650G～（天井狙い）")
            st.subheader("0～32G（ゾーン狙い）")
            st.subheader("100～130G（ゾーン狙い）")
            st.subheader("360～403G（ゾーン狙い）")
        
        elif thru == 1:
            gbefore = st.radio("0スの当選G数", options=("32G以下", "33～149G", "150G以上"), index=0, horizontal=True)
            if gbefore == "32G以下":
                st.write("狙い目:")
                st.subheader("420G")      
            elif gbefore == "33～149G":
                st.write("狙い目:")
                st.subheader("440G")
            elif gbefore == "150G以上":
                st.write("有利区間G数：狙い目")
                st.subheader("不問：510G")
                st.subheader("1150G：400G")
                st.subheader("1260G：300G")
                st.subheader("1310G：250G")

        elif thru == 2:
            gbefore = st.radio("1スの当選G数", options=("149G以下", "150G以上"), index=0, horizontal=True)
            if gbefore == "149G以下":
                st.write("有利区間G数：狙い目")
                st.subheader("不問：270G")
                st.subheader("1040G：200G")
                st.subheader("1160G：100G")
                st.subheader("1250G：32G")
            
            elif gbefore == "150G以上":
                st.write("有利区間G数：狙い目")
                st.subheader("900G：400G")
                st.subheader("1050G：300G")
                st.subheader("1210G：200G")
                st.subheader("1290G：100G")
                st.subheader("1380G：32G")

        elif thru == 3:
            gbefore = st.radio("1スの当選G数", options=("149G以下", "150G以上"), index=0, horizontal=True)
            if gbefore == "149G以下":
                st.write("有利区間G数：狙い目")
                st.subheader("不問：200G")
                st.subheader("960G：100G")
                st.subheader("1050G：32G")
            
            elif gbefore == "150G以上":
                st.write("有利区間G数：狙い目")
                st.subheader("不問：300G")
                st.subheader("940G：200G")
                st.subheader("1060G：100G")
                st.subheader("1180G：32G")

        elif thru == 4:
            st.write("有利区間G数：狙い目")
            st.subheader("不問：200G")
            st.subheader("810G：100G")
            st.subheader("900G：32G")
        
        elif thru == 5:
            st.subheader("天国or有利切れまで全ツ！")
       
    elif select == "マタギ狙い":
        matagi = st.text_input("33G以上は0, 32以下は1で入力。", "0100")
        mtype = st.radio("「1」のゲーム数",("1～11G","12G～32G"), horizontal=True, args=[1,0] )
        if mtype == "1～11G":
            mtype = '1'
        else:
            mtype = '0'
        st.table(pd.read_csv(f'./okigold_data/okigold_matagi{mtype}_{matagi}.csv'))

        st.markdown(""" ## マタギ狙いの注意点
        ＊有利頭から現在の状態まで数えて、有利切れたらヤメ。 \n
        ＊「1」スタートで数えるのは危険
        ＊ダブルマタギは危険なので触らない。例：001010
        """)

def tenzen():
    st.header("バジリスク絆2 天膳BLACK")
    st.write("""有利切れの恩恵が強い台なので、有利差枚が浮いている台ほど期待値が高くなります。
             有利区間切れ条件は、有利差枚+1000枚以上です。穢れ契機の宿怨チャレンジでは切れないものと予想されます。
             宿怨チャレンジ突入の際は、8G以上のBT直撃履歴が残ります。
             有利切れ条件を満たさずに宿怨ループをしている台については有利切れが不明なので、ここでは狙い目を記載しません。狙う際は十分注意してください。
             """)

    morning = st.radio("リセ状態", options=("朝一以外", "朝一"), index=0, horizontal=True)
    thru = st.radio("BCスルー回数", options=(0,1,2,3,4), index=0, horizontal=True)
    shukuen = st.radio("当該有利区間にて、穢れ契機による宿怨チャレンジ履歴が", options=("あり","なし" ))
    if morning == "朝一以外":
        if thru == 4:
            st.subheader("BT当選まで全ツ!")
        
        elif thru == 0:
            if shukuen == "あり":
                diff = st.slider("有利差枚(前回BC終了時時点)", -1500,1000,0,1)
                g  = 237.437621 - 0.0188185767*diff - 1.03004925**(diff/4.14118384)
                if diff <= -1500:
                    g = 270
                if g <= 0:
                    g = 0
                st.subheader(f"狙い目は: {int(g)}G")

            elif shukuen == "なし":
                diff = st.slider("有利差枚(前回BC終了時時点)", 0,1000,0,1)
                g = 253 - 0.00779891544*diff - 1.00968813**(diff/1.32165226)
                if diff <= 100:
                    g = 250
                if g < 0:
                    g = 0
                st.subheader(f"狙い目は: {int(g)}G")


        elif thru == 1:
            if shukuen == "あり":
                samai = st.slider("有利差枚(前回BC終了時時点)", -4500,1000,0,1)
                btg = st.slider("0スのG数", 0,333,0,1)
                g = 185.84031 - 0.0332579531*samai - 0.281781894*btg - 0.000899453468*btg*btg + 4.73745084*samai*btg/100000 - 1.02226623**(samai/3.78449473)
                if g <= 0:
                    g = 0
                elif g >= 333:
                    g = 333
                
                st.subheader(f"狙い目は: {int(g)}G")

            elif shukuen == "なし":
                samai = st.slider("有利差枚(前回BC終了時時点)", -4500,1000,0,1)
                btg = st.slider("0スのG数", 0,333,0,1)
                g = 220.50933 - 0.059265*samai - 0.267112137*btg - 0.001060607*btg*btg + 0.0002073843*samai*btg/100000 - 1.7326**(samai/84.0124)
                if g <= 0:
                    g = 0
                elif g >= 333:
                    g = 333
                
                st.subheader(f"狙い目は: {int(g)}G")

        elif thru == 2:
            if shukuen == "あり":
                samai = st.slider("有利差枚(前回BC終了時時点)", -4500,1000,0,1)
                btg = st.slider("BT間G数(前回BC終了時時点)", 0,666,0,1)
                g = 141 - 0.0332579531*samai - 0.281781894*btg - 0.000899453468*btg*btg + 4.73745084*samai*btg/100000 - 1.02226623**(samai/3.78449473)
                if g <= 0:
                    g = 0
                elif g >= 333:
                    g = 333
                
                st.subheader(f"狙い目は: {int(g)}G")

            elif shukuen == "なし":
                samai = st.slider("有利差枚(前回BC終了時時点)", -4500,1000,0,1)
                btg = st.slider("BT間G数(前回BC終了時時点)", 0,666,0,1)
                g = 180.50933 - 0.059265*samai - 0.267112137*btg - 0.001060607*btg*btg + 0.0002073843*samai*btg/100000 - 1.7326**(samai/84.0124)
                if g <= 0:
                    g = 0
                elif g >= 333:
                    g = 333

                st.subheader(f"狙い目は: {int(g)}G")

        elif thru == 3:
            if shukuen == "あり":
                samai = st.slider("有利差枚(前回BC終了時時点)", -4500,1000,0,1)
                btg = st.slider("BT間G数(前回BC終了時時点)", 0,666,0,1)
                g = 60 - 0.0332579531*samai - 0.281781894*btg - 0.000899453468*btg*btg + 4.73745084*samai*btg/100000 - 1.02226623**(samai/3.78449473)
                if g <= 0:
                    g = 0
                elif g >= 333:
                    g = 333

                st.subheader(f"狙い目は: {int(g)}G")

            elif shukuen == "なし":
                samai = st.slider("有利差枚(前回BC終了時時点)", -4500,1000,0,1)
                btg = st.slider("BT間G数(前回BC終了時時点)", 0,666,0,1)
                g = 180.50933 - 0.059265*samai - 0.267112137*btg - 0.001060607*btg*btg + 0.0002073843*samai*btg/100000 - 1.7326**((samai+2300)/84.0124)
                if g <= 0:
                    g = 0
                elif g >= 333:
                    g = 333
                if btg <= 100:
                    if g > 100:
                        g = 100

                st.subheader(f"狙い目は: {int(g)}G")

    elif morning == "朝一":
        if thru == 0:
            st.subheader("狙い目は: 260G")

        elif thru == 1:
            btg = st.slider("BT間G数(前回BC終了時時点)", 0,333,0,1)
            g = -0.0023*btg**2 + 0.0276*btg + 254.5
            if g <= 0:
                g = 0
            elif g >= 333:
                g = 333
        
            st.subheader(f"狙い目は: {int(g)}G")

        elif thru == 2:
            btg = st.slider("BT間G数(前回BC終了時時点)", 0,666,0,1)
            g = -0.96*btg + 289.5
            if g <= 0:
                g = 0
            elif g >= 333:
                g = 333
            
            st.subheader(f"狙い目は: {int(g)}G")

    st.markdown("""
                ## 穢れ狙いについて
                天膳BC終了時の穢れ示唆によって打ち分けができます。  \n
                ＊メイン液晶横全部まで点灯：打てない  \n
                ＊リール横点灯：ボーダーを大幅に下げる  \n
                ＊下パネル横まで・下パネル消灯：穢れ開放まで続行  \n
                解放まで時間がかかる場合もありますので、閉店まで4時間以上は確保して狙いましょう。
                """)






if st.session_state['machine'] == 'L北斗の拳':
    hokuto()
elif st.session_state['machine'] == '機種を選択':
    home()
elif st.session_state['machine'] == '沖ドキGOLD':
    okidoki_gold()
elif st.session_state['machine'] == '絆2天膳':
    tenzen()
else:
    st.header("工事中...")

