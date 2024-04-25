import streamlit as st

# mysql 연결(접속)
conn = st.connection('shopDB',
              type='sql',
              url='mysql://streamlit:1234@localhost:3306/shopDB')

# 질의 수행
df = conn.query('SELECT * FROM customer;', ttl=600)
st.write(df)

for row in df.itertuples():
    st.write(f'{row.customer_name}의 전화번호는 {row.phone}이다. :phone:')

# sql = '''INSERT INTO customer (customer_id, customer_name, phone, birthday)
#         values (:id,:name, :phone, :birth);
#         '''
# with conn.session as s:
#     s.execute(sql, {'id':6,'name':"홍길동", 'phone':"010-1234-4321", 'birth':"1596-01-01"})
#     s.commit()

# df = conn.query('SELECT * FROM customer;', ttl=600)
# st.write(df)

##############################################################
