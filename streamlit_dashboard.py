# Import Required Libraries
import streamlit as st

# Set the streamlit page layout to wide (reduces padding on the sides, makes page responsive)
st.set_page_config(layout="wide")

def main():

    # Render the grid and the contents for the Streamlit dashboard
    # See https://docs.streamlit.io/library/api-reference/layout
    
    ######################## Row A ##############################
    a1, a2 = st.columns((2,8))
    with a1:
        st.image('images/1.png')
    with a2:
        st.markdown('# Elon Musk Tweet Analysis')
    
    # Insert a spacer
    st.markdown('#')

    ######################## Row B ##############################
    st.header('Analysis of Elon Musk Tweets')
    b1, b2 = st.columns(2)
    
#     # Pull the data for Row B charts
#     data = create_nft_market_vol()
#     with b1:
#         plost.line_chart(
#             data = data,
#             x = 'Date',
#             y = 'Volume in ETH',
#             title = 'First Chart',
#             color = 'green',
#             width = 500,
#             height = 300,
#         )        
#         with st.expander("See analysis"):
#             st.write("""This chart shows ...""")

#     data = create_os_collection_index()
#     with b2:
#         plost.line_chart(
#             data = data,
#             x = 'Date',
#             y = 'Second Chart',
#             title = "Open Sea's Top Ten Collections Volume Traded",
#             color = 'blue',
#             width = 500,
#             height = 300,
#         )
#         with st.expander("See analysis"):
#             st.write("""This chart shows ...""") 
    
#     # Insert a spacer
#     st.markdown('#')

# Call main function for program            
if __name__ == "__main__":
    # calling main function
    main()
