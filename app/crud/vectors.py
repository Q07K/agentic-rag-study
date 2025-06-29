from pymilvus import DataType, MilvusClient

COLLECTION_NAME = "agentic_rag_study"


def create_milvus_collection(client: MilvusClient) -> bool:
    if client.has_collection(collection_name=COLLECTION_NAME):
        return False

    schema = MilvusClient.create_schema(
        auto_id=True,
        enable_dynamic_field=False,
    )

    schema.add_field(
        field_name="chunk_id",
        datatype=DataType.INT64,
        is_primary=True,
    )
    schema.add_field(
        field_name="chunk_vector",
        datatype=DataType.FLOAT_VECTOR,
        dim=1536,
    )

    index_params = client.prepare_index_params()

    index_params.add_index(field_name="chunk_id", index_type="STL_SORT")

    index_params.add_index(
        field_name="chunk_vector",
        index_type="AUTOINDEX",
        metric_type="COSINE",
        params={"nlist": 1024},
    )

    client.create_collection(
        collection_name=COLLECTION_NAME,
        schema=schema,
        index_params=index_params,
    )
    return True
