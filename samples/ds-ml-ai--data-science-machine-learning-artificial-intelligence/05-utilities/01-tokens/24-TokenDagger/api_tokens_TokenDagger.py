import tokendagger as tiktoken


def tokens_in_text_for_encoding (
                                    text: str,
                                    encoding_name: str = "cl100k_base"
                                ) -> tuple[ list[int], int, list[str] ]:
    """
    """
    encoding = tiktoken.get_encoding(encoding_name)
    tokens = encoding.encode(text)
    count_tokens = len(tokens)
    tokens_decoded = [encoding.decode_single_token_bytes(token) for token in tokens]

    return (tokens, count_tokens, tokens_decoded)



def tokens_in_text_for_model (
                                text: str,
                                model_name: str = "gpt-3.5-turbo"
                            ) -> tuple[ list[int], int, list[str] ]:
    """
    """
    encoding = tiktoken.encoding_for_model(model_name)
    tokens = encoding.encode(text)
    count_tokens = len(tokens)
    tokens_decoded = [encoding.decode_single_token_bytes(token) for token in tokens]

    return (tokens, count_tokens, tokens_decoded)


def tokens_in_file_for_encoding (
                                    file_path: str,
                                    encoding_name: str = "cl100k_base"
                                ) -> tuple[ list[int], int, list[str] ]:
    """
    """
    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------
