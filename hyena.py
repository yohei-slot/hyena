import streamlit as st
import numpy as np
import pandas as pd
from enum import Enum
import yoshimune_rising

st.title("ハイエナボーダーメモ")
machine = st.selectbox(
    '機種を選択',
    ('機種を選択','L北斗の拳', '沖ドキGOLD', '絆2天膳', '吉宗RISING', 'ヴァルヴレイヴ', 'Lキン肉マン', "モンキーターンV", "バイオヴィレッジ", "マクロスF4", "Lコードギアス")
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

    st.divider()
    st.caption("L北斗の拳、AT、純増4枚/G、天井1268G+α、リセット天井800G+α")

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

        st.divider()
        st.caption("S沖ドキGOLD-30、6.5号機、AT、純増3枚/G、天井999G+α")

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

    st.divider()

    st.markdown("""
                ## 穢れ狙いについて
                天膳BC終了時の穢れ示唆によって打ち分けができます。  \n
                ＊メイン液晶横全部まで点灯：打てない  \n
                ＊リール横点灯：ボーダーを大幅に下げる  \n
                ＊下パネル横まで・下パネル消灯：穢れ開放まで続行  \n
                解放まで時間がかかる場合もありますので、閉店まで4時間以上は確保して狙いましょう。
                """)
    
    st.divider()
    st.caption("Lバジリスク甲賀忍法帖 絆2 天膳BLACK EDITION、AT、純増2.9枚/G、BC天井333G+α、BT天井 BC8回")

def vvv():
    st.header("L 革命機ヴァルヴレイヴ")
    st.write("正確な期待値計算が難しい台のため、安全のため106～107%想定のボーダーを記載します")
    mimizu = st.checkbox("ミミズ", value=False,  help="ミミズ判別は下記参照")
    rbthru = st.radio("決戦ボーナススルー回数", options=(0,1,2,3,4), index=0, horizontal=True)
    czthru = st.radio("CZスルー回数", options=(0,1,2,3,4), index=0, horizontal=True)
    ekisho = st.slider("液晶G数", 0,1000,0,1)
    if not mimizu:

        if rbthru == 0:
            st.write("CZ・ボナ・ATまで打ったのち押し引き")
            if czthru == 0:
                st.subheader("液晶 510G～")
            elif czthru == 1:
                if ekisho <= 300:
                    g = -0.33*ekisho+900
                else:
                    g = -8.889*ekisho+3466.7
                if g < 0:
                    g = 0
                elif g > 1000:
                    g = 1000

            elif czthru == 2:
                if ekisho <= 80:
                    g = -1.625*ekisho+830
                else:
                    g = -8.75*ekisho+1400
                if g < 0:
                    g = 0
                elif g > 1000:
                    g = 1000

            elif czthru == 3:
                g = -9.375*ekisho + 750
                if g < 0:
                    g = 0
                elif g > 1000:
                    g = 1000

            else:
                g = 0

            if czthru != 0:
                st.subheader(f"ボーナス間 {int(g)}G～")

        elif rbthru == 1:
            st.write("CZ・ボナ・ATまで打ったのち押し引き")
            zerocz = st.radio("0スルー時のCZ回数", options=(1,2,3,4,5), index=0, horizontal=True)
            if zerocz == 1:
                if czthru == 0:
                    st.subheader("液晶 320G～")
                elif czthru == 1:
                    g = -4.4444*ekisho + 800
                    if g < 0:
                        g = 0
                    elif g > 1000:
                        g = 1000
                    st.subheader(f"ボーナス間 {int(g)}G～")
                elif czthru == 2:
                    g = -4.375*ekisho + 700
                    if g < 0:
                        g = 0
                    elif g > 1000:
                        g = 1000
                    st.subheader(f"ボーナス間 {int(g)}G～")
                elif czthru == 3:
                    st.subheader("ツッパ")
            elif zerocz == 2:
                if czthru == 0:
                    st.subheader("液晶 200G～")
                elif czthru == 1:
                    g = -4.375*ekisho + 700
                    if g < 0:
                        g = 0
                    elif g > 1000:
                        g = 1000
                    st.subheader(f"ボーナス間 {int(g)}G～")
                elif czthru == 2:
                    g = -10*ekisho + 700
                    if g < 0:
                        g = 0
                    elif g > 1000:
                        g = 1000
                    st.subheader(f"ボーナス間 {int(g)}G～")
                elif czthru == 3:
                    st.subheader("ツッパ")
            elif zerocz == 3:
                if czthru == 0:
                    st.subheader("液晶 180G～")
                elif czthru == 1:
                    g = -7*ekisho + 700
                    if g < 0:
                        g = 0
                    elif g > 1000:
                        g = 1000
                    st.subheader(f"ボーナス間 {int(g)}G～")
                elif czthru >= 2:
                    st.subheader("ツッパ")
            elif zerocz == 4:
                if czthru == 0:
                    st.subheader("液晶 50G～")
                else:
                    st.subheader("ツッパ")
            else:
                st.subheader("ツッパ")

        elif rbthru == 2:
            zerocz = st.radio("0、１スルー時のCZ回数合計", options=(2,3,4), index=0, horizontal=True)
            if zerocz == 2:
                if czthru == 0:
                    g = -3.5*ekisho + 700
                    if g < 0:
                        g = 0
                    elif g > 1000:
                        g = 1000
                    st.subheader(f"ボーナス間 {int(g)}G～")
                elif czthru == 1:
                    g = -8.5714*ekisho + 600
                    if g < 0:
                        g = 0
                    elif g > 1000:
                        g = 1000
                    st.subheader(f"ボーナス間 {int(g)}G～")
                else:
                    st.subheader("ツッパ")

            elif zerocz == 3:
                if czthru == 0:
                    g = -8.125*ekisho + 650
                    if g < 0:
                        g = 0
                    elif g > 1000:
                        g = 1000
                    st.subheader(f"ボーナス間 {int(g)}G～")
                elif czthru == 1:
                    g = -12*ekisho + 600
                    if g < 0:
                        g = 0
                    elif g > 1000:
                        g = 1000
                    st.subheader(f"ボーナス間 {int(g)}G～")
                else:
                    st.subheader("ツッパ")
            else:
                st.subheader("ツッパ")
        else:
            st.subheader("ツッパ")
    
    elif mimizu:
        if rbthru == 0:
            if czthru == 0:
                st.subheader("液晶 210G～")
            elif czthru == 1:
                st.subheader("液晶 70G～")
            else:
                st.subheader("ツッパ")
        elif rbthru == 1:
            if czthru == 0:
                st.subheader("液晶 70G～")
            else:
                st.subheader("ツッパ")
        else:
            st.subheader("ツッパ")

    st.divider()

    st.markdown("""
                ## 辞め時
                非ミミズ時のボーナス後は即やめ（0から打てる状態でなければ）  \n
                非ミミズ時のAT後は引き戻し確認後やめ
                ミミズ時は全て即やめ
                """)
    
    st.markdown("""
                ## ミミズ判別
                1. データカウンター250～400でのCZ当たりが多い（410Gまでに9割）
                2. 一撃で1150枚を超えない
                3. CZがとても成功しやすい（目安9割）
                4. AT後の引き戻しが少ない
                5. RBよりBBに偏る（BB8 : RB2）
                """)
    
    st.divider()
    st.caption("L革命期ヴァルヴレイヴ、AT、純増7.2枚/G、CZ天井液晶1000G+α、ボナ天井実1500G+α、CZスルー天井 8回目、RBスルー天井 5回目")

def niku():
    st.header("スマスロ キン肉マン 7人の悪魔超人編")
    morning = st.checkbox("リセット後 魔界の荒野移行あり", value=False)
    if not morning:
        thru = st.slider("朝一からの初当たり回数",0,14,0,1)
        nikudict = {0:340,1:290,2:250,3:240,4:190,5:170,6:140,7:80,8:0,9:330,10:370,11:370,12:380,13:380,14:380}
        st.subheader(f"狙い目は 液晶{nikudict[thru]}万pts～")
    elif morning:
        st.write("荒野後3回目の当たりまでに75%でSPが来ます。2スルーは状態不問では0G～と甘くなっていますが、前任者が1,2スルー中にSP発動を確認してやめた場合期待値が大きく下がります。")
        thru = st.slider("魔界の荒野後初当たり回数",0,9,0,1)
        nikudict = {0:130,1:80,2:0,3:300,4:250,5:250,6:250,7:250,8:250,9:260}
        st.subheader(f"狙い目は 液晶{nikudict[thru]}万pts～")

    st.write("正義超人チャレンジに700G当たっていない台は正義超人アタック狙いで打てます。（カウンターで前回900G以上ハマっていて現在液晶とデータカウンターのG数が一致している台など）")
    
    st.divider()

    st.markdown("""
                ## メニュー画面示唆
                打てるもの: \nキン肉マン（朝一以外）\nモンゴルマン（前回終了画面との矛盾の場合のみ）\n悪魔将軍（次回SP濃厚）\n謎の悪魔超人(次回SP強)\nバッファローマン(5回以内SP濃厚、バッファローSP示唆)\nステカセキング(5回以内SP中, シナリオSP示唆)\nアシュラマン(5回以内SP濃厚)\nサンシャイン(5回以内SP強)\nミート君(5回以内SP濃厚、シナリオSP示唆)
                """)
    
    st.markdown("""
                ## 終了画面示唆
                打てるもの（復活は無効）：　\nバッファローマン（5回以内SP濃厚、バッファローSP示唆）\n悪魔将軍（次回SP濃厚）
                """)
    
    st.markdown("""
                ## その他
                打てるもの（1回当たるまで）：　\nアイキャッチ赤orモノクロ\nセリフ赤or紫
                """)
    
    st.divider()
    st.caption("Lキン肉マン 7人の悪魔超人編、AT、純増6.1枚/G、天井液晶900G+α")

def monkeyv():
    st.header("スマスロ　モンキーターンV")
    morning = st.checkbox("朝一リセット", value=False)
    reduce = st.checkbox("天井短縮", value=False, help="波多野vs青島敗北後と上位AT後は天井短縮")
    if morning:
        shuki = st.radio("何周期目？", options=("1", "2", "3以上"))
        if shuki == "1":
            st.subheader("データカウンター 40G~優出まで、スルー時は2周期目のボーダーで押し引き")
        elif shuki == "2":
            st.subheader("データカウンター 150G～天井まで")
        else:
            st.subheader("ツッパ")
    
    else:
        if reduce:
            st.subheader("データカウンター 150G～天井まで")
        else:
            st.subheader("データカウンター 410G～を基準に優出ptsや示唆で押し引き")

    st.divider()
    st.caption("LモンキーターンV、AT、下位純増2.5枚/G 上位純増4枚/G、天井795G+α or 6周期目、リセット時・青島バトル敗北後・上位AT終了後は495+α or 4周期目")

def village(): 
    st.header("スマスロ バイオハザード:ヴィレッジ")
    morning = st.checkbox("朝一リセット", value=False, help="設定変更後は天井550Gに短縮")
    if morning:
        st.subheader("天井狙い 70G～")
    else:
        st.subheader("天井狙い 390G～")
        st.subheader("ゾーン狙い 85G～150G（前兆まで）")

    st.divider()

    st.markdown("""## メニュー画面 \n
                175G以降、メニュー画面にクリスがいればボーダーを下げれる。\n赤背景であれば問答無用で打つ。
                """)
    
    st.markdown("""## 辞め時 \n
                CLIMAX7敗北時は即ヤメ \n
                Hazard Rush 終了後は5G程回し即前兆を確認してヤメ
                """)
    
    st.divider()
    st.caption("Lバイオハザード ヴィレッジ、AT、純増2.5枚/G、天井750G+α")

def macrossf4():
    st.header("スマスロ マクロスフロンティア4")
    st.write("このページでは、内部G数が実G数の1.5倍になるものとして算出した狙い目を表示します。もし打ち込んでいる人で、1.5倍ではないと思う方は下の欄を修正して利用してください。")
    factor = st.number_input("内部G数加算率（デフォルト1.5倍）", 1, 3, step=0.01, value=1.5, help="分からなければ触らなくてok")
    morning = st.checkbox("朝一リセット", value=False, help="朝一0スルーは甘い、1・2スルーは辛い")
    thru = st.slider("ボーナススルー回数", 0,6,0,1)
    if not morning:
        if thru == 0:
            g = 540*factor
        elif thru == 1:
            g = 570*factor
        elif thru == 2:
            g = 570*factor
        elif thru == 3:
            g = 650*factor
        elif thru == 4:
            g = 650*factor
        elif thru == 5:
            g = 220*factor
        else:
            g = 0

        st.subheader(f"液晶 {int(g)}G~ 天井まで")
        st.subheader("液晶 480G～500Gのゾーン狙い 前兆終了まで")
        st.caption("500Gのゾーンで前兆が来なければ良いモードなのでそのまま天井まで")

    else:
        if thru == 0:
            g = 210*factor
        elif thru == 1:
            g = 600*factor
        elif thru == 2:
            g = 640*factor
        elif thru == 3:
            g = 660*factor
        elif thru == 4:
            g = 650*factor
        elif thru == 5:
            g = 220*factor
        else:
            g = 0

        st.subheader(f"液晶 {int(g)}G~ 天井まで")

    st.divider()

    st.markdown("""## ヤメ時
                15G程回す \n
                歌即前兆があれば100Gまで回す。\n
                なければヤメ。
                """)
    
    st.divider()
    st.caption("Lマクロスフロンティア4、AT、純増1.5枚/G or 5枚/G、天井液晶1500G+α or 実ゲーム1000G+α、歌姫ボーナス11回目")

def geass():
    st.subheader("スマスロ コードギアス 復活のルルーシュ")
    morning = st.checkbox("朝一リセット", value=False)
    


if st.session_state['machine'] == '機種を選択':
    home()
elif st.session_state['machine'] == 'L北斗の拳':
    hokuto()
elif st.session_state['machine'] == '沖ドキGOLD':
    okidoki_gold()
elif st.session_state['machine'] == '絆2天膳':
    tenzen()
elif st.session_state['machine'] == '吉宗RISING':
    yoshimune_rising.yoshimune_r()
elif st.session_state['machine'] == 'ヴァルヴレイヴ':
    vvv()
elif st.session_state['machine'] == 'Lキン肉マン':
    niku()
elif st.session_state['machine'] == 'モンキーターンV':
    monkeyv()
elif st.session_state['machine'] == "バイオヴィレッジ":
    village()
elif st.session_state['machine'] == "マクロスF4":
    macrossf4()
elif st.session_state['machine'] == "Lコードギアス":
    geass()
else:
    st.header("工事中...")

