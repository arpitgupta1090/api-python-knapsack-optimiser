

def mapper(input_request, model_output ):
    results = dict()

    metadata = {"optimiser": input_request.optimiser}

    results["total_value"] = model_output[0]
    results["total_weight"] = model_output[1]
    results["values"] = model_output[2]
    results["weights"] = model_output[3]
    return {"metadata": metadata, "results": [results]}
