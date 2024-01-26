#yoshimune_rising.py
import streamlit as st

def one_two():
    bonusG = st.slider("ボーナス間G数", 0,800,0,1)
    G = -0.3527*bonusG + 671.1
    if bonusG >= G:
        st.subheader("ボーナスまで打ち切り")
    else:
        st.subheader(f"狙い目: AT間{int(G)}")

def yoshimune_r():
    st.title("スマスロ　吉宗RISING")
    morning = st.checkbox("朝一", value=False )
    reduce = st.checkbox("天井短縮", value=False, disabled=morning, help="前回AT単発で短縮")
    if morning:
        st.subheader("狙い目は 220G")
        st.caption("AT間のG数。ATまで打ち切り")

    else:
        if reduce:
            st.subheader("狙い目は 140G")
            st.caption("AT間のG数。ATまで打ち切り")

        else:
            thru = st.slider("RBスルー回数",0,4,0,1)
            if thru == 0:
                st.subheader("ゾーン狙い: 85〜250G+前兆")
                st.caption("150GのゾーンでRB当選でAT非当選の場合、AT間240Gから拾い直し")
                st.caption("ゾーン狙いは非短縮時のみ!!")
                st.subheader("天井狙い: 520G~")

            elif thru == 1:
                one_two()

            elif thru == 2:
                one_two()

            elif thru == 3:
                bonusG = st.slider("ボーナス間G数", 0,800,0,1)
                G = -0.3527*bonusG + 671.1
                if bonusG >= G:
                    st.subheader("ATまで全ツ!")
                else:
                    st.subheader(f"狙い目: AT間{int(G)}")

            elif thru == 4:
                st.subheader("ATまで全ツ!")


    st.divider()

    st.markdown("""
    ## そのほか注意事項
    ＊やめ時：ボナ後は前兆確認してやめ、AT後は1G連確認の上即やめ。 \n
    ＊G数の前兆はかなり引っ張られるケースあり。 \n
    ＊同行キャラ：二人いたら不問で消えるまで打てる。一人しかいない場合はボーダーちょい下げ（あまり気にしなくてよし） \n
    ＊穢れ：保有示唆 中・強 と 獲得示唆 強 の場合は解放まで打つ \n
    ＊ライジングポイント：基本わからない。リプレイで800p示唆が出ればATまで打つ
    """)