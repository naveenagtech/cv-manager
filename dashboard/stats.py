import sqlite3
from db_manager.query import dictfetchall
from db_manager import DB
from db_manager.query import (
    SELECT_ALL_QUERY,
    SELECT_VALIDATED_QUERY,
    SELECT_NOT_VALIDATED_QUERY,
    SELECT_PIE_DATA
)

def stats():

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(SELECT_ALL_QUERY)
    total = dictfetchall(cursor)
    cursor.execute(SELECT_VALIDATED_QUERY)
    completed = dictfetchall(cursor)
    cursor.execute(SELECT_NOT_VALIDATED_QUERY)
    pending = dictfetchall(cursor)

    response = {"total": 0, "pending": 0, "completed": 0}
    if len(total) > 0:
        response.update({"total": total[0]['total']})
    if len(pending) > 0:
        response.update({"pending": pending[0]['pending']})
    if len(completed) > 0:
        response.update({"completed": completed[0]['completed']})
    
    return response

def get_pie():

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(SELECT_PIE_DATA)
    total = dictfetchall(cursor)

    labels = []
    data = []
    for i in total:
        data.append(i['total'])
        labels.append(i['name'])
    return data, labels