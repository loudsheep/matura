def decode(k, n, S):
    RESULT = ""
    for i in range(n // k):
        frag = ""
        j = i
        while j < n:
            frag += S[j]
            j += n // k
        if i % 2 == 0:
            RESULT += frag
        else:
            RESULT += frag[::-1]
        print(frag, i, n//k)
    return RESULT

# print(decode(10, 40, "NKI_ATE_USGACYOKZZ_YYSJTCWEKI_SAEMTRLE_P"))
