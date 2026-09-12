from langchain.tools import tool
import subprocess
from pathlib import Path


ALLOWED_PATH = (Path(__file__).resolve().parents[1] / "detective").resolve()


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

tools = [list_directories, list_files]