import configparser as ct
import snowflake.connector
devenvironment='dev'
conf=ct.RawConfigParser()
conf.read('./resources/config.cfg')
username=conf.get(devenvironment,'snowflakeuser')
sfpassword=conf.get(devenvironment,'password')
sfhost=conf.get(devenvironment,'host')
dbconnection = snowflake.connector.connect(user=username,
                                           password=sfpassword,
                                           host=sfhost,
                                           account=sfhost.replace(".snowflakecomputing.com",""))

cur=dbconnection.cursor()
try:
    cur.execute('select current_version()')
    outputrow=cur.fetchone()
    print(outputrow)
    cur.execute('select * from snowflake_sample_data.tpch_sf1.customer limit 100')
    outputrow = cur.fetchall()
    for row in outputrow:
        print(row[0],row[1])

finally:
    cur.close()
dbconnection.close()
