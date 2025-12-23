
import json
def ingest(path):
    with open(path) as f:
        d=json.load(f)
    return {
        "model": d["model_version"],
        "accuracy": d["metrics"]["accuracy"],
        "decision": "Deploy" if d["metrics"]["accuracy"]>0.9 else "Review"
    }
if __name__=="__main__":
    print(ingest("sample_fedbiomed_output.json"))
