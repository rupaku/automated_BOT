import os
import argparse

parser = argparse.ArgumentParser(description="Batch rename files in dir")

parser.add_argument("search",type=str, help="To be replaced text")

parser.add_argument("replace",type=str,help="Text to be used for replacement")

parser.add_argument(
    "--filetype",
    type=str,
    default=None,
    help="Only files with the given type will be renamed"
)

parser.add_argument(
    "--path",
    type=str,
    default=".",
    help="Directory path that contains file to be renamed"
)

args = parser.parse_args()
print(args)

search = args.search
replace = args.replace
type_filter =args.filetype
path= args.path

print(f"Renaming file at path {path}")

dir_content = os.listdir(path)
path_dir_content = [os.path.join(path,doc) for doc in dir_content]
docs = [doc for doc in dir_content if os.path.isfile(doc)]
renamed = 0

print(f"{len(docs)} of {len(dir_content)} elements are files")

for doc in docs:
    #separate name from ext
    full_doc_path,file_type = os.path.splitext(doc)
    doc_path = os.path.dirname(full_doc_path)
    doc_name = os.path.basename(full_doc_path)

    if filetype == type_filter or type_filter is None:
        if search in doc:
            new_doc_name = doc.replace(search, replace) 
            new_doc_path = os.path.join(doc_path,new_doc_name) +filetype
            os.rename(doc,new_name)
            renamed += 1

            print(f"Renamed file {doc} to {new_doc_path}")
print(f"Renamed {renamed} of {len(docs)} files")