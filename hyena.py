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
            st.title(f"狙い目は {neraime}G")

        elif before == "800枚〜1299枚":
            st.write("＊直近の差枚がマイナスでも、前回ATで一撃大量獲得した場合は辛くなります \n \n")
            st.title("狙い目は 600G")
        
        elif before == "1300枚以上":
            st.write("＊直近の差枚がマイナスでも、前回ATで一撃大量獲得した場合は辛くなります \n \n")
            st.title("狙い目は 650G")

    elif reset == "朝一":
        st.write("＊リセット時は天井が800G+前兆に短縮 \n \n")
        st.title("狙い目は 80G")

    elif reset == "朝二":
        st.write("＊朝二はデータ上甘めになっています。 \n \n")
        samai = st.slider("前回差枚", -750, 1000, 0, 1)
        neraime = int(samai*0.2312+400)
        st.title(f"狙い目は{neraime}G")
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
    st.markdown("この台は有利区間が切れるタイミングがよくわかりません。このページでは、一撃1000枚以上後 or 有利2000G後のボナ後に切れるものとした狙い目を記します。実際に有利区間をカウントするときは、32G以内の連荘後は全て有利が切れているものと仮定して数えてください。32G以内の連荘が含まれる履歴の場合はマタギ狙いの狙い目を参考にしてください。")
    st.write(" ")

    select = st.radio("状況を選択", options=("朝一以外","朝一","マタギ狙い"), index=0, horizontal=True)

    if select != "マタギ狙い":
        thru = st.slider("スルー回数",0,5,0,1)
    
    if select == "朝一以外":
        normal = pd.read_csv(f'./okigold_data/okigold_normal{thru}.csv')
        st.table(normal)
    elif select == "朝一":
        st.table(pd.read_csv(f'./okigold_data/okigold_morning{thru}.csv'))
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

