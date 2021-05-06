import streamlit as st

# פונקציה המהזירה אות בשיטת אתבש
def atbash(ot):
    alephbet = 'אבגדהוזחטיכלמנסעפצקרשת'
    
    mikum = alephbet.find(ot)
    mikum_hafuh = -mikum - 1
    return alephbet[mikum_hafuh]


mila = st.text_input('כתוב מילה: ')

#for ot in mila:             # עוברים על כל אות במילה שהמשתמש הקליד כתגובה ל-input
#    print( atbash(ot) )

mila_atbash = [atbash(ot) for ot in mila]
mila_atbash = ''.join(mila_atbash)
st.write(mila_atbash)
