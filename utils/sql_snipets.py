from dataclasses import dataclass, field

@dataclass
class Comand:
    query: str

    def where(self, string):
        self.query += f'''
    WHERE
        {string}
        '''

        return self


@dataclass
class Select(Comand):
    rows: list[str] = ('*',)
    
    query: str = f'''
    SELECT
        {', '.join(rows)}
    FROM
        Timer
    '''

@dataclass
class Update(Comand):
    query: str = f'''
    UPDATE
        Timer
    SET {set}
    '''
    set: str


@dataclass
class Delete(Comand):
    query: str = '''
    DELETE 
    FROM
        Timer
    '''


@dataclass
class Insert:
    schedule: str = ''
    name: str = ''
    id_group: int = 0
    n_lesson: int = 1

    query: str = f'''
    INSERT INTO
        Timer (schedule, name, n_lesson, id_group)
    VALUES
        ('{schedule}', '{name}', {n_lesson}, {id_group})
        '''
    
