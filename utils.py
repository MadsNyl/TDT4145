from pool import cursor, conn


def get_date(line: str) -> str | None:
    if "Dato" in line:
            words = line.split()
            for word in words:
                if len(word) == 10 and word[4] == "-" and word[7] == "-":
                    return word
    return None


def run_sql_script(script_path: str) -> None:
    with open(script_path, 'r') as script_file:
        sql_script = script_file.read()
        cursor.executescript(sql_script)
        conn.commit()
