"""
    Discord : Thibô#0001
    Author : Cheneviere Thibault
    Mail : thibault.cheneviere@telecomnancy.eu
    Date : 10/02/2021
"""

# Import personal modules
from python.database.connectDatabase import connectDatabase


if __name__ == "__main__":
    db, cursor = connectDatabase()
    
    # Script for the database
    query = '''
    
    '''

    cursor.executescript(query)
    db.commit()
    db.close()