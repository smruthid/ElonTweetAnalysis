# Import Required Libraries
import streamlit as st

# Set the streamlit page layout to wide (reduces padding on the sides, makes page responsive)
st.set_page_config(layout="wide")

def main():

    # Render the grid and the contents for the Streamlit dashboard
    # See https://docs.streamlit.io/library/api-reference/layout
    
    ######################## Row A ##############################
    st.image('images/1.png')     
    
    # Insert a spacer
    st.markdown('#')

    ######################## Row B ##############################
    st.header('TSLA Trading Strategy')
    b1, b2 = st.columns((8,2))
    
    # Pull the data for Row B charts
    with b1:
        st.image('images/tsla_trading_strategy.png')
        with st.expander("See analysis"):
            st.write("""Using the Twitter Signal and Mean Reversion signal to conduct our trades for TSLA were less effective than longing TSLA over the same time period.""")

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
