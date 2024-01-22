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
    ＊このサイトの狙い目は全て20円等価交換105%ボーダーです。　\n
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
    注意事項　\n
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
             このページでは、宿怨チャレンジにその日一度も突入していないデータに絞って集計を行い、狙い目を算定しました。
             当日すでに宿怨チャレンジに突入済みの台は辛くなる可能性が高いのでご注意ください。\n
             ＊宿怨無し差枚とは、宿怨チャレンジがその日一度も発生していない場合の朝からの差枚（前回BC or BT 終わり時点）です。
             """)
    thru = st.radio("BCスルー回数", options=(0,1,2,3,4), index=0, horizontal=True)
    if thru == 4:
        st.subheader("BT当選まで全ツ！")
    
    elif thru == 0:
        diff = st.slider("宿怨無し差枚", -2000,1000,0,1)




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

