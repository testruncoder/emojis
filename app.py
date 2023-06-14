import streamlit as st
import pandas as pd
from emojis_lib import emoji_dict


# -------------------------------------------------------------------------------------------------------------
# Renamed as app.py for deployment to streamlit cloud (6/12/2023)
# # st_JY_smallColorEmojis1.py - Ver1 (6/14, 6/12/2023)
# - Update:
# (1) Upgraded a search feature -- Can search for multiple words with pd;
# (2) Cosmetic updates (6/14/2023);


# -------------------------------------------------------------------------------------------------------------
# st_JY_smallColorEmojis0.py - Ver0 (6/07/2023)
# # (1) Display emojis from a dictionary in # https://pastebin.com/raw/w0z7d5Wh
# # (2) Search by a single word (not multiple words) with pd:
# C:\Users\email\OneDrive\DesktopSP7\py_strm\Ex_st_excel_webapp.py
# https://pastebin.com/raw/w0z7d5Wh
# -------------------------------------------------------------------------------------------------------------
CODE_TITLE='st_JY_smallColorEmojis1.py'
CODE_VER='v 1.0'

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

    with st.sidebar.expander('Source of emojis list:', expanded=False):
    # st.markdown('Source of Emojis List:')
        st.markdown('Updated emojis from:')
        st.markdown('https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json')

    with st.sidebar.expander('How to search in the table',expanded=False):
        st.markdown("""
                Press 'Ctrl' + 'f' or '⌘ Cmd + f' to bring up the search bar in the "Table of Emoji Names".
        """)

    search_emoji=st.text_input('Enter emoji name(s): (Note: case-sensitive)', '',
                            placeholder='Enter search word',
                            help="""You may enter multiple words with commas (,) such as
                                "coffee, sparkles".
                            """
                            )

    # # (1) Convert a str into a list to work with pd.contains() later;
    # # (2) TO DO: If multiple words are entered, a list consists of each word that is separated by a comma (,);
    search_emoji_list=search_emoji.replace(', ',',')  # # Remove a blank space after a comma - Ver1 (6/12/2023);
    search_emoji_list=search_emoji_list.split(',')  # # search_emoji_list=[search_emoji]  <= for a single word;
                            # st.markdown(f'search_emoji_list: {search_emoji_list}')

    # multi_words_mode=True if len(search_emoji_list) > 1 else False
    search_method=st.radio('Choose search method:',
                           ['Exact word', 'Contain word'],
                           index=0,
                           horizontal=True,
                           )
                            # st.subheader('Test Run:')
                            # dfa=pd.DataFrame([0,0,0,0], columns=['A'] )
                            # dfb=pd.DataFrame([0,1,1,0], columns=['A'] )
                            # dfc=dfa+dfb
                            # st.dataframe(dfc)
    st.markdown('')
    if search_emoji != '':
        with st.expander('Search Results:', expanded=True):
            if search_method=='Contain word':
                                        # aaa=[word for word in search_emoji_list]
                                        # bbb=[word for word in list(zip(*list(search_emoji_list)))]
                                        # # bbb=[word for word in list(zip(*[['computer'],['coffee']]))]
                                        # st.markdown(f'aaa: {aaa}')
                                        # st.markdown(f'bbb: {bbb}')
                                        # st.markdown(f'emoji_search_list: {search_emoji_list}')

                st.subheader('Option 1:')  # 'Contain word'  # Ver1 (6/12/2023)
                df_searched=pd.DataFrame()
                for word in search_emoji_list:
                                            # st.markdown(f'word: {word}')
                    df_searched_tmp=df_dict[df_dict['name'].str.contains(word)]
                    df_searched=pd.concat([df_searched, df_searched_tmp])
                                        # df_searched=df_dict[df_dict['name'].str.contains(word) for word in search_emoji_list]
                if df_searched.empty:
                    st.markdown(f'Not found')
                else:
                    st.dataframe(df_searched)

                st.subheader('Option 2: ')  # 'Contain word'  # Ver1 (6/12/2023)
                df_searched=pd.DataFrame()
                for i,search_word in enumerate(search_emoji_list):
                                            # st.markdown(f'search_word: {search_word}')
                    odf=df_dict['name'].apply(lambda sentence: any(word in sentence for word in [search_word]))
                                            # st.markdown('odf:')
                                            # st.dataframe(odf)
                    df_searched_tmp=df_dict[odf]
                    df_searched=pd.concat([df_searched, df_searched_tmp])
                if df_searched.empty:
                    st.markdown(f'Not found')
                else:
                    st.dataframe(df_searched)

            elif search_method=='Exact word':
                # st.subheader('Option 1:')
                df_searched=pd.DataFrame()
                c1,c2,_=st.columns((6,2,10))
                for word in search_emoji_list:
                    # # Option 1-A for "Exact word" --Ver1 (6/12/2023)
                    # c1.markdown(word)
                    # c2.markdown(emoji_dict.get(word))

                    # # Option 1-B for "Exact word" -- Ver1 (6/12/2023)
                    mask_tmp=df_dict['name'].isin([word])
                                            # st.markdown('1st mask:')
                                            # st.dataframe(mask_tmp)
                    df_searched_tmp=df_dict[mask_tmp]
                                            # st.markdown('new mask: ')
                                            # st.dataframe(mask_tmp)
                    df_searched=df_dict[mask_tmp]
                    if df_searched.empty:
                        st.markdown(f'Not found')
                    else:
                        st.dataframe(df_searched)

                # --------------------------------------------------------------------------------------------
                # # This Option 2 finds more results than Option 1 above.
                #  For 'umbrella', Option 1 only finds 'umbrella'.
                #  Option 2 finds multiple results such as 'umbrella_with_rain_drops', 'closed_umbrella',
                #  etc., in addition to 'umbrella'.;
                # ---------------------------------------------------------------------------------------------
                # Disabled 'Option 2' -- Ver1 (6/12/2023)
                st.subheader('Option 2: ')  # 'Exact word'  # Ver1 (6/12/2023)
                df_searched=pd.DataFrame()
                for i, search_word in enumerate(search_emoji_list):
                    odf=df_dict['name'].apply(lambda sentence: all(word in sentence for word in [search_word]))
                    df_searched_tmp=df_dict[odf]
                    df_searched=pd.concat([df_searched,df_searched_tmp])
                if df_searched.empty:
                    st.markdown(f'Not found')
                else:
                    st.dataframe(df_searched)

    col1,col2=st.columns((6,4))
    with col1.expander('List of Emojis', expanded=True):
        c1,c2=st.columns((3,2))
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
