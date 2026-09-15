from langchain.tools import tool
import subprocess
from pathlib import Path
import puremagic


ALLOWED_PATH = (Path(__file__).resolve().parents[1] / "detective").resolve()
ALLOWED_MIME_TYPES = {
    "text/plain",
    "text/markdown",
    "application/json",
    "text/csv",
}


@tool
def list_directories(path_name: str):
    """Lists the names and absolute paths of immediate subdirectories within the given directory."""

    path = Path(path_name)
    resolved_input = path.resolve()

    if not resolved_input.is_relative_to(ALLOWED_PATH):
        return {
            "success": False,
            "error": "PATH_OUTSIDE_ALLOWED_ROOT",
            "message": "The requested path is outside the directories available to you."
        }
    if not resolved_input.exists():
        return {
            "success": False,
            "error": "NON_EXISTENT_PATH",
            "message": "The requested path does not exist"
        }

    if resolved_input.is_file():
        return {
            "success": False,
            "error": "NOT_A_DIRECTORY",
            "message": "This tool only returns immediate subdirectories."
        }

    directories = []
    for item in resolved_input.iterdir():
        if item.is_dir():
            directories.append({"name": item.name, "path": str(item)})
    
    return {
        "success": True,
        "action": "",
        "directories": directories
    }

@tool
def list_files(path_name: str):
    """Lists the names and absolute paths of immediate files within the given directory."""

    path = Path(path_name)
    resolved_input = path.resolve()

    if not resolved_input.is_relative_to(ALLOWED_PATH):
        return {
            "success": False,
            "error": "PATH_OUTSIDE_ALLOWED_ROOT",
            "message": "The requested path is outside the directories available to you."
        }
    if not resolved_input.exists():
        return {
            "success": False,
            "error": "NON_EXISTENT_PATH",
            "message": "The requested path does not exist"
        }

    if resolved_input.is_file():
        return {
            "success": False,
            "error": "NOT_A_DIRECTORY",
            "message": "This tool only returns immediate file names and paths based on a path containing a directory."
        }

    files = []
    for item in resolved_input.iterdir():
        if item.is_file():
            files.append({"name": item.name, "path": str(item)})
    
    return {
        "success": True,
        "files": files
    }


@tool
def read_file(path: str):
    """Reads and returns the textual contents of a file at the given file path"""
    resolved_path = Path(path).resolve()

    if not resolved_path.is_relative_to(ALLOWED_PATH):
        return {
            "success": False,
            "error": "PATH_OUTSIDE_ALLOWED_ROOT",
            "message": "The requested file path is outside the directories available to you."
        }
    
    if not resolved_path.exists():
        return {
            "success": False,
            "error": "NON_EXISTENT_PATH",
            "message": "The requested path does not exist"
        }

    if resolved_path.is_dir():
        return {
            "success": False,
            "error": "NOT_A_FILE",
            "message": "This tool only reads files and you supplied a path to a directory"
        }

    mime_type = puremagic.from_file(resolved_path, mime=True)

    if not mime_type in ALLOWED_MIME_TYPES:
        return {
            "success": False,
            "error": "FILE_TYPE_NOT_ALLOWED",
            "message": "The file provided has a mime type not supported by this tool"
        }


    try:
        with open(resolved_path, 'r', encoding='utf-8') as file:
            lines = file.read()
            
    except Exception as e:
        return {
            "success": False,
            "error": "FILE_READ_ERROR",
            "message": f"Failed to read file. Error: {e}"
        }
    
    return {
        "success": True,
        "file_name": resolved_path.name,
        "content": lines
    }



tools = [list_directories, list_files, read_file]