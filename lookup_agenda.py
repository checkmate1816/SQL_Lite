from db_table import db_table
import sys
import pandas as pd

type = sys.argv[1]
value = ' '.join(sys.argv[2:])
table = db_table("agenda_table", {"date": "text NOT NULL", "time_start": "text NOT NULL", "time_end": "text NOT NULL",
                                   "if_session": "text NOT NULL", "title": "text NOT NULL", "location": "text",
                                   "description": "text", "speaker": "text", "id": "Integer PRIMARY KEY", "group_id": "Integer", "individual":"text"})
if type != 'speaker':
    result = table.select(where = {type: value})
else:
    result = table.select(where = {"individual":value})



final_result = {}
for index in range(0, len(result)):
    if result[index]['if_session'] == 'Sub':
        final_result[result[index]['id']] = result[index]
    else:
        group_id = result[index]['group_id']
        temp = table.select(where = {'group_id': group_id})
        for i in range(0,len(temp)):
            final_result[temp[i]['id']] = temp[i]

result_list = list(final_result.values())
df = pd.DataFrame(result_list, columns = ['date', 'time_start', 'time_end', 'if_session', 'title', 'location', 'description', 'speaker'])
df = df.drop_duplicates()
print(df)
