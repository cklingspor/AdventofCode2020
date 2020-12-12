def read_file(unc_path: str):
    lines = []
    doc = open(unc_path)
    for line in doc:
        lines.append(line)

    doc.close()
    return lines