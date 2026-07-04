class Document:
    def __init__(self, file_name, file_type, file_size, project_id):
        self.id = None
        self.project_id = project_id
        self.file_name = file_name
        self.file_type = file_type
        self.file_size = file_size
    
    def __repr__(self):
        return f"Document(id={self.id}, project_id={self.project_id}, file_name={self.file_name}, file_type={self.file_type}, file_size={self.file_size})"
    
    def get_metadata(self):
        return {
            "id": self.id,
            "project_id": self.project_id,
            "file_name": self.file_name,
            "file_type": self.file_type,
            "file_size": self.file_size
        }
        