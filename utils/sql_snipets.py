class Comand:
    def where(self, string):
        self._query += f'''
        WHERE
            {string}
        '''

        return self


class Select(Comand):
    def __init__(self, rows=['*']):
        self.rows = rows

        self._query = f'''
        SELECT
            {', '.join(self.rows)}
        FROM
            Timer
        '''


class Delete(Comand):
    def __init__(self):
        super().__init__()
        self._query = '''
        DELETE 
        FROM Timer
        '''


class Update(Comand):
    def __init__(self, update):
        self.update = update

        self._query = f'''
        UPDATE
            Timer
        SET {self.update}
        '''


class Insert:
    def __init__(self, schedule, name, id_group, n_lesson=1):
        self.schedule = schedule
        self.name = name
        self.id_group = id_group
        self.n_lesson = n_lesson

        self._query = f'''
        INSERT INTO
            Timer (schedule, name, n_lesson, id_group)
        VALUES
            ('{self.schedule}', '{self.name}', {self.n_lesson}, {self.id_group})
        '''
        

if __name__ == '__main__':
    test_u = Update('buybu')
    test_i = Insert('', '', 0, 0)
    test_d = Delete().where('id < 0')

    print(test_u._query)
    print(test_i._query)
    print(test_d._query)