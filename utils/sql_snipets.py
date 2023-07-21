class Comand:
    def where(self, string):
        self.__query += f'''
        WHERE
            {string}
        '''

        return self
    

class GetQuery:
    def get_query(self):
        return self.__dict__[list(self.__dict__.keys())[-1]]


class Select(Comand, GetQuery):
    def __init__(self, rows=['*']):
        self.rows = rows

        self.__query = f'''
        SELECT
            {', '.join(self.rows)}
        FROM
            Timer
        '''


class Update(Comand, GetQuery):
    def __init__(self, update):
        self.update = update

        self.__query = f'''
        UPDATE
            Timer
        SET {self.update}
        '''


class Insert(GetQuery):
    def __init__(self, schedule, name, id_group, n_lesson=1):
        self.schedule = schedule
        self.name = name
        self.id_group = id_group
        self.n_lesson = n_lesson

        self.__query = f'''
        INSERT INTO
            Timer (schedule, name, n_lesson, id_group)
        VALUES
            ('{self.schedule}', '{self.name}', {self.n_lesson}, {self.id_group})
        '''
        
if __name__ == '__main__':
    test_u = Update('buybu')
    test_i = Insert('', '', 0, 0)

    print(test_u.get_query())
    print(test_i.get_query())