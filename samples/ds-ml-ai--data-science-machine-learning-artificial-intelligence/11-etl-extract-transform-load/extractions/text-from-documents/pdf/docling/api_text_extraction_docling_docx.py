#def covert_docx_file_to_markdown (source: str) -> str:
#
#    in_path = Path(source)
#    in_doc = InputDocument(
#        path_or_stream=in_path,
#        format=InputFormat.DOCX,
#        backend=MsWordDocumentBackend,
#    )
#    backend = MsWordDocumentBackend(
#        in_doc=in_doc,
#        path_or_stream=in_path,
#    )
#    doc = backend.convert()
#    result_md = doc.export_to_markdown()
#
#    return result_md

def covert_docx_files_from_folder_to_markdown (source: str) -> str:
    pdf_dir= Path(source)
    input_paths = os.listdir(pdf_dir)
    
    print(f"Processing {len(input_paths)} files...")
    #add pdf dir to each file
    input_paths = [os.path.join(pdf_dir, file) for file in input_paths]
    print(input_paths)
    
    # input_paths = input_paths[:1]  # limit to first 5 files for testing
    
    pipeline_options = TesseractOcrOptions()
    
    for file in input_paths:
        covert_docx_file_to_markdown(file)


