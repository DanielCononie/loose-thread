from pathlib import Path
PATH_NAME = "/detective/cases/"

def try_write(write_path: Path, data: str):
   try:
      write_path.write_text(data, encoding="utf-8")
      return {
         "success": True,
         "item": write_path
      }
   except:
      return {
         "success": False,
         "item": write_path
      }
   

def create_case(scene_evidence: str, crime_report: str, records: str, security_log: str, suspects: str):
    # Generate new case number dynamically by gathering all immediate directories inside of detective, turning into int array, and then adding 1 to last element.
    resolved_path =  (Path(__file__).resolve().parents[0] / "detective/cases").resolve()
    

    case_number = 0
    for item in resolved_path.iterdir():
        if item.is_dir():
            case_number = max(case_number, int(item.name))
    case_number = case_number + 1

    # Create directory with case number generated above
    new_case_path = Path(f"{resolved_path}/{case_number}").resolve()
    new_case_path.mkdir(parents=True, exist_ok=True)

    # Create and write to respective files, return 500 if file writing error

    if scene_evidence != "":
       evidence_path = Path(f"{new_case_path}/scene_evidence.txt")
       result = try_write(evidence_path, scene_evidence)
       if not result["success"]:
          return {
             "create_case_status": 500,
             "create_case_content": {
                "message": f"Case {case_number} could not be created",
             }
          }


    if crime_report != "":
       crime_report_path = Path(f"{new_case_path}/crime_report.txt")
       result = try_write(crime_report_path, crime_report)
       if not result["success"]:
          return {
             "create_case_status": 500,
             "create_case_content": {
                "message": f"Case {case_number} could not be created",
             }
          }

    if records != "":
       records_path = Path(f"{new_case_path}/records.txt")
       try_write(records_path, records)
       if not result["success"]:
          return {
             "create_case_status": 500,
             "create_case_content": {
                "message": f"Case {case_number} could not be created",
             }
          }

    
    if security_log != "":
       security_log_path = Path(f"{new_case_path}/security_log.txt")
       try_write(security_log_path, security_log)
       if not result["success"]:
          return {
             "create_case_status": 500,
             "create_case_content": {
                "message": f"Case {case_number} could not be created",
             }
          }

    if suspects != "":
       suspects_path = Path(f"{new_case_path}/suspects.txt")
       try_write(suspects_path, suspects)
       if not result["success"]:
          return {
             "create_case_status": 500,
             "create_case_content": {
                "message": f"Case {case_number} could not be created",
             }
          }
    
    # return success
    return {
        "create_case_status": 201,
        "create_case_content": {
            "message": f"Case {case_number} created",
        }
    }