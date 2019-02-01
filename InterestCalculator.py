import pymysql

rds_host  = "dbtestdetails.clq0t3efda7a.us-east-2.rds.amazonaws.com"
name = "test12345"
password = "example12345"
db_name = "Financials"

def calculate():
    
    cnxn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    conn = cnxn.cursor()
    conn.execute("""SELECT NAME,FD_AMT,time_to_sec(timediff(CURRENT_TIMESTAMP,BUY_DT))/3600,ID FROM UserFinancials_one""")
    for row in conn.fetchall():
        if int(row[1]) >= 100:
            ROI=0.05
        elif int(row[1]) < 100 and int(row[1]) >= 50:
            ROI=0.04
        else:
            ROI=0.03
        HOUR = float(row[2])
        TAMT = float(row[1])+(float(ROI)*HOUR)
        FAMT = str(TAMT)
        I = str(ROI)
        USERID = str(row[3])
        conn.execute("""UPDATE UserFinancials_one SET ROI=%s,TOTAL_AMT=%s WHERE ID=%s""" , (I,FAMT,USERID))
        cnxn.commit()
    conn.close()

def main(event,context):
    calculate()