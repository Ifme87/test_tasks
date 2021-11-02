import json


def service_discovery(file):
    with open(file) as f:
        db = json.load(f)

    serviceSpecName = db["serviceModel"]["serviceSpecification"]["name"]
    domainClientServ = db["serviceModel"]["serviceCharacteristic"][1]["value"][
        "e2e-client-service"
    ]["domain-client-service"][0]

    lbz = domainClientServ["lbz"]
    rfs_id = domainClientServ["rfs-id"]
    operational_state = domainClientServ["operational-state"]
    user_label = domainClientServ["user-label"]

    if serviceSpecName == "otn-trunk-cfs":
        if domainClientServ["domain"] == "Ciena":
            print("lbz: ", user_label)
            print("rfs_id: ", rfs_id)
            print("operational_state: ", operational_state)
            print("user-label: ", user_label)


if __name__ == "__main__":
    service_discovery("arangodb.txt")
