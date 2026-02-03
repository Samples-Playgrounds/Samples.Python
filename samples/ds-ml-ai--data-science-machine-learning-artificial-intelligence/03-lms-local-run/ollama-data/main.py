 def main(): print("Fetching Ollama model list...") 
 
    models = get_all_models()

    results = []

    for idx, model in enumerate(models, 1):
        print(f"[{idx}/{len(models)}] {model}")

        try:
            tags = get_model_tags(model)
        except Exception:
            continue

        for tag in tags:
            size_bytes = get_manifest_weight_bytes(model, tag)
            if size_bytes:
                results.append({
                    "model": model,
                    "tag": tag,
                    "gb": round(bytes_to_gb(size_bytes), 2)
                })

    results.sort(key=lambda x: x["gb"], reverse=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("Ollama Models Ranked by VRAM Requirement (Weights Only)\n")
        f.write("=" * 60 + "\n\n")

        for r in results:
            f.write(f"{r['gb']:>7} GB  |  {r['model']}:{r['tag']}\n")

    print(f"\nâ Output written to: {OUTPUT_FILE}")
    print(f"â {len(results)} valid model entries written")


if __name__ == "__main__": 
    main()