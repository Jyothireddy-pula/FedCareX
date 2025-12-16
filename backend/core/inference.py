
import pickle, os
MODEL = os.path.join(os.path.dirname(__file__), "..", "models", "demo_model.pkl")

def run_inference(features):
    if not features:
        return {"error": "No features provided"}
    with open(MODEL, "rb") as f:
        model = pickle.load(f)
    pred = model.predict([features])[0]
    return {"prediction": int(pred), "note": "Demo ML inference"}
