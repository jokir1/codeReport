f=open('test.html','w')

studentList=['Josh','Randi','Loosey']

trs=""
for student in studentList:

    trs+=f"""<tr>
      <td>{student}</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    """

html=f"""

<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <table>
        <tr>
            <th>Student</th>
            <th>M</th>
            <th>T</th>
            <th>W</th>
            <th>T</th>
            <th>F</th>
        </tr>
        {trs}
    </table>
  </body>
</html>
"""

f.write(html)
f.close()
