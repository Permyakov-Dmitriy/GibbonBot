from dataclasses import dataclass


@dataclass
class Comand:
    '''TODO удалить'''
    def where(self, string):
        self.query += f'''
    WHERE
        {string}
        '''

        return self


@dataclass
class Select(Comand):
    '''TODO удалить'''
    rows: list[str] = ('*',)

    query: str = f'''
    SELECT
        {', '.join(rows)}
    FROM
        Timer
    '''

@dataclass
class Update(Comand):
    '''TODO удалить'''
    st: str

    query: str = f'''
    UPDATE
        Timer
    SET {self.st}
    '''


class Insert:
    def __init__(self, schedule, name, id_group, n_lesson=1, *args, **kwargs):
        self.schedule = schedule
        self.name = name
        self.id_group = id_group
        self.n_lesson = n_lesson

        self.query = f'''
        INSERT INTO
            Timer (schedule, name, n_lesson, id_group)
        VALUES
            ('{self.schedule}', '{self.name}', {self.n_lesson}, {self.id_group})
            '''
        
if __name__ == '__main__':
    test_u = Update('buybu')

    print(test_u.query)