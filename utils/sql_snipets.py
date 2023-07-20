def dop_query(func):
    def wrapper(*args, **kwargs):
        query = func(*args, **kwargs)

        if 


def SELECT(rows, where=None):
    query = '''
        SELECT
            schedule
        FROM
            Timer
    ''' 

    if where:
        query += f'''
        WHERE
            {where}'
    '''
        
    return query


def DELETE(where=None):
    query = '''
        DELETE FROM
            Timer
        '''
    
    if where:
        query += f'''
        WHERE
            {where}'
    '''