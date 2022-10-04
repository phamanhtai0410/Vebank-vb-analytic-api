from src.extensions import redis_cluster


def get_list_staking_contract(_env: str):
    return [_k for _k in redis_cluster.hkeys(
        name=f"vb.env_{_env}"
    ) if _k.startswith("STAKING_CONTRACT")]