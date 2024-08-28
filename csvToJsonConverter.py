import csv
import json
import re


def convert_csv_to_json(csv_file_path):
    json_data = []
    with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        action_key = 1

        # Identify input columns dynamically
        input_columns = [ column for column in reader.fieldnames if column.startswith("Inputs") ]

        for row in reader:
            conditions = []

            # Helper function to process input and add conditions
            def process_input(input_str):
                if input_str:
                    # Check if the input has the pattern "number > string > number"
                    match = re.match(r"([\d.]+)\s*[><≥≤]+\s*(.+?)\s*[><≥≤]+\s*([\d.]+)", input_str)
                    match2 = re.match(r'(\d+)\s+(\D+?)\s*([<>≤≥])\s*(\D+?)\s*([<>≤≥])\s*(\d+)\s+(\D+)', input_str)

                    if match2:
                        ( number1, string1, operator1, string2, operator2, number2, string3, ) = match2.groups()
                        key = "DAK, " + string2.replace("\u2260", "").strip().replace(
                            '\\"', ""
                        ).replace('"', "")
                        value_1 = float(number1)
                        value_2 = float(number2)
                        conditions.append( { "key": key, "value_1": value_1, "value_2": value_2, "operator": "between", } )
                    elif match:
                        value_1, key, value_2 = match.groups()
                        key = "DAK, " + key.replace("\u2260", "").strip().replace( '\\"', "" ).replace('"', "")
                        value_1 = float( value_1.replace('\\"', "").strip().replace('"', "") )
                        value_2 = float( value_2.replace('\\"', "").strip().replace('"', "") )
                        conditions.append( { "key": key, "value_1": value_1, "value_2": value_2, "operator": "between", } )
                    elif "≠" in input_str:
                        key, or_values = map( str.strip, re.split(r"\s*≠\s*", input_str, 1) )
                        key = "DAK, " + key.replace("Inputs", "").strip().replace( '\\"', "" ).replace('"', "")
                        or_list = re.split(r"\s*OR\s*", or_values)
                        for or_value in or_list:
                            value = "DAK, " + or_value.replace( '\\"', "" ).strip().replace('"', "")
                            conditions.append( {"key": key, "value": value, "operator": "!="} )
                    else:
                        # Check if the input contains "=" or "≥" or "≤" or ">" or "<" operator
                        match = re.match(r"(.+?)\s*(≥|≤|>|<)\s*(.+)", input_str)
                        match2 = re.match(r"(.+?)\s*(=)\s*(.+)", input_str)
                        if match2:
                            key, operator, value = match2.groups()
                            key = "DAK, " + key.replace('"', "")

                            # Check if the value is "True" or "False"
                            if value.strip().lower() in ["true", "false"]:
                                conditions.append( { "key": key, "value": value.strip(), "operator": "=", } )
                            else:
                                value = "DAK, " + value.strip().replace('"', "")
                                conditions.append( {"key": key, "value": value, "operator": "="} )

                        if match:
                            key, operator, value = match.groups()
                            key = "DAK, " + key.replace('"', "")
                            value = value.strip().replace('"', "")

                            # If the value contains units, extract the numeric part
                            numeric_match = re.match(r"([\d.]+)\s*[a-zA-Z]*", value)
                            if numeric_match:
                                value = float(numeric_match.group(1))

                            if "≥" in input_str:
                                operator = ">="
                            elif "≤" in input_str:
                                operator = "<="
                            elif ">" in input_str:
                                operator = ">"
                            elif "<" in input_str:
                                operator = "<"
                            else:
                                operator = "="

                            conditions.append( {"key": key, "value": value, "operator": operator} )

            # Process all input columns
            for input_column in input_columns:
                process_input( row.get(input_column, "").strip(), )

            if conditions:
                json_entry = {
                    "conditions": conditions,
                    "action": row.get("Actions", "").strip(),
                    "annotation": row.get("Annotations", "").strip(),
                    "action_key": action_key,
                }

                json_data.append(json_entry)
                action_key += 1

    return json_data


# Assuming the CSV file ("Physical_Exam.csv") is in the same directory as the script.
csv_file_path = "DAK_DS.csv"
json_data = convert_csv_to_json(csv_file_path)

# Save the generated JSON to 'Physical_Exam_cmp.json'
with open("DAK_DS.json", "w", encoding="utf-8") as jsonfile:
    json.dump(json_data, jsonfile, indent=4)

print("Conversion complete. JSON file saved to DAK_DS.json")
