from tinydb import Query


def command_called(table, command, user, server):
    command_db_entry = Query()
    entry = table.get(command_db_entry.name == command)
    if not entry:
        doc_id = table.insert({'name': command, 'invoked': 1})
        entry = table.get(doc_id=doc_id)
    else:
        invoked = entry['invoked']
        
        table.update({'invoked': invoked+1}, doc_ids=[entry.doc_id])
    
