import streamlit as st
import pandas as pd
from emojis_lib import emoji_dict


# -------------------------------------------------------------------------------------------------------------
# st_JY_smallColorEmojis0.py - Ver0 (6/07/2023)
# # (1) Display emojis from a dictionary in # https://pastebin.com/raw/w0z7d5Wh
# # (2) Search by a single word (not multiple words) with pd:
# C:\Users\email\OneDrive\DesktopSP7\py_strm\Ex_st_excel_webapp.py
# https://pastebin.com/raw/w0z7d5Wh
# -------------------------------------------------------------------------------------------------------------
# CODE_TITLE='st_JY_smallColorEmojis0.py'
CODE_TITLE='Raw Emojis'
CODE_VER='v 0.0'

def main():
    st.title(CODE_TITLE )
    st.caption(CODE_VER)

    # ----------------------------------------------------------------------------------------------------
    # SIDEBAR: DISPLAY THE CODE TITLE
    FYEO=True
    if FYEO==True: 
        my_sidebar_expander00=st.sidebar.expander('Code Title:',expanded=False)
        with my_sidebar_expander00:
            st.write(CODE_TITLE)
    # ----------------------------------------------------------------------------------------------------



    # # Impor an input dictionary that contains emojis;
    df_dict=pd.DataFrame(emoji_dict.items(),columns=['name','emoji'])
                            # df_keys=pd.DataFrame(emoji_dict.keys(),columns=['name'])  # emoji_dict.values()

    with st.sidebar.expander('Table of Emoji Names',expanded=False):
        st.markdown(f'Number of Emojis: {len(df_dict.index)}')
        st.dataframe(df_dict)
                            # aa=emoji_dict['100']
                            # st.markdown(aa)

    with st.sidebar.expander('Source of emojis list:', expanded=False):
    # st.markdown('Source of Emojis List:')
        st.markdown('https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json')


    search_emoji=st.text_input('Enter emoji name', '',
                            placeholder='Enter search word',
                            # help="""You may enter multiple words with commas (,) such as
                            #     "coffee, sparkles".
                            # """
                            )

    # # (1) Convert a str into a list to work with pd.contains() later;
    # # (2) TO DO: If multiple words are entered, a list consists of each word that is separated by a comma (,);
    search_emoji_list=search_emoji.split(',')  # # search_emoji_list=[search_emoji]  <= for a single word;
    # st.markdown(f'search_emoji_list: {search_emoji_list}')

    # multi_words_mode=True if len(search_emoji_list) > 1 else False
    search_method=st.radio('Choose search method',
                           ['Exact word', 'Contain word'],
                           index=0,
                           horizontal=True,
                           )

    if search_emoji != '':
        with st.expander('Search Results:', expanded=True):
            if search_method=='Contain word':
                df_searched=df_dict[df_dict['name'].str.contains(search_emoji)]
                st.dataframe(df_searched)
            elif search_method=='Exact word':
                mask=df_dict['name'].isin(search_emoji_list)
                df_searched=df_dict[mask]
                                        # st.markdown(df_searched)
                st.markdown(emoji_dict.get(search_emoji))

    col1,col2=st.columns((6,4))
    with col1.expander('List of Emojis', expanded=True):
        c1,c2=st.columns(2)
        for (k,v) in emoji_dict.items():
            c1.markdown(k)
            c2.markdown(v)

    with col2.expander('Montage of Emojis', expanded=True):
        c1,c2,c3,c4,c5=st.columns(5)
        colNum=5
        i=0
        for (k,v) in emoji_dict.items():
            if i % colNum == 0:
                c1.markdown(v)
            elif i % colNum == 1:
                c2.markdown(v)
            elif i % colNum == 2:
                c3.markdown(v)
            elif i % colNum == 3:
                c4.markdown(v)
            elif i % colNum == 4:
                c5.markdown(v)
            i += 1
# -------------------------------- END OF main() ----------------------------------

if __name__=='__main__':
    st.set_page_config(
                page_title='Emojis',
                # page_icon=icon,
                layout='centered',  # 'wide'
                initial_sidebar_state='auto',  # 'auto', 'expanded', 'collapsed'
        )
    # # Hide hamburger menu and stremalit footer
    hide_streamlit_style=""" <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .css-hi6a2p {padding-top: 2rem;}
    </style>        
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    main()
    for i in range(15):
        st.sidebar.markdown('')
        st.markdown('')
# -------------------------------- END OF CODE --------------------------------------
