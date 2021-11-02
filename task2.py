import json


def cards_inf(db):
    """
    find cards with active intf
    """
    interfaces = db["task_result"]["content"]["network-element"][0]["interface"]
    result = {}

    for i in interfaces:
        if i["admin-status"] == "up" and i.get("hw-component-reference") != None:
            if i.get("hw-component-reference") in result:
                values = result[i.get("hw-component-reference")]
                if type(values) == str:
                    new_values = [values, i.get("name") + ", up, " + i.get("id")]
                else:
                    new_values.append(i.get("name") + ", up, " + i.get("id"))
                result[i.get("hw-component-reference")] = new_values
            else:
                result[i.get("hw-component-reference")] = (
                    i.get("name") + ", up, " + i.get("id")
                )
    return result


def parse_inf(intf, output_file):
    """
    parse and write info
    """
    hardwareComp = db["task_result"]["content"]["network-element"][0]["hw-component"]
    comp = {}
    parent = {}
    for hw in hardwareComp:
        comp[hw["id"]] = hw["description"]
        parent[hw["id"]] = hw["parent-slot-mkey"]
    with open(output_file, "w") as f:
        for i in intf:
            if i and comp.get(i):
                f.write(comp.get(i) + ", " + parent.get(i)[0] + "\n")
                if type(intf[i]) == list:
                    for line in intf[i]:
                        f.write(" " * 4 + line + "\n")
                    f.write("\n")
                else:
                    f.write(" " * 4 + intf[i] + "\n" * 2)


if __name__ == "__main__":
    with open("ne-data.txt") as f:
        db = json.load(f)

    intf = cards_inf(db)
    parse_inf(intf, "result.txt")
