import os

search = "file"
replace = "document"
type_filter =".py"

dir_content = os.listdir('.')
docs = [doc for doc in dir_content if os.path.isfile(doc)]
renamed = 0

print(f"{len(docs)} of {len(dir_content)} elements are files")

for doc in docs:
    doc_name,file_type = os.path.splitext(doc)

    if file_type == type_filter:
        if search in doc:
            new_name = doc.replace(search, replace)
            os.rename(doc,new_name)
            renamed += 1

            print(f"Renamed file {doc} to {new_name}")
print(f"Renamed {renamed} of {len(docs)} files")