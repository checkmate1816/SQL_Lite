import xlrd
from db_table import db_table
import sys
import copy

file = sys.argv[1]
agenda = xlrd.open_workbook(file)

sh = agenda.sheet_by_index(0)

table = db_table("agenda_table", {"date": "text NOT NULL", "time_start": "text NOT NULL", "time_end": "text NOT NULL",
                                   "if_session": "text NOT NULL", "title": "text NOT NULL", "location": "text",
                                   "description": "text", "speaker": "text", "id": "Integer PRIMARY KEY", "group_id": "Integer", "individual": "text"})
dic_name = ['date', 'time_start', 'time_end', 'if_session', 'title', 'location', 'description', 'speaker', 'id', 'group_id', "individual"]
last_group = 0
id = 0
for rx in range(sh.nrows):
    if rx <= 14:
        continue
    else:
        cur_list = sh.row_values(rx)
        names = cur_list[7].split(';')
        for name in names:
            line = copy.deepcopy(cur_list)
            if line[3] == "Session":
                line.append(id)
                line.append(id)
                line.append(name)
                last_group = id
            else:
                line.append(id)
                line.append(last_group)
                line.append(name)
            id += 1
            in_dic = dict(zip(dic_name, line))
            table.insert(in_dic)


