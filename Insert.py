import pymysql

REGION = 'us-east-2c'


rds_host  = "dbtestdetails.clq0t3efda7a.us-east-2.rds.amazonaws.com"
name = "test12345"
password = "example12345"
db_name = "Financials"

def save_events(event):
  
    try:
        result = []
        conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
        with conn.cursor() as cur:
            cur.execute("""insert into UserFinancials_one (NAME, FD_AMT) values( '%s', %s)""" % (event['NAME'], event['FD_AMT']))
            #cur.execute("""select * from UserFinancials""")
            conn.commit()
            cur.close()
     
    except Exception, e:
        raise e
            
def main(event, context):
    save_events(event)
        