f=open('test.html','w')

studentList=['Josh','Randi','Loosey']

trs=""
for student in studentList:

    trs+=f"<tr><td>{student}</td></tr>\n"

html=f"""

<style>
table {{
    border-collapse:separate;
    border:solid black 1px;
    border-radius:6px;
}}

td, th {{
    border-left:solid #AFAFAF 1px;
    border-top:solid #AFAFAF 1px;
    border-color: #AFAFAF;

}}

th {{
    border-top: none;
}}

td:first-child, th:first-child {{
     border-left: none;
}}
</style>

<table>
    <tr>
        <th>Student</th>
        <th>Mon</th>
        <th>Tue</th>
        <th>Wed</th>
        <th>Thur</th>
        <th>Fri</th>
    </tr>
        {trs}
</table>
"""

f.write(html)
f.close()
