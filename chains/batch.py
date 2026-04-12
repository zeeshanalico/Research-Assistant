from chains.research import key_points_chain

BATCH_TOPICS = [
    {"topic": "Black Holes"},
    {"topic": "Photosynthesis"},
    {"topic": "Machine Learning"},
]


# Batch processing — send multiple inputs through a chain in one call.
def run_batch():
    print("\n  Batch Processing Demo — 3 topics processed concurrently.\n")

    try:
        results = key_points_chain.batch(BATCH_TOPICS)

        for topic_dict, result in zip(BATCH_TOPICS, results):
            print(f"--- {topic_dict['topic']} ---")
            print(result)
            print()
    except Exception as e:
        print(f"Error: {e}\n")
