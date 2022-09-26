from reports.tables import StandardTable

students=['Vernon Magar', 'Laurence Adragna', 'Jami Wright', 'Matthew Lewis', 'Kim Torrez',
        'Betty Kleinman', 'Frank Gomez', 'Martin Salvato', 'Andy Goodwin', 'Shannon Smyth',
        'Robert Crouch', 'George Froelich', 'James Brown', 'Michael Vandyke', 'Dorothy Oyler',
        'Karl Cavanaugh', 'Joan Walls', 'Jerry Willardson', 'Dennis Olson', 'Susan Rodriguez',
        'Catherine Robinson', 'Hillary Baker', 'Rosa Hoang', 'Gerald Lary', 'Laurie Pree']

t=StandardTable(students)

t.createPDF('test.pdf')
