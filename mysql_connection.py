import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
            host = 'yh.cpos3ccatavx.ap-northeast-2.rds.amazonaws.com',
            database = 'TeamUzoo',
            user = 'team_uzoo_user',
            password = 'gkswogns12')

# create user 'team_uzoo_user'@'%' identified by 'gkswogns12';
# grant all on TeamUzoo.* to 'team_uzoo_user'@'%';
    
    return connection